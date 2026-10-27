const { test } = require('node:test');
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const vm = require('node:vm');

const source = fs.readFileSync(path.join(__dirname, '../Code.gs'), 'utf8');
function fixture(shared = {}) {
  let held = false;
  const context = vm.createContext({
    PropertiesService: { getScriptProperties: () => ({
      getProperties: () => ({ ...shared }),
      setProperty: (key, value) => {
        assert.ok(Buffer.byteLength(value, 'utf8') < 9000);
        shared[key] = value;
      }
    }) },
    LockService: { getScriptLock: () => ({
      tryLock: () => { if (held) return false; held = true; return true; },
      releaseLock: () => { held = false; }
    }) }
  });
  vm.runInContext(source, context);
  return { context, shared, board: () => context.getBoard(),
    save: (changes = {}) => context.saveTask({ id: 'W00', status: 'in_progress',
      role: 'M1', note: '', evidence: '', expectedRevision: 0, ...changes }) };
}

test('initial board contains the 22 planned tasks and creates no fake progress', () => {
  const app = fixture();
  assert.equal(app.board().tasks.length, 22);
  assert.equal(app.board().roles.length, 5);
  assert.ok(app.board().tasks.every(t => t.progress.status === 'not_started' && t.progress.revision === 0));
  assert.equal(Object.keys(app.shared).length, 0);
});

test('another session reads the stored task state', () => {
  const app = fixture();
  assert.equal(app.save({ note: 'กำลังแบ่งบทบาท' }).ok, true);
  const other = fixture(app.shared);
  const task = other.board().tasks.find(t => t.id === 'W00');
  assert.equal(task.progress.note, 'กำลังแบ่งบทบาท');
  assert.equal(task.progress.updatedBy, 'M1');
  assert.equal(task.progress.revision, 1);
});

test('stale writes return a conflict without overwriting the other person', () => {
  const app = fixture();
  app.save({ note: 'จากคนแรก' });
  const result = app.save({ note: 'ข้อมูลเก่าจากคนที่สอง' });
  assert.equal(result.conflict, true);
  assert.equal(result.current.note, 'จากคนแรก');
  assert.equal(app.board().tasks[0].progress.note, 'จากคนแรก');
});

test('cannot close or send for review before effective prerequisites are done', () => {
  const app = fixture();
  assert.throws(() => app.save({ id: 'D01', status: 'done', note: 'fixture' }), /W00/);
  assert.throws(() => app.save({ id: 'D01', status: 'review' }), /W00/);
  assert.equal(app.save({ id: 'D01', status: 'in_progress' }).ok, true);
  app.save({ status: 'done', note: 'ตกลงแล้ว' });
  assert.equal(app.save({ id: 'D01', expectedRevision: 1, status: 'done', note: 'ตรวจแล้ว' }).ok, true);
});

test('reopened upstream work makes downstream completion ineffective', () => {
  const app = fixture();
  app.save({ status: 'done', note: 'fixture only' });
  app.save({ id: 'D01', status: 'done', note: 'fixture only' });
  app.save({ status: 'in_progress', expectedRevision: 1 });
  assert.throws(() => app.save({ id: 'D02', status: 'done', note: 'fixture only' }), /D01/);
});

test('validates identifiers, status, role, lengths, revision and evidence URL', () => {
  const app = fixture();
  for (const input of [{ id: 'UNKNOWN' }, { status: 'completed' }, { role: 'admin' },
    { expectedRevision: -1 }, { expectedRevision: '0' }, { note: 'ก'.repeat(401) },
    { evidence: 'https://example.com/' + 'a'.repeat(1500) },
    { evidence: 'javascript:alert(1)' }, { evidence: 'https://example.com/ bad' },
    { evidence: 'https://example.com@evil.com' }, { status: 'done' }]) {
    assert.throws(() => app.save(input));
  }
  assert.equal(app.save({ evidence: 'https://docs.google.com/document/d/example/edit' }).ok, true);
});

test('stores display text as text and bounds multibyte property size', () => {
  const app = fixture();
  const note = '<img src=x onerror=alert(1)>' + 'ก'.repeat(370);
  assert.equal(app.save({ note }).ok, true);
  assert.equal(app.board().tasks[0].progress.note, note);
});

test('malformed stored state is reported rather than silently erased', () => {
  const app = fixture({ 'bicycle_board_v1:W00': '{not-json' });
  assert.throws(() => app.board(), /อ่านสถานะงาน/);
  assert.equal(app.shared['bicycle_board_v1:W00'], '{not-json');
});

test('locks are released after a validation error inside a transaction', () => {
  const app = fixture();
  assert.throws(() => app.save({ id: 'P01', status: 'done', note: 'fixture' }));
  assert.equal(app.save().ok, true);
});

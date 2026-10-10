export function merge(a, b) {
  if (a.family !== b.family || a.level !== b.level) throw new Error('incompatible');
  return {family: a.family, level: a.level + 1};
}

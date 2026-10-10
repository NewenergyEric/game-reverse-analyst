// Original minimal fixture for static analysis; not a shipped game.
import {merge} from './merge.js';
import {submitOrder} from './order.js';
export function completeCorner(a, b, requiredLevel, wallet) {
  const item = merge(a, b);
  return submitOrder(item, requiredLevel, wallet);
}

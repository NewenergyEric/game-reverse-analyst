export function submitOrder(item, requiredLevel, wallet) {
  if (item.level < requiredLevel) return {complete: false, wallet};
  return {complete: true, wallet: wallet + 10, cornerState: 'renovated'};
}

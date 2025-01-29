// Search Criteria Fill
export const fromCarat = "0.30"
export const toCarat = "0.49"
export const fromColor = "E"
export const toColor = "E"
export const fromClarity = "IF"
export const toClarity = "IF"
export const fromFlour = "NON"
export const toFlour = "NON"
export const selectLab = "GIA"

export const stoneLocation = "MUMBAI"
export const stoneStatus = "AVAILABLE"
export const stockStatus = "STOCK"
//BLENDER DIAMOND / ARG DIAMONDS LLP
export const partyHoldName = 'BLENDER DIAMOND'
export const businessSource = "EBID"
export const jangadNotes = "Automation Hold Jangad Test BY Raj Gandhi"
export const selectedTerms = "Export - (0-6 Days)"
// ADV PAYMENT / 15DAY
export const paymentTerms = "ADV PAYMENT"
export const selectedBrokers = "RITESH GANDHI"
export const throughSent = "Automation BY RAJ GANDHI"


export async function selectStones(searchresultRows, page, stoneLocation, stoneStatus, stockStatus) {

  const matchrows = await searchresultRows.filter({
    has: page.locator("//datatable-body-cell[@role='cell']"),
    hasText: stoneLocation,
    hasText: stoneStatus,
    hasText: stockStatus,
  })
  for (let i = 0; i < 2; i++) {
    await matchrows.locator('#selcted')
      .nth(i).check();
      continue;
  }
}

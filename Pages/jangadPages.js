export const jangadNo = '194790 ';

export async function OpenJangad(JangadRows, page, jangadNo) {
    const matchrows = await JangadRows.filter({
        has: page.locator("//td[normalize-space()]"),
        hastext: jangadNo,
    })
    for (let i = 0; i < await matchrows.count(); i++) {
        const row = await matchrows.locator('//td[normalize-space()]').nth(i);
        await row.click();
        console.log("click");
        break; 
    }
}
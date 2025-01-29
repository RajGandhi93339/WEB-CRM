const { test, expect } = require('@playwright/test');
const { jangadUrl } = require('../Pages/loginPage');
const { OpenJangad, jangadNo } = require('../Pages/jangadPages');

test('openJangad', async ({ browser }) => {
    const context = await browser.newContext();
    const page = await context.newPage();
    await page.goto(jangadUrl)
    await page.locator("//button[normalize-space()='Hold']").click();
    const jangadTable = await page.locator("//table[@class='table table-bordered text-center table-hover text-nowrap']")
    const JangadColumns = await jangadTable.locator("//tr[@class='saleHeader']//th");
    console.log("no of columns:", await JangadColumns.count());
    const JangadRows = await jangadTable.locator("//tbody//tr");
    console.log("no of rows:", await JangadRows.count());
    //await JangadRows.locator("//td[normalize-space()=" + jangadNo + "]").click();

    // function call
    OpenJangad(JangadRows, page, jangadNo)

    /* 
    for (let p = 0; p < await JangadColumns.count(); p++) {
        const columnheader = await JangadColumns.nth(p);
        console.log(await columnheader.textContent())
    }
    for (let i = 0; i < await JangadRows.count(); i++) {
        const rows = await JangadRows.nth(i);
        const tds = await rows.locator("//td");
        // console.log(await tds.count())
        for (let j = 0; j < await tds.count() - 1; j++) {
            const cellText = await tds.nth(j).textContent();
            if (cellText.trim() !== "") {
                console.log(await tds.nth(j).textContent())
                continue;
            }
            else if (cellText == " ") {
                continue;
            }
        }
     }
        */
    await page.waitForTimeout(10000);
})

test('Release function', async ({ page }) => {
 
})
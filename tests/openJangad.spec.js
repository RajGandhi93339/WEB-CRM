const { test, expect } = require('@playwright/test');
const { jangadUrl } = require('../Pages/loginPage');
const { OpenJangad, jangadNo } = require('../Pages/jangadPages');
const { paymentTerms } = require('../Pages/searchPage');

async function openJangadfunction(page) {
    await page.goto(jangadUrl)
    await page.locator("//button[normalize-space()='Hold']").click();
    const jangadTable = await page.locator("//table[@class='table table-bordered text-center table-hover text-nowrap']")
    const JangadColumns = await jangadTable.locator("//tr[@class='saleHeader']//th");
    console.log("no of columns:", await JangadColumns.count());
    const JangadRows = await jangadTable.locator("//tbody//tr");
    console.log("no of rows:", await JangadRows.count());
    await JangadRows.locator("//td[normalize-space()=" + jangadNo + "]").click();
    // function call
    // await OpenJangad(JangadRows, page, jangadNo)
    await page.waitForTimeout(2000);
}

async function Savefunction(page) {
    await page.locator("//button[normalize-space()='Save']").click();
    const SaveButton = await page.waitForSelector("//button[@class='btn btn btn-soft-primary mx-1']")
    SaveButton.click();
}

test.skip('openJangad', async ({ browser }) => {
    const context = await browser.newContext();
    const page = await context.newPage();
    await openJangadfunction(page)
})

test.skip('Releasefunction', async ({ page }) => {
    await openJangadfunction(page)
    await page.locator("//button[normalize-space()='Release']").click();
    await page.getByRole('dialog').locator('span').nth(1).click();
    const releaseReasonDrpdwn = await page.$$("//div[@role='option']//span");
    for (let reason of releaseReasonDrpdwn) {
        const element = await reason.textContent();
        // console.log(element);
        if (element.includes('Price Very Far')) {
            await reason.click();
        }
    }
    await page.locator("//button[normalize-space()='Apply To All']").click();
    // await page.locator("//button[normalize-space()='Delete']").click();
    // expect(await page.locator("//button[normalize-space()='Delete']").isVisible()).toBeTruthy();
    console.log("Jangad Release Successfully......")
    await page.waitForTimeout(5000);
})

test.skip("copySerialNoButton", async ({ page }) => {
    await openJangadfunction(page);
    await page.locator("//button[normalize-space()='Copy']").click();
    await page.waitForTimeout(5000);
})

test.skip("SaveButton", async ({ page }) => {
    await openJangadfunction(page);
    await Savefunction(page);
    await page.waitForTimeout(5000);
})

test("confirmButton", async ({ page }) => {
    await openJangadfunction(page);
    await page.locator("//button[normalize-space()='Confirm']").click();
    await page.locator("//button[normalize-space()='Trf to Confirm']").click();
    await page.waitForSelector("//div[@id='toast-container']");

    const toggleMessage = expect.soft(await page.locator("//div[@id='toast-container']").textContent()).toBe(" Please select ADVANCE Or COD EX Or COD BANK THROUGH or 6DAY as terms for sale amount < $10,000.  Info! ")
    console.log(toggleMessage)
    await page.getByPlaceholder("Select Current Business Term").click();
    const businessTermsDrpdwn = await page.$$("//div[@role='option']//span");
    console.log(businessTermsDrpdwn.length)
    for (const paymentTermsdata of businessTermsDrpdwn) {
        const businessTerms = await paymentTermsdata.textContent();
        console.log(businessTerms)
        if (businessTerms.includes(paymentTerms)) {
            paymentTermsdata.click();
            break;
        }
    }
    await page.waitForTimeout(1000);
    await page.locator("//button[normalize-space()='Trf to Confirm']").click();
    await page.waitForTimeout(5000);

})
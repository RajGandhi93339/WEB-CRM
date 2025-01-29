const { test, expect, chromium } = require('@playwright/test');
const { fromCarat, toCarat, fromColor, toColor, fromClarity, toClarity, fromFlour, toFlour, selectLab, selectStones, stoneLocation, stoneStatus, stockStatus, partyHoldName, businessSource, jangadNotes, selectedTerms, paymentTerms, selectedBrokers, throughSent } = require('../Pages/searchPage');
const { searchUrl } = require('../Pages/loginPage');

test('searchPage', async ({ browser }) => {

    const context = await browser.newContext();
    const page = await context.newPage();

    page.goto(searchUrl);
    /* Manage New Tab Open
    // const [newTab] = await Promise.all([
    //     context.waitForEvent('page'),// Wait for new page in context
    //     page.locator("//span[normalize-space()='Search Diamond']").click()
     ])*/

    //Shape Selection
    await page.locator("//div[normalize-space()='RBC']").click()
    await page.locator("//div[normalize-space()='PEAR']").click()

    //From Carat
    await page.locator("//input[@placeholder='From']").click()
    await page.locator("//input[@placeholder='From']").fill(fromCarat)

    //To Carat
    await page.locator("//input[@placeholder='To']").click()
    await page.locator("//input[@placeholder='To']").fill(toCarat)

    //Select From colour
    await page.locator('.ng-arrow-wrapper').first().click();
    await page.getByRole('option', { name: fromColor }).click();
    await page.locator('ng-select:nth-child(2) > .ng-select-container > .ng-arrow-wrapper').first().click();
    await page.getByRole('option', { name: toColor }).click();

    // Select Clarity
    await page.locator('div:nth-child(5) > div > .InputFeild > ng-select > .ng-select-container > .ng-arrow-wrapper').first().click();
    await page.getByLabel('Options list').getByText(fromClarity).click();
    await page.locator('div:nth-child(5) > div > .InputFeild > ng-select:nth-child(2) > .ng-select-container > .ng-arrow-wrapper').click();
    await page.getByLabel('Options list').getByText(toClarity, { exact: true }).click();

    // Select Flour
    await page.locator('ng-select').filter({ hasText: /^From$/ }).locator('span').first().click();
    await page.getByLabel('Options list').getByText(fromFlour).click();
    await page.locator('ng-select').filter({ hasText: /^To$/ }).locator('span').first().click();
    await page.getByRole('option', { name: toFlour }).click();

    // Select lab

    await page.locator("//h2[normalize-space()='" + selectLab + "']").click();
    await page.locator("(//button[@class='btn btn-primary btn-sm fs-14'][normalize-space()='Search'])[1]").click();

    await page.keyboard.press('Escape');
    await page.waitForTimeout(3000);

    const searchresultTable = await page.locator("(//div[@class='card mb-2'])[1]")
    const searchresultColumns = await searchresultTable.locator("//datatable-header-cell[@role='columnheader']");
    console.log("no of columns:", await searchresultColumns.count());

    const searchresultRows = await searchresultTable.locator("//datatable-body-row[@role='row']");
    console.log("no of rows:", await searchresultRows.count());

    selectStones(searchresultRows, page, stoneLocation, stoneStatus, stockStatus)
    //  for (let i = 0; i < await searchresultRows.count(); i++) {
    //     const row = await searchresultRows.nth(i);
    //     const tds = await row.locator("//datatable-body-cell[@role='cell']");
    //     console.log("-----------------New Row " + i + " Started---------------------------")
    //     for (let j = 0; j < await tds.count() - 1; j++) {
    //         const cellData = await tds.nth(j).textContent()
    //         if (cellData.trim() !== "") {
    //             console.log(await tds.nth(j).textContent())
    //             continue;
    //         }
    //         else if (cellData == " ") {
    //             continue;
    //         }
    //     }
    //}
    await page.waitForTimeout(3000);

    // Add count 
    await page.locator("//button[normalize-space()='Add']").click();
    // Hold Button Click 
    await page.locator("//button[normalize-space()='Hold']").click();

    // Create new jangad popup
    const jangadPopup = await page.waitForSelector("//button[normalize-space()='Create New Jangad']")
    await jangadPopup.click();

    await page.locator("//ng-select[@id='partyCompanyName']//div[@class='ng-select-container']").click();
    const partyDrpdown = await page.$$("//div[@class='ng-option']//span");
    for (let partyNamedata of partyDrpdown) {
        const value = await partyNamedata.textContent();
        //console.log(value);
        if (value.includes(partyHoldName)) {
            await partyNamedata.click();
            break;
        }
    }
    // Select Business Source
    await page.getByPlaceholder("Select Business Source").click();
    const sourceDrpdown = await page.$$("(//div[@role='option'])//span[@class='ng-option-label']");
    for (let sources of sourceDrpdown) {
        const sourcetype = await sources.textContent();
        // console.log(sourcetype)
        if (sourcetype.includes(businessSource)) {
            await sources.click()
            break;
        }
    }
    // enter jangad note
    await page.locator("//input[@id='janagadNote']").fill(jangadNotes)

    //Select Sale Type
    await page.getByPlaceholder("Select Sale Type").click();
    const saletypeDrpdwn = await page.$$("//div[@role='option']//span[@class='ng-option-label']");
    for (let saletypedata of saletypeDrpdwn) {
        const saleTypeValues = await saletypedata.textContent();
        // console.log(saleTypeValues)
        if (saleTypeValues.includes(selectedTerms)) {
            saletypedata.click();
            break;
        }
    }

    //Select Current Business Term
    await page.getByPlaceholder("Select Current Business Term").click();
    const businessTermsDrpdwn = await page.$$("//div[@role='option']//span[@class='ng-option-label']");
    for (let paymentTermsdata of businessTermsDrpdwn) {
        const businessTerms = await paymentTermsdata.textContent();
        // console.log(businessTerms)
        if (businessTerms.includes(paymentTerms)) {
            paymentTermsdata.click();
            continue;
        }
    }

    //Select broker
    await page.getByPlaceholder("Select Broker").click();
    const brokerDrpdwn = await page.$$("//div[@role='listbox']//span");
    for (let brokerOption of brokerDrpdwn) {
        const brokerName = await brokerOption.textContent();
        console.log(brokerName)
        if (brokerName.includes(selectedBrokers)) {
            brokerOption.click();
            break;
        }
    }
    await page.getByPlaceholder('Enter Sent Through').fill(throughSent);
    await page.locator("//button[normalize-space()='Create']").click();
    await page.locator("//i[@class='bx bx-copy me-1 fs-14']").click();
    await page.locator("//button[normalize-space()='Open Jangad']").click();
    // expect(await page.url()).toBeCloseTo("https://crm.testsjit.in/#/home/pages/user/jangad-view/Hold");
    await page.waitForTimeout(5000);

})
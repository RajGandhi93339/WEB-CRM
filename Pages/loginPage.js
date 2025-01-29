exports.loginPage =

    class loginPage {

        constructor(page) {
            this.page = page;
            this.baseUrl = "https://crm.testsjit.in/#/login";
            this.SearchUrl = "https://crm.testsjit.in/#/home/pages/user/search-diamond";
            this.jangadUrl = "https://crm.testsjit.in/#/home/pages/user/jangad-view";
            this.authFile = "/auth.json";
            this.userId = "4"
            this.password = "13$HiV@M97J"
        }

    }

// Login User and Passwords


// Login page functions
export async function userLogin(page, userId, password) {

    await page.locator("//input[@id='logemail']").fill(userId);
    await page.locator("//input[@id='password']").fill(password);
    const loginButton = await page.locator("button[type='submit']")
    await loginButton.click();
    await loginButton.click();

}


export const userId = "4"
export const password = "13$HiV@M97J"
export const searchUrl = "https://crm.testsjit.in/#/home/pages/user/search-diamond";
export const jangadUrl = "https://crm.testsjit.in/#/home/pages/user/jangad-view";
export const baseUrl = "https://crm.testsjit.in/#/login";
export const authFile = "../auth.json";
exports.loginPage = class loginPage {
    constructor(page) {
        this.page = page;
        this.userNameLocator = "//input[@id='logemail']";
        this.passwordLocator = "//input[@id='password']";
        this.loginbuttonLocator = "button[type='submit']";
    }

    async gotobaseUrl() {
        await this.page.goto(baseUrl)
    }

    async loginUsers(userId, password) {
        await this.page.locator(this.userNameLocator).fill(userId);
        await this.page.locator(this.passwordLocator).fill(password);
        const loginButton = await this.page.locator(this.loginbuttonLocator)
        await loginButton.click();
        await loginButton.click();
    }
}


// Login User and Passwords


// Login page functions
export async function userLogin(page, userId, password) {



}


//** @odoo-module */

import { Component, useState, onWillStart } from "@odoo/owl";
import { registry } from "@web/core/registry";
//import { rpcService} from "@web/core/network/rpc_service";


class DropdownMenu extends Component {
    constructor() {

        super(...arguments);
        this.state = useState({
            showDropdown: false,
            selectedUser: "Unselected",
            users: []
        });
    //   this.onWillStart(this.onWillStart);   
    onWillStart(() => this.loadUsers()); 
    }
    async loadUsers() {
        try {
            const response = await fetch('/user_dropdown_data', {
                method: 'GET',
                headers: {
                    'Content-Type': 'application/json',
                },
            });

            if (!response.ok) {
                throw new Error(`HTTP bị lỗi! trạng thái: ${response.status}`);
            }

            const userData = await response.json();

            // cập nhật trạng thái chuyển đổi dữ liệu
            this.state.users = userData;
            this.render();
            // if (userData.length > 0) {
            //     // Đặt người dùng đầu tiên làm mặc định
            //     this.state.selectedUser = userData[0].name;
            // }
            console.log("Đã tải dữ liệu người dùng :", userData);
        } catch (error) {
            console.log("Đã xảy ra lỗi :", error);
        }
    }
    

    toggleDropdown() {
        this.state.showDropdown = !this.state.showDropdown;
    }

    selectUser(user) {
        this.state.selectedUser = user.name;
        this.state.showDropdown = false;
        console.log("User selected: " + this.state.selectedUser);
    }
}



DropdownMenu.template = "owl.DropdownMenu";
DropdownMenu.components = {};

// Register the component
registry.category("actions").add("owl.DropdownMenu", DropdownMenu);

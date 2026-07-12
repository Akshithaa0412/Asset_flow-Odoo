import { useEffect, useState } from "react";

import React from "react";
import { getDashboardSummary } from "../../services/dashboard";

export default function Dashboard() {

    const [dashboard, setDashboard] = useState<any>(null);

    useEffect(() => {
        async function loadDashboard() {
            const data = await getDashboardSummary();
            setDashboard(data);
        }

        loadDashboard();
    }, []);

    if (!dashboard) {
        return React.createElement("div", null, "Loading...");
    }

    return React.createElement(
        "div",
        null,
        React.createElement("h1", null, "Total Assets"),
        React.createElement("h2", null, dashboard.kpis.total_assets),
        React.createElement("h2", null, dashboard.kpis.available_assets),
        React.createElement("h2", null, dashboard.kpis.allocated_assets),
        React.createElement("h2", null, dashboard.kpis.maintenance_assets)
    );
}
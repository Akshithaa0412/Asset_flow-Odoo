import { useEffect, useState } from "react";

import React from "react";
import { getAssetStatus } from "../../services/reports";

export default function Reports() {

    const [reports, setReports] = useState<any[]>([]);

    useEffect(() => {
        async function loadReports() {
            const data = await getAssetStatus();
            setReports(data);
        }

        loadReports();
    }, []);

    if (!reports.length) {
        return React.createElement("div", null, "Loading...");
    }

    return React.createElement(
        "div",
        null,

        React.createElement("h1", null, "Asset Status Report"),

        reports.map((item, index) =>
            React.createElement(
                "div",
                { key: index },

                React.createElement(
                    "h3",
                    null,
                    item.status
                ),

                React.createElement(
                    "p",
                    null,
                    "Count: " + item.count
                )
            )
        )
    );
}
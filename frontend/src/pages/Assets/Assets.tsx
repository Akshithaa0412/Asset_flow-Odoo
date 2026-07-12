import { useEffect, useState } from "react";

import React from "react";
import { getAssets } from "../../services/assets";

export default function Assets() {

    const [assets, setAssets] = useState<any[]>([]);

    useEffect(() => {
        async function loadAssets() {
            const data = await getAssets();
            setAssets(data);
        }

        loadAssets();
    }, []);

    if (!assets.length) {
        return React.createElement("div", null, "Loading...");
    }

    return React.createElement(
        "div",
        null,
        React.createElement("h1", null, "Assets"),

        React.createElement(
            "table",
            { border: 1, cellPadding: 10 },

            React.createElement(
                "thead",
                null,
                React.createElement(
                    "tr",
                    null,
                    React.createElement("th", null, "Code"),
                    React.createElement("th", null, "Name"),
                    React.createElement("th", null, "Status")
                )
            ),

            React.createElement(
                "tbody",
                null,

                assets.map((asset) =>
                    React.createElement(
                        "tr",
                        { key: asset.id },

                        React.createElement("td", null, asset.asset_code),
                        React.createElement("td", null, asset.name),
                        React.createElement("td", null, asset.status)
                    )
                )
            )
        )
    );
}
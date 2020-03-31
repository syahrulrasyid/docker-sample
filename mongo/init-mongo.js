db.createUser(
    {
        user: "cag000",
        pwd: "rahasia2016",
        roles: [
            {
                role: "readWrite",
                db: "online-news-trace"
            }
        ]
    }
);
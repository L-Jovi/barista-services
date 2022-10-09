import { ApolloServer } from "apollo-server";
import {
    ApolloServerPluginLandingPageLocalDefault,
    ApolloServerPluginLandingPageGraphQLPlayground,
} from "apollo-server-core";

import { schema } from "./schema";
import { context } from "./context";

export const server = new ApolloServer({
    schema,
    context,
    introspection: true,
    plugins: [
        ApolloServerPluginLandingPageLocalDefault(),
        // ApolloServerPluginLandingPageGraphQLPlayground(),
    ],
});

const port = process.env.PORT || 3005;

server.listen({ port }).then(({ url }) => {
    console.log(`🚀  Server  ready at ${url}`);
});

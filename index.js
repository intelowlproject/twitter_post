const { TwitterApi  } = require('twitter-api-v2');

const {
  INPUT_STATUS,
  INPUT_API_KEY,
  INPUT_API_KEY_SECRET,
  INPUT_ACCESS_TOKEN,
  INPUT_ACCESS_TOKEN_SECRET,
} = process.env;

(async () => {

    try {
        const userClient = new TwitterApi({
          appKey: INPUT_API_KEY,
          appSecret: INPUT_API_KEY_SECRET,
          accessToken:  INPUT_ACCESS_TOKEN,
          accessSecret: INPUT_ACCESS_TOKEN_SECRET,
        });

      await userClient.v2.tweet(INPUT_STATUS);

    } catch (err) {
      console.log(err);
      console.log(`::error ::${err.data}`);
    }

  })();
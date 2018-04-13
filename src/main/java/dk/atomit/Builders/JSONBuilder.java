package dk.atomit.Builders;

import dk.atomit.EasyJSON.JSONArray;
import dk.atomit.EasyJSON.JSONObject;
import dk.atomit.EasyJSON.JSONValue;
import dk.atomit.EasyJSON.parser.JSONParser;

/**
 * @author Kristian Gausel
 *
 * Hopefully this simplifies building JSON in Java.
 */
public class JSONBuilder {

    /*
        Example intended usage:

        data:
            {
                "fields": {
                   "project":
                   {
                      "key": "TEST"
                   },
                   "summary": "REST ye merry gentlemen.",
                   "description": "Creating of an issue using project keys and issue type names using the REST API",
                   "issuetype": {
                      "name": "Bug"
                   }
               }
            }
        code:
            import static dk.atomit.Builders.JSONBuilder.*;

            JSONObject jsonobj = JSONObject(
                    $("fields", JSONObject(
                            $("project", JSONObject(
                                    $("key", "TEST")
                                )
                            ).

                            $("summary", "SUMMARY VALUE").
                            $("description", "description value").
                            $("issuetype", JSONObject(
                                    $("name", "Bug")
                                )
                            )
                        )
                    )
            );

     */

    public static MapBuilder<String, Object> $(String key, Object value){
        return Builders.$(key, value);
    }

    public static CollectionBuilder<Object> $(Object o){
        return Builders.$(o);
    }

    public static JSONObject JSONObject(MapBuilder<String, Object> builder){
        return new JSONObject(builder.build());
    }

    public static JSONArray JSONArray(CollectionBuilder<Object> builder){
        return new JSONArray(builder.build());
    }

    public static JSONObject parseJSONObject(String s){
        return new JSONParser().parseObject(s);
    }

    public static JSONArray parseJSONArray(String s){
        return new JSONParser().parseArray(s);
    }

    public static String objectToJSON(Object o){
        return JSONValue.toJSONString(o);
    }


}

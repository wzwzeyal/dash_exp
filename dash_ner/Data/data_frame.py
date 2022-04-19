import pandas as pd

# Only for testing purposes
# text = "מאחר ויודע אני מי הם הנפשות הפועלות אשר ממלאים את המשכן הבזוי שבו היית אתה כעוף מוזר , כי יושרה ונאמנות , כבוד ואצילות , חוכמה ושנינות , ענווה וצניעות , רגישות ואכפתיות , כל אלה ויותר הינם סגולות המושרשות בך , טבועות בדמך , והם סלע קיומך ונר לרגליך . בשל כל אלה והרבה יותר , אוהב אני אותך , ומעריץ אותך ובטוחני שכמוני מרגישים רוב רובו של עם ישראל ולכן מאחל לך אני ומאחל לי ולעם ישראל שמחר תצלח דרכך ונזכה כולנו שתהיה נשיאנו הבא , כי אין ראוי ממך לנשיאות , והנשיאות לא ראויה לאחר מלבדך . ברגשי כבוד והערצה לך נשיאינו ראובן ( רובי ) ריבלין .	"

ner_value = ['green', 'red', 'yellow', 'orange']

ner_model_df = pd.read_csv('./resources/test.tsv', sep='\t').head(10)[['comment']]
# ner_model_df['index'] = range(0, len(ner_model_df))
# ner_model_df['ner_status'] = False


# un_ner_model_df = ner_model_df.copy()






# no_but_model_df = model_df[~model_df['continent'].str.contains('but')]
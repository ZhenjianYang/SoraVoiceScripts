from ED63RDScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'U7002_5 ._SN',
        MapName             = 'Gaiden2',
        Location            = 'U7002.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60000",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            '',
            '',
            '',
            'ED6_DT21/U7002_6 ._SN',
            '',
            '',
            '',
            ''
        ],
    )

    BuildStringList(
        '@FileName',                            # 8
    )

    DeclEntryPoint(
        Unknown_00              = 0,
        Unknown_04              = 0,
        Unknown_08              = 0,
        Unknown_0C              = 4,
        Unknown_0E              = 5,
        Unknown_10              = 0,
        Unknown_14              = 9500,
        Unknown_18              = -10000,
        Unknown_1C              = 0,
        Unknown_20              = 0,
        Unknown_24              = 2500,
        Unknown_28              = 2800,
        Unknown_2C              = 262,
        Unknown_30              = 45,
        Unknown_32              = 0,
        Unknown_34              = 360,
        Unknown_36              = 0,
        Unknown_38              = 1,
        Unknown_3A              = 1,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )


    ScpFunction(
        "Function_0_AA",           # 00, 0
        "Function_1_AB",           # 01, 1
        "Function_2_AC",           # 02, 2
        "Function_3_85C",          # 03, 3
        "Function_4_274C",         # 04, 4
        "Function_5_41BE",         # 05, 5
        "Function_6_70BD",         # 06, 6
        "Function_7_A1C5",         # 07, 7
        "Function_8_ADE2",         # 08, 8
    )


    def Function_0_AA(): pass

    label("Function_0_AA")

    Return()

    # Function_0_AA end

    def Function_1_AB(): pass

    label("Function_1_AB")

    Return()

    # Function_1_AB end

    def Function_2_AC(): pass

    label("Function_2_AC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x564, 0)), scpexpr(EXPR_END)), "loc_14D")
    SetChrFlags(0xFE, 0x10)
    TalkBegin(0xFE)

    ChrTalk(    #0
        0x11,
        (
            "#1446F...\x02\x03",

            "(Renne and Estelle truly are like sisters,\x01",
            "aren't they?)\x02\x03",

            "(It's amazing to see just how strong\x01",
            "their bond has become.)\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xFE, 0x10)
    TalkEnd(0xFE)
    Jump("loc_85B")

    label("loc_14D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x562, 5)), scpexpr(EXPR_END)), "loc_2BE")
    SetChrFlags(0xFE, 0x10)
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4CD, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_173")
    TalkBegin(0xFE)

    AnonymousTalk(    #1
        "\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    TalkEnd(0xFE)
    Jump("loc_2B3")

    label("loc_173")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_24F")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_206")
    TurnDirection(0xFE, 0x101, 0)

    ChrTalk(    #2
        0x11,
        (
            "#1445F...You know something, Estelle?\x02\x03",

            "#1446FYou really are too soft for your own good.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x101,
        "#1008FA-Ahaha...\x02",
    )

    CloseMessageWindow()
    Jump("loc_249")

    label("loc_206")


    ChrTalk(    #4
        0x11,
        (
            "#1445F...\x02\x03",

            "#1446FEstelle really is too soft for her own good.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_249")

    OP_A2(0xC)
    Jump("loc_2B3")

    label("loc_24F")


    ChrTalk(    #5
        0x11,
        (
            "#1446F...\x02\x03",

            "(Why is she so attached to Renne to begin with?)\x02\x03",

            "#1445F(They should be enemies...)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2B3")

    ClearChrFlags(0xFE, 0x10)
    TalkEnd(0xFE)
    Jump("loc_85B")

    label("loc_2BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4CA, 0)), scpexpr(EXPR_END)), "loc_688")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4AC")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3EA")
    TalkBegin(0xFE)

    ChrTalk(    #6
        0x11,
        (
            "#1446FNow that we know the true nature of this world\x01",
            "and the Lord of Phantasma knows it, they may\x01",
            "use different means of attacking us than before.\x02\x03",

            "#1440FI think we should all be on guard for that...\x01",
            "Perhaps I should go and warn the others here.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Jump("loc_4A6")

    label("loc_3EA")

    SetChrFlags(0xFE, 0x10)
    TalkBegin(0xFE)

    ChrTalk(    #7
        0x11,
        (
            "#1440FI think it would be best that we make sure \x01",
            "everyone here is on guard for what the Lord\x01",
            "of Phantasma may try to do.\x02\x03",

            "#1446FPerhaps I should be the one to do so.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    ClearChrFlags(0xFE, 0x10)

    label("loc_4A6")

    OP_A2(0xC)
    Jump("loc_685")

    label("loc_4AC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5C9")
    TalkBegin(0xFE)

    ChrTalk(    #8
        0x11,
        (
            "#1446FNow that we know the true nature of this world\x01",
            "and the Lord of Phantasma knows it, they may\x01",
            "use different means of attacking us than before.\x02\x03",

            "#1440FI think we should all be on guard for that...\x01",
            "Perhaps I should go and warn the others here.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Jump("loc_685")

    label("loc_5C9")

    SetChrFlags(0xFE, 0x10)
    TalkBegin(0xFE)

    ChrTalk(    #9
        0x11,
        (
            "#1440FI think it would be best that we make sure \x01",
            "everyone here is on guard for what the Lord\x01",
            "of Phantasma may try to do.\x02\x03",

            "#1446FPerhaps I should be the one to do so.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    ClearChrFlags(0xFE, 0x10)

    label("loc_685")

    Jump("loc_85B")

    label("loc_688")

    TalkBegin(0xFE)

    ChrTalk(    #10
        0x109,
        (
            "#1064FOh, Ries...\x02\x03",

            "#1840FSo how are things going between you\x01",
            "and the others? Getting along?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x11,
        (
            "#1448F...Yeah, we are.\x02\x03",

            "We had the chance to get to know one another\x01",
            "better while you were asleep.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x109,
        "#1061FAhaha... That's good, I guess...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x11,
        (
            "#1443FI fully expect you to keep your promise\x01",
            "with me, however.\x02\x03",

            "#1446FIf you dare break it...you're going without\x01",
            "food for a week.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x109,
        "#1068FOuch... I'd rather you spared me THAT one.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x11,
        "#1442FHeehee...\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2650)
    TalkEnd(0xFE)

    label("loc_85B")

    Return()

    # Function_2_AC end

    def Function_3_85C(): pass

    label("Function_3_85C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C9, 3)), scpexpr(EXPR_END)), "loc_A83")
    SetChrFlags(0xFE, 0x10)
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A32")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_924")

    ChrTalk(    #16
        0x1E,
        (
            "#1000FLooking at this water kinda reminds me\x01",
            "of the pond behind our house, actually.\x02\x03",

            "#1012FYou'd always sulk back there when we\x01",
            "were kids.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x110,
        "#1300F...\x02",
    )

    CloseMessageWindow()
    Jump("loc_A2C")

    label("loc_924")


    ChrTalk(    #18
        0x1E,
        (
            "#1000FLooking at this water kinda reminds me\x01",
            "of the pond behind our house, actually.\x02\x03",

            "#1012FYou'd always sulk back there when we\x01",
            "were kids.\x02\x03",

            "#1016F...It sure would be nice if the three of us\x01",
            "could sit by that lake together one day,\x01",
            "huh? You, me, and Renne...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A2C")

    OP_A2(0x8)
    Jump("loc_A78")

    label("loc_A32")


    ChrTalk(    #19
        0x1E,
        (
            "#1012FHeehee...\x02\x03",

            "It's been a while since I last felt so\x01",
            "at ease.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A78")

    ClearChrFlags(0xFE, 0x10)
    TalkEnd(0xFE)
    Jump("loc_274B")

    label("loc_A83")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x565, 3)), scpexpr(EXPR_END)), "loc_1104")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E44")
    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_B28")
    Jump("loc_B6A")

    label("loc_B28")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_B44")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_B6A")

    label("loc_B44")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B60")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_B6A")

    label("loc_B60")

    OP_51(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_B6A")

    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    ChrTalk(    #20
        0x1E,
        (
            "#1012F*sigh* You big dummy.\x02\x03",

            "#1006FI come to cheer you up, and yet you've already\x01",
            "picked yourself up and dusted yourself off.\x02\x03",

            "You can lean on me ONCE in a while, you know?\x01",
            "Having a big sister has its perks.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x102,
        (
            "#1513FHaha... Well, I appreciate the sentiment.\x01",
            "I really am fine, though.\x02\x03",

            "#1501FIf anything, right now, I'm actually grateful\x01",
            "to the Lord of Phantasma.\x02\x03",

            "Thanks to them, I was actually able to say what\x01",
            "I couldn't back on the Liber Ark.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x1E,
        (
            "#1016FHeh... Kind of like how I felt when I was able\x01",
            "to meet Mom again through Luciola's illusion,\x01",
            "then.\x02\x03",

            "#1017F...Well...\x02\x03",

            "#1012FI hope Loewe's up there with Karin feeling\x01",
            "just as peaceful as we do now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x102,
        "#1513FYeah...\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0)
    TalkEnd(0xFE)
    Jump("loc_10FE")

    label("loc_E44")

    SetChrFlags(0xFE, 0x10)
    TalkBegin(0xFE)

    ChrTalk(    #24
        0x1E,
        (
            "#1012F*sigh* You big dummy.\x02\x03",

            "#1006FI come to cheer you up, and yet you've already\x01",
            "picked yourself up and dusted yourself off.\x02\x03",

            "You can lean on me ONCE in a while, you know?\x01",
            "Having a big sister has its perks.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x16,
        (
            "#1513FHaha... Well, I appreciate the sentiment.\x01",
            "I really am fine, though.\x02\x03",

            "#1501FIf anything, right now, I'm actually grateful\x01",
            "to the Lord of Phantasma.\x02\x03",

            "Thanks to them, I was actually able to say what\x01",
            "I couldn't back on the Liber Ark.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x1E,
        (
            "#1016FHeh... Kind of like how I felt when I was able\x01",
            "to meet Mom again through Luciola's illusion,\x01",
            "then.\x02\x03",

            "#1017F...Well...\x02\x03",

            "#1012FI hope Loewe's up there with Karin feeling\x01",
            "just as peaceful as we do now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x16,
        "#1513FYeah...\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0xFE, 0x10)
    TalkEnd(0xFE)

    label("loc_10FE")

    OP_A2(0x264B)
    Jump("loc_274B")

    label("loc_1104")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x564, 0)), scpexpr(EXPR_END)), "loc_1D93")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x564, 1)), scpexpr(EXPR_END)), "loc_13B5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x564, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1121")
    Call(3, 4)
    Jump("loc_13B2")

    label("loc_1121")

    SetChrFlags(0xFE, 0x10)
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_12E1")

    ChrTalk(    #28
        0x1E,
        (
            "#1010FSounds like it's finally time to settle things,\x01",
            "huh?\x02",
        )
    )

    CloseMessageWindow()
    OP_51(0x102, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x1E, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x1E, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x1E, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0x1E)
    ClearChrFlags(0x1E, 0x10)
    TurnDirection(0x1E, 0x102, 0)
    OP_51(0x1E, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x1E, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x1E, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x1E, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x1E, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x1E, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x1E, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x1E, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x1E, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x1E, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x1E, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1207")
    Jump("loc_1249")

    label("loc_1207")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x1E, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1223")
    OP_51(0x1E, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1249")

    label("loc_1223")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x1E, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_123F")
    OP_51(0x1E, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1249")

    label("loc_123F")

    OP_51(0x1E, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x1E, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1249")

    OP_51(0x1E, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x102, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x102, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x1E, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x1E, 0x10)
    Sleep(500)

    ChrTalk(    #29
        0x1E,
        (
            "#1006FYou're up, Joshua!\x02\x03",

            "#1018FDon't let him beat you, now!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x102,
        "#1501F...Don't worry. I won't.\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x1E, 0)
    Jump("loc_13AA")

    label("loc_12E1")


    ChrTalk(    #31
        0x1E,
        (
            "#1010FSounds like it's finally time to settle things,\x01",
            "huh?\x02",
        )
    )

    CloseMessageWindow()
    Sleep(200)
    SetChrSubChip(0x1E, 2)
    Sleep(500)

    ChrTalk(    #32
        0x1E,
        (
            "#1006FYou're up, Joshua!\x02\x03",

            "#1018FDon't let him beat you, now!\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x16, 1)
    Sleep(200)

    ChrTalk(    #33
        0x16,
        "#1501F...Don't worry. I won't.\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x1E, 0)
    SetChrSubChip(0x16, 0)

    label("loc_13AA")

    ClearChrFlags(0xFE, 0x10)
    TalkEnd(0xFE)

    label("loc_13B2")

    Jump("loc_1D90")

    label("loc_13B5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1ABC")
    SetChrFlags(0xFE, 0x10)
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_192D")
    OP_51(0x102, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x102, 0)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1463")
    Jump("loc_14A5")

    label("loc_1463")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_147F")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_14A5")

    label("loc_147F")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_149B")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_14A5")

    label("loc_149B")

    OP_51(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_14A5")

    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x102, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x102, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    ChrTalk(    #34
        0x102,
        (
            "#1504FAre you practicing with your staff alone,\x01",
            "Estelle?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x1E,
        "#1000FSure am. Don't wanna start slacking now.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x102,
        (
            "#1500FSorry for not being able to join you for\x01",
            "today's training session, then...\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C7, 5)), scpexpr(EXPR_END)), "loc_17DE")

    ChrTalk(    #37
        0x1E,
        (
            "#1001FAww, don't sweat it.\x02\x03",

            "#1017FHonestly, it's so hard to keep track of time\x01",
            "here, I can't even be sure this isn't the same\x01",
            "day as my last session.\x02\x03",

            "#1017FI'm just still feeling really fired up after that\x01",
            "battle and can't help myself, I guess.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1787")

    ChrTalk(    #38
        0x104,
        (
            "#1542FDarling Estelle, there was no need to do so\x01",
            "alone, however.\x02\x03",

            "#1541FWhy, you could have asked me! I would have\x01",
            "been most delighted to accompany you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0x1E,
        (
            "#1022F...Yeah, I'm not desperate enough to ask\x01",
            "for YOUR help.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_17DB")

    label("loc_1787")


    ChrTalk(    #40
        0x102,
        (
            "#1500FWell, all right... Just be sure to take breaks\x01",
            "when you need them, okay?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_17DB")

    Jump("loc_192A")

    label("loc_17DE")


    ChrTalk(    #41
        0x1E,
        (
            "#1001FAhaha. You worry too much.\x02\x03",

            "#1000FHonestly, it's so hard to keep track of time\x01",
            "here, I can't even be sure this isn't the same\x01",
            "day as my last session.\x02\x03",

            "#1007FStill, the only way to catch up to Dad is good,\x01",
            "old-fashioned hard work, so I can't slack off.\x02\x03",

            "#1006FOkay! I'll take a little break and then get right\x01",
            "back to it!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_192A")

    Jump("loc_1AA6")

    label("loc_192D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C7, 3)), scpexpr(EXPR_END)), "loc_19AC")

    ChrTalk(    #42
        0x16,
        (
            "#1501FIt's been ages since I last fought Dad,\x01",
            "come to think of it...\x02\x03",

            "#1513FMaybe around...six years or so ago.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A0F")

    label("loc_19AC")


    ChrTalk(    #43
        0x16,
        (
            "#1503FSo you ended up fighting Dad?\x02\x03",

            "#1514FI fought him once, too, but that was\x01",
            "a while back.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A0F")


    ChrTalk(    #44
        0x1E,
        "#1017F...Oh, yeah. So you did.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0x16,
        (
            "#1501F...Yeah.\x02\x03",

            "#1509FHaha. I had no idea at the time just how difficult\x01",
            "the task I was undertaking would be.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1AA6")

    OP_A2(0x8)
    OP_A2(0x2)
    SetChrSubChip(0xFE, 0)
    ClearChrFlags(0xFE, 0x10)
    TalkEnd(0xFE)
    Jump("loc_1D90")

    label("loc_1ABC")

    SetChrFlags(0xFE, 0x10)
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1BCC")
    OP_51(0x102, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x102, 0)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1B62")
    Jump("loc_1BA4")

    label("loc_1B62")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1B7E")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1BA4")

    label("loc_1B7E")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1B9A")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1BA4")

    label("loc_1B9A")

    OP_51(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1BA4")

    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x102, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x102, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jump("loc_1BD1")

    label("loc_1BCC")

    SetChrSubChip(0xFE, 0)

    label("loc_1BD1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C7, 5)), scpexpr(EXPR_END)), "loc_1CDB")

    ChrTalk(    #46
        0x1E,
        (
            "#1007FYou know what? That was the first time\x01",
            "I seriously tried taking Dad on.\x02\x03",

            "#1002FNot that I'm up to snuff against him yet--\x01",
            "it's gonna take more than a few days to\x01",
            "get me there.\x02\x03",

            "#1006FOkay! I'll take a little break and then get\x01",
            "right back to it!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D83")

    label("loc_1CDB")


    ChrTalk(    #47
        0x1E,
        (
            "#1002FThe only way to catch up to Dad is good,\x01",
            "old-fashioned hard work, so I can't slack\x01",
            "off.\x02\x03",

            "#1006FOkay! I'll take a little break and then get\x01",
            "right back to it!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D83")

    SetChrSubChip(0xFE, 0)
    ClearChrFlags(0xFE, 0x10)
    TalkEnd(0xFE)

    label("loc_1D90")

    Jump("loc_274B")

    label("loc_1D93")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x561, 0)), scpexpr(EXPR_END)), "loc_1FE6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F2C")
    TalkBegin(0xFE)

    ChrTalk(    #48
        0x1E,
        (
            "#1003FI wasn't expecting the Lord of Phantasma\x01",
            "to use the Ravens or Phillip against us.\x02\x03",

            "Or the royal academy, for that matter...\x02\x03",

            "#1007F*sigh* Having that place used like this is\x01",
            "really starting to depress me.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1EAC")

    ChrTalk(    #49
        0x105,
        "#1163FI'm sorry, Estelle...\x02",
    )

    CloseMessageWindow()

    label("loc_1EAC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1F23")

    ChrTalk(    #50
        0x102,
        (
            "#1503FWith how many memories we have of\x01",
            "the academy, I could hardly blame you\x01",
            "for feeling that way.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F23")

    OP_A2(0x8)
    TalkEnd(0xFE)
    Jump("loc_1FE3")

    label("loc_1F2C")

    TalkBegin(0xFE)

    ChrTalk(    #51
        0x1E,
        (
            "#1010FI think they're deliberately choosing places\x01",
            "we have a strong attachment to.\x02\x03",

            "#1007F*sigh* If they wanted to make me feel all\x01",
            "depressed, they sure as heck succeeded.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)

    label("loc_1FE3")

    Jump("loc_274B")

    label("loc_1FE6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C9, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_239F")
    SetChrFlags(0xFE, 0x10)
    TalkBegin(0xFE)
    OP_62(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)
    TurnDirection(0xFE, 0x109, 400)
    Sleep(300)

    ChrTalk(    #52
        0x1E,
        (
            "#1004FOh, Kevin!\x02\x03",

            "#1002FAre you feeling okay now? We don't want you\x01",
            "going and collapsing again after you've only just\x01",
            "recovered.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0x109,
        (
            "#1066FHeh! C'mon, Estelle. I'm indestructible.\x02\x03",

            "#1060FPretty swell timing on my part before,\x01",
            "huh? I didn't even get to say hi before\x01",
            "I fell unconscious, now, did I?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_222C")
    TurnDirection(0x10F, 0x109, 0)

    ChrTalk(    #54
        0x10F,
        (
            "#1446F...Indeed. Everyone was shaking their heads with\x01",
            "disappointment when you collapsed.\x02\x03",

            "#1801FYou're supposed to be a Dominion, but you\x01",
            "wouldn't believe it from that shameful show\x01",
            "of weakness.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_230B")

    label("loc_222C")

    OP_4A(0x11, 255)
    RunExpression(0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x11, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TurnDirection(0x11, 0x109, 0)

    ChrTalk(    #55
        0x11,
        (
            "#1446F...Indeed. Everyone was shaking their heads with\x01",
            "disappointment when you collapsed.\x02\x03",

            "#1801FYou're supposed to be a Dominion, but you\x01",
            "wouldn't believe it from that shameful show\x01",
            "of weakness.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_230B")

    OP_62(0xFE, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #56
        0x1E,
        (
            "#1016FA-Ahaha...\x01",
            "(I'm pretty sure everyone was just panicking...\x01",
            "ESPECIALLY you, Ries.)\x02",
        )
    )

    CloseMessageWindow()
    OP_4B(0x11, 255)
    OP_51(0x11, 0x4, (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A2(0x264A)
    ClearChrFlags(0xFE, 0x10)
    TalkEnd(0xFE)
    Jump("loc_274B")

    label("loc_239F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C6, 6)), scpexpr(EXPR_END)), "loc_246A")
    TalkBegin(0xFE)

    ChrTalk(    #57
        0x1E,
        (
            "#1000FJust try not to overdo it again, okay, Kevin?\x02\x03",

            "#1015FI mean, I still don't know a whole lot about\x01",
            "what happened, exactly...\x02\x03",

            "#1002F...but we were all really worried about you.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Jump("loc_274B")

    label("loc_246A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C9, 2)), scpexpr(EXPR_END)), "loc_274B")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_25C6")
    TalkBegin(0xFE)
    TurnDirection(0xFE, 0x102, 0)

    ChrTalk(    #58
        0x1E,
        (
            "#1011F...Oh, Joshua?\x02\x03",

            "#1003FI... Uh... There's something that's kinda\x01",
            "bugging me...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0x102,
        (
            "#1503F...Oh, right.\x02\x03",

            "#1505FI think I know what you must be talking about.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0x1E,
        (
            "#1026FY-Yeah...\x02\x03",

            "So, then you think one of the trials...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0x102,
        (
            "#1505F...Most likely, yes.\x02\x03",

            "#1503FI'm going to have to make sure I'm prepared.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2720")

    label("loc_25C6")

    SetChrFlags(0xFE, 0x10)
    TalkBegin(0xFE)
    OP_4A(0x11, 255)
    OP_4A(0x16, 255)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_264D")

    ChrTalk(    #62
        0x11,
        (
            "#1443F...Yes, that's right.\x02\x03",

            "He introduced himself as 'this land of Phantasma's\x01",
            "foremost guardian.'\x02",
        )
    )

    CloseMessageWindow()

    label("loc_264D")

    TurnDirection(0x1E, 0x16, 400)

    ChrTalk(    #63
        0x1E,
        (
            "#1011FUmm... Joshua...\x02\x03",

            "#1003FBy the sounds of it, you've probably encountered\x01",
            "him more times than I have, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0x16,
        (
            "#1505F...Yeah. I know.\x02\x03",

            "#1503FI'm going to have to make sure I'm prepared.\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xFE, 0x10)

    label("loc_2720")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_273D")

    ChrTalk(    #65
        0x110,
        "#1300F...\x02",
    )

    CloseMessageWindow()

    label("loc_273D")

    OP_4B(0x11, 255)
    OP_4B(0x16, 255)
    OP_A2(0x2636)
    TalkEnd(0xFE)

    label("loc_274B")

    Return()

    # Function_3_85C end

    def Function_4_274C(): pass

    label("Function_4_274C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C9, 3)), scpexpr(EXPR_END)), "loc_2775")
    SetChrFlags(0xFE, 0x10)
    TalkBegin(0xFE)

    ChrTalk(    #66
        0x16,
        "#1513F...\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    ClearChrFlags(0xFE, 0x10)
    Jump("loc_41BD")

    label("loc_2775")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x565, 3)), scpexpr(EXPR_END)), "loc_2DA7")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2B23")
    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_281A")
    Jump("loc_285C")

    label("loc_281A")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2836")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_285C")

    label("loc_2836")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2852")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_285C")

    label("loc_2852")

    OP_51(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_285C")

    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    ChrTalk(    #67
        0x101,
        (
            "#1012F*sigh* You big dummy.\x02\x03",

            "#1006FI come to cheer you up, and yet you've already\x01",
            "picked yourself up and dusted yourself off.\x02\x03",

            "You can lean on me ONCE in a while, you know?\x01",
            "Having a big sister has its perks.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0x16,
        (
            "#1513FHaha... Well, I appreciate the sentiment.\x01",
            "I really am fine, though.\x02\x03",

            "#1501FIf anything, right now, I'm actually grateful\x01",
            "to the Lord of Phantasma.\x02\x03",

            "Thanks to them, I was actually able to say what\x01",
            "I couldn't back on the Liber Ark.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0x101,
        (
            "#1016FHeh... Kind of like how I felt when I was able\x01",
            "to meet Mom again through Luciola's illusion,\x01",
            "then.\x02\x03",

            "#1017F...Well...\x02\x03",

            "#1012FI hope Loewe's up there with Karin feeling\x01",
            "just as peaceful as we do now.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0)
    TalkEnd(0xFE)
    Jump("loc_2DA1")

    label("loc_2B23")

    SetChrFlags(0xFE, 0x10)
    TalkBegin(0xFE)

    ChrTalk(    #70
        0x1E,
        (
            "#1012FYeah...\x02\x03",

            "#1006F*sigh* You big dummy.\x02\x03",

            "I come to cheer you up, and yet you've already\x01",
            "picked yourself up and dusted yourself off.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0x16,
        (
            "#1513FYou can lean on me ONCE in a while, you know?\x01",
            "Having a big sister has its perks.\x02\x03",

            "#1501FIf anything, right now, I'm actually grateful\x01",
            "to the Lord of Phantasma.\x02\x03",

            "Thanks to them, I was actually able to say what\x01",
            "I couldn't back on the Liber Ark.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0x1E,
        (
            "#1016FHeh... Kind of like how I felt when I was able\x01",
            "to meet Mom again through Luciola's illusion,\x01",
            "then.\x02\x03",

            "#1017F...Well...\x02\x03",

            "#1012FI hope Loewe's up there with Karin feeling\x01",
            "just as peaceful as we do now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0x16,
        "#1513FYeah...\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0xFE, 0x10)
    TalkEnd(0xFE)

    label("loc_2DA1")

    OP_A2(0x264B)
    Jump("loc_41BD")

    label("loc_2DA7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x564, 0)), scpexpr(EXPR_END)), "loc_337F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x564, 1)), scpexpr(EXPR_END)), "loc_2F80")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x564, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2DC4")
    Call(3, 4)
    Jump("loc_2F7D")

    label("loc_2DC4")

    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2E54")
    Jump("loc_2E96")

    label("loc_2E54")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2E70")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2E96")

    label("loc_2E70")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2E8C")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2E96")

    label("loc_2E8C")

    OP_51(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2E96")

    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    ChrTalk(    #74
        0x16,
        (
            "#1505FIt sounds like the Schwarzritter specifically\x01",
            "wants me to come with you for whatever reason.\x02\x03",

            "#1500FI'm ready to go whenever you are. Just let me\x01",
            "know when you want to leave.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0)
    TalkEnd(0xFE)

    label("loc_2F7D")

    Jump("loc_337C")

    label("loc_2F80")

    SetChrFlags(0xFE, 0x10)
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_308D")
    OP_51(0x101, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x101, 0)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3026")
    Jump("loc_3068")

    label("loc_3026")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3042")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3068")

    label("loc_3042")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_305E")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3068")

    label("loc_305E")

    OP_51(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3068")

    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x101, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    label("loc_308D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_324C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C7, 3)), scpexpr(EXPR_END)), "loc_3114")

    ChrTalk(    #75
        0x16,
        (
            "#1501FIt's been ages since I last fought Dad,\x01",
            "come to think of it...\x02\x03",

            "#1513FMaybe around...six years or so ago.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3177")

    label("loc_3114")


    ChrTalk(    #76
        0x16,
        (
            "#1503FSo you ended up fighting Dad?\x02\x03",

            "#1514FI fought him once, too, but that was\x01",
            "a while back.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3177")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_31AC")

    ChrTalk(    #77
        0x101,
        "#1017F...Oh, yeah. So you did.\x02",
    )

    CloseMessageWindow()
    Jump("loc_31D0")

    label("loc_31AC")


    ChrTalk(    #78
        0x1E,
        "#1017F...Oh, yeah. So you did.\x02",
    )

    CloseMessageWindow()

    label("loc_31D0")


    ChrTalk(    #79
        0x16,
        (
            "#1501F...Yeah.\x02\x03",

            "#1509FHaha. I had no idea at the time just how difficult\x01",
            "the task I was undertaking would be.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x8)
    OP_A2(0x2)
    Jump("loc_336F")

    label("loc_324C")


    ChrTalk(    #80
        0x16,
        (
            "#1500FThe first time I fought him, he clearly held back\x01",
            "against me. Because I was a child, I suppose.\x02\x03",

            "#1513FStill, it's been six years now...\x02\x03",

            "I honestly never thought I'd get the chance to\x01",
            "fight him again--mostly because I wouldn't be\x01",
            "crazy enough to try challenging him again alone.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_336F")

    SetChrSubChip(0xFE, 0)
    ClearChrFlags(0xFE, 0x10)
    TalkEnd(0xFE)

    label("loc_337C")

    Jump("loc_41BD")

    label("loc_337F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x561, 0)), scpexpr(EXPR_END)), "loc_35B6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_34C8")
    TalkBegin(0xFE)

    ChrTalk(    #81
        0x16,
        (
            "#1500FSo those monuments on the scenic route are\x01",
            "the entrances to the four guardians' territories.\x02\x03",

            "#1503FThe four elements were initially intended to\x01",
            "grant safe passage into and to protect the\x01",
            "capital...\x02\x03",

            "...but it looks like the Lord of Phantasma has\x01",
            "decided to use them for their own purposes.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)
    TalkEnd(0xFE)
    Jump("loc_35B3")

    label("loc_34C8")

    TalkBegin(0xFE)

    ChrTalk(    #82
        0x16,
        (
            "#1503FI'm relatively certain those monuments were\x01",
            "initially intended to grant safe passage into\x01",
            "and to protect the capital...\x02\x03",

            "#1505F...but it looks like the Lord of Phantasma has\x01",
            "decided to use them for their own purposes.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)

    label("loc_35B3")

    Jump("loc_41BD")

    label("loc_35B6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C6, 6)), scpexpr(EXPR_END)), "loc_37D9")
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_373E")

    ChrTalk(    #83
        0x16,
        (
            "#1503FI have a feeling we were given Celeste's sealing\x01",
            "stone to unlock in order to understand the\x01",
            "makeup of this world.\x02\x03",

            "Which means that they wanted us to know--and\x01",
            "may use our memories and feelings against us in\x01",
            "new ways as a result.\x02\x03",

            "#1502F...Perhaps the trials ahead are the whole reason\x01",
            "they started trying to recreate parts of Liberl\x01",
            "in here to begin with.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)
    Jump("loc_37D3")

    label("loc_373E")


    ChrTalk(    #84
        0x16,
        (
            "#1503FIf the trials ahead are the whole reason the Lord \x01",
            "of Phantasma started trying to recreate parts of \x01",
            "Liberl in here to begin with...\x02\x03",

            "...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_37D3")

    TalkEnd(0xFE)
    Jump("loc_41BD")

    label("loc_37D9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x560, 0)), scpexpr(EXPR_END)), "loc_3AAD")
    SetChrFlags(0xFE, 0x10)
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_393A")
    TurnDirection(0xFE, 0x101, 0)

    ChrTalk(    #85
        0x101,
        (
            "#1011F...Oh, Joshua?\x02\x03",

            "#1003FI... Uh... There's something that's kinda\x01",
            "bugging me...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #86
        0x16,
        (
            "#1503F...Oh, right. \x01",
            "#1505FI think I know what you must be talking about.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0x101,
        (
            "#1026FY-Yeah...\x02\x03",

            "So, then you think one of the trials...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0x16,
        (
            "#1505F...Most likely, yes.\x02\x03",

            "#1503FI'm going to have to make sure I'm prepared.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3A7A")

    label("loc_393A")

    OP_4A(0x11, 255)
    OP_4A(0x1E, 255)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_39B9")

    ChrTalk(    #89
        0x11,
        (
            "#1443F...Yes, that's right.\x02\x03",

            "He introduced himself as 'this land of Phantasma's\x01",
            "foremost guardian.'\x02",
        )
    )

    CloseMessageWindow()

    label("loc_39B9")


    ChrTalk(    #90
        0x1E,
        (
            "#1003FUmm... Joshua...\x02\x03",

            "By the sounds of it, you've probably encountered\x01",
            "him more times than I have, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0x16,
        (
            "#1505F...Yeah. I know.\x02\x03",

            "#1503FI'm going to have to make sure I'm prepared.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3A7A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3A97")

    ChrTalk(    #92
        0x110,
        "#1300F...\x02",
    )

    CloseMessageWindow()

    label("loc_3A97")

    OP_4B(0x11, 255)
    OP_4B(0x1E, 255)
    ClearChrFlags(0xFE, 0x10)
    OP_A2(0x2636)
    TalkEnd(0xFE)
    Jump("loc_41BD")

    label("loc_3AAD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x500, 0)), scpexpr(EXPR_END)), "loc_3EBF")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3D85")
    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3B52")
    Jump("loc_3B94")

    label("loc_3B52")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3B6E")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3B94")

    label("loc_3B6E")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3B8A")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3B94")

    label("loc_3B8A")

    OP_51(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3B94")

    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3CB7")

    ChrTalk(    #93
        0x16,
        (
            "#1503FThis 'Lord of Phantasma' seems intent on\x01",
            "challenging us to some kind of game.\x02\x03",

            "#1503FJust what that game is, I don't know...\x02\x03",

            "#1502F...but it's possible it has something to do\x01",
            "with the many rules of this land that seem\x01",
            "to exist.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)
    Jump("loc_3D7A")

    label("loc_3CB7")


    ChrTalk(    #94
        0x16,
        (
            "#1502FIf the Lord of Phantasma wants to challenge\x01",
            "us to some kind of game, there must be a set\x01",
            "of rules or logic to it.\x02\x03",

            "...Either way, if you find out anything new, be\x01",
            "sure to let me know.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3D7A")

    SetChrSubChip(0xFE, 0)
    TalkEnd(0xFE)
    Jump("loc_3EBC")

    label("loc_3D85")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4CA, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3D94")
    Call(5, 7)
    Jump("loc_3EBC")

    label("loc_3D94")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3E2F")

    ChrTalk(    #95
        0x16,
        (
            "#1505FProbably.\x02\x03",

            "#1503FShe was right next to me when I was drawn in\x01",
            "here, so I'd say the odds of her being here too\x01",
            "are pretty high.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)
    Jump("loc_3EB9")

    label("loc_3E2F")


    ChrTalk(    #96
        0x16,
        (
            "#1505FProbably.\x02\x03",

            "#1503FShe was right next to me when I was drawn in\x01",
            "here, so I'd say the odds of her being here too\x01",
            "are pretty high.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3EB9")

    TalkEnd(0xFF)

    label("loc_3EBC")

    Jump("loc_41BD")

    label("loc_3EBF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C6, 5)), scpexpr(EXPR_END)), "loc_3F9C")
    TalkBegin(0xFE)
    TurnDirection(0x16, 0x109, 0)

    ChrTalk(    #97
        0x16,
        (
            "#1503FI don't know what our enemies are trying\x01",
            "to achieve...\x02\x03",

            "#1505F...but I don't see any reason why Estelle\x01",
            "wouldn't have been drawn in here, too.\x02\x03",

            "#1502FSo please let me help however I can.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Jump("loc_41BD")

    label("loc_3F9C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4E2, 4)), scpexpr(EXPR_END)), "loc_41BD")
    TalkBegin(0xFE)
    TurnDirection(0x16, 0x109, 0)

    ChrTalk(    #98
        0x16,
        (
            "#1500F...Hey, Kevin.\x02\x03",

            "I've gone over the whole area, but I can't find\x01",
            "any traps at all.\x02\x03",

            "#1505FIt's still possible there may be varieties I'm not\x01",
            "aware of, but I think it's safe to conclude that\x01",
            "this area is free of them for now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0x109,
        (
            "#1060FThanks. We had a look around ourselves and\x01",
            "reached the same conclusion.\x02\x03",

            "#1067FIt's only this area that's safe, though. Take one\x01",
            "step outside and there're baddies around every\x01",
            "corner.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0x16,
        (
            "#1505FInteresting...\x02\x03",

            "#1503FFor now, it's probably for the best\x01",
            "if we don't act alone.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2635)
    TalkEnd(0xFE)

    label("loc_41BD")

    Return()

    # Function_4_274C end

    def Function_5_41BE(): pass

    label("Function_5_41BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x584, 0)), scpexpr(EXPR_END)), "loc_4818")
    OP_63(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4CC, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_OR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4617")
    SetChrFlags(0xFE, 0x10)
    TalkBegin(0xFE)

    ChrTalk(    #101
        0x1C,
        (
            "#1526F...\x02\x03",

            "#1527F...Heh. I wonder if that's really true?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_42C5")

    ChrTalk(    #102
        0x101,
        (
            "#1011FHuh? ...What's up, Schera?\x02\x03",

            "#1015FYou know you left one of your cards on the\x01",
            "table, right?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)
    Sleep(300)
    Jump("loc_4429")

    label("loc_42C5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_433C")

    ChrTalk(    #103
        0x102,
        (
            "#1504FUmm, Schera...\x02\x03",

            "#1500FYou know you left one of your cards on the\x01",
            "table, right?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x102, 400)
    Sleep(300)
    Jump("loc_4429")

    label("loc_433C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_43B0")

    ChrTalk(    #104
        0x10A,
        (
            "#814F...Oh, hi, Schera.\x02\x03",

            "You know you left one of your cards on the\x01",
            "table, right?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x10A, 400)
    Sleep(300)
    Jump("loc_4429")

    label("loc_43B0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4429")

    ChrTalk(    #105
        0x109,
        (
            "#1066FUmm... You do know you left one of your tarot\x01",
            "cards on the table over there, right?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x109, 400)
    Sleep(300)

    label("loc_4429")


    ChrTalk(    #106
        0x1C,
        (
            "#1526FOh, I know.\x02\x03",

            "#1536FIt's been a while since I had such a good result,\x01",
            "so I've decided to leave it there in honor of the\x01",
            "occasion.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_44EB")

    ChrTalk(    #107
        0x101,
        "#1016FWh-What kind of occasion?\x02",
    )

    CloseMessageWindow()
    Jump("loc_4587")

    label("loc_44EB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_450F")

    ChrTalk(    #108
        0x102,
        "#1504FO-Oh...\x02",
    )

    CloseMessageWindow()
    Jump("loc_4587")

    label("loc_450F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4566")

    ChrTalk(    #109
        0x10A,
        (
            "#814FU-Umm...\x02\x03",

            "#818FY-You're okay with being a card short, then?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4587")

    label("loc_4566")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4587")

    ChrTalk(    #110
        0x109,
        "#1064FO-Oh...\x02",
    )

    CloseMessageWindow()

    label("loc_4587")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4611")

    ChrTalk(    #111
        0x104,
        (
            "#1545FHeh. If that's what you want to do, I see no\x01",
            "reason to oppose it.\x02\x03",

            "#1540FA maiden need only to follow her heart.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4611")

    OP_A2(0x2663)
    Jump("loc_47FB")

    label("loc_4617")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4CC, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_474F")
    SetChrFlags(0xFE, 0x10)
    TalkBegin(0xFE)

    ChrTalk(    #112
        0x1C,
        (
            "#1526F...\x02\x03",

            "#1527F...Heh. I wonder if that's really true?\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    OP_62(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)

    ChrTalk(    #113
        0x1C,
        "#1523F...Hmm?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x0, 400)
    Sleep(300)

    ChrTalk(    #114
        0x1C,
        (
            "#1520FHeehee. I suppose I should start getting ready\x01",
            "soon, too.\x02\x03",

            "#1536FThey won't be calling me the Silver Streak anymore\x01",
            "if I start getting rusty, now, will they?\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x9)
    Jump("loc_47FB")

    label("loc_474F")

    TalkBegin(0xFE)

    ChrTalk(    #115
        0x1C,
        (
            "#1526FHeehee. I suppose I should start getting ready\x01",
            "soon, too.\x02\x03",

            "#1536FThey won't be calling me the Silver Streak anymore\x01",
            "if I start getting rusty, now, will they?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_47FB")

    ClearChrFlags(0xFE, 0x10)
    TalkEnd(0xFE)
    OP_62(0xFE, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Jump("loc_70BC")

    label("loc_4818")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x565, 3)), scpexpr(EXPR_END)), "loc_4CAF")
    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_48AF")
    Jump("loc_48F1")

    label("loc_48AF")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_48CB")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_48F1")

    label("loc_48CB")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_48E7")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_48F1")

    label("loc_48E7")

    OP_51(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_48F1")

    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4B1F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x580, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4A31")

    ChrTalk(    #116
        0x1C,
        (
            "#1526FJoshua really has gotten a whole lot tougher and\x01",
            "more dependable since he started that journey,\x01",
            "by the looks of it.\x02\x03",

            "#1520FI'm sure he still has plenty of room for \x01",
            "improvement...\x02\x03",

            "#1535F...but the same applies to all of us. I'm certainly\x01",
            "no exception.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4B19")

    label("loc_4A31")


    ChrTalk(    #117
        0x1C,
        (
            "#1526FSo the next area is a gospel facility called\x01",
            "Aster House?\x02\x03",

            "That's...interesting.\x02\x03",

            "#1522FQuite a peculiar choice of location to recreate\x01",
            "in here, if you ask me.\x02\x03",

            "And yet there must be some kind of reason...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #118
        0x109,
        "#1067F...\x02",
    )

    CloseMessageWindow()

    label("loc_4B19")

    OP_A2(0x9)
    Jump("loc_4CA4")

    label("loc_4B1F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x580, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4C02")

    ChrTalk(    #119
        0x1C,
        (
            "#1520FBoth Joshua and Estelle really seem to have grown\x01",
            "stronger and more dependable since they left on\x01",
            "their journey.\x02\x03",

            "#1521FAnd I'm looking forward to seeing just how much\x01",
            "more they can grow by the end of it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4CA4")

    label("loc_4C02")


    ChrTalk(    #120
        0x1C,
        (
            "#1522FA gospel facility seems to be quite a peculiar\x01",
            "choice of location to recreate here, if you ask\x01",
            "me.\x02\x03",

            "#1526FAnd yet there must be some kind of reason...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4CA4")

    SetChrSubChip(0xFE, 0)
    TalkEnd(0xFE)
    Jump("loc_70BC")

    label("loc_4CAF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x564, 0)), scpexpr(EXPR_END)), "loc_579B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5397")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x565, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_50A6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C7, 4)), scpexpr(EXPR_END)), "loc_4E7D")
    SetChrSubChip(0xFE, 0)
    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4D62")
    Jump("loc_4DA4")

    label("loc_4D62")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_4D7E")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4DA4")

    label("loc_4D7E")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4D9A")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4DA4")

    label("loc_4D9A")

    OP_51(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4DA4")

    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    ChrTalk(    #121
        0x1C,
        (
            "#1525FAhhh...\x02\x03",

            "#1530FThis really hits the spot!\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4E37")

    ChrTalk(    #122
        0x101,
        "#1019FWell, that didn't take long.\x02",
    )

    CloseMessageWindow()
    Jump("loc_4E72")

    label("loc_4E37")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4E72")

    ChrTalk(    #123
        0x102,
        "#1508FShe's back to drinking already...\x02",
    )

    CloseMessageWindow()

    label("loc_4E72")

    SetChrSubChip(0xFE, 0)
    TalkEnd(0xFE)
    Jump("loc_50A3")

    label("loc_4E7D")

    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4F0D")
    Jump("loc_4F4F")

    label("loc_4F0D")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_4F29")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4F4F")

    label("loc_4F29")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4F45")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4F4F")

    label("loc_4F45")

    OP_51(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4F4F")

    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    ChrTalk(    #124
        0x1C,
        (
            "#1526FOh? You had to fight Cassius?\x02\x03",

            "#1520FI took him on a few times myself back\x01",
            "when I was training to be a bracer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #125
        0x109,
        (
            "#1068F*sigh* I don't think I've ever fought\x01",
            "a harder battle in my life...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #126
        0x1C,
        (
            "#1527FOh, I can imagine! Hard to make a trial\x01",
            "much more difficult than a fight with him.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0)
    TalkEnd(0xFE)

    label("loc_50A3")

    Jump("loc_5391")

    label("loc_50A6")

    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_5136")
    Jump("loc_5178")

    label("loc_5136")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_5152")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5178")

    label("loc_5152")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_516E")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5178")

    label("loc_516E")

    OP_51(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5178")

    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C9, 1)), scpexpr(EXPR_END)), "loc_527A")

    ChrTalk(    #127
        0x1C,
        (
            "#1526F(So now even Luci's been recreated here.)\x02\x03",

            "(Running into her again should have been\x01",
            "more strange than it actually was...)\x02\x03",

            "#1532F(...but then again, she's always been right\x01",
            "here with me in my heart.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_536C")

    label("loc_527A")


    ChrTalk(    #128
        0x1C,
        "#1526FSo you met Luciola, did you?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #129
        0x109,
        "#1067FUmm...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #130
        0x1C,
        (
            "#1520F...Don't worry, honey. I'm a big girl.\x02\x03",

            "If I wanted to find her that badly, I would've\x01",
            "already been doing it this past year.\x02\x03",

            "#1521FHeehee. I'll be just fine on my own now.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_536C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5389")

    ChrTalk(    #131
        0x104,
        "#1542F...\x02",
    )

    CloseMessageWindow()

    label("loc_5389")

    SetChrSubChip(0xFE, 0)
    TalkEnd(0xFE)

    label("loc_5391")

    OP_A2(0x9)
    Jump("loc_5798")

    label("loc_5397")

    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_5427")
    Jump("loc_5469")

    label("loc_5427")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_5443")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5469")

    label("loc_5443")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_545F")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5469")

    label("loc_545F")

    OP_51(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5469")

    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x565, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_56C1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C7, 4)), scpexpr(EXPR_END)), "loc_55BF")

    ChrTalk(    #132
        0x1C,
        (
            "#1528FWell, we've managed to overcome our\x01",
            "toughest ordeal yet.\x02\x03",

            "#1530FI'd say I'm entitled to a drink or two.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5564")

    ChrTalk(    #133
        0x102,
        (
            "#1508FDon't lie. We all know you're not going\x01",
            "to stop at two.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_55BC")

    label("loc_5564")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_55BC")

    ChrTalk(    #134
        0x101,
        (
            "#1019FSo would I...except you've clearly had\x01",
            "more than that ALREADY.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_55BC")

    Jump("loc_56BE")

    label("loc_55BF")


    ChrTalk(    #135
        0x1C,
        (
            "#1527FThis place really has been full of memorable\x01",
            "experiences.\x02\x03",

            "#1526FI'll bet anything the final area will be the\x01",
            "toughest of them all, though. Which,\x01",
            "seeing as we fought Cassius, says a lot.\x02\x03",

            "#1520FWe can't afford to be getting careless.\x01",
            "Not now.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_56BE")

    Jump("loc_5790")

    label("loc_56C1")


    ChrTalk(    #136
        0x1C,
        (
            "#1521F...Haha. I have no intention of trying to find\x01",
            "Luci.\x02\x03",

            "#1520FWe'll meet again if it's meant to be. If it isn't,\x01",
            "we won't. That's all there is to it.\x02\x03",

            "Right now, I'm a bracer, and that comes first.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5790")

    SetChrSubChip(0xFE, 0)
    TalkEnd(0xFE)

    label("loc_5798")

    Jump("loc_70BC")

    label("loc_579B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x562, 5)), scpexpr(EXPR_END)), "loc_59EE")
    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_5832")
    Jump("loc_5874")

    label("loc_5832")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_584E")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5874")

    label("loc_584E")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_586A")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5874")

    label("loc_586A")

    OP_51(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5874")

    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5938")

    ChrTalk(    #137
        0x1C,
        (
            "#1526FThere's no point in getting all panicky now.\x01",
            "Not after we've come this far.\x02\x03",

            "#1520FWhoever we end up facing, we'll find a way\x01",
            "to win.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x9)
    Jump("loc_59E3")

    label("loc_5938")


    ChrTalk(    #138
        0x1C,
        (
            "#1526FThe rest of the guardians we face are likely to\x01",
            "be even stronger than the two we've already\x01",
            "defeated.\x02\x03",

            "#1535FSo don't go skimping on preparations,\x01",
            "you hear me?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_59E3")

    SetChrSubChip(0xFE, 0)
    TalkEnd(0xFE)
    Jump("loc_70BC")

    label("loc_59EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x540, 7)), scpexpr(EXPR_END)), "loc_6240")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5EDF")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5BC1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C9, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5A1A")
    Call(3, 3)
    Jump("loc_5BBE")

    label("loc_5A1A")

    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_5AAA")
    Jump("loc_5AEC")

    label("loc_5AAA")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_5AC6")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5AEC")

    label("loc_5AC6")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5AE2")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5AEC")

    label("loc_5AE2")

    OP_51(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5AEC")

    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    ChrTalk(    #139
        0x1C,
        (
            "#1525FTrust Anelace to cook up an idea like this...\x02\x03",

            "#1534FShe might come across as silly to some,\x01",
            "but I can't help but be impressed by her\x01",
            "boundless optimism.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0)
    TalkEnd(0xFE)

    label("loc_5BBE")

    Jump("loc_5ED9")

    label("loc_5BC1")

    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_5C51")
    Jump("loc_5C93")

    label("loc_5C51")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_5C6D")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5C93")

    label("loc_5C6D")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5C89")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5C93")

    label("loc_5C89")

    OP_51(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5C93")

    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    ChrTalk(    #140
        0x1C,
        (
            "#1525FEvery time we find out something new\x01",
            "about this place, things get weirder.\x02\x03",

            "#1532FSo this world is influenced by our thoughts,\x01",
            "is it?\x02\x03",

            "Is it just me, or does that just sound like the\x01",
            "real world when you're really, really drunk?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5E37")

    ChrTalk(    #141
        0x104,
        (
            "#1545FHaha...\x02\x03",

            "#1546FI know just what you mean, Schera!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #142
        0x101,
        (
            "#1016FYou feeling okay, Olivier? You don't look\x01",
            "very good...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5ED1")

    label("loc_5E37")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5E9B")

    ChrTalk(    #143
        0x102,
        (
            "#1508FWell, if there's anyone I'd trust on that\x01",
            "particular subject, it's you.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5ED1")

    label("loc_5E9B")


    ChrTalk(    #144
        0x101,
        "#1016FY-You WOULD know about that, wouldn't you?\x02",
    )

    CloseMessageWindow()

    label("loc_5ED1")

    SetChrSubChip(0xFE, 0)
    TalkEnd(0xFE)

    label("loc_5ED9")

    OP_A2(0x9)
    Jump("loc_623D")

    label("loc_5EDF")

    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_5F6F")
    Jump("loc_5FB1")

    label("loc_5F6F")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_5F8B")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5FB1")

    label("loc_5F8B")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5FA7")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5FB1")

    label("loc_5FA7")

    OP_51(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5FB1")

    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_618B")
    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_6074")
    Jump("loc_60B6")

    label("loc_6074")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_6090")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_60B6")

    label("loc_6090")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_60AC")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_60B6")

    label("loc_60AC")

    OP_51(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_60B6")

    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    ChrTalk(    #145
        0x1C,
        (
            "#1525FTrust Anelace to cook up an idea like this...\x02\x03",

            "#1534FShe might come across as silly to some,\x01",
            "but I can't help but be impressed by her\x01",
            "boundless optimism.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0)
    TalkEnd(0xFE)
    Jump("loc_6235")

    label("loc_618B")


    ChrTalk(    #146
        0x1C,
        (
            "#1525F*sigh* So this world is influenced by our\x01",
            "thoughts, is it?\x02\x03",

            "#1532FIs it just me, or does that just sound like the\x01",
            "real world when you're really, really drunk?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6235")

    SetChrSubChip(0xFE, 0)
    TalkEnd(0xFE)

    label("loc_623D")

    Jump("loc_70BC")

    label("loc_6240")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C9, 4)), scpexpr(EXPR_END)), "loc_66F5")
    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_62D7")
    Jump("loc_6319")

    label("loc_62D7")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_62F3")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_6319")

    label("loc_62F3")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_630F")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_6319")

    label("loc_630F")

    OP_51(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_6319")

    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6641")
    OP_A2(0x9)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6476")

    ChrTalk(    #147
        0x1C,
        (
            "#1526F...So.\x02\x03",

            "#1527FHow are things coming along with you two,\x01",
            "anyway? Any major developments?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #148
        0x101,
        (
            "#1013FH-Heeey...\x02\x03",

            "#1022FYou think you can give me some kinda heads\x01",
            "up before asking me personal questions?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #149
        0x102,
        (
            "#1514FTo be fair, I did figure it was going to come\x01",
            "up eventually.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_654B")

    label("loc_6476")


    ChrTalk(    #150
        0x1C,
        (
            "#1526F...So.\x02\x03",

            "#1527FHow are things coming along with you two,\x01",
            "anyway? Any major developments?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #151
        0x101,
        (
            "#1013FH-Heeey...\x02\x03",

            "#1022FYou think you can give me some kinda heads\x01",
            "up before asking me something like that?!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_654B")


    ChrTalk(    #152
        0x1C,
        "#1535FGo on! Spill. I need to know these things!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_65D1")

    ChrTalk(    #153
        0x105,
        (
            "#1165FAha...haha...\x02\x03",

            "(I can't deny that I'm curious, too...)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_65D1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_663E")
    OP_62(0x10B, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)

    ChrTalk(    #154
        0x10B,
        (
            "#216FWell, I DON'T want to know, so save it\x01",
            "for when I'm not here!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_663E")

    Jump("loc_66EA")

    label("loc_6641")


    ChrTalk(    #155
        0x1C,
        (
            "#1520FEither way, now we've got both stars of\x01",
            "our old show together.\x02\x03",

            "#1535FIt's time to seriously focus on getting out\x01",
            "of this place and back into the real world.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_66EA")

    SetChrSubChip(0xFE, 0)
    TalkEnd(0xFE)
    Jump("loc_70BC")

    label("loc_66F5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x540, 0)), scpexpr(EXPR_END)), "loc_6DD0")
    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_678C")
    Jump("loc_67CE")

    label("loc_678C")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_67A8")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_67CE")

    label("loc_67A8")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_67C4")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_67CE")

    label("loc_67C4")

    OP_51(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_67CE")

    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    ChrTalk(    #156
        0x1C,
        (
            "#1525FIt's been one thing after another since we got\x01",
            "in here, but I'm just glad you turned out to be\x01",
            "all right.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #157
        0x101,
        "#1004FWho, me?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #158
        0x1C,
        (
            "#1525FBut of course.\x02\x03",

            "#1532FJoshua was putting on a brave face the whole\x01",
            "time, but you know him. Anyone could tell how\x01",
            "worried he was about you.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6B81")

    ChrTalk(    #159
        0x102,
        "#1505FCould you? I don't believe I was showing it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #160
        0x101,
        "#1017FYou were worried about me?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #161
        0x102,
        (
            "#1511FWell...I think most people would be if\x01",
            "they'd heard their girlfriend had been\x01",
            "captured, don't you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #162
        0x101,
        (
            "#1004FI was captured? For real?!\x02\x03",

            "#1013FI... Was I? I mean, I guess I was, but it sure\x01",
            "doesn't feel like it.\x02\x03",

            "I don't even remember anything like that\x01",
            "happening.\x02\x03",

            "Well, whatever... No big deal if I can't\x01",
            "remember, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #163
        0x1C,
        (
            "#1522F...\x02\x03",

            "#1521FYou never change.\x02\x03",

            "And neither do I! Now I can go back\x01",
            "to drinking, worry-free! ㈱\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #164
        0x102,
        "#1508FUmm... Schera...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #165
        0x101,
        "#1009FWhat kind of reaction is that?!\x02",
    )

    CloseMessageWindow()
    Jump("loc_6DC2")

    label("loc_6B81")


    ChrTalk(    #166
        0x101,
        "#1017FI can't believe you...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #167
        0x1C,
        (
            "#1526FWell, I can't say I blame him. Not one bit.\x02\x03",

            "#1535FI was worried sick when I found out the\x01",
            "Lord of Phantasma had captured you.\x01",
            "It must have been so much worse for him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #168
        0x101,
        (
            "#1004FI was captured? For real?!\x02\x03",

            "#1013FI... Was I? I mean, I guess I was, but it sure\x01",
            "doesn't feel like it.\x02\x03",

            "I don't even remember anything like that\x01",
            "happening.\x02\x03",

            "Well, whatever... No big deal if I can't\x01",
            "remember, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #169
        0x1C,
        (
            "#1522F...\x02\x03",

            "#1521FYou never change.\x02\x03",

            "And neither do I! Now I can go back\x01",
            "to drinking, worry-free! ㈱\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #170
        0x101,
        "#1009F...Why? What'd I say?\x02",
    )

    CloseMessageWindow()

    label("loc_6DC2")

    OP_A2(0x264C)
    SetChrSubChip(0xFE, 0)
    TalkEnd(0xFE)
    Jump("loc_70BC")

    label("loc_6DD0")

    SetChrFlags(0xFE, 0x10)
    TalkBegin(0xFE)
    RunExpression(0x2, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7003")

    ChrTalk(    #171
        0x1C,
        (
            "#1525F*sigh* This place just baffles me more the\x01",
            "more I think about it.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xFE, 0x0, 2000, 0xE, 0xF, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #172
        0x1C,
        (
            "#1532FIf only this fountain were full of booze instead\x01",
            "of water. Then I'd at least have something to\x01",
            "keep me company.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #173
        0x102,
        "#1514F...You're kidding me, right?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x1C, 0x102, 400)

    ChrTalk(    #174
        0x1C,
        (
            "#1526FYes, yes. I know.\x02\x03",

            "#1520FI'm pretty familiar with Le Locle since I've\x01",
            "been there myself.\x02\x03",

            "#1520FTake me along if that's where you're planning\x01",
            "on going. I'm sure I could show you around.\x02\x03",

            "#1535FAnd I want to rescue Estelle as much as you\x01",
            "guys do.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x9)
    Jump("loc_70AB")

    label("loc_7003")


    ChrTalk(    #175
        0x1C,
        (
            "#1532F*sigh* This place just baffles me more the more\x01",
            "I think about it.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x1C, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x1)
    Sleep(1500)
    OP_63(0x1C)

    ChrTalk(    #176
        0x1C,
        (
            "#1525F...I wonder how many bottles Aina's gone through\x01",
            "now?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_70AB")

    ClearChrFlags(0xFE, 0x10)
    TalkEnd(0xFE)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_70BC")

    Return()

    # Function_5_41BE end

    def Function_6_70BD(): pass

    label("Function_6_70BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x584, 0)), scpexpr(EXPR_END)), "loc_755D")
    OP_63(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_72BB")
    SetChrFlags(0xFE, 0x10)
    TalkBegin(0xFE)
    OP_62(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)

    ChrTalk(    #177
        0x19,
        (
            "#1543F...Hmm?\x02\x03",

            "Oh...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x0, 400)
    Sleep(300)

    ChrTalk(    #178
        0x19,
        (
            "#1545F...And so the end is finally upon us.\x02\x03",

            "#1544FPart of me would rather remain here than return\x01",
            "to the no-doubt mountains of work that eagerly\x01",
            "await my return, however...\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_72B5")

    ChrTalk(    #179
        0x10D,
        (
            "#272FNot to worry, Olivier. No part of you even has\x01",
            "a choice in the matter.\x02\x03",

            "#270FI'll drag you back to the real world by your ears\x01",
            "if I must.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x10D, 0)

    ChrTalk(    #180
        0x19,
        (
            "#1546FHow could you, dearest Mueller?! Must you\x01",
            "always be so cruel?!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_72B5")

    OP_A2(0xF)
    Jump("loc_7540")

    label("loc_72BB")

    TalkBegin(0xFE)

    ChrTalk(    #181
        0x19,
        (
            "#1545FHeh. Despite being dragged here against my will,\x01",
            "I have to admit that part of me will be sad to\x01",
            "say farewell to this world.\x02\x03",

            "#1540F...Perhaps I should try to add Celeste to my list\x01",
            "of conquests while I still have the chance.\x02\x03",

            "#1541FI'm sure Aidios will forgive me.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7458")

    ChrTalk(    #182
        0x101,
        (
            "#1007FI can smack you at any time, you know.\x02\x03",

            "If she bans you from the garden, you'll only\x01",
            "have yourself to blame.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7458")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_74A2")

    ChrTalk(    #183
        0x102,
        "#1514FYou really are too fearless for your own good...\x02",
    )

    CloseMessageWindow()

    label("loc_74A2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_751C")

    ChrTalk(    #184
        0x103,
        (
            "#1527FHaha. Maybe she'll use her power to throw you \x01",
            "outside the planes and let you fend for yourself.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_751C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7540")

    ChrTalk(    #185
        0x105,
        "#1165FA-Ahaha...\x02",
    )

    CloseMessageWindow()

    label("loc_7540")

    ClearChrFlags(0xFE, 0x10)
    TalkEnd(0xFE)
    OP_62(0xFE, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Jump("loc_A1C4")

    label("loc_755D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x580, 0)), scpexpr(EXPR_END)), "loc_7836")
    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_75F4")
    Jump("loc_7636")

    label("loc_75F4")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_7610")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_7636")

    label("loc_7610")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_762C")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_7636")

    label("loc_762C")

    OP_51(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_7636")

    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_778C")

    ChrTalk(    #186
        0x19,
        (
            "#1540FI'd speculate that there are a fair amount of\x01",
            "gospel facilities in the more remote regions\x01",
            "of the continent.\x02\x03",

            "#1545FI think there were actually a few in the Empire,\x01",
            "too.\x02\x03",

            "States annexed by the Empire tend to grow\x01",
            "weaker economically, which makes facilities\x01",
            "like those invaluable.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xF)
    Jump("loc_782B")

    label("loc_778C")


    ChrTalk(    #187
        0x19,
        (
            "#1545FStates annexed by the Empire tend to grow\x01",
            "weaker economically, you see.\x02\x03",

            "#1540FWithout the church's help, some of said areas\x01",
            "would really struggle.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_782B")

    SetChrSubChip(0xFE, 0)
    TalkEnd(0xFE)
    Jump("loc_A1C4")

    label("loc_7836")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x565, 3)), scpexpr(EXPR_END)), "loc_8195")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4CA, 4)), scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_7CF7")
    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_78DF")
    Jump("loc_7921")

    label("loc_78DF")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_78FB")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_7921")

    label("loc_78FB")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7917")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_7921")

    label("loc_7917")

    OP_51(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_7921")

    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7BEC")

    ChrTalk(    #188
        0x19,
        (
            "#1545FHeh. Sitting here, I can't help but think about\x01",
            "the ancients who lived in the Liber Ark during\x01",
            "its heyday.\x02\x03",

            "#1540FI can't pretend to be an expert on why this\x01",
            "paradise caused ruin by granting people's\x01",
            "wishes...\x02\x03",

            "#1541F...but I still believe people have the right to\x01",
            "wish for their dreams to come true.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7B08")

    ChrTalk(    #189
        0x103,
        (
            "#1523F...Is that an empty glass I spy, Olivier?\x01",
            "This won't do at all.\x02\x03",

            "#1521FShould I pour you another one?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7B7E")

    label("loc_7B08")

    SetChrSubChip(0x1C, 2)

    ChrTalk(    #190
        0x1C,
        (
            "#1523F...Is that an empty glass I spy, Olivier?\x01",
            "This won't do at all.\x02\x03",

            "#1530FShould I pour you another one?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7B7E")

    SetChrSubChip(0x19, 0)
    OP_62(0xFE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(    #191
        0x19,
        (
            "#1546FP-Please, no! Any more and my consciousness\x01",
            "will escape me!\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x1C, 0)
    OP_A2(0xF)
    Jump("loc_7CEC")

    label("loc_7BEC")


    ChrTalk(    #192
        0x19,
        (
            "#1545FHeh. I still believe that people have the right\x01",
            "to wish for their dreams to come true, even if\x01",
            "the Aureole is no longer there to grant them.\x02\x03",

            "#1546FI-I also believe I have the right to refuse libations\x01",
            "in the face of danger. So please! No more!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7CEC")

    SetChrSubChip(0xFE, 0)
    TalkEnd(0xFE)
    Jump("loc_8192")

    label("loc_7CF7")

    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_7D87")
    Jump("loc_7DC9")

    label("loc_7D87")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_7DA3")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_7DC9")

    label("loc_7DA3")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7DBF")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_7DC9")

    label("loc_7DBF")

    OP_51(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_7DC9")

    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    ChrTalk(    #193
        0x102,
        (
            "#1505FBy the way, Olivier?\x02\x03",

            "#1500FWhen we'd arrived in the Empire, Hamel wasn't\x01",
            "sealed off any more.\x02\x03",

            "I heard that had been done on your orders, too.\x02\x03",

            "#1513F...So I just wanted to say thank you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #194
        0x19,
        (
            "#1545FHeh. Think nothing of it.\x02\x03",

            "#1547FWe are soul mates, you and I. I only did\x01",
            "what was natural.\x02\x03",

            "#1541FStill, if you truly wish to thank me...do it\x01",
            "less with sweet words and more with your\x01",
            "ever-sweeter lips.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #195
        0x102,
        (
            "#1514F...Haha...\x02\x03",

            "#1513FYou might be a member of the Imperial family...#400W \x01",
            "#20W...but if anything, I think that would make it\x01",
            "even harder to raise the issue of Hamel.\x02\x03",

            "#1501FSo I really do appreciate you doing what you did.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #196
        0x19,
        (
            "#1540FHaha...\x02\x03",

            "#1545FWell, you're right. With my position, I can't even\x01",
            "get close to the place without leaving an endless\x01",
            "number of scandals in my wake.\x02\x03",

            "Were it up to me, I'd go and place an offering\x01",
            "of flowers there, but alas; I'm going to have to\x01",
            "leave that to you.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2654)
    SetChrSubChip(0xFE, 0)
    TalkEnd(0xFE)

    label("loc_8192")

    Jump("loc_A1C4")

    label("loc_8195")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x564, 0)), scpexpr(EXPR_END)), "loc_8669")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_83C1")
    SetChrFlags(0xFE, 0x10)
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_832F")
    OP_9E(0xFE, 0x14, 0x0, 0x3E8, 0xBB8)

    ChrTalk(    #197
        0x19,
        "#1548FE-Everything is...spinning...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #198
        0x103,
        "#1523FWhat's up with you, Olivier?\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8293")

    ChrTalk(    #199
        0x101,
        (
            "#1016FAre you seriously asking that?\x02\x03",

            "He's like this because you drank him\x01",
            "into oblivion. Duh.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_82F4")

    label("loc_8293")


    ChrTalk(    #200
        0x109,
        (
            "#1061FI think everyone knows full well you're the\x01",
            "cause of this...uhh...poor fellow's woes.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_82F4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_832C")

    ChrTalk(    #201
        0x102,
        "#1508F...Is this really news to you?\x02",
    )

    CloseMessageWindow()

    label("loc_832C")

    Jump("loc_83B3")

    label("loc_832F")

    OP_62(0xFE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(    #202
        0x19,
        (
            "#1546FU-Umm... Schera...\x02\x03",

            "Might you slow your drinking pace just\x01",
            "a teensy little bit?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #203
        0x1C,
        "#1526F*gulp*\x02",
    )

    CloseMessageWindow()

    label("loc_83B3")

    OP_A2(0xF)
    ClearChrFlags(0xFE, 0x10)
    TalkEnd(0xFE)
    Jump("loc_8666")

    label("loc_83C1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8465")
    SetChrFlags(0xFE, 0x10)
    TalkBegin(0xFE)

    ChrTalk(    #204
        0x103,
        (
            "#1527FIf we throw him in the pond, he'll sober right up.\x02\x03",

            "#1530FI say we take him with us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #205
        0x109,
        "#1068F(Y-You're a monster...)\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0xFE, 0x10)
    TalkEnd(0xFE)
    Jump("loc_8666")

    label("loc_8465")

    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_84F5")
    Jump("loc_8537")

    label("loc_84F5")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_8511")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_8537")

    label("loc_8511")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_852D")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_8537")

    label("loc_852D")

    OP_51(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_8537")

    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    ChrTalk(    #206
        0x19,
        (
            "#1542FWhen her mind begins to wander, Schera has a \x01",
            "habit of unconsciously starting to drink faster.\x02\x03",

            "I can't say I mind watching her like that...\x02\x03",

            "#1547F...but trying to keep up with it for too long runs\x01",
            "the risk of knocking me into a coma. Haha.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0)
    TalkEnd(0xFE)
    SetChrSubChip(0xFE, 1)

    label("loc_8666")

    Jump("loc_A1C4")

    label("loc_8669")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x562, 5)), scpexpr(EXPR_END)), "loc_8A28")
    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_8700")
    Jump("loc_8742")

    label("loc_8700")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_871C")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_8742")

    label("loc_871C")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8738")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_8742")

    label("loc_8738")

    OP_51(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_8742")

    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8976")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_88F6")

    ChrTalk(    #207
        0x19,
        (
            "#1540FJulia, Kilika...\x02\x03",

            "#1545FLiberl really does have a frightful number of\x01",
            "dangerous women living there.\x02\x03",

            "#1544FAnd for every docile and doe-eyed young lady\x01",
            "I meet, their...erm...bodyguard...certainly makes\x01",
            "up for it.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_888B")

    ChrTalk(    #208
        0x106,
        "#053FYou say something?\x02",
    )

    CloseMessageWindow()
    Jump("loc_88AB")

    label("loc_888B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_88AB")

    ChrTalk(    #209
        0x107,
        "#064F...Huh?\x02",
    )

    CloseMessageWindow()

    label("loc_88AB")


    ChrTalk(    #210
        0x109,
        (
            "#1077FHaha... I wouldn't be provoking Agate too\x01",
            "much if I was you.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8970")

    label("loc_88F6")


    ChrTalk(    #211
        0x19,
        (
            "#1540FSchera's absolutely right here.\x02\x03",

            "#1541FThe best approach here is to keep calm\x01",
            "and take obstacles as they come.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8970")

    OP_A2(0xF)
    Jump("loc_8A1D")

    label("loc_8976")


    ChrTalk(    #212
        0x19,
        (
            "#1542FStill, if Phantasma is able to recreate people\x01",
            "who are in Calvard, too...\x02\x03",

            "#1551F...we might find ourselves against someone\x01",
            "truly fearsome sooner or later.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8A1D")

    SetChrSubChip(0xFE, 0)
    TalkEnd(0xFE)
    Jump("loc_A1C4")

    label("loc_8A28")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x540, 7)), scpexpr(EXPR_END)), "loc_8D2B")
    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_8ABF")
    Jump("loc_8B01")

    label("loc_8ABF")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_8ADB")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_8B01")

    label("loc_8ADB")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8AF7")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_8B01")

    label("loc_8AF7")

    OP_51(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_8B01")

    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8C92")

    ChrTalk(    #213
        0x19,
        (
            "#1545FHmm... It is an interesting concept, I must say.\x01",
            "Who would have thought this world changes in\x01",
            "accordance to the thoughts and desires of those\x01",
            "within?\x02\x03",

            "If what Renne was saying about discovering that\x01",
            "being one of the conditions to moving on to the\x01",
            "sixth plane is true...\x02\x03",

            "#1540F...then we must be reaching the end of this\x01",
            "particular plane.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xF)
    Jump("loc_8D20")

    label("loc_8C92")


    ChrTalk(    #214
        0x19,
        (
            "#1541FHaha. Still, I never thought this place would test\x01",
            "our reasoning and deductive skills to this extent!\x02\x03",

            "I'm starting to enjoy this.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8D20")

    SetChrSubChip(0xFE, 0)
    TalkEnd(0xFE)
    Jump("loc_A1C4")

    label("loc_8D2B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x540, 4)), scpexpr(EXPR_END)), "loc_9501")
    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_8DC2")
    Jump("loc_8E04")

    label("loc_8DC2")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_8DDE")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_8E04")

    label("loc_8DDE")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8DFA")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_8E04")

    label("loc_8DFA")

    OP_51(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_8E04")

    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9397")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_9100")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_901B")

    ChrTalk(    #215
        0x19,
        "#1543FOh, my...\x02",
    )

    CloseMessageWindow()
    OP_62(0xFE, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0xFE)
    Sleep(300)
    OP_62(0xFE, 0x0, 2000, 0xA, 0xB, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #216
        0x19,
        (
            "#1547FWhat a delightful team you have there.\x02\x03",

            "By all means, come and lay your soft cheeks\x01",
            "upon my person, ladies!\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10F, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(50)
    OP_62(0x107, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #217
        0x101,
        "#1019FDo you have a death wish?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #218
        0x103,
        (
            "#1535FWhat's that? You want me to hang you upside\x01",
            "down by the waterfall? Well, aren't we feeling\x01",
            "naughty today!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #219
        0x19,
        "#1546F...I-I'm sorry! Please, I merely jest.\x02",
    )

    CloseMessageWindow()
    Jump("loc_90FD")

    label("loc_901B")


    ChrTalk(    #220
        0x19,
        (
            "#1540FIf you're looking for Schera, she went to check\x01",
            "up on how that priest is doing.\x02\x03",

            "#1545FWhich means I am alone and in need of comfort!\x01",
            "Which naturally you will be providing, Estelle.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #221
        0x101,
        "#1019FNot a chance, buster.\x02",
    )

    CloseMessageWindow()

    label("loc_90FD")

    Jump("loc_9391")

    label("loc_9100")


    ChrTalk(    #222
        0x19,
        (
            "#1540FTita said that she was feeling a little tired,\x01",
            "you see...\x02\x03",

            "#1541F...so I'm currently in the process of lulling her\x01",
            "into a peaceful slumber with my sweet nothings.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #223
        0x101,
        "#1019F...This just feels like a crime in the making.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_921D")

    ChrTalk(    #224
        0x102,
        "#1505FI have no counter argument.\x02",
    )

    CloseMessageWindow()

    label("loc_921D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_9264")

    ChrTalk(    #225
        0x10D,
        (
            "#272FFunnily enough, I was thinking the same\x01",
            "thing.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9264")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_92B4")

    ChrTalk(    #226
        0x103,
        (
            "#1525FI see that mind of yours is still as filthy as\x01",
            "ever...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_92B4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_92DA")

    ChrTalk(    #227
        0x106,
        "#057F#3S*glare*#2S\x02",
    )

    CloseMessageWindow()

    label("loc_92DA")


    ChrTalk(    #228
        0x19,
        (
            "#1541FHaha. I haven't the faintest clue what you are\x01",
            "all accusing me of!\x02\x03",

            "#1547FI always put the ladies in my life above all else!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #229
        0x101,
        "#1022FYeah, that's exactly the problem...\x02",
    )

    CloseMessageWindow()

    label("loc_9391")

    OP_A2(0xF)
    Jump("loc_94F6")

    label("loc_9397")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_941F")

    ChrTalk(    #230
        0x19,
        (
            "#1551FAh, it just doesn't feel right to be sitting\x01",
            "here alone.\x02\x03",

            "#1542FWould you care to keep me company,\x01",
            "Estelle?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_94F6")

    label("loc_941F")

    SetChrSubChip(0x19, 1)

    ChrTalk(    #231
        0x19,
        (
            "#1540FHeh. Still, her adorable sleeping face does\x01",
            "wonders to stimulate my paternal instincts.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xFE, 0x0, 2000, 0xA, 0xB, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(1500)

    ChrTalk(    #232
        0x19,
        (
            "#1541FPerhaps I should ask her to call me 'Daddy'\x01",
            "after she wakes up? ㈱\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x19, 0)

    label("loc_94F6")

    SetChrSubChip(0xFE, 0)
    TalkEnd(0xFE)
    Jump("loc_A1C4")

    label("loc_9501")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4CA, 3)), scpexpr(EXPR_END)), "loc_9843")
    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9598")
    Jump("loc_95DA")

    label("loc_9598")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_95B4")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_95DA")

    label("loc_95B4")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_95D0")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_95DA")

    label("loc_95D0")

    OP_51(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_95DA")

    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9768")

    ChrTalk(    #233
        0x19,
        (
            "#1551FSo we're dealing with foes who are content\x01",
            "making an enemy out of an extremely powerful\x01",
            "Dominion, are we?\x02\x03",

            "The Schwarzritter and the Lord of Phantasma\x01",
            "will surely be a force to be reckoned with...\x02\x03",

            "#1547F...which is why I'm going to stay here and get\x01",
            "my beauty sleep. I wouldn't stand a chance\x01",
            "against them!\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_9762")

    ChrTalk(    #234
        0x10D,
        "#274F...\x02",
    )

    CloseMessageWindow()

    label("loc_9762")

    OP_A2(0xF)
    Jump("loc_9838")

    label("loc_9768")


    ChrTalk(    #235
        0x19,
        (
            "#1551FSo we're dealing with foes who are content\x01",
            "making an enemy out of an extremely powerful\x01",
            "Dominion, are we?\x02\x03",

            "The Schwarzritter and the Lord of Phantasma\x01",
            "will surely be a force to be reckoned with...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9838")

    SetChrSubChip(0xFE, 0)
    TalkEnd(0xFE)
    Jump("loc_A1C4")

    label("loc_9843")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x540, 0)), scpexpr(EXPR_END)), "loc_9E5B")
    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_98DA")
    Jump("loc_991C")

    label("loc_98DA")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_98F6")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_991C")

    label("loc_98F6")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9912")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_991C")

    label("loc_9912")

    OP_51(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_991C")

    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    ChrTalk(    #236
        0x19,
        (
            "#1542FI've tried looking into the Gralsritter and\x01",
            "the Congregation for the Sacraments myself\x01",
            "before.\x02\x03",

            "#1551FUnfortunately, no amount of research could\x01",
            "have prepared me for the sheer power that\x01",
            "the Dominions seemingly possess.\x02\x03",

            "#1542FIf we're to deal with foes who are comfortable\x01",
            "making an enemy of someone who possesses\x01",
            "such power...this could get very tricky indeed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #237
        0x101,
        (
            "#1002FYeah... From what everyone's said, this Lord\x01",
            "of Phantasma guy doesn't sound like they're\x01",
            "gonna be a walk in the park.\x02\x03",

            "#1011FOh, yeah. While I've got you here...\x02\x03",

            "#1006F...how's that whole plan going these days?\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xFE, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(500)

    ChrTalk(    #238
        0x19,
        "#1543FHmm? Whatever do you mean?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #239
        0x101,
        (
            "#1006FYou know, the one you were heading back to\x01",
            "the Empire to put into action.\x02\x03",

            "#1012FAfter you had us going with that crazy stunt you\x01",
            "pulled back at Haken Gate, you better be putting\x01",
            "your back into it.\x02\x03",

            "#1018FIf you're not, there's a staff here with your name\x01",
            "on it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #240
        0x19,
        (
            "#1543F...\x02\x03",

            "#1540F...Haha. Oh, I see.\x02\x03",

            "#1541FThank you for your words of encouragement, \x01",
            "Estelle. I'll be sure to take them to heart.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #241
        0x101,
        (
            "#1004F...Wait. That's it? No dodging questions or\x01",
            "creepy comments with that dumb grin you've\x01",
            "always got on half the time?\x02\x03",

            "#1002FYou feeling okay, Olivier? Schera didn't drink\x01",
            "you under the table again, did she?\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2653)
    SetChrSubChip(0xFE, 0)
    TalkEnd(0xFE)
    Jump("loc_A1C4")

    label("loc_9E5B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x521, 2)), scpexpr(EXPR_END)), "loc_A1C4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9FFF")
    TalkBegin(0xFF)

    ChrTalk(    #242
        0x19,
        (
            "#1545FIf alcohol is what you desire, my dear Schera,\x01",
            "then I shall be happy to provide!\x02\x03",

            "This beverage I acquired from that great tree\x01",
            "has quite the fragrance--and a taste to match.\x02\x03",

            "#1541F...Unfortunately, however, I haven't a clue of\x01",
            "the maker or year.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #243
        0x102,
        (
            "#1500FYou do know inviting her to drink with you is\x01",
            "going to end with you vomiting in the fountain,\x01",
            "right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #244
        0x19,
        "#1546FI... Uh...\x02",
    )

    CloseMessageWindow()
    OP_A2(0xF)
    TalkEnd(0xFF)
    Jump("loc_A1C4")

    label("loc_9FFF")

    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_A08F")
    Jump("loc_A0D1")

    label("loc_A08F")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_A0AB")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_A0D1")

    label("loc_A0AB")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A0C7")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_A0D1")

    label("loc_A0C7")

    OP_51(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_A0D1")

    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    ChrTalk(    #245
        0x19,
        (
            "#1545FHaha...haha... Dearest Joshua, your concern moves me,\x01",
            "but so long as Aina isn't here, I will persevere!\x02\x03",

            "#1546FWhy are you looking at me like that? I-I WILL be fine,\x01",
            "won't I? ...Won't I?\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0)
    TalkEnd(0xFE)

    label("loc_A1C4")

    Return()

    # Function_6_70BD end

    def Function_7_A1C5(): pass

    label("Function_7_A1C5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4CA, 1)), scpexpr(EXPR_END)), "loc_A58D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A3D7")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A38D")
    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_A272")
    Jump("loc_A2B4")

    label("loc_A272")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_A28E")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_A2B4")

    label("loc_A28E")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A2AA")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_A2B4")

    label("loc_A2AA")

    OP_51(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_A2B4")

    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    ChrTalk(    #246
        0x17,
        (
            "#1160FThis place really is beautiful, though, isn't it?\x02\x03",

            "I'm surprised how at ease I feel here.\x02\x03",

            "#1382FThe trees, the fountain... It's more relaxing than\x01",
            "anything.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0)
    TalkEnd(0xFE)
    Jump("loc_A3D1")

    label("loc_A38D")

    TalkBegin(0xFF)

    ChrTalk(    #247
        0x17,
        (
            "#1169FI see...\x02\x03",

            "So you think that Estelle might have...?\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFF)

    label("loc_A3D1")

    OP_A2(0xD)
    Jump("loc_A58A")

    label("loc_A3D7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A546")
    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_A475")
    Jump("loc_A4B7")

    label("loc_A475")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_A491")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_A4B7")

    label("loc_A491")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A4AD")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_A4B7")

    label("loc_A4AD")

    OP_51(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_A4B7")

    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    ChrTalk(    #248
        0x17,
        (
            "#1383FThis garden is so relaxing, isn't it?\x02\x03",

            "#1160FI'm surprised how at ease I feel here.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0)
    TalkEnd(0xFE)
    Jump("loc_A58A")

    label("loc_A546")

    TalkBegin(0xFF)

    ChrTalk(    #249
        0x17,
        (
            "#1169FI see...\x02\x03",

            "So you think that Estelle might have...?\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFF)

    label("loc_A58A")

    Jump("loc_ADE1")

    label("loc_A58D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x500, 0)), scpexpr(EXPR_END)), "loc_ADE1")
    SetChrFlags(0x17, 0x10)
    TalkBegin(0x17)

    ChrTalk(    #250
        0x17,
        (
            "#1167FI had just finished writing in my diary before \x01",
            "settling down to sleep when I took a glance\x01",
            "out the window.\x02\x03",

            "#1162FWhen I did, I saw a bright light...\x02\x03",

            "#1163F...and next, all I could see was white.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A6D6")

    ChrTalk(    #251
        0x16,
        (
            "#1503FOh, right... You can see the port from your\x01",
            "window in the castle, can't you?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A788")

    label("loc_A6D6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A732")

    ChrTalk(    #252
        0x13,
        (
            "#176FI see... I'd forgotten how you can see the\x01",
            "port from the castle.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A788")

    label("loc_A732")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A788")

    ChrTalk(    #253
        0x15,
        (
            "#213FOh, yeah.\x02\x03",

            "Grancel Castle's right next to the port,\x01",
            "isn't it?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A788")


    ChrTalk(    #254
        0x17,
        (
            "#1167FYes...\x02\x03",

            "So judging by all I've heard, it sounds as though\x01",
            "the first light I saw was the cube activating,\x01",
            "and then I was drawn in here with everyone else.\x02\x03",

            "#1169FIf only I had known what was going to happen,\x01",
            "perhaps I would have been able to do something\x01",
            "after seeing the first light...\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_ABBB")
    TurnDirection(0x10B, 0x17, 0)

    ChrTalk(    #255
        0x10B,
        (
            "#215FThat's... Well...\x02\x03",

            "#210F...Let's look at the positives! We're never gonna\x01",
            "run out of food or water or anything while we're\x01",
            "here, right?\x02\x03",

            "I'll pitch in with the cooking, too, so...don't worry\x01",
            "so much, okay?\x02",
        )
    )

    CloseMessageWindow()
    OP_51(0x10B, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x17, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0x17)
    ClearChrFlags(0x17, 0x10)
    TurnDirection(0x17, 0x10B, 0)
    OP_51(0x17, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x17, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x17, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_AA2E")
    Jump("loc_AA70")

    label("loc_AA2E")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_AA4A")
    OP_51(0x17, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_AA70")

    label("loc_AA4A")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_AA66")
    OP_51(0x17, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_AA70")

    label("loc_AA66")

    OP_51(0x17, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_AA70")

    OP_51(0x17, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x10B, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10B, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x17, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x17, 0x10)

    ChrTalk(    #256
        0x17,
        (
            "#1160FIn that case...perhaps we could cook together\x01",
            "later?\x02\x03",

            "#1165FI'm not a bad chef, if I do say so myself. Heehee.\x01",
            "Besides, I think it'd be easier to calm down if\x01",
            "I could take my mind off things.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #257
        0x10B,
        (
            "#213FOh... Sure thing...\x02\x03",

            "#210F...You know what? Yeah! I'd be totally\x01",
            "up for that!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_ADBB")

    label("loc_ABBB")


    ChrTalk(    #258
        0x15,
        (
            "#215FThat's... Well...\x02\x03",

            "#210F...Let's look at the positives! We're never gonna\x01",
            "run out of food or water or anything while we're\x01",
            "here, right?\x02\x03",

            "I'll pitch in with the cooking, too, so...don't worry\x01",
            "so much, okay?\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x17, 2)

    ChrTalk(    #259
        0x17,
        (
            "#1160FIn that case...perhaps we could cook together\x01",
            "later?\x02\x03",

            "#1165FI'm not a bad chef, if I do say so myself. Heehee.\x01",
            "Besides, I think it'd be easier to calm down if\x01",
            "I could take my mind off things.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #260
        0x15,
        (
            "#213FOh... Sure thing...\x02\x03",

            "#210F...You know what? Yeah! I'd be totally\x01",
            "up for that!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_ADBB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_ADD1")
    SetChrSubChip(0x17, 0)
    Jump("loc_ADD6")

    label("loc_ADD1")

    SetChrSubChip(0x17, 2)

    label("loc_ADD6")

    OP_A2(0x2651)
    ClearChrFlags(0x17, 0x10)
    TalkEnd(0x17)

    label("loc_ADE1")

    Return()

    # Function_7_A1C5 end

    def Function_8_ADE2(): pass

    label("Function_8_ADE2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x565, 3)), scpexpr(EXPR_END)), "loc_B032")
    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_AE79")
    Jump("loc_AEBB")

    label("loc_AE79")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_AE95")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_AEBB")

    label("loc_AE95")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_AEB1")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_AEBB")

    label("loc_AEB1")

    OP_51(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_AEBB")

    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AF5E")

    ChrTalk(    #261
        0x1D,
        (
            "#551FWhew...\x02\x03",

            "#053FOkay, I think it's about time we got moving.\x02\x03",

            "#051FNext up is the seventh plane, right?\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x6)
    Jump("loc_B027")

    label("loc_AF5E")


    ChrTalk(    #262
        0x1D,
        (
            "#053FWe're off to the seventh plane next, right?\x02\x03",

            "#051FThe first place the Lord of Phantasma made\x01",
            "when they came in here or whatever.\x02\x03",

            "We're gonna need to be on guard while we're\x01",
            "there, no doubt.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B027")

    SetChrSubChip(0xFE, 0)
    TalkEnd(0xFE)
    Jump("loc_DA83")

    label("loc_B032")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C9, 7)), scpexpr(EXPR_END)), "loc_B155")
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B0E9")

    ChrTalk(    #263
        0x1D,
        (
            "#053FBack when I first met that old man, he kicked\x01",
            "my sorry ass more times than I can count.\x02\x03",

            "#051FOne day, I'm gonna pay him back tenfold--\x01",
            "count on it.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x6)
    Jump("loc_B14F")

    label("loc_B0E9")


    ChrTalk(    #264
        0x1D,
        (
            "#053FI owe that old man a hell of a lot of beatings.\x02\x03",

            "#051FAnd one day, I'm gonna give him them.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B14F")

    TalkEnd(0xFE)
    Jump("loc_DA83")

    label("loc_B155")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x564, 0)), scpexpr(EXPR_END)), "loc_B61F")
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C7, 1)), scpexpr(EXPR_END)), "loc_B3DF")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B1CB")
    TurnDirection(0x1D, 0x101, 0)

    ChrTalk(    #265
        0x101,
        (
            "#1004FOh. 'Sup, Agate?\x02\x03",

            "#1028FHeehee. So how'd it feel to fight my dad?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B2C4")

    label("loc_B1CB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B23E")
    TurnDirection(0x1D, 0x103, 0)

    ChrTalk(    #266
        0x103,
        (
            "#1520FOh. 'Sup, Agate?\x02\x03",

            "#1521FHaha. So how do you feel after your fight\x01",
            "with Cassius?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B2C4")

    label("loc_B23E")


    ChrTalk(    #267
        0x109,
        (
            "#1066FOh, Agate. Thanks again for pitching in before.\x02\x03",

            "#1060FSure seems like there's a lot between you and\x01",
            "Cassius, though, huh?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B2C4")


    ChrTalk(    #268
        0x1D,
        (
            "#053FHeh. Just beating him once isn't gonna be\x01",
            "enough to settle the score, that's for sure.\x02\x03",

            "#552FBack when I first met that old man, he kicked\x01",
            "my sorry ass more times than I can count.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #269
        0x109,
        "#1064FO-Oh, right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #270
        0x1D,
        (
            "#051FOne day, I'm gonna pay him back tenfold--\x01",
            "count on it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B616")

    label("loc_B3DF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B45D")
    TurnDirection(0x1D, 0x101, 0)

    ChrTalk(    #271
        0x101,
        (
            "#1004FOh, Agate?\x02\x03",

            "#1015FJust so you know, the guardian of the third\x01",
            "area turned out to be Dad...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B545")

    label("loc_B45D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B4E0")
    TurnDirection(0x1D, 0x103, 0)

    ChrTalk(    #272
        0x103,
        (
            "#1523FOh, Agate.\x02\x03",

            "#1520F...Just so you know, the guardian of the third\x01",
            "area turned out to be Cassius.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B545")

    label("loc_B4E0")


    ChrTalk(    #273
        0x109,
        (
            "#1066FUmm... So, uh, Agate?\x02\x03",

            "Just for the record, the guardian of the third\x01",
            "area was Cassius...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B545")


    ChrTalk(    #274
        0x1D,
        (
            "#053F...Yeah, yeah. I already know.\x02\x03",

            "Celeste told me.\x02\x03",

            "#552FI'd be lyin' if I said I wasn't bitter about not\x01",
            "being able to fight him with you...\x02\x03",

            "#556F...but I'll just pay him back another time,\x01",
            "I guess.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B616")

    OP_A2(0x264F)
    TalkEnd(0xFE)
    Jump("loc_DA83")

    label("loc_B61F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x562, 5)), scpexpr(EXPR_END)), "loc_B892")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B813")
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C8, 3)), scpexpr(EXPR_END)), "loc_B73A")

    ChrTalk(    #275
        0x1D,
        (
            "#552FI swear, Kilika's somethin' else.\x02\x03",

            "I always figured she was strict, but come ON.\x02\x03",

            "#053F...Well, whatever.\x02\x03",

            "I guess I'll help out with some of the guild's\x01",
            "workload in Zeiss when I get back.\x02\x03",

            "#051FShe did seem kinda attached to the place\x01",
            "and all.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B80A")

    label("loc_B73A")


    ChrTalk(    #276
        0x1D,
        (
            "#552FI swear, Kilika's somethin' else.\x02\x03",

            "#053F...Well, whatever.\x02\x03",

            "I guess I'll help out with some of the guild's\x01",
            "workload in Zeiss when I get back.\x02\x03",

            "#051FShe did seem kinda attached to the place\x01",
            "and all.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B80A")

    OP_A2(0x6)
    TalkEnd(0xFE)
    Jump("loc_B88F")

    label("loc_B813")

    SetChrFlags(0xFE, 0x10)
    TalkBegin(0xFE)

    ChrTalk(    #277
        0x1D,
        (
            "#057F...Wait. Erika Russell's probably still gonna\x01",
            "be there, isn't she?\x02\x03",

            "#555F......\x02\x03",

            "#552F...Damn it.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    ClearChrFlags(0xFE, 0x10)

    label("loc_B88F")

    Jump("loc_DA83")

    label("loc_B892")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x561, 0)), scpexpr(EXPR_END)), "loc_BAC9")
    SetChrFlags(0xFE, 0x10)
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BA36")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B987")

    ChrTalk(    #278
        0x108,
        "#073FYou doing some training by yourself, Agate?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #279
        0x1D,
        (
            "#051FYep. You're welcome to come join me\x01",
            "if you get the chance. \x02\x03",

            "Pretty sure I'd get better results if I had\x01",
            "a tough old bear like you to fight.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BA30")

    label("loc_B987")


    ChrTalk(    #280
        0x1D,
        (
            "#053FHey. You guys should do some training of your\x01",
            "own, if you ask me.\x02\x03",

            "#051FThere's no tellin' what we've got waiting for us.\x01",
            "No such thing as being too prepared.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BA30")

    OP_A2(0x6)
    Jump("loc_BABE")

    label("loc_BA36")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_BA7D")

    ChrTalk(    #281
        0x1D,
        (
            "#053F*deep breath*\x01",
            "*deep breath*\x02\x03",

            "#057FHaaaaaah!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BABE")

    label("loc_BA7D")


    ChrTalk(    #282
        0x1D,
        (
            "#053FOkay. One more time.\x02\x03",

            "#051FAnd I'm gonna win this one!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BABE")

    TalkEnd(0xFE)
    ClearChrFlags(0xFE, 0x10)
    Jump("loc_DA83")

    label("loc_BAC9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x560, 0)), scpexpr(EXPR_END)), "loc_BED5")
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BE09")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_BBCE")

    ChrTalk(    #283
        0x1D,
        (
            "#053FZin told me somethin' pretty cool earlier.\x02\x03",

            "He says this place is perfect for martial arts\x01",
            "training.\x02\x03",

            "#051FHeh. I might not be into the same combat style\x01",
            "as him, but I'm not gonna say no to a chance to\x01",
            "get stronger.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BCB7")

    label("loc_BBCE")


    ChrTalk(    #284
        0x1D,
        (
            "#053FHey. Zin was sayin' something kinda cool\x01",
            "earlier.\x02\x03",

            "He says this place is perfect for martial arts\x01",
            "training.\x02\x03",

            "#051FHeh. I might not be into the same combat style\x01",
            "as him, but I'm not gonna say no to a chance to\x01",
            "get stronger.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BCB7")

    OP_62(0xFE, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x1)
    Sleep(1400)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_BCFE")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_BCF4")
    TurnDirection(0x106, 0x108, 400)
    Jump("loc_BCFB")

    label("loc_BCF4")

    TurnDirection(0x1D, 0x108, 400)

    label("loc_BCFB")

    Jump("loc_BD1D")

    label("loc_BCFE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_BD16")
    TurnDirection(0x106, 0x1A, 400)
    Jump("loc_BD1D")

    label("loc_BD16")

    TurnDirection(0x1D, 0x1A, 400)

    label("loc_BD1D")


    ChrTalk(    #285
        0x1D,
        (
            "#051FSay, you wanna join me for some sparring later,\x01",
            "Zin?\x02",
        )
    )

    CloseMessageWindow()
    OP_4A(0x1A, 255)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_BD90")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_BD86")
    TurnDirection(0x108, 0x106, 400)
    Jump("loc_BD8D")

    label("loc_BD86")

    TurnDirection(0x1A, 0x106, 400)

    label("loc_BD8D")

    Jump("loc_BDAF")

    label("loc_BD90")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_BDA8")
    TurnDirection(0x108, 0x1D, 400)
    Jump("loc_BDAF")

    label("loc_BDA8")

    TurnDirection(0x1A, 0x1D, 400)

    label("loc_BDAF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_BDDC")

    ChrTalk(    #286
        0x108,
        "#070FHaha. Sure thing.\x02",
    )

    CloseMessageWindow()
    Jump("loc_BDF8")

    label("loc_BDDC")


    ChrTalk(    #287
        0x1A,
        "#070FHaha. Sure thing.\x02",
    )

    CloseMessageWindow()

    label("loc_BDF8")

    OP_4B(0x1A, 255)
    OP_8C(0x1A, 81, 0)
    OP_A2(0x6)
    Jump("loc_BECF")

    label("loc_BE09")


    ChrTalk(    #288
        0x1D,
        (
            "#050FZin told me this place is probably perfect for\x01",
            "martial arts training.\x02\x03",

            "#053FAnd I'm always up for a chance to get my training\x01",
            "on.\x02\x03",

            "#051FBetter take advantage of it while we're still here!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BECF")

    TalkEnd(0xFE)
    Jump("loc_DA83")

    label("loc_BED5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x540, 7)), scpexpr(EXPR_END)), "loc_C12C")
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C013")

    ChrTalk(    #289
        0x1D,
        (
            "#552FAll this crap about how Phantasma's made up is\x01",
            "givin' me a headache...\x02\x03",

            "...but it doesn't take a genius to figure out just\x01",
            "how strong the fiends in it are getting the farther\x01",
            "in we go.\x02\x03",

            "#057FWe're gonna have to get a hell of a lot stronger\x01",
            "if we wanna standing a chance against them.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x6)
    Jump("loc_C126")

    label("loc_C013")


    ChrTalk(    #290
        0x1D,
        (
            "#053FIf the fight against that devil at the end of the\x01",
            "plane's anything to go by, Kevin can handle 'em\x01",
            "just fine...\x02\x03",

            "#057F...but we can't go shovin' the burden of doing the\x01",
            "tough fights onto him every time. We're gonna\x01",
            "need to kick it into high gear at some point, too.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C126")

    TalkEnd(0xFE)
    Jump("loc_DA83")

    label("loc_C12C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C9, 6)), scpexpr(EXPR_END)), "loc_C404")
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C2AE")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xB)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C20E")
    TurnDirection(0x1D, 0x10C, 0)

    ChrTalk(    #291
        0x1D,
        (
            "#051FYou're pretty tough from what I've heard,\x01",
            "Colonel.\x02\x03",

            "So I'm itchin' to fight you one on one while\x01",
            "we've got the chance and see what I can\x01",
            "really do.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #292
        0x10C,
        "#119FHaha... Haha...\x02",
    )

    CloseMessageWindow()
    Jump("loc_C2A8")

    label("loc_C20E")


    ChrTalk(    #293
        0x1D,
        (
            "#051FColonel Richard's supposed to be pretty tough\x01",
            "from what I've heard.\x02\x03",

            "I'm just itchin' to fight him one on one myself\x01",
            "while I've got the chance.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C2A8")

    OP_A2(0x6)
    Jump("loc_C3FE")

    label("loc_C2AE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xB)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C364")
    TurnDirection(0x1D, 0x10C, 0)

    ChrTalk(    #294
        0x1D,
        (
            "#051FYou're pretty tough from what I've heard,\x01",
            "Colonel.\x02\x03",

            "So I'm itchin' to fight you one on one while\x01",
            "we've got the chance and see what I can\x01",
            "really do.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C3FE")

    label("loc_C364")


    ChrTalk(    #295
        0x1D,
        (
            "#051FColonel Richard's supposed to be pretty tough\x01",
            "from what I've heard.\x02\x03",

            "I'm just itchin' to fight him one on one myself\x01",
            "while I've got the chance.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C3FE")

    TalkEnd(0xFE)
    Jump("loc_DA83")

    label("loc_C404")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x540, 4)), scpexpr(EXPR_END)), "loc_D47A")
    TalkBegin(0xFE)
    OP_4A(0x1D, 255)
    OP_4A(0x1B, 255)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xB)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_CCAA")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C5BC")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C518")

    ChrTalk(    #296
        0x1D,
        (
            "#052FOh, if it ain't Estelle and Joshua.\x02\x03",

            "#051FI was talking to Schera earlier, and she told\x01",
            "me somethin' interesting about Anelace.\x02\x03",

            "#051FApparently, she fought our buddy Colonel \x01",
            "Richard here a while back.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C5B9")

    label("loc_C518")


    ChrTalk(    #297
        0x1D,
        (
            "#052FOh, if it ain't Estelle and Joshua.\x02\x03",

            "#051FHey, you heard this thing about Anelace?\x01",
            "Apparently, she fought our buddy Colonel\x01",
            "Richard here a while back.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C5B9")

    Jump("loc_C72D")

    label("loc_C5BC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C697")

    ChrTalk(    #298
        0x1D,
        (
            "#052FOh, if it ain't Estelle.\x02\x03",

            "#051FI was talking to Schera earlier, and she told\x01",
            "me somethin' interesting about Anelace.\x02\x03",

            "#051FApparently, she fought our buddy Colonel \x01",
            "Richard here a while back.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C72D")

    label("loc_C697")


    ChrTalk(    #299
        0x1D,
        (
            "#052FOh, if it ain't Estelle.\x02\x03",

            "#051FHey, you heard this thing about Anelace?\x01",
            "Apparently, she fought our buddy Colonel\x01",
            "Richard here a while back.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C72D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C75D")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C753")
    TurnDirection(0x101, 0x10A, 400)
    Jump("loc_C75A")

    label("loc_C753")

    TurnDirection(0x1E, 0x10A, 400)

    label("loc_C75A")

    Jump("loc_C77C")

    label("loc_C75D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C775")
    TurnDirection(0x101, 0x1B, 400)
    Jump("loc_C77C")

    label("loc_C775")

    TurnDirection(0x1E, 0x1B, 400)

    label("loc_C77C")


    ChrTalk(    #300
        0x101,
        "#1004FWhoa. Really?\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C7C5")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C7BB")
    TurnDirection(0x10A, 0x101, 400)
    Jump("loc_C7C2")

    label("loc_C7BB")

    TurnDirection(0x1B, 0x101, 400)

    label("loc_C7C2")

    Jump("loc_C7E4")

    label("loc_C7C5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C7DD")
    TurnDirection(0x10A, 0x1E, 400)
    Jump("loc_C7E4")

    label("loc_C7DD")

    TurnDirection(0x1B, 0x1E, 400)

    label("loc_C7E4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C883")

    ChrTalk(    #301
        0x10A,
        (
            "#819FHeehee. Yeah, it's true.\x02\x03",

            "I wasn't expecting it to happen, though.\x01",
            "But it was just a friendly bout, so don't\x01",
            "take it too seriously.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C911")

    label("loc_C883")


    ChrTalk(    #302
        0x1B,
        (
            "#819FHeehee. Yeah, it's true.\x02\x03",

            "I wasn't expecting it to happen, either.\x01",
            "But it was just a friendly bout, so don't\x01",
            "take it too seriously.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C911")


    ChrTalk(    #303
        0x10C,
        (
            "#111FIt was just another of Brigadier General Bright's \x01",
            "whims.\x02\x03",

            "#110FStill, I saw no reason to object, so I was happy\x01",
            "to put my swordsmanship to the test.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_CA8D")

    ChrTalk(    #304
        0x101,
        (
            "#1017FO-Oh, right.\x02\x03",

            "#1015FCome to think of it, I've fought you once before,\x01",
            "too, haven't I?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #305
        0x102,
        (
            "#1500FAlthough that was a four-on-one battle, and even\x01",
            "then we barely managed to scrape a victory...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CB56")

    label("loc_CA8D")


    ChrTalk(    #306
        0x101,
        (
            "#1017FO-Oh, right.\x02\x03",

            "#1015FCome to think of it, I've fought you once before,\x01",
            "too, haven't I?\x02\x03",

            "Although that was a four-on-one battle, and even\x01",
            "then we barely managed to scrape by with a victory...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CB56")


    ChrTalk(    #307
        0x10C,
        (
            "#118FHaha... I can't say that occasion is an especially\x01",
            "pleasant memory to me at this point.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x1D, 0x10C, 400)

    ChrTalk(    #308
        0x1D,
        (
            "#051FYou learned your swordsmanship under the\x01",
            "old man directly, right?\x02\x03",

            "I'd be down for a one-on-one fight against\x01",
            "you if you are.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #309
        0x10C,
        (
            "#495F(I fear you're only setting yourself up for\x01",
            "disappointment by comparing me to him...)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D469")

    label("loc_CCAA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_CE42")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_CD9E")

    ChrTalk(    #310
        0x1D,
        (
            "#052FOh, if it ain't Estelle and Joshua.\x02\x03",

            "#051FI was talking to Schera earlier, and she told\x01",
            "me somethin' interesting about Anelace.\x02\x03",

            "#051FApparently, she fought our buddy Colonel \x01",
            "Richard here a while back.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CE3F")

    label("loc_CD9E")


    ChrTalk(    #311
        0x1D,
        (
            "#052FOh, if it ain't Estelle and Joshua.\x02\x03",

            "#051FHey, you heard this thing about Anelace?\x01",
            "Apparently, she fought our buddy Colonel\x01",
            "Richard here a while back.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CE3F")

    Jump("loc_CFB3")

    label("loc_CE42")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_CF1D")

    ChrTalk(    #312
        0x1D,
        (
            "#052FOh, if it ain't Estelle.\x02\x03",

            "#051FI was talking to Schera earlier, and she told\x01",
            "me somethin' interesting about Anelace.\x02\x03",

            "#051FApparently, she fought our buddy Colonel \x01",
            "Richard here a while back.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CFB3")

    label("loc_CF1D")


    ChrTalk(    #313
        0x1D,
        (
            "#052FOh, if it ain't Estelle.\x02\x03",

            "#051FHey, you heard this thing about Anelace?\x01",
            "Apparently, she fought our buddy Colonel\x01",
            "Richard here a while back.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CFB3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_CFE3")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_CFD9")
    TurnDirection(0x101, 0x10A, 400)
    Jump("loc_CFE0")

    label("loc_CFD9")

    TurnDirection(0x1E, 0x10A, 400)

    label("loc_CFE0")

    Jump("loc_D002")

    label("loc_CFE3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_CFFB")
    TurnDirection(0x101, 0x1B, 400)
    Jump("loc_D002")

    label("loc_CFFB")

    TurnDirection(0x1E, 0x1B, 400)

    label("loc_D002")


    ChrTalk(    #314
        0x101,
        "#1004FWhoa. Really?\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D06E")

    ChrTalk(    #315
        0x103,
        (
            "#1525FI couldn't believe my ears when I first heard it,\x01",
            "either.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D06E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D09E")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D094")
    TurnDirection(0x10A, 0x101, 400)
    Jump("loc_D09B")

    label("loc_D094")

    TurnDirection(0x1B, 0x101, 400)

    label("loc_D09B")

    Jump("loc_D0BD")

    label("loc_D09E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D0B6")
    TurnDirection(0x10A, 0x1E, 400)
    Jump("loc_D0BD")

    label("loc_D0B6")

    TurnDirection(0x1B, 0x1E, 400)

    label("loc_D0BD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D15C")

    ChrTalk(    #316
        0x10A,
        (
            "#819FHeehee. Yeah, it's true.\x02\x03",

            "I wasn't expecting it to happen, though.\x01",
            "But it was just a friendly bout, so don't\x01",
            "take it too seriously.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D1EA")

    label("loc_D15C")


    ChrTalk(    #317
        0x1B,
        (
            "#819FHeehee. Yeah, it's true.\x02\x03",

            "I wasn't expecting it to happen, though.\x01",
            "But it was just a friendly bout, so don't\x01",
            "take it too seriously.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D1EA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D2CB")

    ChrTalk(    #318
        0x101,
        (
            "#1017FHuh. Never would've guessed.\x02\x03",

            "#1015FI mean, I've fought him once before,\x01",
            "too, but it's still weird.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #319
        0x102,
        (
            "#1500FYeah. But that fight was four against one,\x01",
            "and even then we barely scraped a victory.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D399")

    label("loc_D2CB")


    ChrTalk(    #320
        0x101,
        (
            "#1017FHuh. Never would've guessed.\x02\x03",

            "#1015FI mean, I've fought him once before,\x01",
            "too, but it's still weird.\x02\x03",

            "Yeah. But that fight was four against one,\x01",
            "and even then we barely scraped by with\x01",
            "a victory.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D399")


    ChrTalk(    #321
        0x1D,
        (
            "#053FWell, you know someone's gonna be tough\x01",
            "when your old man's the one who trained\x01",
            "him with a sword.\x02\x03",

            "#051FI'd be down for a one-on-one fight against\x01",
            "him if he is. Hell, maybe I should go ask him\x01",
            "now.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D469")

    OP_4B(0x1D, 255)
    OP_4B(0x1B, 255)
    OP_A2(0x264E)
    TalkEnd(0xFE)
    Jump("loc_DA83")

    label("loc_D47A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x540, 0)), scpexpr(EXPR_END)), "loc_D628")
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D590")

    ChrTalk(    #322
        0x1D,
        (
            "#552FDominion or not, I dunno what that priest\x01",
            "was thinking goin' nuts and knockin' himself\x01",
            "out cold.\x02\x03",

            "#053FHe could've ran what he was plannin' past us\x01",
            "first before becoming dead weight.\x02\x03",

            "Some people, I swear.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #323
        0x101,
        "#1019FLook who's talking, bucko.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x6)
    Jump("loc_D622")

    label("loc_D590")


    ChrTalk(    #324
        0x1D,
        (
            "#552FI always figured Kevin was more than he\x01",
            "let on...\x02\x03",

            "#053FDidn't think he'd go using some superpower\x01",
            "and collapsin' on us like this. Bah.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D622")

    TalkEnd(0xFE)
    Jump("loc_DA83")

    label("loc_D628")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C6, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D968")
    SetChrFlags(0xFE, 0x10)
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D64D")
    Call(3, 2)
    Jump("loc_D965")

    label("loc_D64D")

    TurnDirection(0x1D, 0x107, 0)

    ChrTalk(    #325
        0x107,
        (
            "#067FI'm so glad you're okay, though!\x02\x03",

            "#560FI was already worried about whether you were\x01",
            "drawn here, but not knowing if you were okay\x01",
            "was--\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #326
        0x1D,
        (
            "#551FOkay, I get it! Stop hugging me!\x02\x03",

            "#050FBesides...\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x107, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #327
        0x1D,
        (
            "#552F...never mind me. You haven't been gettin'\x01",
            "yourself hurt while I was away, have you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #328
        0x107,
        (
            "#565FUmm...\x02\x03",

            "N-No. I'm okay...\x02\x03",

            "#067FI had lots of people looking out for me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #329
        0x1D,
        (
            "#053FReally?\x02\x03",

            "#051FWell, that's good.\x02\x03",

            "Now all that's left is to save the other guys who\x01",
            "ended up trapped in stones and get the hell out \x01",
            "of this weird place.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x1D, 0x109, 400)

    ChrTalk(    #330
        0x1D,
        (
            "#050FNext time you're heading out, take me with you.\x02\x03",

            "I don't feel like I'm gonna get what's going on\x01",
            "unless I see it all for myself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #331
        0x109,
        "#1066FHaha. Daaamn. Someone's motivated.\x02",
    )

    CloseMessageWindow()
    OP_8C(0x1D, 224, 0)
    TalkEnd(0xFE)
    ClearChrFlags(0xFE, 0x10)
    OP_A2(0x2631)

    label("loc_D965")

    Jump("loc_DA83")

    label("loc_D968")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D9A7")
    SetChrFlags(0xFE, 0x10)
    TalkBegin(0xFE)

    ChrTalk(    #332
        0x1D,
        (
            "#555FO-Oh...\x02\x03",

            "R-Right...\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xFE, 0x10)
    TalkEnd(0xFE)
    Jump("loc_DA83")

    label("loc_D9A7")

    TalkBegin(0xFE)

    ChrTalk(    #333
        0x1D,
        (
            "#053FI'm not doing any good standing around here \x01",
            "wasting time.\x02\x03",

            "#051FTake me with you next time you head out, okay?\x01",
            "I wanna get a handle on the situation we're in,\x01",
            "and going with you's the best way to do it.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)

    label("loc_DA83")

    Return()

    # Function_8_ADE2 end

    SaveToFile()

Try(main)

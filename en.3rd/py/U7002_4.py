from ED63RDScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'U7002_4 ._SN',
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
        "Function_3_EF4",          # 03, 3
        "Function_4_1C5C",         # 04, 4
        "Function_5_2594",         # 05, 5
        "Function_6_2F3F",         # 06, 6
        "Function_7_3907",         # 07, 7
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

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x561, 0)), scpexpr(EXPR_END)), "loc_321")
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_229")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C7, 6)), scpexpr(EXPR_END)), "loc_18B")

    ChrTalk(    #0
        0x15,
        "#216FWhat was up with that old man we fought?\x02",
    )

    CloseMessageWindow()
    OP_62(0xFE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1300)

    ChrTalk(    #1
        0x15,
        "#214F#3SHe's frickin' weird!#2S\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x109,
        (
            "#1061FOuch...\x02\x03",

            "#1066FCan't you think of a slightly nicer way of \x01",
            "putting that?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_223")

    label("loc_18B")


    ChrTalk(    #3
        0x15,
        (
            "#215FWhy did someone who should be our ally\x01",
            "get recreated here and end up being our\x01",
            "enemy?\x02\x03",

            "...\x02\x03",

            "#413FI don't even know what's going on anymore...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_223")

    OP_A2(0x5)
    Jump("loc_31B")

    label("loc_229")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C7, 6)), scpexpr(EXPR_END)), "loc_2B2")

    ChrTalk(    #4
        0x15,
        (
            "#216FHe looked like a really serious, polite old man...\x01",
            "How can he be so strong?\x02\x03",

            "#214F#3SThat's just frickin' weird!#2S\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_31B")

    label("loc_2B2")


    ChrTalk(    #5
        0x15,
        (
            "#413FI don't even know what's going on anymore...\x02\x03",

            "#215FAre we even GOING to be able to go home...?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_31B")

    TalkEnd(0xFE)
    Jump("loc_EF3")

    label("loc_321")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x500, 0)), scpexpr(EXPR_END)), "loc_6EC")
    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3B8")
    Jump("loc_3FA")

    label("loc_3B8")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3D4")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3FA")

    label("loc_3D4")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3F0")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3FA")

    label("loc_3F0")

    OP_51(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3FA")

    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_635")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_52A")

    ChrTalk(    #6
        0x15,
        (
            "#215FMaybe it's just me, but it's kinda sorta maybe\x01",
            "a bad idea to lock the next queen of Liberl in\x01",
            "one of those sealing stones, right?\x02\x03",

            "#416FThat Lord of Phantasma should get the death\x01",
            "penalty when we catch him!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x105,
        "#1165FAha...haha...\x02",
    )

    CloseMessageWindow()
    Jump("loc_62F")

    label("loc_52A")


    ChrTalk(    #8
        0x15,
        (
            "#215FUhh... Kloe's the crown princess of Liberl,\x01",
            "right?\x02\x03",

            "Maybe it's just me, but its kinda sorta maybe\x01",
            "a bad idea to lock someone like that in one of\x01",
            "those sealing stones, right?\x02\x03",

            "#416FThat Lord of Phantasma should get the death\x01",
            "penalty when we catch him!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_62F")

    OP_A2(0x5)
    Jump("loc_6E1")

    label("loc_635")


    ChrTalk(    #9
        0x15,
        (
            "#416FNow, I'm not in much of a position to be\x01",
            "judging people here...\x02\x03",

            "#212F...but the Lord of Phantasma should get the\x01",
            "death penalty when we catch him, if you ask\x01",
            "me!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6E1")

    SetChrSubChip(0xFE, 0)
    TalkEnd(0xFE)
    Jump("loc_EF3")

    label("loc_6EC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4E2, 4)), scpexpr(EXPR_END)), "loc_8D3")
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_849")

    ChrTalk(    #10
        0x15,
        (
            "#210FWell, getting stuck here comes with its perks,\x01",
            "at least. I can deal with weird if Joshua's here\x01",
            "to experience it with me!\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_79A")
    TurnDirection(0x15, 0x102, 400)
    Jump("loc_7A1")

    label("loc_79A")

    TurnDirection(0x15, 0x16, 400)

    label("loc_7A1")

    Sleep(300)

    ChrTalk(    #11
        0x15,
        (
            "#211FSay, you wanna go walk around bizarro Grancel \x01",
            "later? Just the two of us?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x109,
        (
            "#1840FI see that you have a knack for looking on the\x01",
            "bright side...\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x5)
    Jump("loc_8CD")

    label("loc_849")


    ChrTalk(    #13
        0x15,
        (
            "#211FWell, getting stuck here comes with its perks,\x01",
            "at least. I can deal with weird if Joshua's here\x01",
            "to experience it with me!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8CD")

    TalkEnd(0xFE)
    Jump("loc_EF3")

    label("loc_8D3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4CB, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E38")
    TalkBegin(0xFE)

    ChrTalk(    #14
        0x15,
        (
            "#214FJust what IS this place?!\x02\x03",

            "#215FEverything here is just so...off. How's that fountain\x01",
            "floating there? Why's there a library in the middle of\x01",
            "nowhere?\x02\x03",

            "#214FAnd what'd happen to you if you fell off the edge\x01",
            "here, anyway? It's not like there're any railings to\x01",
            "catch us!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x109,
        (
            "#1065F(Poor thing looks so worked up...\x01",
            "and I can really blame her.)\x02\x03",

            "#1071FUmm...\x02\x03",

            "#1062FSay, you said you were flying over Crossbell\x01",
            "when you ended up here, right?\x02\x03",

            "#1066FDoes your company do international deliveries\x01",
            "and stuff, then?\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xFE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    TurnDirection(0xFE, 0x109, 400)

    ChrTalk(    #16
        0x15,
        (
            "#215FOh... Yeah.\x02\x03",

            "#212FI-I mean, of course we do! We're originally\x01",
            "from Erebonia, after all, why would we want\x01",
            "to limit ourselves to just Liberl?\x02\x03",

            "We make deliveries aaaall over the continent!\x02\x03",

            "#210FWhen you think of it that way, Crossbell's like\x01",
            "our own back yard.\x02\x03",

            "We've been as far as Leman State a few times,\x01",
            "even.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_CA4")

    ChrTalk(    #17
        0x107,
        (
            "#064FWow! You seriously travel that far?\x02\x03",

            "#067FThat's amazing...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CCF")

    label("loc_CA4")


    ChrTalk(    #18
        0x109,
        (
            "#1064FReally?\x02\x03",

            "That's pretty amazing.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CCF")


    ChrTalk(    #19
        0x15,
        (
            "#210FHaha! Never underestimate what the Bobcat's\x01",
            "capable of!\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D7F")

    ChrTalk(    #20
        0x10D,
        "#272FJust don't forget: you still have a debt to pay off.\x02",
    )

    CloseMessageWindow()
    OP_62(0xFE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    TurnDirection(0xFE, 0x10D, 500)
    Sleep(1000)
    Jump("loc_DDC")

    label("loc_D7F")


    ChrTalk(    #21
        0x14,
        "#272FJust don't forget: you still have a debt to pay off.\x02",
    )

    CloseMessageWindow()
    OP_62(0xFE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    TurnDirection(0xFE, 0x14, 500)
    Sleep(1000)

    label("loc_DDC")


    ChrTalk(    #22
        0x15,
        (
            "#214FI-I wouldn't dare! We're working very hard on that,\x01",
            "thank you very much!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x265A)
    TalkEnd(0xFE)
    Jump("loc_EF3")

    label("loc_E38")

    TalkBegin(0xFE)

    ChrTalk(    #23
        0x15,
        (
            "#215FEverything here is just so off...\x02\x03",

            "How's that fountain floating there, anyway? \x01",
            "And why's there a library in the middle of \x01",
            "nowhere?\x02\x03",

            "#413FI hope Don and Kyle are okay...\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)

    label("loc_EF3")

    Return()

    # Function_2_AC end

    def Function_3_EF4(): pass

    label("Function_3_EF4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x500, 0)), scpexpr(EXPR_END)), "loc_12BC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10CB")
    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_F93")
    Jump("loc_FD5")

    label("loc_F93")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_FAF")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_FD5")

    label("loc_FAF")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_FCB")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_FD5")

    label("loc_FCB")

    OP_51(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_FD5")

    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    ChrTalk(    #24
        0x13,
        (
            "#170FI'm simply glad that Her Highness is safe and well.\x02\x03",

            "#175FStill, there seems to be every chance that plenty\x01",
            "of others have been captured in the same way.\x02\x03",

            "#176FWe should hurry on and aid them.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)
    Jump("loc_12B1")

    label("loc_10CB")

    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_115B")
    Jump("loc_119D")

    label("loc_115B")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1177")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_119D")

    label("loc_1177")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1193")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_119D")

    label("loc_1193")

    OP_51(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_119D")

    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    ChrTalk(    #25
        0x13,
        (
            "#176FI'm still shocked that the Grancel we explored\x01",
            "was a replica of the real thing given its scale...\x02\x03",

            "#178FBut one thing is certain now:\x02\x03",

            "That Lord of Phantasma we encountered is the\x01",
            "one responsible for all of this. I'm sure of it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_12B1")

    SetChrSubChip(0xFE, 0)
    TalkEnd(0xFE)
    Jump("loc_1C5B")

    label("loc_12BC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4E1, 7)), scpexpr(EXPR_END)), "loc_1695")
    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1353")
    Jump("loc_1395")

    label("loc_1353")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_136F")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1395")

    label("loc_136F")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_138B")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1395")

    label("loc_138B")

    OP_51(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1395")

    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_15A3")

    ChrTalk(    #26
        0x13,
        (
            "#176F...It's depressing just how many questions and\x01",
            "how few answers we have at this point, really.\x02\x03",

            "#175FThe place we stand in now is a mystery, the state\x01",
            "of the capital is a mystery, why there are fiends\x01",
            "roaming about it is a mystery...\x02\x03",

            "To say nothing of how we've already come face\x01",
            "to face with a genuine devil from the church's\x01",
            "scriptures.\x02\x03",

            "#176FAnd yet as frustrating as it is, all we can do is\x01",
            "keep pressing on and pray the truth presents\x01",
            "itself to us eventually.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)
    Jump("loc_168A")

    label("loc_15A3")


    ChrTalk(    #27
        0x13,
        (
            "#175FRight now, I want nothing more than to break\x01",
            "the seal blocking the castle's gates and find out\x01",
            "if Her Majesty and Her Highness are safe...\x02\x03",

            "Yet all we can do right now is press on with our\x01",
            "exploration... How frustrating.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_168A")

    SetChrSubChip(0xFE, 0)
    TalkEnd(0xFE)
    Jump("loc_1C5B")

    label("loc_1695")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C6, 7)), scpexpr(EXPR_END)), "loc_17E9")
    TalkBegin(0xFE)

    ChrTalk(    #28
        0x13,
        (
            "#178FThis place truly is baffling... Just where are we?\x02\x03",

            "I've heard about the shadow towers you explored\x01",
            "so I can understand the similarity with them, but\x01",
            "beyond that...\x02\x03",

            "#176F...Never mind. I suppose at this point, no amount of\x01",
            "thinking is going to give us an answer. We just have\x01",
            "too little information to work with.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Jump("loc_1C5B")

    label("loc_17E9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4E1, 0)), scpexpr(EXPR_END)), "loc_1C5B")
    SetChrFlags(0xFE, 0x10)
    TalkBegin(0xFE)

    ChrTalk(    #29
        0x13,
        (
            "#176FI can't believe what's happened to the capital...\x02\x03",

            "#175FI can only pray that Her Majesty and Her Highness\x01",
            "are all right...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x109,
        "#1060FListen, Julia... I know how you must feel, but...\x02",
    )

    CloseMessageWindow()
    OP_62(0xFE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0x13, 0x109, 400)

    ChrTalk(    #31
        0x13,
        (
            "#170FOh, I'm sorry, Father.\x02\x03",

            "#176FI'm still having trouble taking in the current\x01",
            "situation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x109,
        (
            "#1065FI don't think anyone can blame you for that.\x02\x03",

            "#1068FHonestly, I'm still kinda reeling from the shock\x01",
            "of it all myself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x10D,
        (
            "#276FI can't pretend to be all that well versed in our\x01",
            "current predicament...\x02\x03",

            "#270F...but by the sounds of it, our enemies are still\x01",
            "very much an unknown quantity.\x02\x03",

            "I think it would be in all our best interests\x01",
            "to try and keep a cool head and approach\x01",
            "the situation cautiously.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x13,
        "#175FYes... You're absolutely right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x10F,
        (
            "#1440FThere's no telling when we might next find \x01",
            "ourselves facing another deadly foe.\x02\x03",

            "#1446FSo we would appreciate you remaining here\x01",
            "and preparing to be ready to leave any time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x13,
        (
            "#176F...Understood.\x02\x03",

            "#170FThis area appears to be safe, thankfully.\x02\x03",

            "I will prepare myself to the best of my ability,\x01",
            "so leave that to me.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2637)
    TalkEnd(0xFE)

    label("loc_1C5B")

    Return()

    # Function_3_EF4 end

    def Function_4_1C5C(): pass

    label("Function_4_1C5C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x562, 5)), scpexpr(EXPR_END)), "loc_2593")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x562, 6)), scpexpr(EXPR_END)), "loc_2066")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x562, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F7C")
    SetChrFlags(0xFE, 0x10)
    TalkBegin(0xFE)
    RunExpression(0x2, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_62(0xFE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0xFE, 15)
    SetChrSubChip(0xFE, 0)
    TurnDirection(0xFE, 0xEE, 0)
    Sleep(300)

    ChrTalk(    #37
        0x1F,
        "#113FOh... Can I help you with anything?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x109,
        "#1078FWell...\x02",
    )

    CloseMessageWindow()
    EventBegin(0x0)
    Fade(500)
    SetChrPos(0xEE, -67750, 4120, -15480, 296)
    SetChrPos(0xEF, -66720, 4120, -14920, 281)
    SetChrPos(0xF0, -67510, 4120, -17140, 301)
    SetChrPos(0xF1, -66430, 4120, -16400, 321)
    OP_6D(-67750, 4120, -15480, 0)
    OP_67(0, 7900, -10000, 0)
    OP_6B(2530, 0)
    OP_6C(0, 0)
    OP_6E(450, 0)
    TurnDirection(0xFE, 0xEE, 0)
    OP_0D()
    Sleep(300)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(72, 320, 56, 3)

    AnonymousTalk(    #39
        (
            "\x07\x05Kevin explained to Richard that they thought he was the person the carnelia\x01",
            "monument's inscription was asking for.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    ChrTalk(    #40
        0x1F,
        (
            "#113FMe? The 'Divine Blade's successor'?\x02\x03",

            "#116FB-But...\x02\x03",

            "#115F...I suppose there's no point in debating if I am\x01",
            "fit to be called his successor. No one else seems\x01",
            "to match the description, after all.\x02\x03",

            "#110FI'd be happy to accompany you when you return\x01",
            "to that monument.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0x109,
        "#1077FThanks.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2B17)
    Sleep(300)
    EventEnd(0x0)
    TalkEnd(0xFE)
    ClearChrFlags(0xFE, 0x10)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_67(0, 3620, -10000, 1000)
    Jump("loc_2063")

    label("loc_1F7C")

    TalkBegin(0xFE)

    ChrTalk(    #42
        0x1F,
        (
            "#116FI hardly think myself fit to be called the Divine\x01",
            "Blade's successor...\x02\x03",

            "#115FThen again, I suppose that isn't really the issue\x01",
            "here.\x02\x03",

            "#110FWhen you intend to return to that monument,\x01",
            "call on me. I'll accompany you.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)

    label("loc_2063")

    Jump("loc_2593")

    label("loc_2066")

    SetChrFlags(0xFE, 0x10)
    TalkBegin(0xFE)
    RunExpression(0x2, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2481")
    EventBegin(0x0)
    Fade(500)
    OP_6D(-68630, 4120, -16430, 0)
    OP_67(0, 5640, -10000, 0)
    OP_6B(2240, 0)
    OP_6C(180000, 0)
    OP_6E(403, 0)
    SetChrPos(0xEE, -67570, 4120, -15720, 315)
    SetChrPos(0xEF, -66080, 4120, -15490, 315)
    SetChrPos(0xF0, -67810, 4120, -17260, 315)
    SetChrPos(0xF1, -66170, 4120, -17290, 315)
    OP_0D()
    Sleep(300)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2164")

    ChrTalk(    #43
        0x10A,
        (
            "#814F#5PUmm... Colonel, are you practicing your draw\x01",
            "techniques?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_21E4")

    label("loc_2164")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_21B2")

    ChrTalk(    #44
        0x101,
        "#1011F#5PUmm... Colonel, are you training or something?\x02",
    )

    CloseMessageWindow()
    Jump("loc_21E4")

    label("loc_21B2")


    ChrTalk(    #45
        0x109,
        "#1064F#5PYou training or something, Colonel?\x02",
    )

    CloseMessageWindow()

    label("loc_21E4")


    ChrTalk(    #46
        0x1F,
        "#119F#12POh, no...\x02",
    )

    CloseMessageWindow()
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x1F, 15)
    SetChrSubChip(0x1F, 0)
    OP_0D()
    Sleep(300)

    ChrTalk(    #47
        0x1F,
        (
            "#115F#12PIt's just that surrounded by so many skilled\x01",
            "warriors, I can't help but be reminded of just\x01",
            "how feeble my own swordsmanship is.\x02\x03",

            "I'm unable to perfect it and reach the heights\x01",
            "others have, but I'm unable to turn my back on\x01",
            "it, either.\x02\x03",

            "#110FStill, I feel as though by coming here and honing\x01",
            "my senses, I may be able to see something new.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0x109,
        "#1063F#5PO-Oh...\x02",
    )

    CloseMessageWindow()
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x1F, 40)
    SetChrSubChip(0x1F, 0)
    OP_0D()
    Sleep(500)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6D(-66850, 4120, -16340, 0)
    OP_67(0, 3620, -10000, 0)
    OP_6B(2530, 0)
    OP_6C(270000, 0)
    OP_6E(450, 0)
    SetChrPos(0x0, -66850, 4120, -16340, 315)
    SetChrPos(0x1, -66850, 4120, -16340, 315)
    SetChrPos(0x2, -66850, 4120, -16340, 315)
    SetChrPos(0x3, -66850, 4120, -16340, 315)
    SetChrChipByIndex(0x0, 65535)
    SetChrChipByIndex(0x1, 65535)
    SetChrChipByIndex(0x2, 65535)
    SetChrChipByIndex(0x3, 65535)
    SetChrSubChip(0x0, 0)
    SetChrSubChip(0x1, 0)
    SetChrSubChip(0x2, 0)
    SetChrSubChip(0x3, 0)
    OP_69(0x0, 0x0)
    Sleep(500)
    FadeToBright(1000, 0)
    SetMapFlags(0x1)
    ClearMapFlags(0x80)
    EventEnd(0x2)
    OP_A2(0xB)
    Jump("loc_2582")

    label("loc_2481")


    ChrTalk(    #49
        0x1F,
        (
            "#115FMy swordsmanship is a feeble, halfhearted thing...\x02\x03",

            "Still, I feel as though by coming here and honing\x01",
            "my senses, I may be able to see something new.\x02\x03",

            "#110FI couldn't tell you why I feel that way--there's just\x01",
            "something...calming about doing this.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2582")

    ClearChrFlags(0xFE, 0x10)
    TalkEnd(0xFE)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2593")

    Return()

    # Function_4_1C5C end

    def Function_5_2594(): pass

    label("Function_5_2594")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x500, 0)), scpexpr(EXPR_END)), "loc_2835")
    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_262B")
    Jump("loc_266D")

    label("loc_262B")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2647")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_266D")

    label("loc_2647")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2663")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_266D")

    label("loc_2663")

    OP_51(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_266D")

    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2779")

    ChrTalk(    #50
        0x14,
        (
            "#272FIt's clear the Lord of Phantasma is not a\x01",
            "foe to be underestimated.\x02\x03",

            "Unfortunately, we just don't have enough\x01",
            "information to try and work out who they\x01",
            "really are.\x02\x03",

            "#276FIf only we had more clues to go on...\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)
    Jump("loc_282A")

    label("loc_2779")


    ChrTalk(    #51
        0x14,
        (
            "#276FI'm curious as to who that ghost that appeared\x01",
            "in Grancel Castle is, too.\x02\x03",

            "And sadly, we're left with no more clues towards\x01",
            "solving that mystery than we do any other.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_282A")

    SetChrSubChip(0xFE, 0)
    TalkEnd(0xFE)
    Jump("loc_2F3E")

    label("loc_2835")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4E1, 7)), scpexpr(EXPR_END)), "loc_2B40")
    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_28CC")
    Jump("loc_290E")

    label("loc_28CC")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_28E8")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_290E")

    label("loc_28E8")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2904")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_290E")

    label("loc_2904")

    OP_51(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_290E")

    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2A58")

    ChrTalk(    #52
        0x14,
        (
            "#272FNow that we know the existence of that 'lord'\x01",
            "that man mentioned, I can't help but wonder\x01",
            "whether all of this is their work.\x02\x03",

            "And if it is, is it possible that defeating them \x01",
            "might be all that's required for us to escape?\x02\x03",

            "#270FIt would certainly make matters simple.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)
    Jump("loc_2B35")

    label("loc_2A58")


    ChrTalk(    #53
        0x14,
        (
            "#270FIf the only thing keeping us from escaping\x01",
            "this place is defeating our enemies, then it\x01",
            "would certainly make things simple.\x02\x03",

            "#276FIn theory, at least... Defeating them may\x01",
            "prove to be quite difficult in itself.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2B35")

    SetChrSubChip(0xFE, 0)
    TalkEnd(0xFE)
    Jump("loc_2F3E")

    label("loc_2B40")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C7, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2E73")

    ChrTalk(    #54
        0x109,
        (
            "#1078FBoy, am I glad to have you with us.\x02\x03",

            "#1077FThe more brute strength we've got with us,\x01",
            "the better.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0x10E,
        (
            "#170FIndeed. Our odds of success here felt rather \x01",
            "grim until you joined us, Major.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0x14,
        (
            "#270FI'm not sure how much of a difference I alone\x01",
            "make in that regard. I feel as apprehensive\x01",
            "about our current situation as you likely do.\x02\x03",

            "However, if we have enemies here who wish\x01",
            "us harm, then I can't stand back idly and do\x01",
            "nothing.\x02\x03",

            "#276FNot until I know for sure whether or not that\x01",
            "fool's been caught up in all this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0x10E,
        (
            "#172FI see...\x02\x03",

            "#178FThat's true, I suppose.\x02\x03",

            "Still, if our current predicament is the work of\x01",
            "our enemies...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0x14,
        (
            "#272FI'm sure our questions will be answered so long\x01",
            "as we keep looking.\x02\x03",

            "In the meantime, let me know if you need me.\x01",
            "I'll be more than happy to aid you.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2638)
    Jump("loc_2F3B")

    label("loc_2E73")


    ChrTalk(    #59
        0x14,
        (
            "#276FWe may know very little about who our enemies\x01",
            "are and what they want...\x02\x03",

            "#272F...but we can't afford to just ignore them.\x02\x03",

            "So let me know if you need me. I'll be more than\x01",
            "happy to aid you.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2F3B")

    TalkEnd(0xFE)

    label("loc_2F3E")

    Return()

    # Function_5_2594 end

    def Function_6_2F3F(): pass

    label("Function_6_2F3F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x565, 3)), scpexpr(EXPR_END)), "loc_353D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4CA, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_34BA")
    SetChrFlags(0xFE, 0x10)
    TalkBegin(0xFE)
    SetChrSubChip(0xFE, 0)
    Sleep(300)

    ChrTalk(    #60
        0x20,
        (
            "#263FOh, good evening. It's a lovely night, isn't it?\x02\x03",

            "#260FIt's a shame we can't see the moon from here,\x01",
            "but the stars are pretty enough to make up for\x01",
            "that.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3095")

    ChrTalk(    #61
        0x102,
        "#1503FRenne...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0x20,
        (
            "#1300F...Don't say anything, Joshua.\x02\x03",

            "I knew everything from the very beginning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0x102,
        "#1505F...Okay...\x02",
    )

    CloseMessageWindow()
    Jump("loc_31F8")

    label("loc_3095")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_31B1")

    ChrTalk(    #64
        0x101,
        "#1003FUmm... Renne...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0x20,
        (
            "#1300FLoewe...\x02\x03",

            "Loewe taught me all kinds of things, but whenever\x01",
            "I asked him to tell me 'the truth' about something,\x01",
            "he never would.\x02\x03",

            "#268F'The truth is something you have to find out for \x01",
            "yourself,' he would say.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0x101,
        "#1025F...Oh...\x02",
    )

    CloseMessageWindow()
    Jump("loc_31F8")

    label("loc_31B1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_31DC")

    ChrTalk(    #67
        0x107,
        "#063FUmm... Renne...\x02",
    )

    CloseMessageWindow()
    Jump("loc_31F8")

    label("loc_31DC")


    ChrTalk(    #68
        0x109,
        "#1840FUmm... Renne...?\x02",
    )

    CloseMessageWindow()

    label("loc_31F8")


    ChrTalk(    #69
        0x20,
        "#261FHeehee.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x20, 0x0, 400)
    Sleep(300)

    ChrTalk(    #70
        0x20,
        (
            "#260FI've got a really neat idea, actually.\x02\x03",

            "It's not often you have this many strange people\x01",
            "in one place...\x02\x03",

            "#265F...so how about we all go and play hide-and-seek\x01",
            "in that really black Glorious? Doesn't that sound\x01",
            "exciting?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3335")

    ChrTalk(    #71
        0x101,
        "#1016FY-Yeah, let's not do that...\x02",
    )

    CloseMessageWindow()
    Jump("loc_34AC")

    label("loc_3335")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3448")

    ChrTalk(    #72
        0x10F,
        (
            "#1446FOut of all of us, you're by far the most\x01",
            "familiar with the Glorious' layout. I'd say\x01",
            "you would have an unfair advantage.\x02\x03",

            "#1440FI'm not opposed to the idea, but we need\x01",
            "additional rules to even out the odds.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0x109,
        "#1061FYou're actually up for it?!\x02",
    )

    CloseMessageWindow()
    Jump("loc_34AC")

    label("loc_3448")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3484")
    OP_62(0x107, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(    #74
        0x107,
        "#065FE-Eeek...\x02",
    )

    CloseMessageWindow()
    Jump("loc_34AC")

    label("loc_3484")


    ChrTalk(    #75
        0x109,
        "#1066FY-Yeah, let's not do that...\x02",
    )

    CloseMessageWindow()

    label("loc_34AC")

    ClearChrFlags(0xFE, 0x10)
    OP_A2(0x2655)
    TalkEnd(0xFE)
    Jump("loc_353A")

    label("loc_34BA")

    TalkBegin(0xFE)

    ChrTalk(    #76
        0x20,
        (
            "#260FHeehee. The stars are all so pretty.\x02\x03",

            "#261FIt's just a shame there's no moon. That would\x01",
            "make it even lovelier.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)

    label("loc_353A")

    Jump("loc_3906")

    label("loc_353D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x564, 0)), scpexpr(EXPR_END)), "loc_3906")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3787")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_35FE")
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3580")
    TurnDirection(0xFE, 0x101, 0)
    Jump("loc_3587")

    label("loc_3580")

    TurnDirection(0xFE, 0x102, 0)

    label("loc_3587")


    ChrTalk(    #77
        0x20,
        (
            "#260FThe two of you train together every day, huh?\x02\x03",

            "#263FI wonder if Estelle's getting stronger because\x01",
            "of it?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_367E")

    label("loc_35FE")

    SetChrFlags(0xFE, 0x10)
    TalkBegin(0xFE)

    ChrTalk(    #78
        0x20,
        (
            "#267FHuh...\x02\x03",

            "So Estelle and Joshua train together every day,\x01",
            "huh?\x02\x03",

            "#263FI wonder if it's having any effect on her.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_367E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3702")

    ChrTalk(    #79
        0x101,
        (
            "#1017FWell, I'd like to think I'm getting stronger, \x01",
            "yeah...\x02\x01",

            "#1008FIt's slow going, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0x20,
        "#267FHuh...\x02",
    )

    CloseMessageWindow()
    Jump("loc_3779")

    label("loc_3702")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3779")

    ChrTalk(    #81
        0x102,
        (
            "#1501FI'd say she's getting stronger, yeah. It's gradual,\x01",
            "but progress is progress.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0x20,
        "#267FOh...\x02",
    )

    CloseMessageWindow()

    label("loc_3779")

    ClearChrFlags(0xFE, 0x10)
    OP_A2(0x7)
    TalkEnd(0xFE)
    Jump("loc_3906")

    label("loc_3787")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x565, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_384F")
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_37A7")
    TurnDirection(0xFE, 0x101, 0)

    label("loc_37A7")


    ChrTalk(    #83
        0x20,
        (
            "#267FSo Estelle trains with Joshua every day, huh?\x02\x03",

            "#261FPerhaps I should help train her up myself.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3849")

    ChrTalk(    #84
        0x101,
        "#1016FA-Ahaha... Go easy on me, okay?\x02",
    )

    CloseMessageWindow()

    label("loc_3849")

    TalkEnd(0xFE)
    Jump("loc_3906")

    label("loc_384F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C9, 0)), scpexpr(EXPR_END)), "loc_38E7")
    TalkBegin(0xFE)

    ChrTalk(    #85
        0x20,
        (
            "#266F*sigh* I'm still disappointed those three didn't\x01",
            "stay any longer.\x02\x03",

            "I wanted to play more!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #86
        0x109,
        "#1068FI sure as heck didn't...\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Jump("loc_3906")

    label("loc_38E7")

    SetChrFlags(0xFE, 0x10)
    TalkBegin(0xFE)

    ChrTalk(    #87
        0x20,
        "#1300F...\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    ClearChrFlags(0xFE, 0x10)

    label("loc_3906")

    Return()

    # Function_6_2F3F end

    def Function_7_3907(): pass

    label("Function_7_3907")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x561, 0)), scpexpr(EXPR_END)), "loc_3B33")
    SetChrFlags(0xFE, 0x10)
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3A9B")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_39D9")

    ChrTalk(    #88
        0x1A,
        (
            "#070FI'm ready for some sparring whenever you are,\x01",
            "Agate.\x02\x03",

            "Whenever you're up for it, come hit me up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0x106,
        (
            "#051FSorry for the wait, man. I'll be by later. \x01",
            "Promise.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3A95")

    label("loc_39D9")


    ChrTalk(    #90
        0x1A,
        (
            "#573FThe actual makeup of this place might be a\x01",
            "mystery to us even now...\x02\x03",

            "#070F...but one thing's for sure: the clear air makes it\x01",
            "the perfect environment for training and sparring.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3A95")

    OP_A2(0xE)
    Jump("loc_3B28")

    label("loc_3A9B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3ACF")

    ChrTalk(    #91
        0x1A,
        (
            "#074F*deep breath*\x02\x03",

            "Haaaaaah!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3B28")

    label("loc_3ACF")


    ChrTalk(    #92
        0x1A,
        (
            "#573FTime to stop holding back, Agate.\x02\x03",

            "#070FYou're not gonna beat me if you don't!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3B28")

    ClearChrFlags(0xFE, 0x10)
    TalkEnd(0xFE)
    Jump("loc_520B")

    label("loc_3B33")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x560, 0)), scpexpr(EXPR_END)), "loc_3D95")
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3C9C")

    ChrTalk(    #93
        0x1A,
        (
            "#074FI'm just mulling over all Celeste told us about\x01",
            "Phantasma earlier.\x02\x03",

            "It's strange to think we've suddenly ended up\x01",
            "in a world that's part of a higher plane of the\x01",
            "universe.\x02\x03",

            "#070FThinking about it, this place is probably perfect\x01",
            "for martial arts training. It's like being at the\x01",
            "top of a tall mountain, isolated from the world.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xE)
    Jump("loc_3D8F")

    label("loc_3C9C")


    ChrTalk(    #94
        0x1A,
        (
            "#074FSounds wild, but it's true--we've ended up in a\x01",
            "higher plane of the universe.\x02\x03",

            "#070FThinking about it, this place is probably perfect\x01",
            "for martial arts training. It's like being at the\x01",
            "top of a tall mountain, isolated from the world.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3D8F")

    TalkEnd(0xFE)
    Jump("loc_520B")

    label("loc_3D95")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x540, 7)), scpexpr(EXPR_END)), "loc_3F51")
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3E83")

    ChrTalk(    #95
        0x1A,
        (
            "#074FIf the world we're in really does change as\x01",
            "a result of our thoughts...\x02\x03",

            "#072F...then we're going to need more than just\x01",
            "physical strength in the battles ahead--\x01",
            "we're going to need mental strength, too.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xE)
    Jump("loc_3F4B")

    label("loc_3E83")


    ChrTalk(    #96
        0x1A,
        (
            "#074FWe're going to need more than just physical\x01",
            "strength in the battles ahead--we're going to\x01",
            "need mental strength, too.\x02\x03",

            "I'd be surprised if that wasn't what the Lord\x01",
            "of Phantasma had in mind.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3F4B")

    TalkEnd(0xFE)
    Jump("loc_520B")

    label("loc_3F51")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x540, 4)), scpexpr(EXPR_END)), "loc_40EF")
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4091")

    ChrTalk(    #97
        0x1A,
        (
            "#573FMan, I sure wasn't expecting Colonel Richard\x01",
            "of all guys to be in a sealing stone!\x02\x03",

            "#070FAt this rate, it'll be Master Cassius in the next\x01",
            "one.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x1A, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #98
        0x1A,
        (
            "#073FHold up a sec...\x02\x03",

            "#074FI ended up here despite being in Calvard,\x01",
            "so maybe she could even end up here...\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xE)
    Jump("loc_40E9")

    label("loc_4091")


    ChrTalk(    #99
        0x1A,
        "#572FHmm...\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(72, 320, 56, 3)

    AnonymousTalk(    #100
        "\x07\x05Zin is deep in thought, something clearly on his mind.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_40E9")

    TalkEnd(0xFE)
    Jump("loc_520B")

    label("loc_40EF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4CA, 3)), scpexpr(EXPR_END)), "loc_43A9")
    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4186")
    Jump("loc_41C8")

    label("loc_4186")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_41A2")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_41C8")

    label("loc_41A2")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_41BE")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_41C8")

    label("loc_41BE")

    OP_51(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_41C8")

    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4300")

    ChrTalk(    #101
        0x1A,
        (
            "#074FEverything about the Lord of Phantasma is still\x01",
            "a mystery to us...\x02\x03",

            "#070FBut look on the bright side--that ghost seems all\x01",
            "right with us.\x02\x03",

            "We've got a whole lot of capable people here,\x01",
            "too. I'm sure there's got to be a way for us to\x01",
            "get through this.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xE)
    Jump("loc_439E")

    label("loc_4300")


    ChrTalk(    #102
        0x1A,
        (
            "#074FEverything about the Lord of Phantasma is still\x01",
            "a mystery to us...\x02\x03",

            "#070F...but there's got to be a way for us to win against\x01",
            "them. I'm sure of it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_439E")

    SetChrSubChip(0xFE, 0)
    TalkEnd(0xFE)
    Jump("loc_520B")

    label("loc_43A9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x540, 0)), scpexpr(EXPR_END)), "loc_4883")
    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4440")
    Jump("loc_4482")

    label("loc_4440")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_445C")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4482")

    label("loc_445C")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4478")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4482")

    label("loc_4478")

    OP_51(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4482")

    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    ChrTalk(    #103
        0x101,
        (
            "#1000FOh, by the way, Zin?\x02\x03",

            "#1015FIs it true that Kilika quit her job as guild\x01",
            "receptionist?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0x1A,
        (
            "#573FHaha... Yeah, it is.\x02\x03",

            "#070FShe got a job offer from elsewhere that she\x01",
            "ended up taking. It wasn't an easy choice for\x01",
            "her, to be sure...\x02\x03",

            "But it was a good opportunity, so I'm glad she\x01",
            "took it. Either way, because of that, she had\x01",
            "to go back to Calvard.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0x101,
        (
            "#1010FOh, right...\x02\x03",

            "#1006FWell, she's got to do what's best for her, \x01",
            "I guess.\x02\x03",

            "#1007FIt's gonna be really weird when I next go to the\x01",
            "guild in Zeiss and she's not there, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #106
        0x1A,
        (
            "#071FHaha. Maybe so, but it's not like you can't go\x01",
            "and see her over in Calvard.\x02\x03",

            "#070FI mean, you're in the middle of touring the \x01",
            "continent as it is!\x02\x03",

            "Just drop by and pay her a visit! You can come\x01",
            "and see me, too, while you're at it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0x101,
        (
            "#1008FYou make a compelling argument, Zin...\x02\x03",

            "#1006FOkay, then!\x02\x03",

            "When we finally manage to get ourselves\x01",
            "out of here, I'll do just that!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #108
        0x1A,
        "#071FI'm looking forward to it already!\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2653)
    SetChrSubChip(0xFE, 0)
    TalkEnd(0xFE)
    Jump("loc_520B")

    label("loc_4883")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x521, 6)), scpexpr(EXPR_END)), "loc_4B8B")
    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_491A")
    Jump("loc_495C")

    label("loc_491A")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_4936")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_495C")

    label("loc_4936")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4952")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_495C")

    label("loc_4952")

    OP_51(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_495C")

    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4A7C")

    ChrTalk(    #109
        0x1A,
        (
            "#074FThe fiends we've encountered in here so far\x01",
            "have been fierce enough...\x02\x03",

            "The farther we descend through the planes of\x01",
            "this place, though, the more dangerous they're\x01",
            "likely to become.\x02\x03",

            "#070FWe're gonna have to keep our guard up.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xE)
    Jump("loc_4B80")

    label("loc_4A7C")


    ChrTalk(    #110
        0x1A,
        (
            "#070FIt's my first time seeing fiends up close and\x01",
            "personal...although I suppose that's true of\x01",
            "all of us.\x02\x03",

            "So all the battles in here are one big learning\x01",
            "experience with trying to work out how to handle\x01",
            "them. But hey! All experience is good experience.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4B80")

    SetChrSubChip(0xFE, 0)
    TalkEnd(0xFE)
    Jump("loc_520B")

    label("loc_4B8B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4CA, 2)), scpexpr(EXPR_END)), "loc_4D3D")
    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4C22")
    Jump("loc_4C64")

    label("loc_4C22")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_4C3E")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4C64")

    label("loc_4C3E")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4C5A")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4C64")

    label("loc_4C5A")

    OP_51(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4C64")

    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    ChrTalk(    #111
        0x1A,
        (
            "#070FStill, with the fragrance of the trees and the sound\x01",
            "of the waterfall gently falling, this place really takes\x01",
            "me back to my training days.\x02\x03",

            "It's kind of nice.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0)
    TalkEnd(0xFE)
    Jump("loc_520B")

    label("loc_4D3D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x521, 2)), scpexpr(EXPR_END)), "loc_520B")
    SetChrFlags(0xFE, 0x10)
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4F9E")
    OP_51(0x103, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x103, 0)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4DEA")
    Jump("loc_4E2C")

    label("loc_4DEA")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_4E06")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4E2C")

    label("loc_4E06")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4E22")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4E2C")

    label("loc_4E22")

    OP_51(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4E2C")

    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x103, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x103, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    ChrTalk(    #112
        0x1A,
        (
            "#074FI was surprised when I saw your new haircut,\x01",
            "Schera.\x02\x03",

            "#070FI'd heard you'd been growing your hair out since \x01",
            "your troupe days.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0x103,
        (
            "#1520FI had...\x02\x03",

            "But, well...after all that happened, I just felt\x01",
            "like a change, I suppose.\x02\x03",

            "#1521FSo I cut it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #114
        0x1A,
        (
            "#573F...Ah, right.\x02\x03",

            "#070FIt suits you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0x103,
        "#1527FHaha. Why, thank you.\x02",
    )

    CloseMessageWindow()
    Jump("loc_51FB")

    label("loc_4F9E")

    OP_51(0x102, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x102, 0)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_502E")
    Jump("loc_5070")

    label("loc_502E")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_504A")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5070")

    label("loc_504A")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5066")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5070")

    label("loc_5066")

    OP_51(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5070")

    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x102, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x102, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    ChrTalk(    #116
        0x1A,
        (
            "#074FI was surprised when I saw Schera's new look.\x02\x03",

            "As far as I'm aware, she'd been growing it out\x01",
            "since her troupe days.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #117
        0x102,
        (
            "#1500FYeah.\x02\x03",

            "#1514FStill, she did go through a lot during her time\x01",
            "with us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #118
        0x1A,
        (
            "#074FDid she ever.\x02\x03",

            "#070FI think we all know she'll be just fine, though.\x01",
            "She's a tough cookie, both in body and mind.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #119
        0x102,
        "#1501FYeah. I agree.\x02",
    )

    CloseMessageWindow()

    label("loc_51FB")

    OP_A2(0x2652)
    SetChrSubChip(0xFE, 0)
    ClearChrFlags(0xFE, 0x10)
    TalkEnd(0xFE)

    label("loc_520B")

    Return()

    # Function_7_3907 end

    SaveToFile()

Try(main)

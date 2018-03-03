from ED63RDScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'U7003_5 ._SN',
        MapName             = 'Gaiden2',
        Location            = 'U7003.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60000",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            '',
            '',
            '',
            '',
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
        "Function_3_12EE",         # 03, 3
        "Function_4_1983",         # 04, 4
        "Function_5_2D90",         # 05, 5
        "Function_6_46BD",         # 06, 6
        "Function_7_6654",         # 07, 7
        "Function_8_735E",         # 08, 8
        "Function_9_955E",         # 09, 9
        "Function_10_ABCF",        # 0A, 10
        "Function_11_AF11",        # 0B, 11
        "Function_12_CB19",        # 0C, 12
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

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x584, 0)), scpexpr(EXPR_END)), "loc_5A1")
    SetChrFlags(0xFE, 0x10)
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4CC, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_495")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_32A")

    ChrTalk(    #0
        0x11,
        (
            "#1936F...\x02\x03",

            "Five years ago, Kevin and Rufina did all they could\x01",
            "to help me and save me from danger.\x02\x03",

            "#1938FThey might have regretted the outcome, but that\x01",
            "doesn't change their intentions--or how important\x01",
            "they both are to me.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x109, 400)
    Sleep(300)

    ChrTalk(    #1
        0x11,
        (
            "#1932FThat's why we need to defeat the Lord of\x01",
            "Phantasma. Together.\x02\x03",

            "For Rufina as well as anyone else.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x109,
        (
            "#1075FYeah. You're right.\x02\x03",

            "...\x02\x03",

            "#1079FWhat're you doing here, by the way?\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xFE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(300)

    ChrTalk(    #3
        0x11,
        (
            "#1940FE-Ensuring the army has enough in the\x01",
            "way of rations is key to any operation.\x01",
            "That's what I'm doing.\x02\x03",

            "...Laugh, and I will whack you.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_48F")

    label("loc_32A")


    ChrTalk(    #4
        0x11,
        (
            "#1936F...\x02\x03",

            "Five years ago, Kevin and Rufina did all they could\x01",
            "to help me and save me from danger.\x02\x03",

            "#1938FThey might have regretted the outcome, but that\x01",
            "doesn't change their intentions--or how important\x01",
            "they both are to me.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x0, 400)
    Sleep(300)

    ChrTalk(    #5
        0x11,
        (
            "#1932FThat's why we need to defeat the Lord of\x01",
            "Phantasma. Together.\x02\x03",

            "#1932FFor Rufina as well as anyone else.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_48F")

    OP_A2(0x2665)
    Jump("loc_596")

    label("loc_495")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_51E")
    TurnDirection(0xFE, 0x109, 0)

    ChrTalk(    #6
        0x11,
        (
            "#1936FWe need to defeat the Lord of Phantasma\x01",
            "with our own hands.\x02\x03",

            "#1932FFor Rufina as well as anyone else.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_596")

    label("loc_51E")

    TurnDirection(0xFE, 0x0, 0)

    ChrTalk(    #7
        0x11,
        (
            "#1936FWe need to defeat the Lord of Phantasma\x01",
            "with our own hands.\x02\x03",

            "#1932FFor Rufina as well as anyone else.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_596")

    ClearChrFlags(0xFE, 0x10)
    TalkEnd(0xFE)
    Jump("loc_12ED")

    label("loc_5A1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x580, 0)), scpexpr(EXPR_END)), "loc_837")
    SetChrFlags(0xFE, 0x10)
    TalkBegin(0xFE)
    OP_51(0x109, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x109, 0)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_640")
    Jump("loc_682")

    label("loc_640")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_65C")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_682")

    label("loc_65C")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_678")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_682")

    label("loc_678")

    OP_51(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_682")

    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x109, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x109, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_786")

    ChrTalk(    #8
        0x11,
        (
            "#1446FKevin, you know as well as I do that you'll need\x01",
            "me with you to go inside Aster House.\x02\x03",

            "#1801FYou're not kicking me off the team on purpose,\x01",
            "are you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x109,
        "#1077FD-Don't be silly!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x11,
        "#1801F*stare*\x02",
    )

    CloseMessageWindow()
    OP_A2(0xB)
    Jump("loc_827")

    label("loc_786")


    ChrTalk(    #11
        0x11,
        (
            "#1446FKevin, you know as well as I do that you'll need\x01",
            "me with you to go inside Aster House.\x02\x03",

            "#1801FYou're not kicking me off the team on purpose,\x01",
            "are you?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_827")

    SetChrSubChip(0xFE, 0)
    ClearChrFlags(0xFE, 0x10)
    TalkEnd(0xFE)
    Jump("loc_12ED")

    label("loc_837")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x565, 4)), scpexpr(EXPR_END)), "loc_B70")
    SetChrFlags(0xFE, 0x10)
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A37")

    ChrTalk(    #12
        0x109,
        "#1065FUmm... Ries?\x02",
    )

    CloseMessageWindow()
    OP_62(0xFE, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)
    OP_51(0x109, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x109, 0)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_912")
    Jump("loc_954")

    label("loc_912")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_92E")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_954")

    label("loc_92E")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_94A")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_954")

    label("loc_94A")

    OP_51(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_954")

    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x109, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x109, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Sleep(200)

    ChrTalk(    #13
        0x11,
        "#1802FYes? What is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x109,
        (
            "#1060FCould you come with me for a bit?\x02\x03",

            "#1075FI'll explain why later.\x01",
            "Although I probably won't need to.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x11,
        (
            "#1440F...\x02\x03",

            "#1446FOkay. I'll come.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xB)
    Jump("loc_B60")

    label("loc_A37")

    OP_51(0x109, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x109, 0)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_AC7")
    Jump("loc_B09")

    label("loc_AC7")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_AE3")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_B09")

    label("loc_AE3")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_AFF")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_B09")

    label("loc_AFF")

    OP_51(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_B09")

    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x109, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x109, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    ChrTalk(    #16
        0x11,
        (
            "#1445F...\x02\x03",

            "#1443FI'm ready whenever you are.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B60")

    SetChrSubChip(0xFE, 0)
    ClearChrFlags(0xFE, 0x10)
    TalkEnd(0xFE)
    Jump("loc_12ED")

    label("loc_B70")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x565, 3)), scpexpr(EXPR_END)), "loc_10AA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4CC, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C47")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C40")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C0E")
    SetChrFlags(0xFE, 0x10)
    TalkBegin(0xFE)

    ChrTalk(    #17
        0x11,
        (
            "#1445F(Leonhardt the Bladelord...)\x02\x03",

            "#1446F(He sounded like he knew Rufina, too...but how?)\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xFE, 0x10)
    TalkEnd(0xFE)
    Jump("loc_C3D")

    label("loc_C0E")

    SetChrFlags(0xFE, 0x10)
    TalkBegin(0xFE)

    ChrTalk(    #18
        0x11,
        (
            "#1446F...\x02\x03",

            "#1445FI see...\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xFE, 0x10)
    TalkEnd(0xFE)

    label("loc_C3D")

    Jump("loc_C44")

    label("loc_C40")

    Call(5, 8)

    label("loc_C44")

    Jump("loc_10A7")

    label("loc_C47")

    RunExpression(0x2, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E88")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_END)), "loc_CFB")
    SetChrFlags(0xFE, 0x10)
    TalkBegin(0xFE)

    ChrTalk(    #19
        0x11,
        (
            "#1447F#32WThe droplets from the spirits called forth\x01",
            "a morning mist in the forest.\x02\x03",

            "And by that spring, seven bells gathered...#20W\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xFE, 0x10)
    TalkEnd(0xFE)
    Jump("loc_E82")

    label("loc_CFB")

    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_D8B")
    Jump("loc_DCD")

    label("loc_D8B")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_DA7")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_DCD")

    label("loc_DA7")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_DC3")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_DCD")

    label("loc_DC3")

    OP_51(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_DCD")

    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    ChrTalk(    #20
        0x11,
        (
            "#1448FPerhaps this would be a good time to read\x01",
            "a story from one of the Testaments.\x02\x03",

            "#1442FI am a sister of the church, after all.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0)
    TalkEnd(0xFE)

    label("loc_E82")

    OP_A2(0xB)
    Jump("loc_109E")

    label("loc_E88")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_END)), "loc_F17")
    SetChrFlags(0xFE, 0x10)
    TalkBegin(0xFE)

    ChrTalk(    #21
        0x11,
        (
            "#1447F#32WMay the two of them rest in peace.\x02\x03",

            "#1442FAnd may all those who live have courage\x01",
            "and be blessed.#20W\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xFE, 0x10)
    TalkEnd(0xFE)
    Jump("loc_109E")

    label("loc_F17")

    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_FA7")
    Jump("loc_FE9")

    label("loc_FA7")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_FC3")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_FE9")

    label("loc_FC3")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_FDF")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_FE9")

    label("loc_FDF")

    OP_51(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_FE9")

    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    ChrTalk(    #22
        0x11,
        (
            "#1448FPerhaps this would be a good time to read\x01",
            "a story from one of the Testaments.\x02\x03",

            "#1442FI am a sister of the church, after all.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0)
    TalkEnd(0xFE)

    label("loc_109E")

    OP_51(0xFE, 0x8, (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_10A7")

    Jump("loc_12ED")

    label("loc_10AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x564, 0)), scpexpr(EXPR_END)), "loc_10B4")
    Jump("loc_12ED")

    label("loc_10B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x562, 5)), scpexpr(EXPR_END)), "loc_1197")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4CC, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_10D5")
    Call(3, 2)
    Jump("loc_1194")

    label("loc_10D5")

    SetChrFlags(0xFE, 0x10)
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1158")

    ChrTalk(    #23
        0x11,
        "#1445F...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x109,
        "#1079FSomething wrong, Ries?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x11,
        "#1446F...No. It's nothing.\x02",
    )

    CloseMessageWindow()
    OP_62(0x109, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)
    OP_A2(0xB)
    Jump("loc_118C")

    label("loc_1158")


    ChrTalk(    #26
        0x11,
        (
            "#1445F...\x02\x03",

            "(Why did both Kevin and Rufina...?)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_118C")

    ClearChrFlags(0xFE, 0x10)
    TalkEnd(0xFE)

    label("loc_1194")

    Jump("loc_12ED")

    label("loc_1197")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x561, 0)), scpexpr(EXPR_END)), "loc_12ED")
    OP_63(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_124A")
    SetChrFlags(0xFE, 0x10)
    TalkBegin(0xFE)

    ChrTalk(    #27
        0x11,
        (
            "#1447F#40W...#20W\x02\x03",

            "#1442FAhh...\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xFE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    SetChrChipByIndex(0xFE, 2)
    SetChrSubChip(0xFE, 0)
    OP_62(0xFE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    TurnDirection(0xFE, 0x0, 800)
    Sleep(200)

    ChrTalk(    #28
        0x11,
        "#1802FWh-What is it?!\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    ClearChrFlags(0xFE, 0x10)
    OP_43(0xFE, 0x0, 0x0, 0xD)
    OP_A2(0xB)
    Jump("loc_12ED")

    label("loc_124A")

    TalkBegin(0xFE)

    ChrTalk(    #29
        0x11,
        (
            "#1800F*cough*\x02\x03",

            "The Testaments exist to bring peace to the\x01",
            "hearts of Aidios' children.\x02\x03",

            "#1805FWould you like me to read you an excerpt\x01",
            "from them?\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    OP_43(0xFE, 0x0, 0x0, 0xD)

    label("loc_12ED")

    Return()

    # Function_2_AC end

    def Function_3_12EE(): pass

    label("Function_3_12EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x584, 0)), scpexpr(EXPR_END)), "loc_15AE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_140A")
    TalkBegin(0xFE)

    ChrTalk(    #30
        0x1E,
        (
            "#1008FIt's gonna be a long journey, right?\x02\x03",

            "#1017FSo we'll probably get hungry on the way.\x01",
            "And if we don't have any food with us,\x01",
            "we're gonna be in biiig trouble!\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1401")

    ChrTalk(    #31
        0x10F,
        "#1932F...I like the way you think.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1401")

    ChrTalk(    #32
        0x109,
        "#1066FHahaha...\x02",
    )

    CloseMessageWindow()

    label("loc_1401")

    OP_A2(0x7)
    TalkEnd(0xFE)
    Jump("loc_15AB")

    label("loc_140A")

    SetChrFlags(0xFE, 0x10)
    TalkBegin(0xFE)

    ChrTalk(    #33
        0x1E,
        (
            "#1015FUmm... Celeste says she's not going to need any,\x01",
            "so that leaves, like, what?\x02\x03",

            "Enough food for 16 people, I guess?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_15A3")

    ChrTalk(    #34
        0x10F,
        (
            "#1932F...I think you should bring enough for 18.\x02\x03",

            "#1938FI need about three people's worth of it.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x1E, 0x10F, 0)
    SetChrSubChip(0xFE, 0)

    ChrTalk(    #35
        0x1E,
        (
            "#1004FF-For real...?\x02\x03",

            "#1006FOkay, then!\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_15A3")

    ChrTalk(    #36
        0x109,
        (
            "#1068F(I hope Gilbert's got a small stomach... \x01",
            "Sounds like he's gettin' jack all.)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_15A3")

    ClearChrFlags(0xFE, 0x10)
    TalkEnd(0xFE)

    label("loc_15AB")

    Jump("loc_1982")

    label("loc_15AE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x562, 5)), scpexpr(EXPR_END)), "loc_1982")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_187E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4CD, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1743")
    TalkBegin(0xFE)

    ChrTalk(    #37
        0x1E,
        (
            "#1008FI'm feeling kinda hungry, so I came over here\x01",
            "to get something to eat.\x02\x03",

            "#1019FWh-What are you looking at me like that for?! \x01",
            "Exercise makes you hungry! It's a fact of life!\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_173D")

    ChrTalk(    #38
        0x10F,
        (
            "#1447FI couldn't agree more, Estelle.\x02\x03",

            "#1448FThat's a universal rule of this world.\x01",
            "To try to deny it would be folly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0x109,
        "#1068F(These two sure have a lot in common...)\x02",
    )

    CloseMessageWindow()

    label("loc_173D")

    TalkEnd(0xFE)
    Jump("loc_1878")

    label("loc_1743")

    SetChrFlags(0xFE, 0x10)
    TalkBegin(0xFE)

    ChrTalk(    #40
        0x1E,
        (
            "#1007F*sigh* I wish those two could get along...\x02\x03",

            "I wanna do something to help on that front,\x01",
            "but I'm not sure what I can do.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1833")

    ChrTalk(    #41
        0x109,
        (
            "#1061F(Oh, I'm sure you could if you put\x01",
            "your mind to it, Estelle.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1870")

    label("loc_1833")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1853")

    ChrTalk(    #42
        0x10F,
        "#1440F...\x02",
    )

    CloseMessageWindow()
    Jump("loc_1870")

    label("loc_1853")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1870")

    ChrTalk(    #43
        0x110,
        "#1300F...\x02",
    )

    CloseMessageWindow()

    label("loc_1870")

    ClearChrFlags(0xFE, 0x10)
    TalkEnd(0xFE)

    label("loc_1878")

    OP_A2(0x7)
    Jump("loc_1982")

    label("loc_187E")

    SetChrFlags(0xFE, 0x10)
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4CD, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_18F7")

    ChrTalk(    #44
        0x1E,
        (
            "#1015FI'm feeling kinda thirsty, too...\x02\x03",

            "#1006FMaybe I could go for some ice cream\x01",
            "or something?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_197A")

    label("loc_18F7")


    ChrTalk(    #45
        0x1E,
        (
            "#1007F*sigh* I wish those two could get along...\x02\x03",

            "I wanna do something to help on that front,\x01",
            "but I'm not sure what I can do.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_197A")

    ClearChrFlags(0xFE, 0x10)
    TalkEnd(0xFE)

    label("loc_1982")

    Return()

    # Function_3_12EE end

    def Function_4_1983(): pass

    label("Function_4_1983")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x584, 0)), scpexpr(EXPR_END)), "loc_206D")
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4CC, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1E2C")
    TurnDirection(0x16, 0x109, 0)

    ChrTalk(    #46
        0x16,
        (
            "#1500FIt's weird how it feels like we've known each\x01",
            "other for such a long time...but when you\x01",
            "think about it, it hasn't been that long at all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x109,
        (
            "#1075FHahaha. True enough.\x02\x03",

            "#1840FYou know...I might as well tell you this now.\x02\x03",

            "Right now, I'm pretty damn jealous of you,\x01",
            "Joshua.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0x16,
        "#1504F...You are?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0x109,
        (
            "#1844FWhen you think about it, we've walked fairly\x01",
            "similar paths in life, right?\x02\x03",

            "But while I'm still feeling my way around in the\x01",
            "dark, you managed to make it back out into the\x01",
            "light again.\x02\x03",

            "#1846FI didn't really feel this way when you were finally\x01",
            "free from the Stigma and able to move on and all...\x02\x03",

            "...but now? That's a whole different story.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0x16,
        (
            "#1514F...You know? I think I know why, too.\x02\x03",

            "#1513FIt's probably because before now, you'd given\x01",
            "up on ever being able to come back to the light.\x01",
            "Except now, you want to believe you can again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0x109,
        (
            "#1068FMan...you've got me all figured out.\x02\x03",

            "#1066FHaha... Pretty pitiful of me, huh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0x16,
        (
            "#1509FMaybe, but there's no harm in that.\x02\x03",

            "#1501FBefore that, though, we've got to get\x01",
            "out of this world. \x02\x03",

            "But as long as we believe in ourselves,\x01",
            "I'm sure we can manage that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0x109,
        "#1840FFor sure.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2667)
    Jump("loc_2067")

    label("loc_1E2C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F46")

    ChrTalk(    #54
        0x16,
        (
            "#1505FThe Lord of Phantasma keeps referring to us as\x01",
            "pieces on a game board.\x02\x03",

            "#1502FAnd it's obvious enough that unless we all work\x01",
            "together, there's no way we're getting out of\x01",
            "here.\x02\x03",

            "Especially with how fixated she is on playing by\x01",
            "the rules she's established.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)
    Jump("loc_2067")

    label("loc_1F46")


    ChrTalk(    #55
        0x16,
        (
            "#1502FIt's obvious enough that unless we all work\x01",
            "together, there's no way we're getting out of\x01",
            "here.\x02\x03",

            "#1503FThat's probably one of the rules that governs\x01",
            "the world itself.\x02\x03",

            "But at the same time, it feels like the Lord of\x01",
            "Phantasma herself is defined by the rules of\x01",
            "this world, too.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2067")

    TalkEnd(0xFE)
    Jump("loc_2D8F")

    label("loc_206D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x540, 7)), scpexpr(EXPR_END)), "loc_2D8F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4CC, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2966")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2259")
    SetChrFlags(0xFE, 0x10)
    TalkBegin(0xFE)

    ChrTalk(    #56
        0x110,
        (
            "#264F...Joshua?\x02\x03",

            "#260FWhat are you doing here?\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x16, 0x110, 400)
    Sleep(300)

    ChrTalk(    #57
        0x16,
        (
            "#1513FOh, not much...\x02\x03",

            "#1500FI was just giving some thought to what we\x01",
            "might find ourselves up against during the\x01",
            "remainder of our time here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0x110,
        (
            "#266F*sigh* Why would you waste time doing that\x01",
            "when we'll find out by proceeding anyway?\x02\x03",

            "#262FYou don't need to worry about anything as\x01",
            "long as I'm with you all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0x16,
        "#1509FHaha. I suppose you're right.\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0xFE, 0x10)
    TalkEnd(0xFE)
    Jump("loc_2963")

    label("loc_2259")

    RunExpression(0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x16, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    EventBegin(0x0)
    OP_4A(0x16, 0)
    OP_4A(0x17, 0)
    TurnDirection(0x16, 0x101, 0)
    TurnDirection(0x0, 0x16, 0)
    TurnDirection(0x1, 0x16, 0)
    TurnDirection(0x2, 0x16, 0)
    TurnDirection(0x3, 0x16, 0)
    RunExpression(0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x6, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x7, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2446")
    TurnDirection(0x105, 0x101, 0)

    ChrTalk(    #60
        0x101,
        (
            "#1000F...Joshua?\x02\x03",

            "What're you doing here?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0x16,
        "#1505FOh, I was just thinking about Renne...\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    Fade(800)
    SetChrPos(0x10F, 58170, 1000, -57430, 147)
    SetChrPos(0xF0, 58610, 1000, -57100, 129)
    SetChrPos(0xF1, 60960, 1000, -56480, 129)
    SetChrPos(0x101, 60320, 1000, -59930, 129)
    SetChrPos(0x105, 58640, 1000, -59150, 133)
    TurnDirection(0x101, 0x105, 0)
    TurnDirection(0x16, 0x105, 0)
    TurnDirection(0x105, 0x101, 0)
    OP_6D(64870, -50, -60500, 0)
    OP_67(0, 4290, -10000, 0)
    OP_6B(6020, 0)
    OP_6C(71000, 0)
    OP_6E(203, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #62
        0x105,
        (
            "#1382FThe two of you have been trying to find\x01",
            "her ever since you left Liberl, right?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_25AB")

    label("loc_2446")

    TurnDirection(0x17, 0x101, 0)

    ChrTalk(    #63
        0x101,
        (
            "#1000F...Hmm?\x02\x03",

            "What're you guys doing here?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0x16,
        "#1505FWe were just talking about Renne.\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    Fade(800)
    SetChrPos(0x10F, 58040, 1000, -58350, 129)
    SetChrPos(0xF0, 58610, 1000, -57100, 129)
    SetChrPos(0xF1, 60960, 1000, -56480, 129)
    SetChrPos(0x101, 59430, 1000, -60340, 129)
    TurnDirection(0x101, 0x17, 0)
    TurnDirection(0x16, 0x17, 0)
    TurnDirection(0x17, 0x101, 0)
    OP_6D(64870, -50, -60500, 0)
    OP_67(0, 4290, -10000, 0)
    OP_6B(6020, 0)
    OP_6C(71000, 0)
    OP_6E(203, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #65
        0x17,
        (
            "#1382FThe two of you have been trying to find her\x01",
            "ever since you left Liberl, right?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_25AB")


    ChrTalk(    #66
        0x101,
        (
            "#1003FYeah... I don't feel like we got to talk to her\x01",
            "properly back at the Axis Pillar.\x02\x03",

            "#1007FThere's something I really want to tell her,\x01",
            "too...and I'm not going to be satisfied until\x01",
            "I've done it.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 129, 400)
    OP_8C(0x17, 129, 400)
    OP_8C(0x16, 129, 400)
    OP_62(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x101)
    Sleep(300)

    ChrTalk(    #67
        0x101,
        (
            "#1016FHeehee. Still, she looks like she's doing okay.\x02\x03",

            "#1017FSo I think the best thing to do for now is keep\x01",
            "watching over her and see what happens.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0x16,
        (
            "#1501F...That might be for the best, yeah.\x02\x03",

            "#1513FAt the end of the day, she needs to be the one who\x01",
            "chooses what to do. Nothing good's going to come\x01",
            "from pushing her to make that call any faster.\x02\x03",

            "I just hope that ending up here with us and\x01",
            "everyone else has a positive effect on her.\x02\x03",

            "#1500FBut all we can really do is wait and see, huh?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_28D9")

    ChrTalk(    #69
        0x105,
        "#1168F...Yes, I think you're right.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2902")

    label("loc_28D9")


    ChrTalk(    #70
        0x17,
        "#1168F...Yes, I think you're right.\x02",
    )

    CloseMessageWindow()

    label("loc_2902")

    Sleep(500)
    Fade(500)
    ClearChrFlags(0x0, 0x8)
    ClearChrFlags(0x1, 0x8)
    ClearChrFlags(0x2, 0x8)
    ClearChrFlags(0x3, 0x8)
    OP_51(0x0, 0x1, (scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x2, (scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x3, (scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x4, (scpexpr(EXPR_GET_RESULT, 0x7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4B(0x16, 0)
    OP_4B(0x17, 0)
    OP_51(0x16, 0x4, (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x17, 0x4, (scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A2(0x2666)
    EventEnd(0x6)

    label("loc_2963")

    Jump("loc_2D8F")

    label("loc_2966")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C0B")
    OP_A2(0x1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2AA3")

    ChrTalk(    #71
        0x16,
        (
            "#1505FIf Renne's theory that this world was molded into\x01",
            "its current form by the Lord of Phantasma is true...\x02\x03",

            "...I can only assume the rest of the planes in here\x01",
            "will be tailored to forwarding whatever their goal\x01",
            "is, too.\x02\x03",

            "#1503FI doubt said goal is in our best interests, either.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2C08")

    label("loc_2AA3")


    ChrTalk(    #72
        0x16,
        (
            "#1501FWe're better off just keeping watch over Renne for\x01",
            "the time being.\x02\x03",

            "At the end of the day, she needs to be the one who\x01",
            "chooses what to do. Nothing good's going to come\x01",
            "from pushing her to make that call any faster.\x02\x03",

            "#1513F...Personally, I'm hoping that meeting everyone here\x01",
            "like this will end up having a positive effect on her\x01",
            "in the long run.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2C08")

    Jump("loc_2D8C")

    label("loc_2C0B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2CAA")

    ChrTalk(    #73
        0x16,
        (
            "#1505FThe Lord of Phantasma clearly has some kind of\x01",
            "'game' for us in mind...#1200W #20W \x01",
            "#1503FI can't see it being very enjoyable for us, either.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2D8C")

    label("loc_2CAA")


    ChrTalk(    #74
        0x16,
        (
            "#1501FWe're better off just keeping watch over Renne for\x01",
            "the time being.\x02\x03",

            "At the end of the day, she needs to be the one who\x01",
            "chooses what to do. Nothing good's going to come\x01",
            "from pushing her to make that call any faster.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2D8C")

    TalkEnd(0xFE)

    label("loc_2D8F")

    Return()

    # Function_4_1983 end

    def Function_5_2D90(): pass

    label("Function_5_2D90")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x561, 0)), scpexpr(EXPR_END)), "loc_33C1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3268")
    TalkBegin(0xFE)
    RunExpression(0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x14, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2FA8")
    TurnDirection(0xFE, 0x10E, 0)

    ChrTalk(    #75
        0x19,
        (
            "#1541FWhy, hello, Julia.\x02\x03",

            "It's occurred to me that I never did properly\x01",
            "thank you for your assistance during my return\x01",
            "to Erebonia.\x02\x03",

            "#1547FSo, what say you? Would you like to accompany\x01",
            "me for a drink or two? On me, of course.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0x10E,
        "#172FI... Well... I'm not sure that would be...\x02",
    )

    CloseMessageWindow()
    OP_4A(0x14, 255)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2F10")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2F06")
    TurnDirection(0x10D, 0x10E, 400)
    Jump("loc_2F0D")

    label("loc_2F06")

    TurnDirection(0x14, 0x10E, 400)

    label("loc_2F0D")

    Jump("loc_2F2F")

    label("loc_2F10")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2F28")
    TurnDirection(0x10D, 0x13, 400)
    Jump("loc_2F2F")

    label("loc_2F28")

    TurnDirection(0x14, 0x13, 400)

    label("loc_2F2F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2F6C")

    ChrTalk(    #77
        0x10D,
        "#272FFeel free to ignore him, Captain.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2F98")

    label("loc_2F6C")


    ChrTalk(    #78
        0x14,
        "#272FFeel free to ignore him, Captain.\x02",
    )

    CloseMessageWindow()

    label("loc_2F98")

    OP_4B(0x14, 255)
    OP_51(0x14, 0x4, (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_325F")

    label("loc_2FA8")


    ChrTalk(    #79
        0x19,
        (
            "#1545FHeh. I've begun to think this may be a good\x01",
            "chance to get to know Julia a little better.\x02\x03",

            "#1542FI've been waiting for my chance to strike...\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3205")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3096")

    ChrTalk(    #80
        0x102,
        "#1505FI...wouldn't recommend it, Olivier. Really.\x02",
    )

    CloseMessageWindow()
    Jump("loc_316A")

    label("loc_3096")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_30FB")

    ChrTalk(    #81
        0x101,
        (
            "#1007F*sigh* If you thought my staff was bad,\x01",
            "wait until you meet her sword...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_316A")

    label("loc_30FB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_316A")

    ChrTalk(    #82
        0x105,
        (
            "#1165FA-Ahaha...\x02\x03",

            "I...strongly wouldn't recommend it. Really,\x01",
            "I say that for your own good.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_316A")


    ChrTalk(    #83
        0x10D,
        (
            "#274FHow many times must I tell you not to cause\x01",
            "trouble before it gets through that seemingly\x01",
            "impenetrable skull of yours?\x02\x03",

            "Stay here and behave.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_325F")

    label("loc_3205")


    ChrTalk(    #84
        0x19,
        (
            "#1541F...but unfortunately, Mueller caught me before \x01",
            "I could make good on my plans.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_325F")

    OP_A2(0xE)
    TalkEnd(0xFE)
    Jump("loc_33BE")

    label("loc_3268")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3359")
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_32E2")
    TurnDirection(0x19, 0x10E, 0)

    ChrTalk(    #85
        0x19,
        (
            "#1547FHohoho! It would be my pleasure to treat you\x01",
            "to a drink later, Julia.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3353")

    label("loc_32E2")


    ChrTalk(    #86
        0x19,
        (
            "#1542FHmm... Now, how shall I go about this...?\x02\x03",

            "A good chance just doesn't seem to be\x01",
            "presenting itself...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3353")

    TalkEnd(0xFE)
    Jump("loc_33BE")

    label("loc_3359")

    SetChrFlags(0xFE, 0x10)
    TalkBegin(0xFE)
    OP_4A(0x14, 255)

    ChrTalk(    #87
        0x19,
        "#1541FMy dear friend, you misunderstand me!\x02",
    )

    CloseMessageWindow()
    OP_62(0x14, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)
    OP_4B(0x14, 255)
    ClearChrFlags(0xFE, 0x10)
    TalkEnd(0xFE)

    label("loc_33BE")

    Jump("loc_46BC")

    label("loc_33C1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x560, 0)), scpexpr(EXPR_END)), "loc_3713")
    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3458")
    Jump("loc_349A")

    label("loc_3458")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3474")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_349A")

    label("loc_3474")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3490")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_349A")

    label("loc_3490")

    OP_51(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_349A")

    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3615")

    ChrTalk(    #88
        0x19,
        (
            "#1540FHello, Kevin.\x02\x03",

            "#1545FIt sure seems like you've got quite a lot on your\x01",
            "mind.\x02\x03",

            "I won't force you to tell us everything, but given\x01",
            "that we've all been caught up in this, I think it's\x01",
            "fair to expect some kind of explanation. \x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0x109,
        (
            "#1843FYou'll get one. I promise.\x02\x03",

            "#1060FHope you don't mind waiting a little bit longer.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xE)
    Jump("loc_3708")

    label("loc_3615")


    ChrTalk(    #90
        0x19,
        (
            "#1545FI can appreciate that someone in your line of\x01",
            "work will have plenty of things they can't speak\x01",
            "of freely...\x02\x03",

            "#1540F...but given that we've all been caught up in this,\x01",
            "I think it's fair to expect some kind of explanation\x01",
            "eventually.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3708")

    SetChrSubChip(0xFE, 0)
    TalkEnd(0xFE)
    Jump("loc_46BC")

    label("loc_3713")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x520, 5)), scpexpr(EXPR_END)), "loc_3BF8")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_39A2")
    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_37B8")
    Jump("loc_37FA")

    label("loc_37B8")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_37D4")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_37FA")

    label("loc_37D4")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_37F0")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_37FA")

    label("loc_37F0")

    OP_51(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_37FA")

    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_391C")

    ChrTalk(    #91
        0x19,
        (
            "#1545FHaha. It's been one fancy party after another \x01",
            "for me lately.\x02\x03",

            "#1540FSo truthfully, it's actually nice to have some\x01",
            "time to sit and relax once in a while.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0x10D,
        (
            "#272F...Does the possibility of 'doing some work'\x01",
            "not occur to you?\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xE)
    Jump("loc_3997")

    label("loc_391C")

    TalkBegin(0xFE)

    ChrTalk(    #93
        0x19,
        (
            "#1545FBe sure to work Mueller to the bone in my place,\x01",
            "my wonderful friends.\x02\x03",

            "He knows how to make himself useful.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3997")

    SetChrSubChip(0xFE, 0)
    TalkEnd(0xFE)
    Jump("loc_3BF5")

    label("loc_39A2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3B6D")
    SetChrFlags(0x19, 0x10)
    TalkBegin(0x19)
    OP_4A(0x19, 255)
    OP_4A(0x14, 255)

    ChrTalk(    #94
        0x19,
        (
            "#1542F...No. I think it's safe to say that His Excellency\x01",
            "the Chancellor isn't in any way involved in this.\x02\x03",

            "This is far too roundabout a plan of attack even\x01",
            "for him.\x02\x03",

            "#1551FI can't be so sure that Ouroboros isn't, however...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0x14,
        (
            "#272FWell, I can't disagree that this doesn't feel like\x01",
            "something he would do.\x02\x03",

            "#276FNot least because if he wanted to harm you,\x01",
            "he had plenty of chances to do so in Heimdallr.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xE)
    ClearChrFlags(0x19, 0x10)
    OP_4B(0x19, 255)
    OP_4B(0x14, 255)
    TalkEnd(0x19)
    Jump("loc_3BF5")

    label("loc_3B6D")

    TalkBegin(0xFE)

    ChrTalk(    #96
        0x19,
        (
            "#1540FGreetings! How fares the investigation?\x02\x03",

            "#1541FIf you find anything out, do come and let me know.\x01",
            "I'm ever so curious.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)

    label("loc_3BF5")

    Jump("loc_46BC")

    label("loc_3BF8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x520, 0)), scpexpr(EXPR_END)), "loc_46BC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4CC, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_43BD")
    OP_4A(0x17, 255)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3C1D")
    OP_4A(0x14, 255)

    label("loc_3C1D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3C3A")
    OP_4A(0x13, 255)

    label("loc_3C3A")

    SetChrFlags(0x19, 0x10)
    TalkBegin(0x19)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3DE7")
    OP_51(0x105, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x19, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0x19)
    ClearChrFlags(0x19, 0x10)
    TurnDirection(0x19, 0x105, 0)
    OP_51(0x19, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x19, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x19, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3CE0")
    Jump("loc_3D22")

    label("loc_3CE0")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3CFC")
    OP_51(0x19, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3D22")

    label("loc_3CFC")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3D18")
    OP_51(0x19, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3D22")

    label("loc_3D18")

    OP_51(0x19, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3D22")

    OP_51(0x19, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x105, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x105, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x19, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x19, 0x10)

    ChrTalk(    #97
        0x105,
        (
            "#1382FHow have you been since we last met, \x01",
            "Your Highness?\x02\x03",

            "Word of your popularity in Erebonian high\x01",
            "society has been reaching us over in Liberl,\x01",
            "too.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3E89")

    label("loc_3DE7")

    SetChrSubChip(0x19, 0)

    ChrTalk(    #98
        0x17,
        (
            "#1382FHow have you been since we last met, \x01",
            "Your Highness?\x02\x03",

            "Word of your popularity in Erebonian high\x01",
            "society has been reaching us over in Liberl,\x01",
            "too.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3E89")


    ChrTalk(    #99
        0x19,
        (
            "#1545FWell, I'm doing a good enough job of convincing\x01",
            "them I'm little more than an elegant-yet-harmless\x01",
            "prince at the moment.\x02\x03",

            "#1542FStill, spending so much of my time pretending to \x01",
            "be someone I'm not can be terribly exhausting.\x02\x03",

            "#1544FSo I'm biding my time and waiting for the perfect\x01",
            "chance to cast it all aside and reveal my true form\x01",
            "to the world...\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #100
        0x19,
        "#1541F#3SThen all shall know Olivier, the Gospeler of Love!\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    OP_62(0x19, 0x12C, 1600, 0x36, 0x39, 0xFA, 0x0)
    OP_22(0x89, 0x0, 0x64)
    Sleep(2000)
    OP_62(0x0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x2, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x3, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_40E5")
    OP_62(0x17, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)

    label("loc_40E5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_410A")
    OP_62(0x14, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)

    label("loc_410A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_413A")
    OP_62(0x13, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)

    label("loc_413A")

    Sleep(1000)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4167")

    ChrTalk(    #101
        0x10D,
        "#274FYou moron...\x02",
    )

    CloseMessageWindow()
    Jump("loc_417E")

    label("loc_4167")


    ChrTalk(    #102
        0x14,
        "#274FYou moron...\x02",
    )

    CloseMessageWindow()

    label("loc_417E")


    ChrTalk(    #103
        0x109,
        (
            "#1068F'Gospeler of Love'? THAT'S what you're going\x01",
            "with?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4244")

    ChrTalk(    #104
        0x102,
        (
            "#1508FWho else thinks he's going to be even more of\x01",
            "a menace to society than the black orbment\x01",
            "Gospels ever were?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_42BB")

    label("loc_4244")


    ChrTalk(    #105
        0x16,
        (
            "#1508FWho else thinks he's going to be even more of\x01",
            "a menace to society than the black orbment\x01",
            "Gospels ever were?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_42BB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4320")

    ChrTalk(    #106
        0x105,
        (
            "#1165FHeehee. It's reassuring to see how little\x01",
            "he's changed at heart, though.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4374")

    label("loc_4320")


    ChrTalk(    #107
        0x17,
        (
            "#1165FHeehee. It's reassuring to see how little\x01",
            "he's changed at heart, though.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4374")

    OP_63(0x19)
    OP_4B(0x17, 255)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_438D")
    OP_4B(0x14, 255)

    label("loc_438D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_43AA")
    OP_4B(0x13, 255)

    label("loc_43AA")

    SetChrSubChip(0x19, 0)
    ClearChrFlags(0x19, 0x10)
    TalkEnd(0x19)
    OP_A2(0x2660)
    Jump("loc_46BC")

    label("loc_43BD")

    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x19, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0x19)
    ClearChrFlags(0x19, 0x10)
    TurnDirection(0x19, 0x0, 0)
    OP_51(0x19, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x19, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x19, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_444D")
    Jump("loc_448F")

    label("loc_444D")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_4469")
    OP_51(0x19, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_448F")

    label("loc_4469")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4485")
    OP_51(0x19, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_448F")

    label("loc_4485")

    OP_51(0x19, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_448F")

    OP_51(0x19, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x19, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x19, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_45CF")

    ChrTalk(    #108
        0x19,
        (
            "#1545FStill, the thought of that ghost has yet to\x01",
            "leave my mind since I first heard about her.\x02\x03",

            "Just imagine the spirit of a beautiful woman,\x01",
            "left all alone in this empty realm...\x02\x03",

            "#1547FHahaha! Doesn't the thought just get your\x01",
            "imagination racing?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #109
        0x102,
        "#1508F...\x02",
    )

    CloseMessageWindow()
    OP_A2(0xE)
    Jump("loc_46B4")

    label("loc_45CF")


    ChrTalk(    #110
        0x19,
        (
            "#1540FStill, the thought of that ghost has yet to\x01",
            "leave my mind since I first heard about her.\x02\x03",

            "I wonder whether this garden's appearance is\x01",
            "a reflection of her interests?\x02\x03",

            "#1541FIf so, I have to commend her for her tastes.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_46B4")

    SetChrSubChip(0x19, 0)
    TalkEnd(0x19)

    label("loc_46BC")

    Return()

    # Function_5_2D90 end

    def Function_6_46BD(): pass

    label("Function_6_46BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x565, 3)), scpexpr(EXPR_END)), "loc_4D62")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C8, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4CD, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4954")
    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_476C")
    Jump("loc_47AE")

    label("loc_476C")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_4788")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_47AE")

    label("loc_4788")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_47A4")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_47AE")

    label("loc_47A4")

    OP_51(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_47AE")

    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    ChrTalk(    #111
        0x17,
        (
            "#1383FSo...\x02\x03",

            "#1382F...you got to say farewell, Joshua?\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #112
        0x102,
        (
            "#1513F...Yeah. Thanks.\x02\x03",

            "#1514FI'm impressed you worked that out without me\x01",
            "saying anything, Kloe. Heh. You're too sharp\x01",
            "for your own good.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0x17,
        (
            "#1165FAww. Hardly.\x02\x03",

            "#1168FYou just look like a huge burden's been lifted\x01",
            "from your shoulders, that's all. Kind of gave it\x01",
            "away to me.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2669)
    SetChrSubChip(0xFE, 0)
    TalkEnd(0xFE)
    Jump("loc_4D5F")

    label("loc_4954")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4BA5")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4B11")
    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_49FA")
    Jump("loc_4A3C")

    label("loc_49FA")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_4A16")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4A3C")

    label("loc_4A16")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4A32")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4A3C")

    label("loc_4A32")

    OP_51(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4A3C")

    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    ChrTalk(    #114
        0x17,
        (
            "#1164FOh... Umm...\x02\x03",

            "#1382FHeehee. I'm just taking a break for now.\x02\x03",

            "#1165FI got a little too engrossed in reading the\x01",
            "books over in the library area, you see. \x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0)
    TalkEnd(0xFE)
    Jump("loc_4B9F")

    label("loc_4B11")

    SetChrFlags(0xFE, 0x10)
    TalkBegin(0xFE)

    ChrTalk(    #115
        0x17,
        (
            "#1165FA-Ahaha... Sorry, Josette.\x02\x03",

            "I've always had this habit of getting really \x01",
            "engrossed in things when I'm doing them.\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xFE, 0x10)
    TalkEnd(0xFE)

    label("loc_4B9F")

    OP_A2(0xC)
    Jump("loc_4D5F")

    label("loc_4BA5")

    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4C35")
    Jump("loc_4C77")

    label("loc_4C35")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_4C51")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4C77")

    label("loc_4C51")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4C6D")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4C77")

    label("loc_4C6D")

    OP_51(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4C77")

    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    ChrTalk(    #116
        0x17,
        (
            "#1168FThis place is incredibly calming somehow, isn't it?\x02\x03",

            "#1168FI might've been more surprised than anything when\x01",
            "I first found myself here, but now I'm actually quite\x01",
            "comfortable.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0)
    TalkEnd(0xFE)

    label("loc_4D5F")

    Jump("loc_6653")

    label("loc_4D62")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x540, 7)), scpexpr(EXPR_END)), "loc_5CAC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4CC, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5899")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4DFC")
    SetChrFlags(0xFE, 0x10)
    TalkBegin(0xFE)
    OP_62(0xFE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    TurnDirection(0x17, 0x110, 400)

    ChrTalk(    #117
        0x17,
        (
            "#1164FE-Erm... Renne...?\x02\x03",

            "#1165FAhaha... Umm...\x02\x03",

            "Take care, okay?\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xFE, 0x10)
    TalkEnd(0xFE)
    Jump("loc_5896")

    label("loc_4DFC")

    RunExpression(0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x16, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    EventBegin(0x0)
    OP_4A(0x16, 0)
    OP_4A(0x17, 0)
    TurnDirection(0x16, 0x101, 0)
    TurnDirection(0x17, 0x101, 0)
    TurnDirection(0x0, 0x17, 0)
    TurnDirection(0x1, 0x17, 0)
    TurnDirection(0x2, 0x17, 0)
    TurnDirection(0x3, 0x17, 0)
    RunExpression(0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x6, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x7, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5361")

    ChrTalk(    #118
        0x101,
        (
            "#1000FKloe?\x02\x03",

            "What're you doing here?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #119
        0x17,
        (
            "#1164FOh, it's just...\x02\x03",

            "#1382FI was just curious how Renne was doing,\x01",
            "that's all.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    Fade(800)
    SetChrPos(0x10F, 58040, 1000, -58350, 129)
    SetChrPos(0xF0, 58610, 1000, -57100, 129)
    SetChrPos(0xF1, 60960, 1000, -56480, 129)
    SetChrPos(0x101, 59430, 1000, -60340, 129)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4F62")
    SetChrPos(0x105, 59050, 1000, -59340, 129)

    label("loc_4F62")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4F81")
    SetChrPos(0x102, 59020, 1000, -59390, 81)

    label("loc_4F81")

    ClearChrFlags(0x101, 0x8)
    ClearChrFlags(0x10F, 0x8)
    TurnDirection(0x102, 0x17, 0)
    TurnDirection(0x101, 0x17, 0)
    TurnDirection(0x17, 0x101, 0)
    OP_6D(64870, -50, -60500, 0)
    OP_67(0, 4290, -10000, 0)
    OP_6B(6020, 0)
    OP_6C(71000, 0)
    OP_6E(203, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #120
        0x17,
        (
            "#1382FThe two of you have been trying to find\x01",
            "her ever since you left Liberl, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #121
        0x102,
        (
            "#1503FYeah... I don't feel like we got to talk to\x01",
            "her properly back at the Axis Pillar.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #122
        0x101,
        (
            "#1011FThere's something I really want to tell her,\x01",
            "too...and I'm not going to be satisfied until\x01",
            "I've done it.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 129, 400)
    OP_8C(0x17, 129, 400)
    OP_8C(0x102, 129, 400)
    OP_62(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x101)
    Sleep(300)

    ChrTalk(    #123
        0x101,
        (
            "#1016FHeehee. Still, she looks like she's doing okay.\x02\x03",

            "#1017FSo I think the best thing to do for now is keep\x01",
            "watching over her and see what happens.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #124
        0x102,
        (
            "#1501F...That might be for the best, yeah.\x02\x03",

            "#1513FAt the end of the day, she needs to be the one who\x01",
            "chooses what to do. Nothing good's going to come\x01",
            "from pushing her to make that call any faster.\x02\x03",

            "I just hope that ending up here with us and\x01",
            "everyone else has a positive effect on her.\x02\x03",

            "#1500FBut all we can really do is wait and see, huh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #125
        0x17,
        "#1168F...Yes, I think you're right.\x02",
    )

    CloseMessageWindow()
    Jump("loc_5835")

    label("loc_5361")


    ChrTalk(    #126
        0x101,
        (
            "#1000FHmm?\x02\x03",

            "What are the two of you doing here?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #127
        0x17,
        (
            "#1164FOh, Estelle.\x02\x03",

            "#1382FWe were just talking about Renne.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    Fade(800)
    SetChrPos(0x10F, 58260, 1000, -58840, 129)
    SetChrPos(0xF0, 58610, 1000, -57100, 129)
    SetChrPos(0xF1, 60960, 1000, -56480, 129)
    SetChrPos(0x101, 59430, 1000, -60340, 129)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5444")
    SetChrPos(0x105, 59050, 1000, -59340, 129)

    label("loc_5444")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_545C")
    SetChrFlags(0x102, 0x8)
    ClearChrFlags(0x16, 0x80)

    label("loc_545C")

    ClearChrFlags(0x101, 0x8)
    ClearChrFlags(0x10F, 0x8)
    TurnDirection(0x16, 0x17, 0)
    TurnDirection(0x101, 0x17, 0)
    TurnDirection(0x17, 0x101, 0)
    OP_6D(64870, -50, -60500, 0)
    OP_67(0, 4290, -10000, 0)
    OP_6B(6020, 0)
    OP_6C(71000, 0)
    OP_6E(203, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #128
        0x17,
        (
            "#1382FThe two of you have been trying to find\x01",
            "her ever since you left Liberl, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #129
        0x101,
        (
            "#1003FYeah... I don't feel like we got to talk to\x01",
            "her properly back at the Axis Pillar.\x02\x03",

            "#1007FThere's something I really want to tell her,\x01",
            "too...and I'm not going to be satisfied until\x01",
            "I've done it.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 129, 400)
    OP_8C(0x17, 129, 400)
    OP_8C(0x16, 129, 400)
    OP_62(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x101)
    Sleep(300)

    ChrTalk(    #130
        0x101,
        (
            "#1016FHeehee. Still, she looks like she's doing okay.\x02\x03",

            "#1017FSo I think the best thing to do for now is keep\x01",
            "watching over her and see what happens.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #131
        0x16,
        (
            "#1501F...That might be for the best, yeah.\x02\x03",

            "#1513FAt the end of the day, she needs to be the one who\x01",
            "chooses what to do. Nothing good's going to come\x01",
            "from pushing her to make that call any faster.\x02\x03",

            "I just hope that ending up here with us and\x01",
            "everyone else has a positive effect on her.\x02\x03",

            "#1500FBut all we can really do is wait and see, huh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #132
        0x17,
        "#1168F...Yes, I think you're right.\x02",
    )

    CloseMessageWindow()

    label("loc_5835")

    Sleep(500)
    Fade(500)
    ClearChrFlags(0x0, 0x8)
    ClearChrFlags(0x1, 0x8)
    ClearChrFlags(0x2, 0x8)
    ClearChrFlags(0x3, 0x8)
    OP_51(0x0, 0x1, (scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x2, (scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x3, (scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x4, (scpexpr(EXPR_GET_RESULT, 0x7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4B(0x16, 0)
    OP_4B(0x17, 0)
    OP_51(0x16, 0x4, (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x17, 0x4, (scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A2(0x2666)
    EventEnd(0x6)

    label("loc_5896")

    Jump("loc_5CA9")

    label("loc_5899")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5B43")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_59D4")

    ChrTalk(    #133
        0x17,
        (
            "#1162FIf this world really does change as a result\x01",
            "of people's thoughts...\x02\x03",

            "...then it seems reasonable to assume that\x01",
            "someone must have wished for all of us to\x01",
            "come together, too.\x02\x03",

            "#1169FCould that someone be the Lord of Phantasma?\x01",
            "Or is it that ghost?\x02\x03",

            "#1167F...Or maybe even us?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5B3D")

    label("loc_59D4")


    ChrTalk(    #134
        0x17,
        (
            "#1167FI'm sure it's not going to be easy to come to an\x01",
            "understanding with Renne after all she's been\x01",
            "through, but you know what? \x02\x03",

            "#1168FIf anyone can do it, it's you and Joshua, Estelle.\x02\x03",

            "The bond between the two of you is so strong\x01",
            "that I'm not sure there's anything you couldn't\x01",
            "do together.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #135
        0x101,
        (
            "#1008FAwww...\x02\x03",

            "#1006FThanks, Kloe. I hope you're right.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5B3D")

    OP_A2(0xC)
    Jump("loc_5CA6")

    label("loc_5B43")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5BE8")

    ChrTalk(    #136
        0x17,
        (
            "#1167FNo sooner have we solved one mystery, another\x01",
            "presents itself...\x02\x03",

            "#1162FAs a game, this is certainly well thought out,\x01",
            "to say the least.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5CA6")

    label("loc_5BE8")


    ChrTalk(    #137
        0x17,
        (
            "#1383FI'm not sure how much I'll be able to do to help\x01",
            "you when it comes to Renne, but I do want to do\x01",
            "everything within my power.\x02\x03",

            "#1382FSo if there's anything I can do, say the word.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5CA6")

    TalkEnd(0xFE)

    label("loc_5CA9")

    Jump("loc_6653")

    label("loc_5CAC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x540, 4)), scpexpr(EXPR_END)), "loc_5E73")
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5DC5")

    ChrTalk(    #138
        0x17,
        (
            "#1160FThis is my first time meeting Richard ever since\x01",
            "he officially left the army.\x02\x03",

            "#1161FI'd heard his company's name mentioned on a\x01",
            "number of occasions since then, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #139
        0x101,
        (
            "#1004FOh, really?\x02\x03",

            "#1015FMaybe it's doing pretty well for itself, then.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xC)
    Jump("loc_5E6D")

    label("loc_5DC5")


    ChrTalk(    #140
        0x17,
        (
            "#1160FI've heard about Richard's company a number\x01",
            "of times since it was first established.\x02\x03",

            "#1383FThere've been small adverts for it in magazines,\x01",
            "too, I believe.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5E6D")

    TalkEnd(0xFE)
    Jump("loc_6653")

    label("loc_5E73")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x521, 6)), scpexpr(EXPR_END)), "loc_60C8")
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5FA0")

    ChrTalk(    #141
        0x17,
        (
            "#1167FWe have every reason to believe that there\x01",
            "are still people sealed in stones in this land\x01",
            "that we have yet to discover.\x02\x03",

            "#1167FWhether that is somewhere in Le Locle or on\x01",
            "the next plane, I don't know...but we need to\x01",
            "find them.\x02\x03",

            "#1162FSo let's keep going. Together.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xC)
    Jump("loc_60C2")

    label("loc_5FA0")


    ChrTalk(    #142
        0x17,
        (
            "#1162FI'm worried about all the people still trapped\x01",
            "in sealing stones here. We should hurry on.\x02\x03",

            "#1167F...Althooough, I'm also worried about Ries...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #143
        0x109,
        (
            "#1840F(Erk... Why do I get the feeling she knows\x01",
            "more than she's letting on?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #144
        0x102,
        "#1514F(She's a sharp girl. She probably does.)\x02",
    )

    CloseMessageWindow()

    label("loc_60C2")

    TalkEnd(0xFE)
    Jump("loc_6653")

    label("loc_60C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x521, 2)), scpexpr(EXPR_END)), "loc_62D9")
    SetChrFlags(0xFE, 0x10)
    TalkBegin(0xFE)
    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_6167")
    Jump("loc_61A9")

    label("loc_6167")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_6183")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_61A9")

    label("loc_6183")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_619F")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_61A9")

    label("loc_619F")

    OP_51(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_61A9")

    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6245")

    ChrTalk(    #145
        0x17,
        (
            "#1164FOh, I'm just feeding Sieg. He said he was hungry.\x02\x03",

            "#1165FHeehee. It won't take long. Promise.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xC)
    Jump("loc_62C9")

    label("loc_6245")


    ChrTalk(    #146
        0x17,
        (
            "#1160FStill, I'm truly glad that we were able to find\x01",
            "plenty of food and water here.\x02\x03",

            "We probably owe that to that ghost, too.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_62C9")

    SetChrSubChip(0xFE, 1)
    ClearChrFlags(0xFE, 0x10)
    TalkEnd(0xFE)
    Jump("loc_6653")

    label("loc_62D9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x520, 5)), scpexpr(EXPR_END)), "loc_647B")
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_63DD")

    ChrTalk(    #147
        0x17,
        (
            "#1167FI certainly wasn't expecting Anelace to have\x01",
            "been drawn in here, too...\x02\x03",

            "...\x02\x03",

            "#1162FWe should keep up with our investigation as\x01",
            "quickly as we can.\x02\x03",

            "If you need anything from me, let me know. \x01",
            "I'm always happy to lend a hand.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xC)
    Jump("loc_6475")

    label("loc_63DD")


    ChrTalk(    #148
        0x17,
        (
            "#1162FWe should keep up with our investigation as\x01",
            "quickly as we can.\x02\x03",

            "If you need anything from me, let me know. \x01",
            "I'm always happy to lend a hand.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6475")

    TalkEnd(0xFE)
    Jump("loc_6653")

    label("loc_647B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x520, 0)), scpexpr(EXPR_END)), "loc_6653")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4CC, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_649C")
    Call(5, 5)
    Jump("loc_6653")

    label("loc_649C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_658E")

    ChrTalk(    #149
        0x17,
        (
            "#1383FIt has always felt like we were being somehow\x01",
            "protected when we were in this garden\x01",
            "as opposed to anywhere else in Phantasma...\x02\x03",

            "#1160F...so I can certainly believe the idea that it may\x01",
            "be connected to that ghost.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xC)
    Jump("loc_6650")

    label("loc_658E")


    ChrTalk(    #150
        0x17,
        (
            "#1160FIt don't see any reason why this garden wouldn't\x01",
            "be connected to that ghost somehow.\x02\x03",

            "#1168FHeehee. And I don't mind that one bit. It feels\x01",
            "reassuring to know she's watching over us.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6650")

    TalkEnd(0xFE)

    label("loc_6653")

    Return()

    # Function_6_46BD end

    def Function_7_6654(): pass

    label("Function_7_6654")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x584, 0)), scpexpr(EXPR_END)), "loc_735D")
    SetChrFlags(0xFE, 0x10)
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6DC1")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_69C9")
    OP_51(0x101, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x101, 0)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_6714")
    Jump("loc_6756")

    label("loc_6714")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_6730")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_6756")

    label("loc_6730")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_674C")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_6756")

    label("loc_674C")

    OP_51(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_6756")

    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x101, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    ChrTalk(    #151
        0x101,
        (
            "#1015FHuh? Why aren't you hanging out with Tita,\x01",
            "Agate?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6882")

    ChrTalk(    #152
        0x1D,
        (
            "#551FThe hell kinda question is that? I'm not her dad.\x02\x03",

            "#053F...Besides, she's not a little kid.\x02\x03",

            "She knows what she needs to do without me\x01",
            "telling her or breathin' over her neck.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_68F9")

    label("loc_6882")


    ChrTalk(    #153
        0x1D,
        (
            "#551FThe hell kinda question is that? I'm not her dad.\x02\x03",

            "#051FBesides, she's with her friend right now. It's fine.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_68F9")


    ChrTalk(    #154
        0x101,
        "#1028FOh-hooo...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #155
        0x1D,
        "#555F...What? You got a problem?\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_69C6")

    ChrTalk(    #156
        0x104,
        (
            "#1541FThere's no need to be so flustered, dearest. ㈱\x01",
            "Your feelings are nothing to be ashamed of.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xFE, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    label("loc_69C6")

    Jump("loc_6DBB")

    label("loc_69C9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6C47")
    OP_51(0x10F, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x10F, 0)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_6A72")
    Jump("loc_6AB4")

    label("loc_6A72")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_6A8E")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_6AB4")

    label("loc_6A8E")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6AAA")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_6AB4")

    label("loc_6AAA")

    OP_51(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_6AB4")

    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x10F, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10F, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    ChrTalk(    #157
        0x10F,
        (
            "#1936FUmm...\x02\x03",

            "#1938FYou do know Tita is over there at the moment,\x01",
            "don't you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #158
        0x1D,
        (
            "#052FYeah, sure...\x02\x03",

            "#051FWhy're you asking?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #159
        0x10F,
        (
            "#1938FWell, it's just that you always seemed\x01",
            "to be with her...\x02\x03",

            "#1937FI thought you may have been wondering\x01",
            "where she was.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #160
        0x1D,
        (
            "#055FI ain't some chick separated from its\x01",
            "mother hen, you know!\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6C44")

    ChrTalk(    #161
        0x110,
        "#261FTeehee...\x02",
    )

    CloseMessageWindow()

    label("loc_6C44")

    Jump("loc_6DBB")

    label("loc_6C47")

    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_6CD7")
    Jump("loc_6D19")

    label("loc_6CD7")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_6CF3")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_6D19")

    label("loc_6CF3")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6D0F")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_6D19")

    label("loc_6D0F")

    OP_51(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_6D19")

    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    ChrTalk(    #162
        0x1D,
        (
            "#053FSounds like this is it. The end's finally in sight.\x02\x03",

            "#051FBetter train myself up as best I can--I'm gonna\x01",
            "need it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6DBB")

    OP_A2(0x5)
    Jump("loc_7350")

    label("loc_6DC1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6FBA")
    OP_51(0x101, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x101, 0)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_6E6A")
    Jump("loc_6EAC")

    label("loc_6E6A")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_6E86")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_6EAC")

    label("loc_6E86")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6EA2")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_6EAC")

    label("loc_6EA2")

    OP_51(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_6EAC")

    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x101, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    ChrTalk(    #163
        0x1D,
        (
            "#053FShe's not a kid anymore, so I'm sure she'll be\x01",
            "fine without me.\x02\x03",

            "#051FIf she needs me, I'm always there, but I know\x01",
            "she can otherwise handle herself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #164
        0x101,
        "#1028FOh, my... ☆\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #165
        0x1D,
        "#055FWhat's with that starry-eyed look?!\x02",
    )

    CloseMessageWindow()
    Jump("loc_7350")

    label("loc_6FBA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_71BE")
    OP_51(0x10F, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x10F, 0)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_7063")
    Jump("loc_70A5")

    label("loc_7063")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_707F")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_70A5")

    label("loc_707F")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_709B")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_70A5")

    label("loc_709B")

    OP_51(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_70A5")

    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x10F, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10F, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    ChrTalk(    #166
        0x1D,
        (
            "#551FWe're not always with one another! We just happen\x01",
            "to be together sometimes.\x02\x03",

            "#051FBesides, she's not a kid anymore. She doesn't need\x01",
            "me looking after her every second of the day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #167
        0x10F,
        "#1930F...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #168
        0x1D,
        "#055FWh-What's with that look?!\x02",
    )

    CloseMessageWindow()
    Jump("loc_7350")

    label("loc_71BE")

    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_724E")
    Jump("loc_7290")

    label("loc_724E")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_726A")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_7290")

    label("loc_726A")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7286")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_7290")

    label("loc_7286")

    OP_51(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_7290")

    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    ChrTalk(    #169
        0x1D,
        (
            "#050FFrom here on, we ain't gonna have time for standin'\x01",
            "still. We've gotta push on, on, and on.\x02\x03",

            "#051FSo make sure you train up while you can, okay?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7350")

    SetChrSubChip(0xFE, 0)
    ClearChrFlags(0xFE, 0x10)
    TalkEnd(0xFE)

    label("loc_735D")

    Return()

    # Function_7_6654 end

    def Function_8_735E(): pass

    label("Function_8_735E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x584, 0)), scpexpr(EXPR_END)), "loc_7799")
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7740")

    ChrTalk(    #170
        0x12,
        (
            "#060FWith the Arseille's speed, I don't think it'll take long\x01",
            "at all for us to break out of the planes.\x02\x03",

            "#067FMom was actually able to raise its top speed with a\x01",
            "few improvements the other month, too, so that'll\x01",
            "be a huge help.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7592")

    ChrTalk(    #171
        0x101,
        (
            "#1001FHuh. Really?\x02\x03",

            "#1006FI hope I can meet your mom someday.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #172
        0x12,
        (
            "#067FHeehee... I'd love you to meet her, too!\x02\x03",

            "#560FI'll have to introduce you to both my parents one day.\x01",
            "I know they've been looking forward to meeting you\x01",
            "and Joshua!\x02\x03",

            "#061FCome over any time when you get back to Liberl!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_773A")

    label("loc_7592")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_768C")

    ChrTalk(    #173
        0x102,
        (
            "#1504FTheir names were, uh...\x02\x03",

            "#1500F...Dan and Erika, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #174
        0x12,
        (
            "#067FYup. That's right.\x02\x03",

            "#560FThe two of them have been really looking forward\x01",
            "to meeting you and Estelle.\x02\x03",

            "#061FCome over any time when you get back to Liberl!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_773A")

    label("loc_768C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_773A")

    ChrTalk(    #175
        0x106,
        (
            "#552F(Oh, I'd forgotten about her messing around with\x01",
            "it before.)\x02\x03",

            "#551F(...I just remember being hit by a flying spanner\x01",
            "when she was.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #176
        0x12,
        "#565F...Hmm?\x02",
    )

    CloseMessageWindow()

    label("loc_773A")

    OP_A2(0x0)
    Jump("loc_7793")

    label("loc_7740")


    ChrTalk(    #177
        0x12,
        (
            "#062FR-Right!\x02\x03",

            "If I wanna get back to Mom and Dad,\x01",
            "I've gotta give it my all!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7793")

    TalkEnd(0xFE)
    Jump("loc_955D")

    label("loc_7799")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x565, 3)), scpexpr(EXPR_END)), "loc_80D8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4CC, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x565, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7E0B")
    SetChrFlags(0x12, 0x10)
    SetChrFlags(0x11, 0x10)
    TalkBegin(0x12)
    OP_4A(0x1B, 255)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_77F3")

    ChrTalk(    #178
        0x1B,
        "#1314F...Oh, I see.\x02",
    )

    CloseMessageWindow()
    Jump("loc_7808")

    label("loc_77F3")


    ChrTalk(    #179
        0x11,
        "#1445FReally...\x02",
    )

    CloseMessageWindow()

    label("loc_7808")


    ChrTalk(    #180
        0x12,
        (
            "#060F...Yeah.\x02\x03",

            "#563FI only know part of the story...\x02\x03",

            "...but I think Loewe must've always wanted\x01",
            "a chance to properly say goodbye to Joshua,\x01",
            "too.\x02\x03",

            "I'm happy he was finally given that chance.\x02\x03",

            "And that Joshua was able to say a proper\x01",
            "goodbye to him, too.\x02\x03",

            "#066FI'm sure Joshua's just as happy in his own way.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7968")

    ChrTalk(    #181
        0x1B,
        "#816FYeah. Me, too.\x02",
    )

    CloseMessageWindow()

    label("loc_7968")


    ChrTalk(    #182
        0x11,
        "#1448F...Indeed.\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7C35")
    OP_51(0x110, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x11, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x11, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x11, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0x11)
    ClearChrFlags(0x11, 0x10)
    TurnDirection(0x11, 0x110, 0)
    OP_51(0x11, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x11, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x11, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x11, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x11, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x11, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x11, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x11, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x11, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x11, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x11, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_7A21")
    Jump("loc_7A63")

    label("loc_7A21")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x11, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_7A3D")
    OP_51(0x11, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_7A63")

    label("loc_7A3D")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x11, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7A59")
    OP_51(0x11, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_7A63")

    label("loc_7A59")

    OP_51(0x11, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x11, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_7A63")

    OP_51(0x11, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x110, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x110, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x11, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x11, 0x10)
    Sleep(200)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C8, 4)), scpexpr(EXPR_END)), "loc_7AD9")

    ChrTalk(    #183
        0x11,
        (
            "#1962FI'm glad Renne was able to say goodbye to him\x01",
            "as well.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7B3B")

    label("loc_7AD9")


    ChrTalk(    #184
        0x11,
        (
            "#1802FStill...\x02\x03",

            "#1445F...it's a shame you weren't able to say goodbye\x01",
            "to him as well, Renne.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7B3B")


    ChrTalk(    #185
        0x110,
        (
            "#269FA shame, huh? I never expected to hear something\x01",
            "like that from you.\x02\x03",

            "#263FNevertheless, I appreciate the sentiment.\x02\x03",

            "Perhaps now that you have, you could read him\x01",
            "a story from the Testaments?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #186
        0x11,
        "#1448F...It would be my pleasure.\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x11, 0)
    Jump("loc_7DF4")

    label("loc_7C35")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C8, 4)), scpexpr(EXPR_END)), "loc_7D05")

    ChrTalk(    #187
        0x11,
        (
            "#1447FI'm glad Renne was able to say goodbye to him\x01",
            "as well.\x02\x03",

            "#1806FIt's always a painful thing to have to part with\x01",
            "someone, but it's even more painful to not have\x01",
            "the chance to say farewell.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7DF4")

    label("loc_7D05")


    ChrTalk(    #188
        0x11,
        (
            "#1806FI just wish Renne would have had a chance to say\x01",
            "goodbye to him as well.\x02\x03",

            "#1445FIt's always a painful thing to have to part with\x01",
            "someone, but it's even more painful to not have\x01",
            "the chance to say farewell...especially to family.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7DF4")

    OP_A2(0x2664)
    ClearChrFlags(0x12, 0x10)
    ClearChrFlags(0x11, 0x10)
    OP_4B(0x1B, 255)
    TalkEnd(0x12)
    Jump("loc_80D5")

    label("loc_7E0B")

    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_7E9B")
    Jump("loc_7EDD")

    label("loc_7E9B")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_7EB7")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_7EDD")

    label("loc_7EB7")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7ED3")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_7EDD")

    label("loc_7ED3")

    OP_51(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_7EDD")

    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7FDB")

    ChrTalk(    #189
        0x12,
        (
            "#060FI only know part of the story...\x02\x03",

            "#563F...but I think Loewe must've always wanted\x01",
            "a chance to properly say goodbye to Joshua.\x02\x03",

            "#066FAnd to Renne, too.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7FD5")

    ChrTalk(    #190
        0x110,
        "#263F...Heehee. Maybe.\x02",
    )

    CloseMessageWindow()

    label("loc_7FD5")

    OP_A2(0x0)
    Jump("loc_80BA")

    label("loc_7FDB")


    ChrTalk(    #191
        0x12,
        (
            "#060FWhenever I met Loewe back when he was still alive,\x01",
            "he always looked so...lonely, somehow.\x02\x03",

            "#564FThat was my first impression of him when we first\x01",
            "met, too.\x02\x03",

            "#067FHeehee. At least he's not lonely any more, though.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_80BA")

    SetChrSubChip(0xFE, 0)
    TalkEnd(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_80D5")
    SetChrSubChip(0xFE, 2)

    label("loc_80D5")

    Jump("loc_955D")

    label("loc_80D8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x561, 0)), scpexpr(EXPR_END)), "loc_8A7D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_87DD")
    RunExpression(0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x12, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x20, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    TalkBegin(0xFE)
    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x12, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x12, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x12, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0x12)
    ClearChrFlags(0x12, 0x10)
    TurnDirection(0x12, 0x0, 0)
    OP_51(0x12, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x12, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x12, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x12, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x12, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x12, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x12, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x12, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x12, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x12, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x12, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_8191")
    Jump("loc_81D3")

    label("loc_8191")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x12, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_81AD")
    OP_51(0x12, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_81D3")

    label("loc_81AD")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x12, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_81C9")
    OP_51(0x12, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_81D3")

    label("loc_81C9")

    OP_51(0x12, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x12, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_81D3")

    OP_51(0x12, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x12, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x12, 0x10)

    ChrTalk(    #192
        0x12,
        (
            "#064FPhillip is Duke Dunan's butler, isn't he?\x02\x03",

            "#063FWhat was the Lord of Phantasma thinking by\x01",
            "dragging him into all of this? He's got nothing\x01",
            "to do with it...\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_836A")

    ChrTalk(    #193
        0x110,
        (
            "#263FOh, but if you ask me, they really know how to\x01",
            "keep things interesting.\x02\x03",

            "#260FI've taken a liking to them, to be honest.\x02\x03",

            "#261FI can't wait to finally get to face them head on.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_851C")

    label("loc_836A")

    OP_51(0x12, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x20, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x20, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x20, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0x20)
    ClearChrFlags(0x20, 0x10)
    TurnDirection(0x20, 0x12, 0)
    OP_51(0x20, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x20, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x20, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x20, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x20, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x20, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x20, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x20, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x20, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x20, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x20, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_83FA")
    Jump("loc_843C")

    label("loc_83FA")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x20, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_8416")
    OP_51(0x20, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_843C")

    label("loc_8416")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x20, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8432")
    OP_51(0x20, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_843C")

    label("loc_8432")

    OP_51(0x20, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x20, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_843C")

    OP_51(0x20, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x12, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x12, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x20, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x20, 0x10)

    ChrTalk(    #194
        0x20,
        (
            "#263FOh, but if you ask me, they really know how to\x01",
            "keep things interesting.\x02\x03",

            "#260FI've taken a liking to them, to be honest.\x02\x03",

            "#261FI can't wait to finally get to face them head on.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_851C")


    ChrTalk(    #195
        0x109,
        (
            "#1066FJuuust don't think of trying to go off\x01",
            "on your own, okay?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8669")
    OP_51(0x110, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x12, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x12, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x12, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0x12)
    ClearChrFlags(0x12, 0x10)
    TurnDirection(0x12, 0x110, 0)
    OP_51(0x12, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x12, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x12, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x12, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x12, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x12, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x12, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x12, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x12, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x12, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x12, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_85FF")
    Jump("loc_8641")

    label("loc_85FF")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x12, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_861B")
    OP_51(0x12, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_8641")

    label("loc_861B")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x12, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8637")
    OP_51(0x12, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_8641")

    label("loc_8637")

    OP_51(0x12, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x12, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_8641")

    OP_51(0x12, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x110, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x110, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x12, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x12, 0x10)
    Jump("loc_8760")

    label("loc_8669")

    OP_51(0x20, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x12, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x12, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x12, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0x12)
    ClearChrFlags(0x12, 0x10)
    TurnDirection(0x12, 0x20, 0)
    OP_51(0x12, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x12, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x12, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x12, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x12, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x12, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x12, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x12, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x12, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x12, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x12, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_86F9")
    Jump("loc_873B")

    label("loc_86F9")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x12, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_8715")
    OP_51(0x12, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_873B")

    label("loc_8715")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x12, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8731")
    OP_51(0x12, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_873B")

    label("loc_8731")

    OP_51(0x12, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x12, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_873B")

    OP_51(0x12, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x20, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x20, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x12, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x12, 0x10)

    label("loc_8760")


    ChrTalk(    #196
        0x12,
        (
            "#562FS-Seriously...\x02\x03",

            "That'd be really, really dangerous...\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_87BD")

    ChrTalk(    #197
        0x10F,
        "#1440F...\x02",
    )

    CloseMessageWindow()

    label("loc_87BD")

    ClearChrFlags(0xFE, 0x10)
    OP_A2(0x0)
    TalkEnd(0xFE)
    OP_51(0x12, 0x8, (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x20, 0x8, (scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_8A7A")

    label("loc_87DD")

    SetChrFlags(0xFE, 0x10)
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_88ED")
    OP_51(0x110, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x12, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x12, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x12, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0x12)
    ClearChrFlags(0x12, 0x10)
    TurnDirection(0x12, 0x110, 0)
    OP_51(0x12, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x12, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x12, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x12, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x12, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x12, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x12, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x12, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x12, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x12, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x12, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_8883")
    Jump("loc_88C5")

    label("loc_8883")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x12, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_889F")
    OP_51(0x12, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_88C5")

    label("loc_889F")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x12, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_88BB")
    OP_51(0x12, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_88C5")

    label("loc_88BB")

    OP_51(0x12, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x12, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_88C5")

    OP_51(0x12, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x110, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x110, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x12, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x12, 0x10)
    Jump("loc_89E4")

    label("loc_88ED")

    OP_51(0x20, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x12, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x12, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x12, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0x12)
    ClearChrFlags(0x12, 0x10)
    TurnDirection(0x12, 0x20, 0)
    OP_51(0x12, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x12, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x12, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x12, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x12, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x12, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x12, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x12, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x12, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x12, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x12, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_897D")
    Jump("loc_89BF")

    label("loc_897D")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x12, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_8999")
    OP_51(0x12, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_89BF")

    label("loc_8999")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x12, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_89B5")
    OP_51(0x12, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_89BF")

    label("loc_89B5")

    OP_51(0x12, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x12, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_89BF")

    OP_51(0x12, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x20, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x20, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x12, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x12, 0x10)

    label("loc_89E4")


    ChrTalk(    #198
        0x12,
        (
            "#562FTrying to proceed on your own would be really,\x01",
            "REALLY dangerous, Renne.\x02\x03",

            "Please don't try and do that...\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8A6D")
    SetChrSubChip(0xFE, 0)
    Jump("loc_8A72")

    label("loc_8A6D")

    SetChrSubChip(0xFE, 1)

    label("loc_8A72")

    ClearChrFlags(0xFE, 0x10)
    TalkEnd(0xFE)

    label("loc_8A7A")

    Jump("loc_955D")

    label("loc_8A7D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x560, 0)), scpexpr(EXPR_END)), "loc_8D51")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8C3C")
    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_8B22")
    Jump("loc_8B64")

    label("loc_8B22")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_8B3E")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_8B64")

    label("loc_8B3E")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8B5A")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_8B64")

    label("loc_8B5A")

    OP_51(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_8B64")

    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    ChrTalk(    #199
        0x12,
        (
            "#064FOh, Renne! Heehee.\x01",
            "#061FWe'll have to talk again later.\x02\x03",

            "I still want to finish our conversation from\x01",
            "earlier.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #200
        0x110,
        "#261FI'd be delighted.\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0)
    TalkEnd(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8C39")
    SetChrSubChip(0xFE, 1)

    label("loc_8C39")

    Jump("loc_8D4E")

    label("loc_8C3C")

    SetChrFlags(0xFE, 0x10)
    TalkBegin(0xFE)

    ChrTalk(    #201
        0x12,
        "#061FSo then I decided to give him a name...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #202
        0x20,
        (
            "#261FI raised a cat once before, too, you know.\x02\x03",

            "#265FThe professor called him a Steel Cougar,\x01",
            "if I recall...\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xFE, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(    #203
        0x12,
        (
            "#065FTh-That doesn't sound like the kind of cat\x01",
            "I'm thinking of!\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xFE, 0x10)
    TalkEnd(0xFE)

    label("loc_8D4E")

    Jump("loc_955D")

    label("loc_8D51")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x540, 7)), scpexpr(EXPR_END)), "loc_955D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4CC, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_93A0")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8F83")
    TalkBegin(0xFE)
    TurnDirection(0xFE, 0x110, 0)

    ChrTalk(    #204
        0x12,
        "#064FOooh, Renne!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #205
        0x110,
        "#264FWhat are you doing here, Tita?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #206
        0x12,
        (
            "#060FOh, I was sort of just wandering aimlessly\x01",
            "while I was preoccupied.\x02\x03",

            "#061FSeeing you again made me remember all the\x01",
            "fun things we did together before, so I've been\x01",
            "thinking about those.\x02\x03",

            "Like that time we went shopping and bought\x01",
            "those really pretty brooches and stuff.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #207
        0x110,
        (
            "#260FHeehee. Oh, right.\x02\x03",

            "#267FThat reminds me, though...\x01",
            "I found one exactly like them in a tiny little\x01",
            "shop a while back.\x02\x03",

            "#261FThe jewel in the middle was red, though.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_901C")

    label("loc_8F83")

    SetChrFlags(0xFE, 0x10)
    TalkBegin(0xFE)

    ChrTalk(    #208
        0x20,
        (
            "#261F...But guess what? I found a brooch exactly\x01",
            "like the ones we bought a while back there.\x02\x03",

            "#265FThe jewel in the middle was red, though.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_901C")


    ChrTalk(    #209
        0x12,
        (
            "#064FAww... You're so lucky.\x02\x03",

            "They were all sold out of those in the shop\x01",
            "in Grancel.\x02\x03",

            "#562F*sigh* I really wanted a red one, too...\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_91B4")

    ChrTalk(    #210
        0x110,
        (
            "#265FI know! Why don't we go on a shopping trip\x01",
            "together sometime, then? We could go to\x01",
            "somewhere reeeally far away.\x02\x03",

            "#269FYou'd like the Eastern Quarter in Calvard,\x01",
            "that's for sure. You could spend a whole day\x01",
            "shopping there and never feel bored.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_92B1")

    label("loc_91B4")


    ChrTalk(    #211
        0x20,
        (
            "#265FI know! Why don't we go on a shopping trip\x01",
            "together sometime, then? We could go to\x01",
            "somewhere reeeally far away.\x02\x03",

            "#269FYou'd like the Eastern Quarter in Calvard,\x01",
            "that's for sure. You could spend a whole day\x01",
            "shopping there and never feel bored.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_92B1")


    ChrTalk(    #212
        0x12,
        (
            "#064FR-Really?\x02\x03",

            "#061FI wonder what kinds of cute accessories\x01",
            "they'd have there?\x02\x03",

            "#560FOh, yeah! Let me tell you about the pendant \x01",
            "I bought a while back!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #213
        0x101,
        (
            "#1016F(It looks like they're back to good times\x01",
            "in no time.)\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xFE, 0x10)
    OP_A2(0x2662)
    TalkEnd(0xFE)
    Jump("loc_955D")

    label("loc_93A0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_94DE")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_9487")
    TalkBegin(0xFE)
    TurnDirection(0x12, 0x110, 0)

    ChrTalk(    #214
        0x12,
        (
            "#061FWe'll have to go shopping together again\x01",
            "sometime!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #215
        0x110,
        (
            "#260F...Sure. I wouldn't mind.\x02\x03",

            "#263FBut first we're going to have to get out of\x01",
            "Phantasma, aren't we?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #216
        0x12,
        "#064F...Oh, right.\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Jump("loc_94D8")

    label("loc_9487")

    SetChrFlags(0xFE, 0x10)
    TalkBegin(0xFE)

    ChrTalk(    #217
        0x12,
        (
            "#065FWh-What? Really?!\x02\x03",

            "#067F...I kinda want to see it now.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    ClearChrFlags(0xFE, 0x10)

    label("loc_94D8")

    OP_A2(0x0)
    Jump("loc_955D")

    label("loc_94DE")

    TalkBegin(0xFE)

    ChrTalk(    #218
        0x12,
        (
            "#560FRenne's so lucky to be able to visit all\x01",
            "those shops, isn't she?\x02\x03",

            "#067FI want to go and see more of them, too!\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)

    label("loc_955D")

    Return()

    # Function_8_735E end

    def Function_9_955E(): pass

    label("Function_9_955E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x565, 4)), scpexpr(EXPR_END)), "loc_95BA")
    TalkBegin(0xFE)

    ChrTalk(    #219
        0x1B,
        "#814FHuh? Did something happen?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #220
        0x109,
        "#1075FNothing to worry about, no.\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Jump("loc_ABCE")

    label("loc_95BA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x565, 3)), scpexpr(EXPR_END)), "loc_9A3D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4CC, 4)), scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9885")
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9748")
    TurnDirection(0xFE, 0x102, 0)

    ChrTalk(    #221
        0x1B,
        (
            "#1316FHmm... Okay, so...I'm not really sure on the\x01",
            "details of what happened...\x02\x03",

            "#816F...but I know one thing for sure.\x02\x03",

            "#811FYou're looking a lot brighter and more positive\x01",
            "now, Joshua.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #222
        0x102,
        (
            "#1504FReally?\x02\x03",

            "#1513F...Thanks.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_9742")
    TurnDirection(0xFE, 0x101, 400)
    Sleep(300)

    ChrTalk(    #223
        0x1B,
        "#816FThat goes for you, too, Estelle!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #224
        0x101,
        "#1017FA-Ahaha... Really?\x02",
    )

    CloseMessageWindow()

    label("loc_9742")

    OP_A2(0x9)
    Jump("loc_987F")

    label("loc_9748")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_97B0")
    TurnDirection(0xFE, 0x102, 0)

    ChrTalk(    #225
        0x1B,
        (
            "#816FYou look a lot more positive now, Joshua.\x02\x03",

            "#811FI'm so happy for you!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_987F")

    label("loc_97B0")


    ChrTalk(    #226
        0x1B,
        (
            "#817FI don't know that much about Joshua and Loewe's\x01",
            "relationship, either...\x02\x03",

            "#1314F...but what happened seems to have gone a long\x01",
            "way in helping him move forward, at least. That's\x01",
            "a good thing, right?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_987F")

    TalkEnd(0xFE)
    Jump("loc_9A3A")

    label("loc_9885")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_98A5")
    Call(5, 8)
    Jump("loc_9A3A")

    label("loc_98A5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_998A")
    SetChrFlags(0xFE, 0x10)
    TalkBegin(0xFE)

    ChrTalk(    #227
        0x1B,
        (
            "#1314FWell, I'm not really that filled in on the whole\x01",
            "thing, to be honest.\x02\x03",

            "#813FFrom what I know, Loewe was like a brother\x01",
            "to Joshua.\x02\x03",

            "#817FBut during what happened on the Liber Ark,\x01",
            "he...\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xFE, 0x10)
    TalkEnd(0xFE)
    Jump("loc_9A3A")

    label("loc_998A")

    TalkBegin(0xFE)

    ChrTalk(    #228
        0x1B,
        (
            "#817FUmm...\x02\x03",

            "Loewe was basically like a brother to Joshua,\x01",
            "right?\x02\x03",

            "#813FI wasn't able to go to the Liber Ark with you guys,\x01",
            "so I'm not clued up on all this stuff...\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)

    label("loc_9A3A")

    Jump("loc_ABCE")

    label("loc_9A3D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x564, 0)), scpexpr(EXPR_END)), "loc_9DC8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9A96")
    SetChrFlags(0xFE, 0x10)
    TalkBegin(0xFE)

    ChrTalk(    #229
        0x1B,
        (
            "#814FH-Huh...?!\x02\x03",

            "#1317FWhere did everyone go?!\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xFE, 0x10)
    OP_A2(0x9)
    TalkEnd(0xFE)
    Jump("loc_9DC5")

    label("loc_9A96")

    SetChrFlags(0xFE, 0x10)
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9BDE")
    OP_62(0x1B, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x1B, 0x107, 500)

    ChrTalk(    #230
        0x1B,
        "#1310FOh! There you two are!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #231
        0x107,
        "#067FHeehee...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #232
        0x110,
        (
            "#263FWe're off for a while.\x02\x03",

            "#260FWe'll talk with you again later,\x01",
            "though, okay?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_9BDB")

    ChrTalk(    #233
        0x1B,
        (
            "#818FAww...\x02\x03",

            "#1311FOkay, then... But you'll have to come and join us,\x01",
            "too, Ries. ㈱\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #234
        0x10F,
        "#1802FO-Oh...\x02",
    )

    CloseMessageWindow()

    label("loc_9BDB")

    Jump("loc_9DBD")

    label("loc_9BDE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_9CA4")
    OP_62(0x1B, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x1B, 0x107, 500)

    ChrTalk(    #235
        0x1B,
        (
            "#1310FOh!! I spy a Tita!\x02\x03",

            "#811FC'mere and give me a cuddle!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #236
        0x107,
        (
            "#067FU-Umm...\x02\x03",

            "#560FI-I've gotta head out now... We'll talk later,\x01",
            "though, okay?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9DBD")

    label("loc_9CA4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_9D45")
    OP_62(0x1B, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x1B, 0x110, 500)

    ChrTalk(    #237
        0x1B,
        "#1310FOh!! I spy a Renne!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #238
        0x110,
        (
            "#263FHeehee. We're off to explore now.\x02\x03",

            "#260FWe can talk again later, though.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9DBD")

    label("loc_9D45")


    ChrTalk(    #239
        0x1B,
        (
            "#1316FTita and Renne were here before, too.\x02\x03",

            "#818FI guess they must've wandered off while\x01",
            "I was taking a nap here.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9DBD")

    ClearChrFlags(0xFE, 0x10)
    TalkEnd(0xFE)

    label("loc_9DC5")

    Jump("loc_ABCE")

    label("loc_9DC8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x562, 5)), scpexpr(EXPR_END)), "loc_9FB5")
    SetChrFlags(0x21, 0x10)
    TalkBegin(0x21)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9F23")
    OP_A2(0x9)

    ChrTalk(    #240
        0x21,
        (
            "#1311F#60WZzz... Mmm...#20W\x02\x03",

            "#819F#60WAhaha... Wait for meee...#20W\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_9E59")

    ChrTalk(    #241
        0x101,
        "#1016FU-Umm... Anelace...?\x02",
    )

    CloseMessageWindow()

    label("loc_9E59")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_9E8A")

    ChrTalk(    #242
        0x102,
        "#1514FShe's fast asleep...\x02",
    )

    CloseMessageWindow()
    Jump("loc_9F20")

    label("loc_9E8A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_9ED7")

    ChrTalk(    #243
        0x103,
        "#1526F*sigh* She really can sleep anywhere, can't she?\x02",
    )

    CloseMessageWindow()
    Jump("loc_9F20")

    label("loc_9ED7")


    ChrTalk(    #244
        0x109,
        (
            "#1068FI wonder what she's chasing in that bizarre\x01",
            "dream of hers...?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9F20")

    Jump("loc_9FAA")

    label("loc_9F23")

    OP_9E(0x21, 0x14, 0x0, 0xC8, 0xBB8)
    Sleep(300)
    OP_9E(0x21, 0x14, 0x0, 0x1F4, 0xFA0)
    Sleep(200)

    ChrTalk(    #245
        0x21,
        (
            "#1311F#60WHeehee... I got youuu...\x02\x03",

            "Now I can go to the Plushy Kingdom, too... ♪\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9FAA")

    ClearChrFlags(0x21, 0x10)
    TalkEnd(0x21)
    Jump("loc_ABCE")

    label("loc_9FB5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x561, 0)), scpexpr(EXPR_END)), "loc_A516")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x561, 1)), scpexpr(EXPR_END)), "loc_A2A4")
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x561, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A1E5")

    ChrTalk(    #246
        0x1B,
        "#814FOh, 'sup? Anything wrong?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #247
        0x109,
        "#1078FWell...\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(72, 320, 56, 3)

    AnonymousTalk(    #248
        (
            "\x07\x05Kevin explained to Anelace that they thought she was the person the amberl\x01",
            "monument's inscription was asking for.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #249
        0x1B,
        (
            "#814FMe? The 'sword-wielding dame'?\x02\x03",

            "#818FI dunnooo... I mean, it's a cool-sounding title\x01",
            "and all, but does it really fit me?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #250
        0x109,
        (
            "#1066FIt does if you ask me. But hey, even if you're\x01",
            "not sure, it's worth a try, right?\x02\x03",

            "Do you mind coming with us and giving it a go?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #251
        0x1B,
        (
            "#814FYou got it.\x02\x03",

            "#810FOff we go, then!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2B0B)
    Jump("loc_A29E")

    label("loc_A1E5")


    ChrTalk(    #252
        0x1B,
        (
            "#818FI'm still not sure I'm the person that monument\x01",
            "wants, but it's worth a try, at least.\x02\x03",

            "#810FSo just let me know when you're ready to go back\x01",
            "there. I'm ready to go any time.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A29E")

    TalkEnd(0xFE)
    Jump("loc_A513")

    label("loc_A2A4")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A3F1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C7, 7)), scpexpr(EXPR_END)), "loc_A36A")

    ChrTalk(    #253
        0x1B,
        (
            "#1317FD-Damn. I didn't think he was going to be\x01",
            "that powerful...\x02\x03",

            "#1316FThat fancy-schmancy skill of his was just\x01",
            "cheating...\x02\x03",

            "#815FHow can you even DO that with a sword?!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A3EB")

    label("loc_A36A")


    ChrTalk(    #254
        0x1B,
        (
            "#814FPhillip was that duke's butler, right?\x02\x03",

            "#818FWas he really that strong?\x02\x03",

            "He didn't really look it when I last saw him.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A3EB")

    OP_A2(0x9)
    Jump("loc_A510")

    label("loc_A3F1")


    ChrTalk(    #255
        0x1B,
        (
            "#1316F*sigh* I guess if I couldn't tell his true strength,\x01",
            "that means I've got a long way to go.\x02\x03",

            "#812FAll right! Time to get Richard to join me for \x01",
            "some more training!\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xB)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A510")
    TurnDirection(0x1B, 0x10C, 400)
    Sleep(500)

    ChrTalk(    #256
        0x1B,
        "#815FWell? Would you be willing to?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #257
        0x10C,
        "#111FHaha... I'll give it some thought.\x02",
    )

    CloseMessageWindow()

    label("loc_A510")

    TalkEnd(0xFE)

    label("loc_A513")

    Jump("loc_ABCE")

    label("loc_A516")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x560, 0)), scpexpr(EXPR_END)), "loc_ABCE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A9DF")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A7A6")
    TalkBegin(0xFE)

    ChrTalk(    #258
        0x1B,
        (
            "#817FSooo...\x02\x03",

            "...this world is on a high-level plane, repeating a \x01",
            "process of self-organization and creation in order\x01",
            "to realize the desires of humanity, operating on...\x02\x03",

            "...\x01",
            "...\x01",
            "...\x02",
        )
    )

    CloseMessageWindow()
    OP_9E(0x1B, 0x14, 0x0, 0x320, 0xBB8)
    Sleep(1000)

    ChrTalk(    #259
        0x1B,
        "#819F...Blaaarghhh...\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A66C")

    ChrTalk(    #260
        0x101,
        "#1004FI think her head just exploded.\x02",
    )

    CloseMessageWindow()
    Jump("loc_A7A3")

    label("loc_A66C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A6E0")

    ChrTalk(    #261
        0x102,
        (
            "#1512FAnelace, you don't need to force yourself to\x01",
            "understand how this world works, you know.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A7A3")

    label("loc_A6E0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A754")

    ChrTalk(    #262
        0x103,
        (
            "#1525FAnelace, you don't need to force yourself to\x01",
            "understand how this world works, you know.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A7A3")

    label("loc_A754")


    ChrTalk(    #263
        0x107,
        "#065FA-Anelace! Hang in there!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #264
        0x109,
        "#1068FI think her head just exploded.\x02",
    )

    CloseMessageWindow()

    label("loc_A7A3")

    Jump("loc_A9D1")

    label("loc_A7A6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A859")
    SetChrFlags(0xFE, 0x10)
    TalkBegin(0xFE)
    TurnDirection(0xFE, 0x110, 0)

    ChrTalk(    #265
        0x1B,
        (
            "#816FSo you like plushies, too, huh, Renne?\x02\x03",

            "#811FWe're gonna have to sit and talk about\x01",
            "them later, then!\x02\x03",

            "I need to find out just HOW MUCH.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A9D1")

    label("loc_A859")

    SetChrFlags(0xFE, 0x10)
    TalkBegin(0xFE)

    ChrTalk(    #266
        0x1B,
        (
            "#814FWhat? You've got that really rare Landmore\x01",
            "limited edition plushie?\x02\x03",

            "#1317FI really want that one, too! You're so lucky...\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A911")

    ChrTalk(    #267
        0x101,
        "#1016F(A-Anelace...)\x02",
    )

    CloseMessageWindow()
    Jump("loc_A967")

    label("loc_A911")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A941")

    ChrTalk(    #268
        0x102,
        "#1512F(Umm... Anelace...)\x02",
    )

    CloseMessageWindow()
    Jump("loc_A967")

    label("loc_A941")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A967")

    ChrTalk(    #269
        0x103,
        "#1525F(I swear...)\x02",
    )

    CloseMessageWindow()

    label("loc_A967")


    ChrTalk(    #270
        0x109,
        (
            "#1068F(I think she's probably the one least bothered\x01",
            "about what's going on here out of all of us...)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A9D1")

    ClearChrFlags(0xFE, 0x10)
    OP_A2(0x9)
    TalkEnd(0xFE)
    Jump("loc_ABCE")

    label("loc_A9DF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_AA6A")
    SetChrFlags(0xFE, 0x10)
    TalkBegin(0xFE)

    ChrTalk(    #271
        0x1B,
        (
            "#817FSo what's a girl gotta do to get plushies to pop\x01",
            "up out of nowhere?\x02\x03",

            "Hmm...\x02\x03",

            "#1312FHmmmmm...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_ABC6")

    label("loc_AA6A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_AB1C")
    SetChrFlags(0xFE, 0x10)
    TalkBegin(0xFE)
    TurnDirection(0xFE, 0x110, 0)

    ChrTalk(    #272
        0x1B,
        (
            "#816FSo you like plushies, too, huh, Renne?\x02\x03",

            "#811FWe're gonna have to sit and talk about them later,\x01",
            "then! I need to find out just HOW MUCH.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_ABC6")

    label("loc_AB1C")

    SetChrFlags(0xFE, 0x10)
    TalkBegin(0xFE)

    ChrTalk(    #273
        0x1B,
        (
            "#812FI was all set on going to get that one when it \x01",
            "came out...\x02\x03",

            "#1316F...but then this major job came in all of a sudden\x01",
            "and I couldn't go out and buy it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_ABC6")

    ClearChrFlags(0xFE, 0x10)
    TalkEnd(0xFE)

    label("loc_ABCE")

    Return()

    # Function_9_955E end

    def Function_10_ABCF(): pass

    label("Function_10_ABCF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x565, 3)), scpexpr(EXPR_END)), "loc_AF10")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AD23")
    SetChrFlags(0xFE, 0x10)
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_AC8B")

    ChrTalk(    #274
        0x15,
        (
            "#416F...Okay. That should do for now.\x02\x03",

            "#210FIt always pays to give your gun a good polish once\x01",
            "in a while to keep it in top working condition.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AD15")

    label("loc_AC8B")


    ChrTalk(    #275
        0x15,
        (
            "#213FHey, take it easy. Everyone needs to rest from\x01",
            "time to time, you know.\x02\x03",

            "#212FCome on! Have a drink of this and take a load\x01",
            "off.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AD15")

    ClearChrFlags(0xFE, 0x10)
    OP_A2(0x4)
    TalkEnd(0xFE)
    Jump("loc_AF10")

    label("loc_AD23")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_ADD0")
    SetChrFlags(0xFE, 0x10)
    TalkBegin(0xFE)
    TurnDirection(0xFE, 0x102, 0)

    ChrTalk(    #276
        0x15,
        (
            "#213FOh, Joshua...\x02\x03",

            "#215FUmm... Umm...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #277
        0x102,
        (
            "#1513FI'm fine.\x02\x03",

            "#1501FThanks for worrying about me, Josette.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #278
        0x15,
        "#414FO-Oh, right...\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0xFE, 0x10)
    Jump("loc_AF0D")

    label("loc_ADD0")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_AE86")

    ChrTalk(    #279
        0x15,
        (
            "#210FOrbal guns are pretty delicate things, so you need\x01",
            "to take them apart and give them a good clean once\x01",
            "in a while to keep them in top working condition.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AF0D")

    label("loc_AE86")


    ChrTalk(    #280
        0x15,
        (
            "#416FI swear, this princess...\x02\x03",

            "#212FI don't know why she won't just rely on us some\x01",
            "instead of trying to investigate by herself.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AF0D")

    TalkEnd(0xFE)

    label("loc_AF10")

    Return()

    # Function_10_ABCF end

    def Function_11_AF11(): pass

    label("Function_11_AF11")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x565, 3)), scpexpr(EXPR_END)), "loc_B190")
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B066")

    ChrTalk(    #281
        0x13,
        (
            "#175FWhile this is just my personal belief, and I will never\x01",
            "have a chance to find out if it is right...\x02\x03",

            "#170F...I can't help but feel that 2nd Lieutenant Lorence\x01",
            "may have admired the colonel on a personal level,\x01",
            "too.\x02\x03",

            "#179FI don't have any hard evidence to back up my\x01",
            "belief, of course. Just call it instinct.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)
    Jump("loc_B18A")

    label("loc_B066")


    ChrTalk(    #282
        0x13,
        (
            "#176FWhile there's no doubt that 2nd Lieutenant Lorence\x01",
            "used the Intelligence Division, I don't think that was\x01",
            "the only reason he served in it.\x02\x03",

            "#170FWhile I don't have any hard evidence to back up\x01",
            "my belief, I feel as though he felt a genuine sense\x01",
            "of loyalty to the organization, too.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B18A")

    TalkEnd(0xFE)
    Jump("loc_CB18")

    label("loc_B190")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x564, 0)), scpexpr(EXPR_END)), "loc_B19A")
    Jump("loc_CB18")

    label("loc_B19A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x562, 5)), scpexpr(EXPR_END)), "loc_B3D5")
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B329")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C8, 2)), scpexpr(EXPR_END)), "loc_B242")

    ChrTalk(    #283
        0x13,
        (
            "#179FI had hoped to meet Kilika one day...\x02\x03",

            "#178F...but I hadn't expected she would be quite that\x01",
            "much of a force to be reckoned with.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B323")

    label("loc_B242")


    ChrTalk(    #284
        0x13,
        (
            "#178FI'd heard Kilika was able to make her way through\x01",
            "one of the shadow towers alone, so she is clearly\x01",
            "a force to be reckoned with.\x02\x03",

            "#179FI wish I had been able to meet her while she was\x01",
            "still in Liberl, to be honest.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B323")

    OP_A2(0x2)
    Jump("loc_B3CF")

    label("loc_B329")


    ChrTalk(    #285
        0x13,
        (
            "#175FRegardless, at least now we are half way through\x01",
            "this plane.\x02\x03",

            "#176FPerhaps now would be a good time to make sure\x01",
            "everyone is well trained and battle ready.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B3CF")

    TalkEnd(0xFE)
    Jump("loc_CB18")

    label("loc_B3D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x561, 0)), scpexpr(EXPR_END)), "loc_B817")
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B727")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B51B")
    TurnDirection(0xFE, 0x104, 0)

    ChrTalk(    #286
        0x104,
        (
            "#1541FWhy, hello, Julia.\x02\x03",

            "It's occurred to me that I never did properly\x01",
            "thank you for your assistance during my return\x01",
            "to Erebonia.\x02\x03",

            "#1547FSo, what say you? Would you like to accompany\x01",
            "me for a drink or two? On me, of course.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #287
        0x13,
        "#172FI... Well... I'm not sure that would be...\x02",
    )

    CloseMessageWindow()
    Jump("loc_B6E7")

    label("loc_B51B")


    ChrTalk(    #288
        0x13,
        (
            "#175FPrince Olivert seems rather insistent on me\x01",
            "accompanying him for drinks. I'm not sure\x01",
            "what to do...\x02\x03",

            "#176FP-Perhaps it would be best for me to accept\x01",
            "his offer?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B654")

    ChrTalk(    #289
        0x101,
        (
            "#1007FI swear, that Olivier...\x02\x03",

            "#1009FThe best thing to do is to ignore him, Julia!\x01",
            "Just pretend he doesn't even exist.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B6E7")

    label("loc_B654")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B6B8")

    ChrTalk(    #290
        0x102,
        (
            "#1512FI think the best thing to do would be to refuse.\x01",
            "In no uncertain terms.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B6E7")

    label("loc_B6B8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B6E7")

    ChrTalk(    #291
        0x105,
        "#1165FAhaha... Weeeeeell...\x02",
    )

    CloseMessageWindow()

    label("loc_B6E7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B721")

    ChrTalk(    #292
        0x10D,
        "#272FFeel free to ignore him, Captain.\x02",
    )

    CloseMessageWindow()

    label("loc_B721")

    OP_A2(0x2)
    Jump("loc_B811")

    label("loc_B727")


    ChrTalk(    #293
        0x13,
        (
            "#176F*cough* The prince aside...\x02\x03",

            "#178F...I'm still rather surprised that Phillip was one of\x01",
            "those recreated in this world.\x02\x03",

            "#175FAll of this just makes me wish that I could have\x01",
            "the chance to learn from him in the real world...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B811")

    TalkEnd(0xFE)
    Jump("loc_CB18")

    label("loc_B817")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x560, 0)), scpexpr(EXPR_END)), "loc_BA1B")
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B963")

    ChrTalk(    #294
        0x13,
        (
            "#179FI never would have imagined the very ghost who\x01",
            "aided us all this time was an ancestor of the\x01",
            "Liberlian royal family.\x02\x03",

            "#171FHaha. Still, I can hardly imagine a more reassuring\x01",
            "revelation.\x02\x03",

            "#170FI'd like to think that with her help, we may be\x01",
            "able to compete against the Lord of Phantasma\x01",
            "after all.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)
    Jump("loc_BA15")

    label("loc_B963")


    ChrTalk(    #295
        0x13,
        (
            "#170FIt's far too soon to be getting optimistic about\x01",
            "our odds of success...\x02\x03",

            "...but with Celeste's help, we may be able to\x01",
            "compete against the Lord of Phantasma after\x01",
            "all.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BA15")

    TalkEnd(0xFE)
    Jump("loc_CB18")

    label("loc_BA1B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x540, 7)), scpexpr(EXPR_END)), "loc_BDCE")
    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_BAB2")
    Jump("loc_BAF4")

    label("loc_BAB2")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_BACE")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_BAF4")

    label("loc_BACE")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_BAEA")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_BAF4")

    label("loc_BAEA")

    OP_51(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_BAF4")

    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BCC6")

    ChrTalk(    #296
        0x13,
        (
            "#176FIt's amazing to think that this world is where\x01",
            "people's thoughts become reality...\x02\x03",

            "#175FEven after all we've seen so far, I still find\x01",
            "myself doubting that could even be possible,\x01",
            "but it certainly makes sense.\x02\x03",

            "Still, if we assume that everything that's \x01",
            "happened so far has gone according to plan\x01",
            "for the Lord of Phantasma...\x02\x03",

            "#170F...then I think it's about time we started trying\x01",
            "to change that, hmm?\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)
    Jump("loc_BDC3")

    label("loc_BCC6")


    ChrTalk(    #297
        0x13,
        (
            "#176FEven after all we've seen so far, I still find\x01",
            "myself doubting that what Renne said could even\x01",
            "be possible, but I can't deny her logic...\x02\x03",

            "Still, enough is enough.\x02\x03",

            "#170FI think the Lord of Phantasma has had things their\x01",
            "way for far too long.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BDC3")

    SetChrSubChip(0xFE, 0)
    TalkEnd(0xFE)
    Jump("loc_CB18")

    label("loc_BDCE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x540, 4)), scpexpr(EXPR_END)), "loc_C1BB")
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C102")

    ChrTalk(    #298
        0x13,
        (
            "#170FBoth General Morgan and Brigadier General Bright\x01",
            "did their best to stop Richard from leaving the army\x01",
            "when he made his decision to do so.\x02\x03",

            "No one denies that he made a mistake, but he was\x01",
            "an exceptionally skilled soldier, and the military is\x01",
            "worse off without him.\x02\x03",

            "#179FI've heard rumors that Brigadier General Bright\x01",
            "hasn't given up on bringing him back into the\x01",
            "ranks yet, even.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_BFF3")

    ChrTalk(    #299
        0x105,
        "#1165FThat sounds just like something he would do.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #300
        0x101,
        (
            "#1007FYeah... He's never been one for giving people\x01",
            "a break.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C0FC")

    label("loc_BFF3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C08E")

    ChrTalk(    #301
        0x102,
        (
            "#1508FPresumably so that he can offload more of\x01",
            "his work onto him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #302
        0x101,
        (
            "#1007FYeah... He's never been one for giving people\x01",
            "a break.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C0FC")

    label("loc_C08E")


    ChrTalk(    #303
        0x101,
        (
            "#1019FYou've got to be kidding me...\x02\x03",

            "#1007FHe really doesn't believe in giving people\x01",
            "a break, does he?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C0FC")

    OP_A2(0x2)
    Jump("loc_C1B5")

    label("loc_C102")


    ChrTalk(    #304
        0x13,
        (
            "#178FRegardless, I wasn't expecting Richard of all\x01",
            "people to end up here...\x02\x03",

            "#176FBut he does fit within the rule that only those\x01",
            "who have aided us end up in sealing stones.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C1B5")

    TalkEnd(0xFE)
    Jump("loc_CB18")

    label("loc_C1BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x540, 0)), scpexpr(EXPR_END)), "loc_C35D")
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C2AD")

    ChrTalk(    #305
        0x13,
        (
            "#176FI was aware that Father Graham was a member\x01",
            "of the Gralsritter...\x02\x03",

            "#175FI certainly wasn't aware that he was such a high-\x01",
            "ranking member of the group, however.\x02\x03",

            "And one of its most powerful members, at that.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)
    Jump("loc_C357")

    label("loc_C2AD")


    ChrTalk(    #306
        0x13,
        (
            "#176FI was aware that Father Graham was a member\x01",
            "of the Gralsritter...\x02\x03",

            "#175FI certainly wasn't aware that he was such a high-\x01",
            "ranking member of the group, however.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C357")

    TalkEnd(0xFE)
    Jump("loc_CB18")

    label("loc_C35D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x521, 6)), scpexpr(EXPR_END)), "loc_C4F2")
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C445")

    ChrTalk(    #307
        0x13,
        (
            "#178FWe've now conquered all three of the ordeals\x01",
            "that this garden's master mentioned.\x02\x03",

            "I presume that means our next destination must be\x01",
            "the fifth plane.\x02\x03",

            "#176FI wonder what kind of place that will be.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)
    Jump("loc_C4EC")

    label("loc_C445")


    ChrTalk(    #308
        0x13,
        (
            "#178FI presume that since we've conquered all three\x01",
            "of the ordeals here, our next destination will be\x01",
            "the fifth plane.\x02\x03",

            "I wonder what kind of place that will be.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C4EC")

    TalkEnd(0xFE)
    Jump("loc_CB18")

    label("loc_C4F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x521, 2)), scpexpr(EXPR_END)), "loc_C6FE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C5E7")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C5A3")
    TalkBegin(0xFE)

    ChrTalk(    #309
        0x13,
        (
            "#176F*sigh* I had an important meeting to attend at\x01",
            "military HQ tomorrow, too.\x02\x03",

            "But it looks like I'll have no choice but to miss it.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Jump("loc_C5E1")

    label("loc_C5A3")

    SetChrFlags(0xFE, 0x10)
    TalkBegin(0xFE)

    ChrTalk(    #310
        0x13,
        "#178FShould you not rest, Your Highness?\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0xFE, 0x10)
    TalkEnd(0xFE)

    label("loc_C5E1")

    OP_A2(0x2)
    Jump("loc_C6FB")

    label("loc_C5E7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C6BD")
    TalkBegin(0xFE)

    ChrTalk(    #311
        0x13,
        (
            "#172FOr is the meeting today, now? \x02\x03",

            "#175FBeing in this place truly distorts your sense\x01",
            "of time's passing...\x02\x03",

            "It's even possible the meeting could've been\x01",
            "days ago, thinking about it...\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Jump("loc_C6FB")

    label("loc_C6BD")

    SetChrFlags(0xFE, 0x10)
    TalkBegin(0xFE)

    ChrTalk(    #312
        0x13,
        "#178FShould you not rest, Your Highness?\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0xFE, 0x10)
    TalkEnd(0xFE)

    label("loc_C6FB")

    Jump("loc_CB18")

    label("loc_C6FE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x520, 5)), scpexpr(EXPR_END)), "loc_C925")
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C822")

    ChrTalk(    #313
        0x13,
        (
            "#178FIt's clear from everything they've said and done\x01",
            "so far that our foes have thoroughly researched\x01",
            "all of us.\x02\x03",

            "#175FAnd yet recreating a place from outside Liberl\x01",
            "was certainly not something I expected them to\x01",
            "do...\x02\x03",

            "Just who is the Lord of Phantasma, anyway?\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)
    Jump("loc_C91F")

    label("loc_C822")


    ChrTalk(    #314
        0x13,
        (
            "#178FWe know now that the Lord of Phantasma\x01",
            "is challenging us with a significant amount\x01",
            "of research on us under their belt.\x02\x03",

            "#176FIt doesn't make sense to me. The more they do,\x01",
            "the more I can't fathom what it is they want.\x02\x03",

            "#175FOr who they are...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C91F")

    TalkEnd(0xFE)
    Jump("loc_CB18")

    label("loc_C925")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x520, 0)), scpexpr(EXPR_END)), "loc_CB18")
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CA38")

    ChrTalk(    #315
        0x13,
        (
            "#176FIt's disturbing to think that we are literally\x01",
            "fighting fiends taken from the church's texts...\x02\x03",

            "#175FThen again, our enemies are capable of making\x01",
            "a replica of an entire city. I suppose summoning\x01",
            "mirrors and tanks are child's play to them.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)
    Jump("loc_CB15")

    label("loc_CA38")


    ChrTalk(    #316
        0x13,
        (
            "#178FHaving listened to the archbishop's sermons often,\x01",
            "I am fairly familiar with the Testaments...\x02\x03",

            "#175FI never thought I would one day find myself face to\x01",
            "face with some of the monstrosities within them,\x01",
            "however.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CB15")

    TalkEnd(0xFE)

    label("loc_CB18")

    Return()

    # Function_11_AF11 end

    def Function_12_CB19(): pass

    label("Function_12_CB19")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x565, 3)), scpexpr(EXPR_END)), "loc_CDC0")
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CC5D")

    ChrTalk(    #317
        0x14,
        (
            "#270FIt seems like we're finally able to see the light at\x01",
            "the end of the tunnel.\x02\x03",

            "#270FNow we just need to keep walking towards it.\x01",
            "For the sake of everyone we know, including\x01",
            "those no longer with us because of the Aureole.\x02\x03",

            "#278FLet's see what this seventh plane has in store\x01",
            "for us, shall we?\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)
    Jump("loc_CDBA")

    label("loc_CC5D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_CD38")
    TurnDirection(0xFE, 0x104, 0)

    ChrTalk(    #318
        0x14,
        (
            "#277FIt seems like we're finally able to see the light\x01",
            "at the end of the tunnel.\x02\x03",

            "#276FBe careful, Olivier.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #319
        0x104,
        "#1541FHeh. But of course, my love!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #320
        0x14,
        "#274FAnd who, exactly, is your love?\x02",
    )

    CloseMessageWindow()
    Jump("loc_CDBA")

    label("loc_CD38")


    ChrTalk(    #321
        0x14,
        (
            "#277FIt seems like we're finally able to see the light\x01",
            "at the end of the tunnel.\x02\x03",

            "#278FPerhaps I'd best go and grab Olivier.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CDBA")

    TalkEnd(0xFE)
    Jump("loc_E960")

    label("loc_CDC0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x564, 0)), scpexpr(EXPR_END)), "loc_CF36")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C7, 2)), scpexpr(EXPR_END)), "loc_CE79")
    SetChrFlags(0xFE, 0x10)
    TalkBegin(0xFE)

    ChrTalk(    #322
        0x14,
        (
            "#276FSo that is how a true master fights...\x02\x03",

            "#278FHeh. That was a worthwhile reminder of just how\x01",
            "much room I still have to improve my own skills.\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xFE, 0x10)
    TalkEnd(0xFE)
    Jump("loc_CF33")

    label("loc_CE79")

    TalkBegin(0xFE)

    ChrTalk(    #323
        0x14,
        (
            "#272FSo you were able to test your skills against the\x01",
            "famed Cassius Bright, were you?\x02\x03",

            "#277FI can't help but wish that I had been able to see\x01",
            "him fight up close and personal.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)

    label("loc_CF33")

    Jump("loc_E960")

    label("loc_CF36")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x562, 5)), scpexpr(EXPR_END)), "loc_D105")
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D044")

    ChrTalk(    #324
        0x14,
        (
            "#276FThe Lord of Phantasma appears to have some\x01",
            "rather capable warriors under his command.\x02\x03",

            "#272FIf that's the strength of the second guardian,\x01",
            "I dread to think how powerful the rest will be.\x02\x03",

            "*sigh* This is going to be quite the challenge.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)
    Jump("loc_D0FF")

    label("loc_D044")


    ChrTalk(    #325
        0x14,
        (
            "#270FThe Lord of Phantasma really seems to have\x01",
            "some capable warriors under his command.\x02\x03",

            "#276FCome to think of it, that Schwarzritter said\x01",
            "that he's one of the guardians, too, yes?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D0FF")

    TalkEnd(0xFE)
    Jump("loc_E960")

    label("loc_D105")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x561, 0)), scpexpr(EXPR_END)), "loc_D485")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D328")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D274")
    TalkBegin(0xFE)
    TurnDirection(0xFE, 0x104, 0)

    ChrTalk(    #326
        0x14,
        (
            "#272F...Olivier, don't go causing any trouble while\x01",
            "you're here.\x02\x03",

            "Just because we're not in the real world\x01",
            "right now doesn't mean your actions can't\x01",
            "cause international problems.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #327
        0x104,
        (
            "#1541FHahaha! Why must you always be so paranoid\x01",
            "about me?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #328
        0x14,
        (
            "#274FBecause you never take me seriously.\x01",
            "Like you're not doing now.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Jump("loc_D322")

    label("loc_D274")

    SetChrFlags(0xFE, 0x10)
    TalkBegin(0xFE)

    ChrTalk(    #329
        0x14,
        (
            "#274F...You really are a few gears short of a\x01",
            "functioning battle orbment.\x02\x03",

            "Perhaps you need to be taught a lesson\x01",
            "so you don't get any more silly ideas.\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xFE, 0x10)
    TalkEnd(0xFE)

    label("loc_D322")

    OP_A2(0x3)
    Jump("loc_D482")

    label("loc_D328")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D3FB")
    TurnDirection(0xFE, 0x104, 0)

    ChrTalk(    #330
        0x14,
        (
            "#272F...Olivier, don't go causing any trouble while\x01",
            "you're here.\x02\x03",

            "Just because we're not in the real world\x01",
            "right now doesn't mean your actions can't\x01",
            "cause international problems.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D47F")

    label("loc_D3FB")


    ChrTalk(    #331
        0x14,
        (
            "#272FJust leave this idiot to me.\x02\x03",

            "#270FI'll take responsibility for making sure he\x01",
            "behaves--no matter what it takes to do it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D47F")

    TalkEnd(0xFE)

    label("loc_D482")

    Jump("loc_E960")

    label("loc_D485")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x560, 0)), scpexpr(EXPR_END)), "loc_D70F")
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D5F2")

    ChrTalk(    #332
        0x14,
        (
            "#276FI never imagined that would be the origin of\x01",
            "the cube we've been reliant on all this time.\x02\x03",

            "At least now we understand how we came\x01",
            "to be drawn in here...to a degree.\x02\x03",

            "#270FIt seems like the one directly responsible for\x01",
            "that happening was the Lord of Phantasma,\x01",
            "too.\x02\x03",

            "#272FHmph. I can't wait to make them pay for what\x01",
            "they've done.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)
    Jump("loc_D709")

    label("loc_D5F2")


    ChrTalk(    #333
        0x14,
        (
            "#272FAt least now that we know where the Recluse Cube\x01",
            "came from, we've got a relatively good idea how we\x01",
            "all ended up here.\x02\x03",

            "#276FThe one directly responsible for that happening was\x01",
            "no doubt the Lord of Phantasma.\x02\x03",

            "Hmph. I can't wait to make them pay for what\x01",
            "they've done.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D709")

    TalkEnd(0xFE)
    Jump("loc_E960")

    label("loc_D70F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x540, 7)), scpexpr(EXPR_END)), "loc_D8D6")
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D83D")

    ChrTalk(    #334
        0x14,
        (
            "#272FIt seems like the situation we're in is even more\x01",
            "severe than I feared.\x02\x03",

            "#276FWe've discovered a number of rules that govern\x01",
            "this world, all implemented by that Lord of\x01",
            "Phantasma...\x02\x03",

            "...but what if they created a rule that dictates\x01",
            "we can't actually leave this world?\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)
    Jump("loc_D8D0")

    label("loc_D83D")


    ChrTalk(    #335
        0x14,
        (
            "#272FOur only hope may turn out to be that ghost.\x02\x03",

            "#276FEspecially given how the Lord of Phantasma's\x01",
            "power seems unable to affect the garden.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D8D0")

    TalkEnd(0xFE)
    Jump("loc_E960")

    label("loc_D8D6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x540, 4)), scpexpr(EXPR_END)), "loc_DAA9")
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D9F0")

    ChrTalk(    #336
        0x14,
        (
            "#277FSo our latest ally is the former Royal Army\x01",
            "officer Colonel Richard, is it?\x02\x03",

            "I've heard many great things about his skill in\x01",
            "battle and espionage, as well as his intellect.\x02\x03",

            "#278FHeh. He doesn't sound like the kind of man\x01",
            "I would want as an enemy.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)
    Jump("loc_DAA3")

    label("loc_D9F0")


    ChrTalk(    #337
        0x14,
        (
            "#277FSo our latest ally is the former Royal Army\x01",
            "officer Colonel Richard, is it?\x02\x03",

            "He's not someone I would want as an enemy,\x01",
            "but I'll welcome him any day as a powerful ally.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_DAA3")

    TalkEnd(0xFE)
    Jump("loc_E960")

    label("loc_DAA9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x540, 0)), scpexpr(EXPR_END)), "loc_DD62")
    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_DB40")
    Jump("loc_DB82")

    label("loc_DB40")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_DB5C")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_DB82")

    label("loc_DB5C")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_DB78")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_DB82")

    label("loc_DB78")

    OP_51(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_DB82")

    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DCE3")

    ChrTalk(    #338
        0x14,
        (
            "#272FThere was a point when Olivier tried delving\x01",
            "into research on the Gralsritter.\x02\x03",

            "He wasn't able to ascertain much in the end\x01",
            "no matter how hard he tried, though...\x02\x03",

            "#276FAfter seeing for myself what their strongest\x01",
            "members are capable of, I can understand why\x01",
            "he would want to look into them.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)
    Jump("loc_DD57")

    label("loc_DCE3")


    ChrTalk(    #339
        0x14,
        (
            "#276FThe ability to slay a devil of that strength in\x01",
            "one blow is...unusual, to say the least.\x02\x03",

            "Unnatural, too.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_DD57")

    SetChrSubChip(0xFE, 0)
    TalkEnd(0xFE)
    Jump("loc_E960")

    label("loc_DD62")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x521, 6)), scpexpr(EXPR_END)), "loc_E0B2")
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DF30")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DE60")

    ChrTalk(    #340
        0x14,
        (
            "#276FWhere has that fool gotten himself to, anyway?\x02\x03",

            "#272FI swear, I take my eyes off him for one moment...\x02\x03",

            "You'd think he could at least manage to play the\x01",
            "good prince during times of serious crisis like this...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DF2A")

    label("loc_DE60")


    ChrTalk(    #341
        0x14,
        (
            "#276FSo all of the sealing stones in that bracer training\x01",
            "area contained bracers in the end.\x02\x03",

            "That masked jester has thankfully proven to play\x01",
            "by their own rules thus far, at least.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #342
        0x102,
        "#1503F...\x02",
    )

    CloseMessageWindow()

    label("loc_DF2A")

    OP_A2(0x3)
    Jump("loc_E0AC")

    label("loc_DF30")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DFD6")

    ChrTalk(    #343
        0x14,
        (
            "#272FHmph. Well, whatever. I'll leave him to his own\x01",
            "devices for now.\x02\x03",

            "It's not as though he can leave this garden\x01",
            "without the cube regardless.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E0AC")

    label("loc_DFD6")


    ChrTalk(    #344
        0x14,
        (
            "#270FI may loathe that masked jester, but at least\x01",
            "they seem to always play by their own rules, \x01",
            "if nothing else.\x02\x03",

            "#276FI just hope there's some way that we can take\x01",
            "advantage of that in order to defeat them.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E0AC")

    TalkEnd(0xFE)
    Jump("loc_E960")

    label("loc_E0B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x521, 2)), scpexpr(EXPR_END)), "loc_E36E")
    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_E149")
    Jump("loc_E18B")

    label("loc_E149")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_E165")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_E18B")

    label("loc_E165")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_E181")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_E18B")

    label("loc_E181")

    OP_51(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_E18B")

    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E2AF")

    ChrTalk(    #345
        0x14,
        (
            "#276FI take it those armed beastmen we encountered\x01",
            "are another reflection of the Lord of Phantasma's \x01",
            "unpleasant tastes.\x02\x03",

            "#272F...But whatever. I'm tired of putting up with their\x01",
            "ridiculous games at this point.\x02\x03",

            "Let's keep pressing on.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)
    Jump("loc_E363")

    label("loc_E2AF")


    ChrTalk(    #346
        0x14,
        (
            "#272FI've got no idea what the Lord of Phantasma\x01",
            "is planning...\x02\x03",

            "...but I'm tired of having to put up with their\x01",
            "ridiculous games at this point.\x02\x03",

            "#270FLet's keep pressing on.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E363")

    SetChrSubChip(0xFE, 0)
    TalkEnd(0xFE)
    Jump("loc_E960")

    label("loc_E36E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x520, 5)), scpexpr(EXPR_END)), "loc_E6EE")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E643")
    SetChrFlags(0xFE, 0x10)
    TalkBegin(0xFE)
    OP_51(0x104, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x104, 0)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_E41B")
    Jump("loc_E45D")

    label("loc_E41B")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_E437")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_E45D")

    label("loc_E437")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_E453")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_E45D")

    label("loc_E453")

    OP_51(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_E45D")

    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x104, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x104, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E5FD")

    ChrTalk(    #347
        0x14,
        "#272F...Olivier. I need to talk to you later.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #348
        0x104,
        (
            "#1540FOh, my! My, my, my! Whatever for?\x02\x03",

            "#1541FHave you finally decided you cannot contain\x01",
            "your burning passion for me locked within\x01",
            "that rugged heart of yours a moment longer?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #349
        0x14,
        (
            "#270FNo, idiot. I just need to check up on how you're\x01",
            "doing.\x02\x03",

            "#276FAs well as how you were doing before we were\x01",
            "drawn in here.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)
    Jump("loc_E633")

    label("loc_E5FD")


    ChrTalk(    #350
        0x14,
        "#272FDon't go getting too carried away, Olivier.\x02",
    )

    CloseMessageWindow()

    label("loc_E633")

    SetChrSubChip(0xFE, 0)
    ClearChrFlags(0xFE, 0x10)
    TalkEnd(0xFE)
    Jump("loc_E6EB")

    label("loc_E643")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E652")
    Call(5, 5)
    Jump("loc_E6EB")

    label("loc_E652")

    SetChrFlags(0xFE, 0x10)
    TalkBegin(0xFE)

    ChrTalk(    #351
        0x14,
        (
            "#276FWe must find a way out of here as soon as\x01",
            "possible.\x02\x03",

            "#272FWho knows what's happening in the outside\x01",
            "world while we're in here?\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xFE, 0x10)
    TalkEnd(0xFE)

    label("loc_E6EB")

    Jump("loc_E960")

    label("loc_E6EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x520, 0)), scpexpr(EXPR_END)), "loc_E960")
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E8D4")

    ChrTalk(    #352
        0x14,
        (
            "#270FIt's seeming more and more like we were all\x01",
            "drawn in here at the same time.\x02\x03",

            "#272F...Which is a relief in some ways. If that pitiful THING\x01",
            "had been left in the outside world without me to watch\x01",
            "it, I shudder to think what would have happened.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #353
        0x102,
        "#1505FI'd come to his defense but...no, I can't blame you.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E8CE")

    ChrTalk(    #354
        0x104,
        (
            "#1542FTruly, I am offended.\x02\x03",

            "#1541FAt the very worst, I would have thrown\x01",
            "a luxurious banquet for all to enjoy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #355
        0x14,
        "#274F...\x02",
    )

    CloseMessageWindow()

    label("loc_E8CE")

    OP_A2(0x3)
    Jump("loc_E95D")

    label("loc_E8D4")


    ChrTalk(    #356
        0x14,
        (
            "#272FIt's seeming more and more like we were all\x01",
            "drawn in here at the same time.\x02\x03",

            "Which is a relief, as guilty as I feel to say so.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E95D")

    TalkEnd(0xFE)

    label("loc_E960")

    Return()

    # Function_12_CB19 end

    SaveToFile()

Try(main)

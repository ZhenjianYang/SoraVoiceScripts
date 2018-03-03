from ED63RDScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'U7003_4 ._SN',
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
        "Function_3_1B7F",         # 03, 3
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

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x584, 0)), scpexpr(EXPR_END)), "loc_657")
    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x1A, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x1A, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x1A, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0x1A)
    ClearChrFlags(0x1A, 0x10)
    TurnDirection(0x1A, 0x0, 0)
    OP_51(0x1A, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x1A, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x1A, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x1A, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x1A, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x1A, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x1A, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x1A, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x1A, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x1A, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x1A, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_143")
    Jump("loc_185")

    label("loc_143")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x1A, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_15F")
    OP_51(0x1A, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_185")

    label("loc_15F")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x1A, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_17B")
    OP_51(0x1A, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_185")

    label("loc_17B")

    OP_51(0x1A, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x1A, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_185")

    OP_51(0x1A, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x1A, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x1A, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_339")

    ChrTalk(    #0
        0x1A,
        (
            "#074FAfter we leave this garden, we'll never be able\x01",
            "to return again.\x02\x03",

            "#072FIt's probably best to assume there won't be\x01",
            "anywhere for us to buy new equipment, either.\x02\x03",

            "#070FSo make sure you've got everything you think\x01",
            "you'll need, okay?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x584, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_333")

    ChrTalk(    #1
        0x1A,
        (
            "#073FOh, yeah...\x02\x03",

            "#070FIt sounds like Celeste has found a new area\x01",
            "that we can access, too.\x02\x03",

            "I'd ask her about that if I were you.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_333")

    OP_A2(0xD)
    Jump("loc_64C")

    label("loc_339")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x584, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_514")

    ChrTalk(    #2
        0x1A,
        (
            "#074FIt's only thanks to the power of this garden\x01",
            "that we're able to buy new equipment and goods,\x01",
            "or synthesize new quartz for our orbments.\x02\x03",

            "#070FAfter we leave here, there's no guarantee we'll be\x01",
            "able to do any of those things.\x02\x03",

            "Make sure you've got everything you think you'll\x01",
            "need before leaving, okay?\x02\x03",

            "#573FOh, yeah... It sounds like Celeste has found a new\x01",
            "area that we can access, too.\x02\x03",

            "#070FI'd ask her about that if I were you. Might come in\x01",
            "handy.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_64C")

    label("loc_514")


    ChrTalk(    #3
        0x1A,
        (
            "#074FIt's only thanks to the power of this garden\x01",
            "that we're able to buy new equipment and goods,\x01",
            "or synthesize new quartz for our orbments.\x02\x03",

            "#070FAfter we leave here, there's no guarantee we'll be\x01",
            "able to do any of those things.\x02\x03",

            "Make sure you've got everything you think you'll\x01",
            "need before leaving, okay?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_64C")

    SetChrSubChip(0x1A, 0)
    TalkEnd(0x1A)
    Jump("loc_1B7E")

    label("loc_657")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x565, 3)), scpexpr(EXPR_END)), "loc_8BF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_79B")
    SetChrFlags(0xFE, 0x10)
    TalkBegin(0xFE)

    ChrTalk(    #4
        0x1A,
        (
            "#074F...\x02\x03",

            "*sigh* No matter how much I think on it, I can't\x01",
            "find an answer.\x02\x03",

            "#072FIf the Lord of Phantasma is the reason all of this\x01",
            "is happening...what are they trying to achieve?\x02\x03",

            "#074FThey have control of a world that can grant\x01",
            "humanity's every wish... What else could they\x01",
            "want from it?\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xD)
    Jump("loc_8B4")

    label("loc_79B")

    TalkBegin(0xFE)

    ChrTalk(    #5
        0x1A,
        (
            "#075F*sigh* Heavy thinking like this isn't my strong\x01",
            "point, I've gotta admit.\x02\x03",

            "#070FI wish Kilika was here to take on this job.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_84E")

    ChrTalk(    #6
        0x101,
        "#1001FAhaha... Yeah.\x02",
    )

    CloseMessageWindow()
    Jump("loc_8B4")

    label("loc_84E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_888")

    ChrTalk(    #7
        0x102,
        "#1501FShe'd certainly be helpful...\x02",
    )

    CloseMessageWindow()
    Jump("loc_8B4")

    label("loc_888")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8B4")

    ChrTalk(    #8
        0x103,
        "#1536FHaha. True enough.\x02",
    )

    CloseMessageWindow()

    label("loc_8B4")

    ClearChrFlags(0xFE, 0x10)
    TalkEnd(0xFE)
    Jump("loc_1B7E")

    label("loc_8BF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x564, 0)), scpexpr(EXPR_END)), "loc_F13")
    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_956")
    Jump("loc_998")

    label("loc_956")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_972")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_998")

    label("loc_972")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_98E")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_998")

    label("loc_98E")

    OP_51(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_998")

    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D18")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x565, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B6B")

    ChrTalk(    #9
        0x1A,
        (
            "#074FMaster Cassius' ability in combat is basically\x01",
            "unparalleled...\x02\x03",

            "#072FIt isn't his strength that makes him so incredible,\x01",
            "though. It's his ability to see the true nature of\x01",
            "things.\x02\x03",

            "That's why he's able to function equally well in\x01",
            "both the army and as part of the Bracer Guild.\x02\x03",

            "#573FHe is a master in every sense of the word.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B41")

    ChrTalk(    #10
        0x102,
        "#1513FYeah...\x02",
    )

    CloseMessageWindow()
    Jump("loc_B68")

    label("loc_B41")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B68")

    ChrTalk(    #11
        0x10D,
        "#278FSo it seems...\x02",
    )

    CloseMessageWindow()

    label("loc_B68")

    Jump("loc_D12")

    label("loc_B6B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C8, 7)), scpexpr(EXPR_END)), "loc_CA2")

    ChrTalk(    #12
        0x1A,
        (
            "#074FI wonder what Walter's even doing out in the\x01",
            "real world these days?\x02\x03",

            "#070FHe should be in a position where he can hear\x01",
            "what's going on in Kilika's life, at least...\x02\x03",

            "#573F*sigh* If he's got something he wants to tell her,\x01",
            "he should just go and tell her himself instead of\x01",
            "asking me, though.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D12")

    label("loc_CA2")


    ChrTalk(    #13
        0x1A,
        (
            "#572FSo you ran into Walter, huh?\x02\x03",

            "#075F*sigh* I wonder what he's even doing in the\x01",
            "real world these days.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D12")

    OP_A2(0xD)
    Jump("loc_F08")

    label("loc_D18")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x565, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DCB")

    ChrTalk(    #14
        0x1A,
        (
            "#074FHow long will it take me to be able to reach\x01",
            "his level...?\x02\x03",

            "#070F*sigh* Well, I know one thing: I'm gonna need\x01",
            "to put a whole lot of work into getting there.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F08")

    label("loc_DCB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E51")

    ChrTalk(    #15
        0x1A,
        (
            "#074FAnyway, next up is the fourth and final guardian.\x02\x03",

            "#070FGood luck out there, Joshua.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x102,
        "#1500FThank you!\x02",
    )

    CloseMessageWindow()
    Jump("loc_F08")

    label("loc_E51")


    ChrTalk(    #17
        0x1A,
        (
            "#070FAnyway, next up is the fourth and final guardian.\x02\x03",

            "#573FHeh. It's probably not even worth saying anything\x01",
            "at this point. We've just got to keep doing what\x01",
            "we've been doing.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F08")

    SetChrSubChip(0xFE, 0)
    TalkEnd(0xFE)
    Jump("loc_1B7E")

    label("loc_F13")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x562, 5)), scpexpr(EXPR_END)), "loc_12E4")
    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_FAA")
    Jump("loc_FEC")

    label("loc_FAA")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_FC6")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_FEC")

    label("loc_FC6")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_FE2")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_FEC")

    label("loc_FE2")

    OP_51(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_FEC")

    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_11B4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C8, 1)), scpexpr(EXPR_END)), "loc_10AE")

    ChrTalk(    #18
        0x1A,
        (
            "#075F*sigh* Oh, boy...\x02\x03",

            "I have a horrible feeling I'm gonna get a real\x01",
            "earful from Kilika when I get out of here. I hope\x01",
            "I'm wrong...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_11AE")

    label("loc_10AE")


    ChrTalk(    #19
        0x1A,
        (
            "#573FSo you fought Kilika, huh?\x02\x03",

            "#070FHaha. She's a nasty fight, isn't she?\x02\x03",

            "If you let her fight with her chakram, she's even\x01",
            "stronger than Walter.\x02\x03",

            "#075FIf she doesn't inherit the Taito style, she's gonna\x01",
            "have trouble finding a husband for herself.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_11AE")

    OP_A2(0xD)
    Jump("loc_12D9")

    label("loc_11B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C8, 1)), scpexpr(EXPR_END)), "loc_123C")

    ChrTalk(    #20
        0x1A,
        (
            "#074FKilika's not a great loser... Take it from me.\x02\x03",

            "#075FI see a whole lot of yelling in my future next\x01",
            "time I see her.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_12D9")

    label("loc_123C")


    ChrTalk(    #21
        0x1A,
        (
            "#070FThat said, she's been working as a guild\x01",
            "receptionist for ages now...\x02\x03",

            "It's possible she's gotten a bit rusty.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x109,
        "#1068F...She hasn't. Trust me.\x02",
    )

    CloseMessageWindow()

    label("loc_12D9")

    SetChrSubChip(0xFE, 0)
    TalkEnd(0xFE)
    Jump("loc_1B7E")

    label("loc_12E4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x520, 5)), scpexpr(EXPR_END)), "loc_1513")
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1418")

    ChrTalk(    #23
        0x1A,
        (
            "#074FThe guild has facilities in both Calvard and Erebonia,\x01",
            "and yet it's Le Locle that's been recreated here.\x02\x03",

            "There's got to be some kind of meaning to that\x01",
            "choice.\x02\x03",

            "#072FCould the Lord of Phantasma be intentionally\x01",
            "recreating places that're connected to our group\x01",
            "in some way?\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xD)
    Jump("loc_150D")

    label("loc_1418")


    ChrTalk(    #24
        0x1A,
        (
            "#572FLeman State is far from Liberl, which makes me\x01",
            "curious why it's Le Locle that was recreated here\x01",
            "and not anywhere else...\x02\x03",

            "#074FCould the Lord of Phantasma be intentionally\x01",
            "recreating places that're connected to our group\x01",
            "in some way?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_150D")

    TalkEnd(0xFE)
    Jump("loc_1B7E")

    label("loc_1513")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x520, 0)), scpexpr(EXPR_END)), "loc_1B7E")
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4CC, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1932")
    TurnDirection(0xFE, 0x102, 0)

    ChrTalk(    #25
        0x1A,
        (
            "#070FIt sure has been a long time since we last met, huh,\x01",
            "Joshua?\x02\x03",

            "You've been to Erebonia and Crossbell now, right?\x01",
            "Why not make your way over to Calvard?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x102,
        (
            "#1513FOh, it's something I'd like to do eventually.\x02\x03",

            "#1503FEstelle and I are currently looking for someone,\x01",
            "though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x1A,
        "#074FHmm... Fair enough.\x02",
    )

    CloseMessageWindow()
    OP_62(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(    #28
        0x102,
        (
            "#1504FIncidentally, I heard from Schera in one of her\x01",
            "letters that Kilika returned to the Republic?\x02\x03",

            "#1500FShe mentioned something about her retiring from\x01",
            "the guild after being scouted by the Calvardian\x01",
            "government.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x109,
        (
            "#1079FWhat? That lady who used to look after the\x01",
            "Zeiss branch?\x02\x03",

            "#1078FFor real? Never would've seen that coming.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x1A,
        (
            "#070FYeah, it's all true. I hear she's up to her eyes in\x01",
            "work these days.\x02\x03",

            "#075FAnd you know how she is--taking it easy isn't an\x01",
            "option for her. She gives her all to everything she\x01",
            "does.\x02\x03",

            "She's doing a hell of a job, though. Her coworkers\x01",
            "and subordinates're all terrified of her already.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x102,
        "#1509FHaha... I wouldn't have Kilika any other way.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2661)
    Jump("loc_1B7B")

    label("loc_1932")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A87")

    ChrTalk(    #32
        0x1A,
        (
            "#074FStill, who could've pictured anything like this\x01",
            "happening? Or that I'd find myself smack dab\x01",
            "in the middle of it!\x02\x03",

            "#070FOn the plus side, at least you guys have\x01",
            "been doing a fine job with your investigating,\x01",
            "so we've got some idea what we're doing.\x02\x03",

            "We'll just have to keep using that as a guide\x01",
            "to try and press on.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xD)
    Jump("loc_1B7B")

    label("loc_1A87")


    ChrTalk(    #33
        0x1A,
        (
            "#070FAt least you guys have been doing a fine job with\x01",
            "your investigating, so we've got some kind of idea\x01",
            "what we need to do to get ourselves out of here.\x02\x03",

            "All we can do is keep believing we're going about\x01",
            "this the right way and press on.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B7B")

    TalkEnd(0xFE)

    label("loc_1B7E")

    Return()

    # Function_2_AC end

    def Function_3_1B7F(): pass

    label("Function_3_1B7F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x565, 3)), scpexpr(EXPR_END)), "loc_1D1D")
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C68")

    ChrTalk(    #34
        0x1F,
        (
            "#119FHaha. I can't sit around idly, now.\x02\x03",

            "#110FNot when I work to be doing.\x02\x03",

            "The time to take on the Lord of Phantasma\x01",
            "and bring all of this to an end seems to be\x01",
            "almost upon us, too. We're almost there.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xA)
    Jump("loc_1D17")

    label("loc_1C68")


    ChrTalk(    #35
        0x1F,
        (
            "#110FNow that we've defeated the Schwarzritter,\x01",
            "we should have taken all of the enemy's pieces.\x02\x03",

            "#115FAll that remains is to settle the score with the\x01",
            "Lord of Phantasma.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D17")

    TalkEnd(0xFE)
    Jump("loc_34EF")

    label("loc_1D1D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x564, 0)), scpexpr(EXPR_END)), "loc_1F6E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1DF7")
    SetChrFlags(0xFE, 0x10)
    TalkBegin(0xFE)

    ChrTalk(    #36
        0x1F,
        "#115F...Oh, hello.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x0, 400)
    Sleep(300)

    ChrTalk(    #37
        0x1F,
        (
            "#110FI truly cannot thank you all enough.\x02\x03",

            "I feel as though I can finally start to\x01",
            "move forward again.\x02\x03",

            "#111FSo let's keep going. Together.\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xFE, 0x10)
    OP_A2(0xA)
    TalkEnd(0xFE)
    Jump("loc_1F6B")

    label("loc_1DF7")

    TalkBegin(0xFE)

    ChrTalk(    #38
        0x1F,
        (
            "#115FEver since the coup d'etat, I have found myself\x01",
            "hesitating to commit to anything and everything.\x02\x03",

            "#116FI think I spent so long admiring the brigadier \x01",
            "general that when the time came to begin a new\x01",
            "path away from him, I...wasn't sure what to do.\x02\x03",

            "#110FWith all that's transpired here, however, I feel\x01",
            "like I can finally dedicate myself to doing just\x01",
            "that.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)

    label("loc_1F6B")

    Jump("loc_34EF")

    label("loc_1F6E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x561, 0)), scpexpr(EXPR_END)), "loc_225C")
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_218D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C8, 0)), scpexpr(EXPR_END)), "loc_2057")

    ChrTalk(    #39
        0x1F,
        (
            "#115FI'm astounded at just how skilled Phillip still is\x01",
            "despite retiring from the front lines over two\x01",
            "decades ago.\x02\x03",

            "#111FHaha. That was the most exciting fight I have\x01",
            "experienced in quite some time.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2187")

    label("loc_2057")


    ChrTalk(    #40
        0x1F,
        (
            "#110FWe looked into Philip's history back during the\x01",
            "time the Intelligence Division was active, too.\x02\x03",

            "He has an interesting background--being known\x01",
            "as the Sword Fox and possessing five exceptional\x01",
            "techniques in combat.\x02\x03",

            "#119FThat said, he's been away from the front lines\x01",
            "for over twenty years now.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2187")

    OP_A2(0xA)
    Jump("loc_2256")

    label("loc_218D")


    ChrTalk(    #41
        0x1F,
        (
            "#115FPhilip retired from the Royal Guard over twenty\x01",
            "years ago in order to focus his efforts on Duke\x01",
            "Dunan's upbringing.\x02\x03",

            "His skills don't seem to have grown at all rusty\x01",
            "in that time, however...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2256")

    TalkEnd(0xFE)
    Jump("loc_34EF")

    label("loc_225C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x560, 0)), scpexpr(EXPR_END)), "loc_2409")
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_235B")

    ChrTalk(    #42
        0x1F,
        (
            "#115FSo, Father...\x02\x03",

            "How are you feeling now?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0x109,
        (
            "#1060FFine, thanks.\x02\x03",

            "#1840FSorry about worrying you guys so much.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0x1F,
        (
            "#111FOh, don't be.\x02\x03",

            "#110FI wasn't there to see you collapse, so I was\x01",
            "simply curious how you were doing.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xA)
    Jump("loc_2403")

    label("loc_235B")


    ChrTalk(    #45
        0x1F,
        (
            "#115FIf not even Celeste knows how the Lord of\x01",
            "Phantasma managed to get in here...\x02\x03",

            "...I'm not sure any amount of speculating is\x01",
            "going to let us reach the answer.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2403")

    TalkEnd(0xFE)
    Jump("loc_34EF")

    label("loc_2409")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x540, 7)), scpexpr(EXPR_END)), "loc_2B59")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4CD, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2A95")
    SetChrFlags(0xFE, 0x10)
    TalkBegin(0xFE)

    ChrTalk(    #46
        0x1F,
        (
            "#115F(I can't deny that there's still a part of me\x01",
            "that refuses to move on from the past.)\x02\x03",

            "#116F(Sooner or later, I'll have to completely put\x01",
            "it behind me and move on...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x101,
        "#1015FUmm... Is something up, Colonel?\x02",
    )

    CloseMessageWindow()
    OP_62(0xFE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    TurnDirection(0xFE, 0x101, 400)
    Sleep(300)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_293B")

    ChrTalk(    #48
        0x1F,
        "#110FNothing major, no. I was just lost in thought.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0x110,
        "#260FAre you still thinking about what I said earlier?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0x1F,
        (
            "#111FHaha. You really are a perceptive one.\x02\x03",

            "#110F...You wouldn't be interested in coming to\x01",
            "work at R&A Research, would you?\x02\x03",

            "I'm sure someone with your level of foresight\x01",
            "would be a valuable asset to us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0x110,
        (
            "#267FHmm...\x02\x03",

            "#260FMaybe I'll give it some thought if you play with\x01",
            "me again? Maaaybe.\x02\x03",

            "#261FOur playtime at Grancel Castle ended up getting\x01",
            "interrupted before it'd really started...so I'm up\x01",
            "for another try if you are!\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_279D")
    OP_62(0x107, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(    #52
        0x107,
        "#562FR-Renne, please...\x02",
    )

    CloseMessageWindow()

    label("loc_279D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2837")

    ChrTalk(    #53
        0x105,
        (
            "#1165F(I-I'd forgotten that the two of them ended\x01",
            "up fighting when Ouroboros tried attacking\x01",
            "the capital...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0x101,
        "#1016F(Y-Yeah...)\x02",
    )

    CloseMessageWindow()
    Jump("loc_290C")

    label("loc_2837")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_28A7")

    ChrTalk(    #55
        0x102,
        (
            "#1514F(I nearly forgot they ended up fighting when\x01",
            "the Enforcers attacked the capital...)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_290C")

    label("loc_28A7")


    ChrTalk(    #56
        0x101,
        (
            "#1016F(I-I totally forgot they ended up fighting when\x01",
            "Ouroboros tried attacking the capital...)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_290C")


    ChrTalk(    #57
        0x1F,
        "#111FHa...haha... I'll think about it.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2A87")

    label("loc_293B")


    ChrTalk(    #58
        0x1F,
        (
            "#111FNothing major, no. I was just lost in thought.\x02\x03",

            "#110FIn any case, I'd heard rumors about how intelligent\x01",
            "young Renne was...\x02\x03",

            "Having spoken with her personally, however, they\x01",
            "may have been underselling her.\x02\x03",

            "#115F*sigh* I almost wish I could hire her to work at \x01",
            "R&A Research. She'd be quite the asset.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0x101,
        "#1016FAhaha...\x02",
    )

    CloseMessageWindow()

    label("loc_2A87")

    ClearChrFlags(0xFE, 0x10)
    OP_A2(0x266B)
    TalkEnd(0xFE)
    Jump("loc_2B56")

    label("loc_2A95")

    SetChrFlags(0xFE, 0x10)
    TalkBegin(0xFE)

    ChrTalk(    #60
        0x1F,
        (
            "#115F(I can't deny that there's still a part of me\x01",
            "that refuses to move on from the past.)\x02\x03",

            "#116F(Sooner or later, I'll have to completely put\x01",
            "it behind me and move on...)\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xFE, 0x10)
    TalkEnd(0xFE)

    label("loc_2B56")

    Jump("loc_34EF")

    label("loc_2B59")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4CD, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3284")
    SetChrFlags(0xFE, 0x10)
    TalkBegin(0xFE)

    ChrTalk(    #61
        0x1F,
        (
            "#115F*sigh* This place is full of peculiar things.\x02\x03",

            "It appears to be a dimensional space of its\x01",
            "own...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0x101,
        (
            "#1011FYou still finding all of this hard\x01",
            "to take in?\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #63
        0x1F,
        (
            "#110FOh, it's you, Estelle.\x02\x03",

            "#119FYou could put it that way, yes.\x02\x03",

            "I fear it's going to take me a while longer\x01",
            "to come up with an effective enough plan\x01",
            "to conquer this place.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0x101,
        (
            "#1016FC-Conquer...?\x02\x03",

            "There was me thinking you might still be trying\x01",
            "to process the situation you're in, but you're\x01",
            "already one step ahead. That's our colonel!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0x1F,
        (
            "#495FAs I believe I have told you several times already,\x01",
            "I'm not a colonel anymore...\x02\x03",

            "I'm not even part of the army anymore.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0x101,
        (
            "#1015FOh. Oops.\x02\x03",

            "You're running a research company for\x01",
            "civilians these days, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0x1F,
        (
            "#111FIndeed. We're still a relatively insignificant\x01",
            "startup, though.\x02\x03",

            "#110FWe operate out of a small office in Ruan.\x02\x03",

            "The only employees at present are myself\x01",
            "and Kanone. \x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0x101,
        (
            "#1004FWhat?! Captain Amalthea's working with you,\x01",
            "too?\x02\x03",

            "#1007FSomehow I can't imagine her sitting behind a \x01",
            "desk doing normal people work...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0x1F,
        (
            "#111FHahaha... I suppose that's hardly surprising.\x02\x03",

            "#119FStill, she's also changed since the coup.\x02\x03",

            "We've been living a rather relaxed life since\x01",
            "our new business began.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0x101,
        (
            "#1008FReally?\x02\x03",

            "#1012FI can believe it, though. You've got this whole\x01",
            "different aura about you now.\x02\x03",

            "#1001FMaybe this was actually the right career choice \x01",
            "for you after all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0x1F,
        "#111FHaha. I certainly hope so.\x02",
    )

    CloseMessageWindow()
    Sleep(300)

    ChrTalk(    #72
        0x1F,
        (
            "#110F...Regardless, returning to work is just another\x01",
            "reason I can't afford to remain here any longer\x01",
            "than necessary.\x02\x03",

            "We need to strive to return to our world as soon\x01",
            "as possible.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0x101,
        (
            "#1006F...Yeah. Agreed.\x02\x03",

            "#1018FWe'll be counting on you, Colonel!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0x1F,
        (
            "#495F(Did that entire conversation fly right over her\x01",
            "head...?)\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xFE, 0x10)
    OP_A2(0x266A)
    TalkEnd(0xFE)
    Jump("loc_34EF")

    label("loc_3284")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_33DE")
    OP_A2(0xA)

    ChrTalk(    #75
        0x1F,
        (
            "#115FThis world we are in clearly operates by its own\x01",
            "set of rules...\x02\x03",

            "And as such, it seems reasonable to conclude\x01",
            "that they exist because it was created for a\x01",
            "specific purpose.\x02\x03",

            "#110FIf I can work out what that purpose is, I may be\x01",
            "able to think of an effective way of conquering\x01",
            "it...but therein lies the real challenge.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_34EC")

    label("loc_33DE")


    ChrTalk(    #76
        0x1F,
        (
            "#115FThis world we are in clearly operates by its own\x01",
            "set of rules, and therefore must have a specific\x01",
            "purpose for existing.\x02\x03",

            "If I can work out what that purpose is, I may be\x01",
            "able to think of an effective way of conquering\x01",
            "it...but therein lies the real challenge.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_34EC")

    TalkEnd(0xFE)

    label("loc_34EF")

    Return()

    # Function_3_1B7F end

    SaveToFile()

Try(main)

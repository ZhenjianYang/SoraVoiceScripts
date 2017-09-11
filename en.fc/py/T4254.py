from ED6ScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'T4254   ._SN',
        MapName             = 'Grancel',
        Location            = 'T4254.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60017",
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
        'Head Maid Hilda',                      # 9
        'Shea',                                 # 10
    )

    DeclEntryPoint(
        Unknown_00              = 0,
        Unknown_04              = 0,
        Unknown_08              = 6000,
        Unknown_0C              = 4,
        Unknown_0E              = 0,
        Unknown_10              = 0,
        Unknown_14              = 9500,
        Unknown_18              = -10000,
        Unknown_1C              = 0,
        Unknown_20              = 0,
        Unknown_24              = 0,
        Unknown_28              = 2800,
        Unknown_2C              = 262,
        Unknown_30              = 45,
        Unknown_32              = 0,
        Unknown_34              = 360,
        Unknown_36              = 0,
        Unknown_38              = 0,
        Unknown_3A              = 0,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )


    AddCharChip(
        'ED6_DT07/CH02460 ._CH',             # 00
        'ED6_DT07/CH02540 ._CH',             # 01
        'ED6_DT07/CH02230 ._CH',             # 02
        'ED6_DT07/CH02240 ._CH',             # 03
        'ED6_DT07/CH02463 ._CH',             # 04
        'ED6_DT07/CH00003 ._CH',             # 05
        'ED6_DT07/CH00013 ._CH',             # 06
    )

    AddCharChipPat(
        'ED6_DT07/CH02460P._CP',             # 00
        'ED6_DT07/CH02540P._CP',             # 01
        'ED6_DT07/CH02230P._CP',             # 02
        'ED6_DT07/CH02240P._CP',             # 03
        'ED6_DT07/CH02463P._CP',             # 04
        'ED6_DT07/CH00003P._CP',             # 05
        'ED6_DT07/CH00013P._CP',             # 06
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )


    ScpFunction(
        "Function_0_122",          # 00, 0
        "Function_1_2B9",          # 01, 1
        "Function_2_2D3",          # 02, 2
        "Function_3_450",          # 03, 3
        "Function_4_81C",          # 04, 4
        "Function_5_C18",          # 05, 5
        "Function_6_1387",         # 06, 6
        "Function_7_2F54",         # 07, 7
    )


    def Function_0_122(): pass

    label("Function_0_122")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_14C")
    SetChrChipByIndex(0x0, 0)
    SetChrChipByIndex(0x1, 2)
    SetChrChipByIndex(0x138, 3)
    SetChrFlags(0x0, 0x1000)
    SetChrFlags(0x1, 0x1000)
    SetChrFlags(0x138, 0x1000)

    label("loc_14C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 2)), scpexpr(EXPR_END)), "loc_15A")
    OP_A3(0x3FA)
    Event(0, 5)

    label("loc_15A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 3)), scpexpr(EXPR_END)), "loc_168")
    OP_A3(0x3FB)
    Event(0, 7)

    label("loc_168")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (100, "loc_174"),
        (SWITCH_DEFAULT, "loc_18A"),
    )


    label("loc_174")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_187")
    OP_A2(0x642)
    Event(0, 6)

    label("loc_187")

    Jump("loc_18A")

    label("loc_18A")

    OP_A2(0x639)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 7)), scpexpr(EXPR_END)), "loc_1B4")
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, 72500, 0, 68560, 90)
    OP_43(0x8, 0x0, 0x0, 0x2)
    Jump("loc_2B8")

    label("loc_1B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_1DB")
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, 64129, 0, 99150, 167)
    OP_43(0x8, 0x0, 0x0, 0x2)
    Jump("loc_2B8")

    label("loc_1DB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 6)), scpexpr(EXPR_END)), "loc_21F")
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, 72500, 0, 68560, 90)
    OP_43(0x8, 0x0, 0x0, 0x2)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, 62980, 0, 65500, 180)
    OP_43(0x9, 0x0, 0x0, 0x2)
    Jump("loc_2B8")

    label("loc_21F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 2)), scpexpr(EXPR_END)), "loc_246")
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, 70630, 0, 98590, 48)
    OP_43(0x9, 0x0, 0x0, 0x2)
    Jump("loc_2B8")

    label("loc_246")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 0)), scpexpr(EXPR_END)), "loc_250")
    Jump("loc_2B8")

    label("loc_250")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC7, 6)), scpexpr(EXPR_END)), "loc_294")
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, 72490, 0, 68540, 90)
    OP_43(0x8, 0x0, 0x0, 0x2)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, 70630, 0, 98590, 48)
    OP_43(0x9, 0x0, 0x0, 0x2)
    Jump("loc_2B8")

    label("loc_294")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC7, 1)), scpexpr(EXPR_END)), "loc_2B8")
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, 70630, 0, 98590, 48)
    OP_43(0x9, 0x0, 0x0, 0x2)

    label("loc_2B8")

    Return()

    # Function_0_122 end

    def Function_1_2B9(): pass

    label("Function_1_2B9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 4)), scpexpr(EXPR_END)), "loc_2C9")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x54), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2C9")

    OP_4F(0x2B, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_1_2B9 end

    def Function_2_2D3(): pass

    label("Function_2_2D3")

    RunExpression(0x0, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2F8")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_43A")

    label("loc_2F8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_311")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_43A")

    label("loc_311")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_32A")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_43A")

    label("loc_32A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_343")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_43A")

    label("loc_343")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_35C")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_43A")

    label("loc_35C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_375")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_43A")

    label("loc_375")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_38E")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_43A")

    label("loc_38E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3A7")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_43A")

    label("loc_3A7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3C0")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_43A")

    label("loc_3C0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3D9")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_43A")

    label("loc_3D9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3F2")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_43A")

    label("loc_3F2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_40B")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_43A")

    label("loc_40B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_424")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_43A")

    label("loc_424")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_43A")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_43A")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_44F")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_43A")

    label("loc_44F")

    Return()

    # Function_2_2D3 end

    def Function_3_450(): pass

    label("Function_3_450")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 7)), scpexpr(EXPR_END)), "loc_45D")
    Jump("loc_818")

    label("loc_45D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_467")
    Jump("loc_818")

    label("loc_467")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 6)), scpexpr(EXPR_END)), "loc_4C9")

    ChrTalk(    #0
        0xFE,
        (
            "Oh, I do hope the princess\x01",
            "is doing all right!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        "I should have gone with her...\x02",
    )

    CloseMessageWindow()
    Jump("loc_818")

    label("loc_4C9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 2)), scpexpr(EXPR_END)), "loc_559")
    TurnDirection(0xFE, 0x138, 0)

    ChrTalk(    #2
        0xFE,
        (
            "Joshua, your skin is almost\x01",
            "as soft as a woman's!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0xFE,
        (
            "It's absolutely perfect for make-up.\x01",
            "I'm actually kind of jealous!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_818")

    label("loc_559")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 0)), scpexpr(EXPR_END)), "loc_563")
    Jump("loc_818")

    label("loc_563")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC7, 6)), scpexpr(EXPR_END)), "loc_663")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC7, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC7, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC7, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_60D")

    ChrTalk(    #4
        0xFE,
        (
            "Each of our invited guests are\x01",
            "currently relaxing in their rooms.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0xFE,
        (
            "Please wait a little longer\x01",
            "while the preparations are\x01",
            "completed.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_660")

    label("loc_60D")


    ChrTalk(    #6
        0xFE,
        (
            "We'll be ready for dinner very,\x01",
            "very soon. I'm very sorry for\x01",
            "the wait.\x02",
        )
    )

    CloseMessageWindow()
    OP_28(0x49, 0x1, 0x800)

    label("loc_660")

    Jump("loc_818")

    label("loc_663")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC7, 1)), scpexpr(EXPR_END)), "loc_818")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_6FF")

    ChrTalk(    #7
        0xFE,
        (
            "It...will be a bit longer yet\x01",
            "before dinner is ready.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0xFE,
        (
            "In the meantime, please, feel\x01",
            "free to look around to your\x01",
            "heart's content!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_818")

    label("loc_6FF")

    OP_A2(0x1)

    ChrTalk(    #9
        0xFE,
        "Oh! Is everything all right?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0xFE,
        "Has something happened?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x101,
        (
            "#000FNo, not at all. I just wanted\x01",
            "to look around a bit...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0xFE,
        "I see.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0xFE,
        (
            "It...will be a bit longer yet\x01",
            "before dinner is ready.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0xFE,
        (
            "In the meantime, please, feel\x01",
            "free to look around to your\x01",
            "heart's content!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_818")

    TalkEnd(0xFE)
    Return()

    # Function_3_450 end

    def Function_4_81C(): pass

    label("Function_4_81C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 7)), scpexpr(EXPR_END)), "loc_916")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_896")

    ChrTalk(    #15
        0x8,
        (
            "#711FYou must be tired from the\x01",
            "Birthday Celebration.\x02\x03",

            "If you need anything, please\x01",
            "let me know.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_913")

    label("loc_896")

    OP_A2(0x0)

    ChrTalk(    #16
        0x8,
        (
            "#711FAh, Madam Estelle!\x02\x03",

            "You must be tired from the\x01",
            "Birthday Celebration.\x02\x03",

            "If you need anything, please\x01",
            "let me know.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_913")

    Jump("loc_C14")

    label("loc_916")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_A27")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_995")

    ChrTalk(    #17
        0x8,
        (
            "#710FThe town is no doubt abuzz\x01",
            "with festivities.\x02\x03",

            "If you are to attend them yourself,\x01",
            "please take care.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A24")

    label("loc_995")

    OP_A2(0x0)

    ChrTalk(    #18
        0x8,
        (
            "#710FOh, are you two heading out?\x02\x03",

            "The town is no doubt abuzz\x01",
            "with festivities.\x02\x03",

            "If you are to attend them yourself,\x01",
            "please take care.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A24")

    Jump("loc_C14")

    label("loc_A27")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 6)), scpexpr(EXPR_END)), "loc_AF5")

    ChrTalk(    #19
        0x8,
        (
            "#714FI don't believe any suspicions\x01",
            "have been raised...\x02\x03",

            "Just keep alert until you return\x01",
            "to your room.\x02\x03",

            "You never can be too certain how\x01",
            "closely the Intelligence Division\x01",
            "is watching you...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C14")

    label("loc_AF5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 2)), scpexpr(EXPR_END)), "loc_AFF")
    Jump("loc_C14")

    label("loc_AFF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 0)), scpexpr(EXPR_END)), "loc_B09")
    Jump("loc_C14")

    label("loc_B09")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC7, 1)), scpexpr(EXPR_END)), "loc_C14")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC7, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC7, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC7, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_B7E")

    ChrTalk(    #20
        0x8,
        (
            "#711FRegarding dinner...\x02\x03",

            "The pre-cooking is being done\x01",
            "now. Please remain patient.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C14")

    label("loc_B7E")


    ChrTalk(    #21
        0x8,
        (
            "#711FThe pre-cooking is done, so we\x01",
            "will be starting the banquet\x01",
            "shortly.\x02\x03",

            "Please wait in your room. We\x01",
            "will call you when the time\x01",
            "comes.\x02",
        )
    )

    CloseMessageWindow()
    OP_28(0x49, 0x1, 0x800)

    label("loc_C14")

    TalkEnd(0xFE)
    Return()

    # Function_4_81C end

    def Function_5_C18(): pass

    label("Function_5_C18")

    EventBegin(0x0)
    OP_6D(62970, 640, 71000, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_44(0x8, 0xFF)
    SetChrChipByIndex(0x8, 4)
    SetChrChipByIndex(0x101, 5)
    SetChrChipByIndex(0x102, 6)
    SetChrFlags(0x8, 0x800)
    SetChrFlags(0x8, 0x4)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, 64390, 200, 71030, 270)
    SetChrPos(0x101, 61580, 200, 71540, 90)
    SetChrPos(0x102, 61580, 200, 70620, 90)
    FadeToBright(2000, 0)
    OP_0D()

    ChrTalk(    #22
        0x8,
        (
            "#713F...I understand.\x02\x03",

            "You need to deliver Professor\x01",
            "Russell's message to Her Majesty.\x02\x03",

            "#714FCorrect?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x101,
        (
            "#002FRight...\x02\x03",

            "If now's not a good time,\x01",
            "we can try later, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x8,
        (
            "#715FNo, it's not an issue...\x02\x03",

            "But those Special Ops men have had\x01",
            "the Royal Keep under constant\x01",
            "surveillance for some time now.\x02\x03",

            "Only the duke, the colonel, and\x01",
            "hired attendants such as myself\x01",
            "are allowed in.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x101,
        (
            "#007FWhich means that a private\x01",
            "audience is probably a no-go.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x102, 1)

    ChrTalk(    #26
        0x102,
        (
            "#2P#012FWhat do you think, Estelle?\x02\x03",

            "We could ask Hilda to relay\x01",
            "the professor's message to\x01",
            "Her Majesty...\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 2)

    ChrTalk(    #27
        0x101,
        (
            "#505FHmmm... No, I'd really rather\x01",
            "speak to her face-to-face.\x02\x03",

            "There are just too many particulars\x01",
            "we don't know, that we'd really need\x01",
            "to discuss directly...\x02\x03",

            "Like what Duke Dunan and\x01",
            "Colonel Richard are after.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x8,
        (
            "#713FEstelle and Joshua...\x02\x03",

            "#714FI have a bit of an idea.\x02\x03",

            "Could I get you to return here,\x01",
            "once the dinner party is over?\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x102, 0)
    Sleep(200)
    SetChrSubChip(0x101, 0)

    ChrTalk(    #29
        0x101,
        "#004FWhy...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x102,
        (
            "#014FHave you thought of a way\x01",
            "for us to see Her Majesty?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x8,
        (
            "#711FI believe I have.\x02\x03",

            "It may be difficult...but\x01",
            "I think it's worth a try.\x02\x03",

            "I'm going to need some time to\x01",
            "get ready, so can you come back\x01",
            "after the dinner party?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x101,
        "#001FAwesome!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x102,
        (
            "#010FUnderstood.\x01",
            "We'll be back then.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC7, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC7, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC7, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_123D")

    ChrTalk(    #34
        0x8,
        (
            "#713FI'll be waiting.\x02\x03",

            "#711FOh, and about the party...\x02\x03",

            "Preparing the food is going\x01",
            "to take some time, so please,\x01",
            "bear with me.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_12D6")

    label("loc_123D")


    ChrTalk(    #35
        0x8,
        (
            "#713FI'll be waiting.\x02\x03",

            "#711FFood prep is done, so I think\x01",
            "we'll begin serving shortly.\x02\x03",

            "For now, it's probably best\x01",
            "if you wait in your room.\x02",
        )
    )

    CloseMessageWindow()
    OP_28(0x49, 0x1, 0x800)

    label("loc_12D6")

    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x101, 66930, 0, 66430, 180)
    SetChrPos(0x102, 66930, 0, 66430, 180)
    SetChrPos(0x8, 72490, 0, 68540, 90)
    SetChrChipByIndex(0x8, 0)
    SetChrChipByIndex(0x101, 65535)
    SetChrChipByIndex(0x102, 65535)
    ClearChrFlags(0x101, 0x4)
    ClearChrFlags(0x102, 0x4)
    ClearChrFlags(0x8, 0x4)
    ClearChrFlags(0x8, 0x800)
    OP_43(0x8, 0x0, 0x0, 0x2)
    OP_6D(66930, 0, 66430, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    Return()

    # Function_5_C18 end

    def Function_6_1387(): pass

    label("Function_6_1387")

    EventBegin(0x0)
    OP_6D(67590, 0, 65319, 0)
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, 70120, 0, 69770, 225)
    SetChrPos(0x101, 66580, 0, 64769, 45)
    SetChrPos(0x102, 67630, 0, 64590, 45)

    def lambda_13D8():
        OP_6D(69520, 0, 68800, 2000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_13D8)

    def lambda_13F0():
        OP_8E(0xFE, 0x10B6C, 0x0, 0x10BE4, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_13F0)

    def lambda_140B():
        OP_8E(0xFE, 0x1113E, 0x0, 0x1095A, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_140B)
    WaitChrThread(0x102, 0x2)
    TurnDirection(0x102, 0x8, 400)
    WaitChrThread(0x101, 0x3)

    ChrTalk(    #36
        0x8,
        (
            "#710FAh, there you are. I've\x01",
            "been waiting for you.\x02\x03",

            "You're awfully late, aren't you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0x101,
        (
            "#506FSorry about that...\x02\x03",

            "We kinda got caught by\x01",
            "Colonel Richard...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x8,
        "#712FDid you, now?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0x102,
        (
            "#010FHe had some things to tell\x01",
            "us about our dad.\x02\x03",

            "I don't think he has any idea\x01",
            "what we're up to, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0x8,
        (
            "#713FI see...\x02\x03",

            "#710FAh, yes. That letter of introduction\x01",
            "did mention that you were Mister\x01",
            "Cassius' children.\x02\x03",

            "I can understand at least some\x01",
            "of how Colonel Richard feels.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0x101,
        "#004FOh, do you know our dad, too?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0x8,
        (
            "#711FHe used to come here when he\x01",
            "worked as General Morgan's\x01",
            "aide-de-camp.\x02\x03",

            "I'm told that he was a school\x01",
            "friend of the late prince's...\x01",
            "Her Majesty's son.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0x101,
        "#505F'Late prince'?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0x102,
        "#012FPrincess Klaudia's father.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0x8,
        (
            "#715FYes... He was killed, fifteen\x01",
            "years ago, in a tragic shipwreck.\x02\x03",

            "Would that he were still\x01",
            "alive today, none of this\x01",
            "would be happening...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0x101,
        "#002FHuh...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x8,
        (
            "#713F...But lamenting what might\x01",
            "have been is a fool's errand.\x02\x03",

            "Evening is fast approaching. We\x01",
            "must make our preparations at once.\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x9, 69050, 0, 75720, 180)
    ClearChrFlags(0x9, 0x80)
    OP_4A(0x9, 255)
    TurnDirection(0x8, 0x9, 400)

    ChrTalk(    #48
        0x8,
        "#710FCome on in, Shea.\x02",
    )

    CloseMessageWindow()
    OP_72(0x3, 0x10)
    OP_6F(0x3, 0)
    OP_70(0x3, 0x3C)
    OP_73(0x3)

    def lambda_189B():
        TurnDirection(0xFE, 0x9, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_189B)

    def lambda_18A9():
        TurnDirection(0xFE, 0x9, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_18A9)
    Sleep(300)

    def lambda_18BC():

        label("loc_18BC")

        OP_8C(0xFE, 180, 0)
        OP_48()
        Jump("loc_18BC")

    QueueWorkItem2(0x9, 1, lambda_18BC)

    def lambda_18CD():
        OP_8E(0xFE, 0x10CCA, 0x0, 0x112B0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_18CD)

    def lambda_18E8():

        label("loc_18E8")

        TurnDirection(0xFE, 0x9, 0)
        OP_48()
        Jump("loc_18E8")

    QueueWorkItem2(0x8, 1, lambda_18E8)

    def lambda_18F9():

        label("loc_18F9")

        TurnDirection(0xFE, 0x9, 0)
        OP_48()
        Jump("loc_18F9")

    QueueWorkItem2(0x101, 1, lambda_18F9)

    def lambda_190A():

        label("loc_190A")

        TurnDirection(0xFE, 0x9, 0)
        OP_48()
        Jump("loc_190A")

    QueueWorkItem2(0x102, 1, lambda_190A)
    OP_6D(70030, 0, 70300, 2000)

    ChrTalk(    #49
        0x101,
        "#2P#004FOh, hey... Aren't you...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0x102,
        "#010F...Shea, right?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0x9,
        (
            "#3PYes, thank you for remembering.\x01",
            "You look well, Estelle. Joshua.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0x9,
        (
            "#3PI've been told of your\x01",
            "current predicament.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0x8,
        (
            "#711F#4PYou won't find a more\x01",
            "dependable child.\x02\x03",

            "She's a great help to us whenever\x01",
            "the princess is in the castle.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0x101,
        "#2P#501FPrincess Klaudia...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0x102,
        "#019FThat shouldn't pose a problem.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0x9,
        "#3PTh-Thank you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0x9,
        (
            "#3PIf you're ready, you should go\x01",
            "change into your uniforms...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0x9,
        (
            "#3PThe ribbons and the headpiece\x01",
            "are tricky, so I'll adjust them\x01",
            "for you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0x101,
        "#2P#004FWha...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0x102,
        "#014FWhat do you mean...?\x02",
    )

    CloseMessageWindow()
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_44(0x9, 0x1)
    OP_44(0x8, 0xFF)
    TurnDirection(0x8, 0x101, 400)

    ChrTalk(    #61
        0x8,
        (
            "#711F#4PEstelle is going to need to dress\x01",
            "as one of the maids in order to\x01",
            "get into the Royal Keep.\x02\x03",

            "A little playing with the hair,\x01",
            "and you'll blend right in.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0x101,
        "#2P#501FOhhhh, I get it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0x102,
        (
            "#010FUniforms don't allow for much\x01",
            "in the way of personalization.\x02\x03",

            "That should be ideal for\x01",
            "sneaking in.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0x101,
        (
            "#2P#008FHuh...\x01",
            "Me, in a maid's outfit.\x02\x03",

            "I've been wanting to try one on since we first\x01",
            "met Lila.\x02\x03",

            "Cute, breezy and easy to move in...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0x9,
        (
            "#3PHa ha... Well, if our uniforms weren't easy to\x01",
            "move in, they'd make the cleaning much more\x01",
            "difficult.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0x101,
        (
            "#2P#006FI thought so.\x02\x03",

            "#001FWell, let's get this sucker on me!\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x102, 270, 400)

    ChrTalk(    #67
        0x102,
        (
            "#019F#2PWhy so excited?\x02\x03",

            "#010FI'm glad you're in high spirits,\x01",
            "but you need to remember your\x01",
            "manners in front of the queen.\x02\x03",

            "You won't have me to\x01",
            "lean on this time.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 90, 400)

    ChrTalk(    #68
        0x101,
        (
            "#004FWhy not?\x02\x03",

            "You're changing too,\x01",
            "aren't you?\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1200)
    OP_63(0x102)

    ChrTalk(    #69
        0x102,
        "#014F#2P#5S...Err?\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    TurnDirection(0x8, 0x101, 400)

    ChrTalk(    #70
        0x8,
        "#712F#4PPardon?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0x101,
        (
            "#501FI mean, he DID play the\x01",
            "princess during the play\x01",
            "at the campus festival.\x02\x03",

            "Is there really that much of\x01",
            "a difference between the fancy\x01",
            "dress and a maid outfit?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0x102,
        (
            "#018F#2PThat's different.\x01",
            "It was a play.\x02\x03",

            "I can't appear before Her\x01",
            "Majesty in women's clothes...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0x101,
        (
            "#001FOh, you'll be fine. It's not\x01",
            "at all shameful or anything.\x02\x03",

            "Besides, you made such\x01",
            "a gorgeous princess!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0x102,
        (
            "#017F#2PN-Not this again...\x01",
            "Cut the jokes, will you?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x8, 400)

    ChrTalk(    #75
        0x102,
        (
            "#012FHilda... Shea... Help me\x01",
            "out here. Say something...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x102, 400)

    ChrTalk(    #76
        0x8,
        "#712F#6P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0x9,
        "#3P...\x02",
    )

    CloseMessageWindow()
    OP_62(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #78
        0x102,
        "#018FAnyone?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0x8,
        (
            "#713F#6PI see...\x01",
            "That shouldn't pose a problem.\x02\x03",

            "#710FShea, don't you have that extra\x01",
            "hairpiece designed for the princess?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0x9,
        "#3PY-Yes... It's never been used, though.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0x9,
        (
            "#3PHe has that full, dark hair,\x01",
            "so it would probably look\x01",
            "good on him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0x102,
        "#018FHey, hold on a second...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0x101,
        (
            "#001FWell, it looks like a three-to-one\x01",
            "vote. Majority rules! ♪\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0x9,
        (
            "#3PThis way, please. We can use\x01",
            "this as a changing room.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_234B():

        label("loc_234B")

        TurnDirection(0xFE, 0x102, 0)
        OP_48()
        Jump("loc_234B")

    QueueWorkItem2(0x8, 1, lambda_234B)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0x9, 0x4)
    SetChrFlags(0x9, 0x40)
    OP_8C(0x9, 0, 400)

    def lambda_2377():
        OP_8E(0xFE, 0x10C48, 0x0, 0x12D4A, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_2377)
    Sleep(300)
    OP_8E(0x101, 0x10FF4, 0x0, 0x10AEA, 0xBB8, 0x0)

    ChrTalk(    #85
        0x102,
        (
            "#012FW-Wait a minute, I don't remember ever agreeing\x01",
            "to changing!\x02",
        )
    )

    CloseMessageWindow()
    OP_8E(0x102, 0x10FEA, 0x0, 0x1090A, 0x7D0, 0x0)
    OP_8C(0x102, 180, 400)

    def lambda_240D():
        OP_6D(69970, 0, 72360, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_240D)

    def lambda_2425():
        OP_8E(0xFE, 0x10C48, 0x0, 0x12D4A, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2425)

    def lambda_2440():
        OP_8F(0xFE, 0x10C48, 0x0, 0x12D4A, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2440)
    OP_62(0x8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(3000)
    OP_72(0x3, 0x800)
    OP_22(0x7, 0x0, 0x64)
    OP_6F(0x3, 60)
    OP_70(0x3, 0x0)
    OP_73(0x3)
    OP_71(0x3, 0x800)
    Sleep(1000)

    ChrTalk(    #86
        0x102,
        (
            "#4PAll right, all right. If I have\x01",
            "to change, I can do it myself...\x02\x03",

            "Uh...Shea... You're not planning\x01",
            "on using makeup, too, are you...?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8)

    ChrTalk(    #87
        0x8,
        "#716F*sigh* Kids these days...\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6D(69200, 0, 72370, 0)
    SetChrPos(0x8, 68890, 0, 69520, 0)
    SetChrFlags(0x101, 0x1000)
    SetChrFlags(0x102, 0x1000)
    SetChrChipByIndex(0x101, 2)
    SetChrChipByIndex(0x102, 3)
    Sleep(500)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x3, 0)
    OP_70(0x3, 0x3C)
    OP_73(0x3)

    def lambda_25AC():

        label("loc_25AC")

        OP_8C(0xFE, 225, 0)
        OP_48()
        Jump("loc_25AC")

    QueueWorkItem2(0x101, 2, lambda_25AC)

    def lambda_25BD():
        OP_8E(0xFE, 0x11062, 0x0, 0x116F2, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_25BD)
    Sleep(600)

    def lambda_25DD():
        OP_8E(0xFE, 0x10E00, 0x0, 0x11D78, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_25DD)
    WaitChrThread(0x9, 0x1)

    def lambda_25FD():
        OP_8E(0xFE, 0x1090A, 0x0, 0x11E18, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_25FD)
    WaitChrThread(0x9, 0x1)

    def lambda_261D():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_261D)

    ChrTalk(    #88
        0x8,
        "#712FOh, my...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0x101,
        "#321F#6P#3STa-dah!\x02",
    )

    CloseMessageWindow()
    OP_44(0x101, 0xFF)
    OP_8C(0x101, 317, 400)
    OP_8C(0x101, 75, 400)
    OP_8C(0x101, 225, 400)

    ChrTalk(    #90
        0x101,
        (
            "#328F#6PHee hee...\x01",
            "What do you think?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0x9,
        (
            "Heehee...\x01",
            "I think it suits her very well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0x8,
        (
            "#711FSuch a bright, active maid-in-training, and\x01",
            "after only just coming to the castle, too...\x01",
            "You certainty have me convinced!\x02\x03",

            "And with the hair down like that,\x01",
            "no one will be any the wiser.\x02\x03",

            "Perhaps you'd like to work\x01",
            "at Grancel Castle for real\x01",
            "when this is all settled?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0x101,
        (
            "#474F#6PW-Well, we already work\x01",
            "as bracers, so, uh...\x02\x03",

            "#471FAnyway...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(    #94
        0x101,
        (
            "#321FCome on, Joshua.\x01",
            "Get out here.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_285B():
        TurnDirection(0xFE, 0x102, 400)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_285B)

    def lambda_2869():
        TurnDirection(0xFE, 0x102, 400)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_2869)
    OP_6D(69080, 0, 73680, 1000)
    SetChrPos(0x102, 69050, 0, 77130, 180)

    ChrTalk(    #95
        0x102,
        (
            "#4P*sigh*...\x02\x03",

            "No chance I can talk\x01",
            "you out of this?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #96
        0x101,
        (
            "#326FNone at all.\x02\x03",

            "You're just making this take longer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0x102,
        (
            "#4PFine...\x02\x03",

            "You're impossible sometimes...\x02",
        )
    )

    CloseMessageWindow()

    def lambda_293F():

        label("loc_293F")

        TurnDirection(0xFE, 0x102, 0)
        OP_48()
        Jump("loc_293F")

    QueueWorkItem2(0x9, 1, lambda_293F)

    def lambda_2950():

        label("loc_2950")

        TurnDirection(0xFE, 0x102, 0)
        OP_48()
        Jump("loc_2950")

    QueueWorkItem2(0x8, 1, lambda_2950)

    def lambda_2961():

        label("loc_2961")

        TurnDirection(0xFE, 0x102, 0)
        OP_48()
        Jump("loc_2961")

    QueueWorkItem2(0x101, 1, lambda_2961)

    def lambda_2972():
        OP_6C(5000, 3000)
        ExitThread()

    QueueWorkItem(0x102, 3, lambda_2972)

    def lambda_2982():
        OP_67(0, 6130, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_2982)
    Sleep(1600)

    def lambda_299F():
        OP_8E(0xFE, 0x10DBA, 0x0, 0x11DC8, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_299F)
    Sleep(3000)

    def lambda_29BF():
        OP_6C(45000, 3000)
        ExitThread()

    QueueWorkItem(0x102, 3, lambda_29BF)

    def lambda_29CF():
        OP_67(0, 8000, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_29CF)
    OP_62(0x102, 0x12C, 1600, 0x36, 0x39, 0xFA, 0x0)
    Sleep(500)
    OP_22(0x89, 0x0, 0x64)
    WaitChrThread(0x102, 0x1)
    WaitChrThread(0x102, 0x2)
    OP_63(0x102)

    ChrTalk(    #98
        0x102,
        "#333F#6P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0x8,
        (
            "#712FWell... It's almost frightening\x01",
            "how good that looks.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0x101,
        (
            "#326FIsn't it awesome?!\x02\x03",

            "#327FIt looks better on him than\x01",
            "it does on me, and I'm an\x01",
            "actual girl!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0x9,
        (
            "Ha ha... A bit of makeup can\x01",
            "make all the difference in\x01",
            "the world.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0x102,
        (
            "#335F#6PPlease...\x01",
            "Just say you're done.\x02",
        )
    )

    CloseMessageWindow()
    OP_6D(68990, 0, 71660, 1000)

    def lambda_2B4C():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2B4C)

    def lambda_2B5A():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_2B5A)
    OP_8C(0x102, 180, 0)

    ChrTalk(    #103
        0x8,
        (
            "#710FWell... I suppose so.\x02\x03",

            "I'll show you the way\x01",
            "to the Royal Keep.\x02\x03",

            "You need to make certain you\x01",
            "watch me and learn how a maid\x01",
            "handles herself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0x101,
        (
            "#471FY-Yes, ma'am.\x02\x03",

            "#322F*gulp* We're finally gonna\x01",
            "meet the queen in person.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0x102,
        (
            "#332FYes...\x01",
            "This is the do-or-die moment.\x02\x03",

            "We just have to stay focused \x01",
            "and get to the Royal Keep.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(    #106
        0x101,
        (
            "#475F*snicker*... It's hard to take\x01",
            "you seriously in that outfit.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 800)

    ChrTalk(    #107
        0x102,
        (
            "#337FW-Well, excuse me!\x02\x03",

            "#333FThis was YOUR idea! I can't\x01",
            "believe you've got the nerve\x01",
            "to pick on--\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #108
        0x101,
        (
            "#321FSorry, sorry...\x01",
            "Don't get all mad.\x02\x03",

            "I'll treat you to some\x01",
            "ice cream later, okay?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #109
        0x102,
        (
            "#332FHmph. I'm not like you. I'm\x01",
            "not obsessed with food.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #110
        0x101,
        "#476FH-Hey! I'm not obsessed with food...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0x9,
        (
            "Ha ha ha... They get along\x01",
            "so well, don't they?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #112
        0x8,
        (
            "#713FWe're out of time. Let's\x01",
            "go to the Royal Keep.\x02",
        )
    )

    CloseMessageWindow()
    SetMapFlags(0x80000000)
    OP_28(0x4A, 0x1, 0x20)
    OP_28(0x4A, 0x1, 0x40)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrFlags(0x9, 0x80)
    AddParty(0x37, 0xFF)
    SetChrChipByIndex(0x0, 0)
    SetChrChipByIndex(0x1, 2)
    SetChrChipByIndex(0x138, 3)
    SetChrFlags(0x0, 0x1000)
    SetChrFlags(0x1, 0x1000)
    SetChrFlags(0x138, 0x1000)
    SetChrFlags(0x8, 0x80)
    SetChrPos(0x101, 67460, 0, 69310, 180)
    SetChrPos(0x102, 67460, 0, 69310, 180)
    SetChrPos(0x138, 67460, 0, 69310, 180)
    OP_6D(67460, 0, 69310, 0)
    OP_6F(0x3, 0)
    OP_71(0x3, 0x10)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    Return()

    # Function_6_1387 end

    def Function_7_2F54(): pass

    label("Function_7_2F54")

    EventBegin(0x0)
    FadeToBright(2000, 0)
    OP_6D(68370, 0, 69650, 0)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x8, 68920, 0, 70070, 180)
    SetChrPos(0x9, 67750, 0, 70350, 180)
    OP_4A(0x8, 255)
    OP_4A(0x9, 255)
    RemoveParty(0x37, 0xFF)
    SetChrPos(0x101, 68360, 0, 68190, 0)
    SetChrPos(0x102, 67080, 0, 68350, 45)
    FadeToBright(1500, 0)
    OP_0D()

    ChrTalk(    #113
        0x101,
        (
            "#006FThanks for everything!\x01",
            "Both of you!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #114
        0x102,
        (
            "#010FIf not for you, I don't know\x01",
            "what we'd have done.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0x8,
        (
            "#711FPlease. It was the least we could\x01",
            "do in Her Majesty's service.\x02\x03",

            "I only ask that you complete\x01",
            "the request she made of you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #116
        0x9,
        "U-Umm... I feel the same way.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #117
        0x9,
        (
            "I beg of you, do everything in\x01",
            "your power to save the princess.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #118
        0x101,
        (
            "#002FOh... Are you one of\x01",
            "her royal retainers?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #119
        0x9,
        (
            "Y-Yes... I regret that I rarely\x01",
            "get the chance to serve her\x01",
            "directly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #120
        0x9,
        (
            "She's so kind and open...\x01",
            "She's always treated me more\x01",
            "like a friend than a servant.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #121
        0x9,
        (
            "The thought of her being held\x01",
            "captive keeps me up at night...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #122
        0x101,
        (
            "#006FI understand. Well, you can rest\x01",
            "easy now that we're on the job!\x01",
            "We'll save her!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #123
        0x102,
        "#010FShall we be going?\x02",
    )

    CloseMessageWindow()
    OP_4B(0x8, 255)
    OP_4B(0x9, 255)
    ClearMapFlags(0x80000000)
    OP_43(0x8, 0x0, 0x0, 0x2)
    OP_43(0x9, 0x0, 0x0, 0x2)
    EventEnd(0x0)
    Return()

    # Function_7_2F54 end

    SaveToFile()

Try(main)

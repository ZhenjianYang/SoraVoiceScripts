from ED6ScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 蔡斯

    CreateScenaFile(
        FileName            = 'T3116   ._SN',
        MapName             = 'Zeiss',
        Location            = 'T3116.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60013",
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
        'Professor Russell',                    # 9
        'Tita',                                 # 10
        'Factory Chief Murdock',                # 11
        'Karl',                                 # 12
        'Prometheus',                           # 13
        'Antoine',                              # 14
        'Orbment',                              # 15
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
        'ED6_DT07/CH02020 ._CH',             # 00
        'ED6_DT07/CH00060 ._CH',             # 01
        'ED6_DT07/CH02620 ._CH',             # 02
        'ED6_DT07/CH01190 ._CH',             # 03
        'ED6_DT07/CH01100 ._CH',             # 04
        'ED6_DT07/CH01700 ._CH',             # 05
        'ED6_DT06/CH20021 ._CH',             # 06
    )

    AddCharChipPat(
        'ED6_DT07/CH02020P._CP',             # 00
        'ED6_DT07/CH00060P._CP',             # 01
        'ED6_DT07/CH02620P._CP',             # 02
        'ED6_DT07/CH01190P._CP',             # 03
        'ED6_DT07/CH01100P._CP',             # 04
        'ED6_DT07/CH01700P._CP',             # 05
        'ED6_DT06/CH20021P._CP',             # 06
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
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
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
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = 20,
        Z                   = 700,
        Y                   = 39430,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 917510,
        ChipIndex           = 0x6,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    ScpFunction(
        "Function_0_1C2",          # 00, 0
        "Function_1_3E3",          # 01, 1
        "Function_2_497",          # 02, 2
        "Function_3_4AD",          # 03, 3
        "Function_4_4D1",          # 04, 4
        "Function_5_4F1",          # 05, 5
        "Function_6_633",          # 06, 6
        "Function_7_188E",         # 07, 7
        "Function_8_1974",         # 08, 8
        "Function_9_1A47",         # 09, 9
        "Function_10_1B10",        # 0A, 10
        "Function_11_2E1F",        # 0B, 11
        "Function_12_41CB",        # 0C, 12
        "Function_13_4219",        # 0D, 13
        "Function_14_4244",        # 0E, 14
        "Function_15_426F",        # 0F, 15
        "Function_16_42AE",        # 10, 16
        "Function_17_4BD1",        # 11, 17
    )


    def Function_0_1C2(): pass

    label("Function_0_1C2")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (100, "loc_1CE"),
        (SWITCH_DEFAULT, "loc_210"),
    )


    label("loc_1CE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1E1")
    OP_A2(0x513)
    Event(0, 10)

    label("loc_1E1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1FA")
    SetMapFlags(0x10000000)
    Event(0, 11)

    label("loc_1FA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_20D")
    OP_A2(0x531)
    Event(0, 16)

    label("loc_20D")

    Jump("loc_210")

    label("loc_210")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_230")
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, -4500, 0, 6620, 99)
    Jump("loc_3E2")

    label("loc_230")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_250")
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, -4500, 0, 6620, 99)
    Jump("loc_3E2")

    label("loc_250")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 1)), scpexpr(EXPR_END)), "loc_270")
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, -4500, 0, 6620, 99)
    Jump("loc_3E2")

    label("loc_270")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 0)), scpexpr(EXPR_END)), "loc_2A6")
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, -4500, 0, 6620, 99)
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, -90, 0, 9830, 355)
    Jump("loc_3E2")

    label("loc_2A6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 6)), scpexpr(EXPR_END)), "loc_2CD")
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, 670, 0, 8480, 6)
    OP_43(0xD, 0x0, 0x0, 0x3)
    Jump("loc_3E2")

    label("loc_2CD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_2D7")
    Jump("loc_3E2")

    label("loc_2D7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_332")
    SetChrPos(0xE, 40, 800, 11550, 0)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0x8, 0x80)
    OP_43(0x8, 0x0, 0x0, 0x2)
    SetChrPos(0x8, 140, 0, 12690, 175)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_32F")
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, -130, 0, 10450, 0)

    label("loc_32F")

    Jump("loc_3E2")

    label("loc_332")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 3)), scpexpr(EXPR_END)), "loc_37E")
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, -100, 0, 12700, 180)
    SetChrPos(0x8, -2310, 0, 14200, 0)
    SetChrPos(0xE, 40, 800, 11550, 0)
    ClearChrFlags(0xE, 0x80)
    Jump("loc_3E2")

    label("loc_37E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 1)), scpexpr(EXPR_END)), "loc_3A5")
    ClearChrFlags(0x8, 0x80)
    OP_43(0x8, 0x0, 0x0, 0x2)
    SetChrPos(0x8, 140, 0, 12690, 175)
    Jump("loc_3E2")

    label("loc_3A5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_3C5")
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, -4500, 0, 6620, 99)
    Jump("loc_3E2")

    label("loc_3C5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_3E2")
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, -4500, 0, 6620, 99)

    label("loc_3E2")

    Return()

    # Function_0_1C2 end

    def Function_1_3E3(): pass

    label("Function_1_3E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3FB")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x54), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_428")

    label("loc_3FB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_413")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x52), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_428")

    label("loc_413")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_428")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x51), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_428")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_48A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_48A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_48A")
    LoadEffect(0x1, "map\\\\mpfog.eff")
    PlayEffect(0x1, 0x1, 0xFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    label("loc_48A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_496")
    OP_72(0x0, 0x4)

    label("loc_496")

    Return()

    # Function_1_3E3 end

    def Function_2_497(): pass

    label("Function_2_497")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4AC")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_497")

    label("loc_4AC")

    Return()

    # Function_2_497 end

    def Function_3_4AD(): pass

    label("Function_3_4AD")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4D0")
    OP_8D(0xFE, -1710, 9770, 3200, 6310, 3000)
    Jump("Function_3_4AD")

    label("loc_4D0")

    Return()

    # Function_3_4AD end

    def Function_4_4D1(): pass

    label("Function_4_4D1")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 6)), scpexpr(EXPR_END)), "loc_4ED")
    OP_22(0x192, 0x0, 0x64)

    ChrTalk(    #0
        0xFE,
        "Nyaa...\x02",
    )

    CloseMessageWindow()

    label("loc_4ED")

    TalkEnd(0xFE)
    Return()

    # Function_4_4D1 end

    def Function_5_4F1(): pass

    label("Function_5_4F1")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 0)), scpexpr(EXPR_END)), "loc_62F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_59D")

    ChrTalk(    #1
        0xFE,
        (
            "It looks like Professor Russell's\x01",
            "already gone home.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0xFE,
        (
            "Oh well...I really wanted to get\x01",
            "his advice on something.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0xFE,
        "Some other time, I guess.\x02",
    )

    CloseMessageWindow()
    Jump("loc_62F")

    label("loc_59D")

    OP_A2(0x1)

    ChrTalk(    #4
        0xFE,
        (
            "It looks like Professor Russell's\x01",
            "already gone home.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0xFE,
        "He sure left early...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0xFE,
        (
            "Oh well...stranger things have\x01",
            "happened, am I right?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_62F")

    TalkEnd(0xFE)
    Return()

    # Function_5_4F1 end

    def Function_6_633(): pass

    label("Function_6_633")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_7B6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_6BD")

    ChrTalk(    #7
        0xFE,
        (
            "Come to think of it, where\x01",
            "IS Professor Russell?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0xFE,
        (
            "I'd hoped he would've at least\x01",
            "cleaned up his workstation.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7B3")

    label("loc_6BD")

    OP_A2(0x0)

    ChrTalk(    #9
        0xFE,
        (
            "I've got to completely recalibrate\x01",
            "the orbal guns.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0xFE,
        (
            "There's definitely some kind of\x01",
            "irregularity, but I can't seem to\x01",
            "quite pin it down.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0xFE,
        (
            "*sigh* It'd probably be easier to\x01",
            "just scrap everything and start\x01",
            "it all over from scratch.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7B3")

    Jump("loc_188A")

    label("loc_7B6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_8C2")

    ChrTalk(    #12
        0xFE,
        (
            "The orbal guns I'm currently\x01",
            "working on are poorly balanced\x01",
            "and incredibly hard to use.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0xFE,
        (
            "But if I could get them onto\x01",
            "the market they'd be a \x01",
            "bestseller for sure.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0xFE,
        "Performance vs. usability...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0xFE,
        (
            "A difficult choice...may as\x01",
            "well try for both.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_188A")

    label("loc_8C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 1)), scpexpr(EXPR_END)), "loc_B49")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_A01")

    ChrTalk(    #16
        0xFE,
        (
            "I'm finishing the initial paperwork\x01",
            "for my next thesis.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0xFE,
        (
            "It's going to be about the need\x01",
            "for pursuing a user-accessible\x01",
            "design philosophy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0xFE,
        (
            "At this stage there are a lot of\x01",
            "vague points, and even I don't\x01",
            "grasp all the specifics.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0xFE,
        (
            "But I think as engineers,\x01",
            "it's an important challenge.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B46")

    label("loc_A01")

    OP_A2(0x0)

    ChrTalk(    #20
        0xFE,
        "Oh, good morning!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0xFE,
        (
            "I started putting together my\x01",
            "next thesis yesterday.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0xFE,
        (
            "It's going to be about the need\x01",
            "for pursuing a user-accessible\x01",
            "design philosophy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0xFE,
        (
            "At this stage there are a lot of\x01",
            "vague points, and even I don't\x01",
            "grasp all the specifics.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0xFE,
        (
            "But I think as engineers,\x01",
            "it's an important challenge.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B46")

    Jump("loc_188A")

    label("loc_B49")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 0)), scpexpr(EXPR_END)), "loc_E6E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_CAF")

    ChrTalk(    #25
        0xFE,
        (
            "Today I had to explain about some\x01",
            "easy-to-use cameras to a woman\x01",
            "at the maintenance desk.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0xFE,
        (
            "But 'user-friendly' isn't a thing\x01",
            "we measure with numbers.\x01",
            "I found explaining it...hard.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0xFE,
        (
            "The owner of the weapons shop\x01",
            "keeps talking to me about\x01",
            "considering accessibility...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0xFE,
        (
            "...Now I think I'm starting to\x01",
            "understand what he means.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E6B")

    label("loc_CAF")

    OP_A2(0x0)

    ChrTalk(    #29
        0xFE,
        "Whew, what a day.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0xFE,
        (
            "Today I had to explain a product\x01",
            "to a customer over at the\x01",
            "maintenance desk.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0xFE,
        (
            "I tried to approach it from our\x01",
            "efficiency reports, but she\x01",
            "didn't seem to get that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0xFE,
        (
            "She wanted an 'easy-to-use' camera,\x01",
            "but...that's not a value we can just\x01",
            "simply measure.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0xFE,
        (
            "The owner of the weapons shop\x01",
            "keeps talking to me about\x01",
            "considering accessibility...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0xFE,
        (
            "...Now I think I'm starting to\x01",
            "understand what he means.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E6B")

    Jump("loc_188A")

    label("loc_E6E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_1404")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x22, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_1310")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB0, 5)), scpexpr(EXPR_END)), "loc_F8D")

    ChrTalk(    #35
        0xFE,
        (
            "I think it's safe to say the orbal gun's\x01",
            "research is moving along nicely.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0xFE,
        (
            "It will take time to properly\x01",
            "micronize the components,\x01",
            "but we can do it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0xFE,
        (
            "If things go smoothly we can have\x01",
            "them on the shelves soon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0xFE,
        "I hope they end up big sellers.\x02",
    )

    CloseMessageWindow()
    Jump("loc_130D")

    label("loc_F8D")

    OP_A2(0x585)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FD2")

    ChrTalk(    #39
        0xFE,
        "Hi, Tita. And...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #40
        0xFE,
        "Hey...don't I..?\x02",
    )

    CloseMessageWindow()
    Jump("loc_FE6")

    label("loc_FD2")


    ChrTalk(    #41
        0xFE,
        "Haven't we...?\x02",
    )

    CloseMessageWindow()

    label("loc_FE6")


    ChrTalk(    #42
        0x101,
        "#501FWhat? What?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0x102,
        (
            "#010FNow that you mention it...\x02\x03",

            "We DID meet previously,\x01",
            "when we were in Ruan!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x102, 400)

    ChrTalk(    #44
        0xFE,
        (
            "I thought so! You two were a\x01",
            "real help that time!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #45
        0xFE,
        (
            "I appreciate you finding the orbal\x01",
            "gun prototype for me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0x101,
        (
            "#001FOh, yeah!\x01",
            "You're that science guy!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x107,
        (
            "#560FI remember you told me\x01",
            "about that!\x02\x03",

            "You had lost one of the samples\x01",
            "en route to Ruan...?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x107, 400)

    ChrTalk(    #48
        0xFE,
        (
            "Yeah, that was a heap of trouble,\x01",
            "wasn't it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0xFE,
        "You guys really saved my butt.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0x101,
        (
            "#000FHow'd all your research and stuff\x01",
            "end up doing, anyway?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #51
        0xFE,
        (
            "I think it's safe to say the orbal gun's\x01",
            "research is moving along nicely.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0xFE,
        (
            "It will take time to properly\x01",
            "micronize the components,\x01",
            "but we can do it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0xFE,
        (
            "If things go smoothly we can\x01",
            "have them on the shelves soon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0xFE,
        "I hope they end up big sellers.\x02",
    )

    CloseMessageWindow()

    label("loc_130D")

    Jump("loc_1401")

    label("loc_1310")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1371")

    ChrTalk(    #55
        0xFE,
        "No time for chit-chat...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0xFE,
        (
            "I've got to draw up the efficiency\x01",
            "ratings indexes.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1401")

    label("loc_1371")

    OP_A2(0x0)

    ChrTalk(    #57
        0xFE,
        (
            "I'm really glad Louise was able\x01",
            "to reconstruct the prototype\x01",
            "unit like she did.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0xFE,
        (
            "Without it, my research would've\x01",
            "ground to a halt.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1401")

    Jump("loc_188A")

    label("loc_1404")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_188A")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x22, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_1799")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB0, 5)), scpexpr(EXPR_END)), "loc_1523")

    ChrTalk(    #59
        0xFE,
        (
            "I think it's safe to say the orbal gun's\x01",
            "research is moving along nicely.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0xFE,
        (
            "It will take time to properly\x01",
            "micronize the components,\x01",
            "but we can do it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0xFE,
        (
            "If things go smoothly we can\x01",
            "have them on the shelves soon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0xFE,
        "I hope they end up big sellers.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1796")

    label("loc_1523")

    OP_A2(0x585)

    ChrTalk(    #63
        0xFE,
        "Haven't we...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0x101,
        "#501FWhat? What?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0x102,
        (
            "#010FNow that you mention it...\x02\x03",

            "We DID meet previously,\x01",
            "when we were in Ruan!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x102, 400)

    ChrTalk(    #66
        0xFE,
        (
            "I thought so! You two were a\x01",
            "real help that time!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #67
        0xFE,
        (
            "I appreciate you finding the orbal\x01",
            "gun prototype for me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0x101,
        (
            "#001FOh, yeah!\x01",
            "You're that science guy!\x02\x03",

            "#000FHow'd all your research and\x01",
            "stuff end up doing, anyway?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0xFE,
        (
            "I think it's safe to say the orbal gun's\x01",
            "research is moving along nicely.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0xFE,
        (
            "It will take time to properly\x01",
            "micronize the components,\x01",
            "but we can do it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0xFE,
        (
            "If things go smoothly we can\x01",
            "have them on the shelves soon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0xFE,
        "I hope they end up big sellers.\x02",
    )

    CloseMessageWindow()

    label("loc_1796")

    Jump("loc_188A")

    label("loc_1799")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_17FA")

    ChrTalk(    #73
        0xFE,
        "No time for chit-chat...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0xFE,
        (
            "I've got to draw up the efficiency\x01",
            "ratings indexes.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_188A")

    label("loc_17FA")

    OP_A2(0x0)

    ChrTalk(    #75
        0xFE,
        (
            "I'm really glad Louise was able\x01",
            "to reconstruct the prototype\x01",
            "unit like she did.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0xFE,
        (
            "Without it, my research would've\x01",
            "ground to a halt.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_188A")

    TalkEnd(0xFE)
    Return()

    # Function_6_633 end

    def Function_7_188E(): pass

    label("Function_7_188E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_1970")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1902")

    ChrTalk(    #77
        0xA,
        (
            "#800FVery well, then. I'll leave Tita in\x01",
            "your capable hands.\x02\x03",

            "Tita, be careful out there.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1970")

    label("loc_1902")


    ChrTalk(    #78
        0xA,
        (
            "#800FIs anything wrong?\x02\x03",

            "You can get to the Elmo Hot\x01",
            "Springs by using the gate at\x01",
            "the south end of town.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1970")

    TalkEnd(0xFE)
    Return()

    # Function_7_188E end

    def Function_8_1974(): pass

    label("Function_8_1974")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_19E3")

    ChrTalk(    #79
        0x8,
        (
            "#100FThanks in advance.\x02\x03",

            "As long as you get her there,\x01",
            "Tita can do all the work.\x02\x03",

            "Good luck.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A43")

    label("loc_19E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 1)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1A43")

    ChrTalk(    #80
        0x8,
        (
            "#100FHuh? What are you doing?\x02\x03",

            "I need that Combustion Engine\x01",
            "and some gasoline!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A43")

    TalkEnd(0xFE)
    Return()

    # Function_8_1974 end

    def Function_9_1A47(): pass

    label("Function_9_1A47")

    TalkBegin(0xFE)

    ChrTalk(    #81
        0x9,
        (
            "#060FRemember? They're in storage in\x01",
            "Operations on the fifth floor.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 6)), scpexpr(EXPR_END)), "loc_1ACA")

    ChrTalk(    #82
        0x101,
        (
            "#000FYeah, I remember.\x01",
            "Let's get going.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1B0C")

    label("loc_1ACA")


    ChrTalk(    #83
        0x101,
        (
            "#505FFifth floor, Operations.\x02\x03",

            "#000FGot it. Let's get going.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B0C")

    TalkEnd(0xFE)
    Return()

    # Function_9_1A47 end

    def Function_10_1B10(): pass

    label("Function_10_1B10")

    ClearMapFlags(0x1)
    EventBegin(0x0)
    OP_6D(-770, 0, 1240, 0)
    RemoveParty(0x6, 0xFF)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0x8, 0x80)
    OP_4A(0x9, 255)
    OP_4A(0x8, 255)
    SetChrPos(0x8, -100, 0, 12700, 180)
    SetChrPos(0x9, -1030, 0, 1690, 0)
    SetChrPos(0x101, -600, 0, 510, 0)
    SetChrPos(0x102, -1950, 0, 750, 0)
    SetChrPos(0xE, 40, 800, 11550, 0)
    ClearChrFlags(0xE, 0x80)
    FadeToBright(2000, 0)
    OP_0D()

    ChrTalk(    #84
        0x8,
        "#4PBah! Another failure!\x02",
    )

    CloseMessageWindow()

    def lambda_1BC5():
        OP_6D(1050, 0, 11840, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1BC5)

    def lambda_1BDD():
        OP_8E(0xFE, 0x55A, 0x0, 0x26D4, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_1BDD)
    Sleep(300)

    def lambda_1BFD():
        OP_8E(0xFE, 0xFFFFFCE0, 0x0, 0x2710, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1BFD)
    Sleep(200)

    def lambda_1C1D():
        OP_8E(0xFE, 0x82, 0x0, 0x263E, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1C1D)
    WaitChrThread(0x9, 0x1)
    TurnDirection(0x9, 0x8, 0)

    ChrTalk(    #85
        0x9,
        (
            "#560FGrandpa? We came to see\x01",
            "if we could help.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #86
        0x8,
        (
            "#103FAh, hello, Tita.\x02\x03",

            "And you two are here, as well,\x01",
            "I see.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0x101,
        (
            "#506FHeh heh... What can I say?\x01",
            "We were worried.\x02\x03",

            "#006FSo, what are you working on?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0x8,
        (
            "#104FWell, as you can see, I'm trying\x01",
            "to cut into the Black Orbment...\x02\x03",

            "...but it hasn't been\x01",
            "going very well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0x102,
        "#014FWhat seems to be the problem?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0x8,
        (
            "#102FPerhaps a demonstration is in\x01",
            "order...\x02\x03",

            "...aaaaand CLICK.\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0x9C, 0x0, 0x64)
    Sleep(400)
    OP_22(0xE0, 0x0, 0x64)
    OP_71(0x1, 0x20)
    OP_71(0x2, 0x20)
    OP_70(0x1, 0x3)
    OP_70(0x2, 0x3)
    Sleep(1000)
    OP_62(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    ChrTalk(    #91
        0x101,
        (
            "#004FWhoa...\x01",
            "What's THAT thing?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0x9,
        (
            "#062FIt's a circular saw.\x02\x03",

            "It's made of a special alloy\x01",
            "that can cut through basically\x01",
            "anything...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0x101,
        "#501FThat outta do it, then.\x02",
    )

    CloseMessageWindow()
    OP_72(0x1, 0x20)
    OP_72(0x2, 0x20)
    OP_6F(0x1, 3)
    OP_6F(0x2, 3)
    OP_70(0x1, 0x25)
    OP_70(0x2, 0x25)
    OP_73(0x1)
    OP_71(0x1, 0x20)
    OP_71(0x2, 0x20)
    OP_6F(0x1, 34)
    OP_6F(0x2, 34)
    OP_70(0x1, 0x25)
    OP_70(0x2, 0x25)
    OP_22(0xC7, 0x0, 0x64)
    LoadEffect(0x0, "map\\\\mp007_00.eff")
    PlayEffect(0x0, 0x0, 0xE, 0, 300, 0, 0, 0, 0, 300, 300, 300, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    OP_72(0x1, 0x20)
    OP_72(0x2, 0x20)
    OP_23(0xE0)
    OP_23(0xC7)
    OP_22(0x9A, 0x0, 0x64)
    OP_7C(0x0, 0x64, 0xBB8, 0x64)
    OP_73(0x1)
    Sleep(500)
    OP_82(0x0, 0x2)
    Sleep(500)

    ChrTalk(    #94
        0x101,
        "#004FUh...it stopped...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0x9,
        "#561FI thought that might happen...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #96
        0x102,
        (
            "#012FIt's on a smaller scale, but\x01",
            "it's the same phenomenon\x01",
            "as yesterday.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0x8,
        (
            "#102FIt seems like the Black Orbment is blocking\x01",
            "the functionality of the other orbments.\x01",
            "Interfering with them, in some way.\x02\x03",

            "And I doubt it was solely made\x01",
            "for the purpose of killing the lights.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0x101,
        "#002FYeah...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0x9,
        (
            "#064FBut, Grandpa...\x02\x03",

            "Doesn't the effect spread \x01",
            "like it did last night?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0x8,
        (
            "#101FYes, good thinking.\x02\x03",

            "This interference with nearby orbments \x01",
            "seems to spread out, moving from orbment\x01",
            "to orbment, like chain lightning.\x02\x03",

            "#100FI'd put the range at about five arge.\x02\x03",

            "But if there are no orbments powered\x01",
            "on within that range...well, then\x01",
            "that's where the effect stops.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0x102,
        (
            "#014FI see...\x01",
            "That makes sense.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0x8,
        (
            "#104FHowever, even with that knowledge, there's no\x01",
            "way to know why it causes machines to simply\x01",
            "stop without getting a look inside it.\x02\x03",

            "It's very troubling.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0x101,
        (
            "#006FIs there any way to\x01",
            "destroy the thing?\x02\x03",

            "Maybe with a good scream\x01",
            "and a really hard whack?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0x102,
        (
            "#018FDon't be ridiculous.\x02\x03",

            "Didn't you see the big saw do\x01",
            "exactly nothing to it just a\x01",
            "moment ago?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0x101,
        (
            "#505FWell, yeah...\x02\x03",

            "#006FAnyone thought of trying fire?\x02\x03",

            "Maybe it'd melt down in a\x01",
            "blast furnace or something.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #106
        0x9,
        (
            "#065FIf we did that, the insides\x01",
            "of it would melt, too...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0x101,
        (
            "#007FOh, yeah.\x01",
            "Well, it was worth a shot.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #108
        0x8,
        (
            "#103F...\x02\x03",

            "Actually, it might work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #109
        0x101,
        "#004FReally?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #110
        0x102,
        (
            "#014FYou know of a way to burn\x01",
            "it open?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0x8,
        (
            "#102FNo, that's not what I meant.\x02\x03",

            "Orbal power...that which drives\x01",
            "orbments to work...can't be used\x01",
            "for this problem.\x02\x03",

            "We'll have to find a way that\x01",
            "doesn't rely on any orbal energy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #112
        0x101,
        "#505FHmmm...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0x102,
        "#010FIs there even such a thing?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #114
        0x8,
        (
            "#104FThe Combustion Engine...\x02\x03",

            "It's a device that burns\x01",
            "fuel to generate energy.\x02\x03",

            "The idea's been around for a long\x01",
            "time, but it's very inefficient\x01",
            "when compared to an orbal engine.\x02\x03",

            "#100FHowever, all you need to work\x01",
            "on them are standard tools.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0x101,
        "#004FHuh...neat.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #116
        0x102,
        (
            "#019FI get it...\x01",
            "Fire is the key.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #117
        0x9,
        (
            "#064FBut, Grandpa...\x02\x03",

            "I've never even seen one of them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #118
        0x8,
        (
            "#100FI'm pretty certain that there's\x01",
            "one under study in the central\x01",
            "factory workshop.\x02\x03",

            "#103FOh, you'll need to get fuel,\x01",
            "as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #119
        0x101,
        "#000FLike oil or something?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #120
        0x8,
        (
            "#100FNo, it's called gasoline.\x01",
            "It's extremely flammable.\x02\x03",

            "There's likely a tank or canister \x01",
            "of it stored in reserve.\x02\x03",

            "Hmm...\x01",
            "Yes, it should do the job.\x02\x03",

            "#101FI'll start getting the tools ready!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #121
        0x9,
        "#560FI'll help...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #122
        0x101,
        (
            "#006FIs there anything we can do?\x02\x03",

            "I mean, I can't do anything super-\x01",
            "technical like Tita can...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #123
        0x8,
        (
            "#100FWell, you could go and get\x01",
            "the engine and gasoline.\x02\x03",

            "It's going to be heavy, but\x01",
            "you bracers should be strong\x01",
            "enough to move it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #124
        0x101,
        "#006FOkay! Leave it to us!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #125
        0x102,
        (
            "#010FSo...\x02\x03",

            "Where would we find these?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #126
        0x8,
        (
            "#103FHmm?\x02\x03",

            "...\x02\x03",

            "Let's see...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #127
        0x102,
        "#014FDon't tell me that you've forgotten...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #128
        0x8,
        "#104FI've forgotten.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #129
        0x101,
        "#509FHe just said not to say that!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x101, 400)

    ChrTalk(    #130
        0x9,
        (
            "#560F#2PU-Umm...Estelle?\x02\x03",

            "If you look in the Operations room,\x01",
            "you could probably find them.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x9, 400)
    TurnDirection(0x101, 0x9, 400)

    ChrTalk(    #131
        0x101,
        (
            "#505FWhat the heck is an\x01",
            "'Operations' room?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #132
        0x9,
        (
            "#060F#2PIt's a room with a bunch of orbal\x01",
            "computers. It's on the fifth floor. \x02\x03",

            "We store all kinds of information\x01",
            "there for safekeeping.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #133
        0x102,
        (
            "#014FWow... I didn't even know\x01",
            "there was such a place.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #134
        0x8,
        (
            "#101FThen I leave it in your\x01",
            "capable hands.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #135
        0x101,
        (
            "#007F*sigh* Making coffee, fetching stuff...\x01",
            "Well played, old man. Well played.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(    #136
        0x101,
        (
            "#006FOh, well. Let's go find this\x01",
            "Operations room thingy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #137
        0x102,
        "#010FTo the 5th floor, then.\x02",
    )

    CloseMessageWindow()
    OP_28(0x3F, 0x1, 0x80)
    OP_28(0x3F, 0x1, 0x100)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x101, -410, 0, 8910, 180)
    SetChrPos(0x102, -410, 0, 8910, 180)
    SetChrPos(0x9, -100, 0, 12700, 180)
    SetChrPos(0x8, -2310, 0, 14200, 0)
    OP_4B(0x8, 255)
    OP_43(0x9, 0x0, 0x0, 0x2)
    OP_6F(0x1, 0)
    OP_6F(0x2, 0)
    OP_69(0x101, 0x0)
    Sleep(500)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    Return()

    # Function_10_1B10 end

    def Function_11_2E1F(): pass

    label("Function_11_2E1F")

    AddParty(0x6, 0xFF)
    EventBegin(0x0)
    OP_6D(600, 0, 11100, 0)
    ClearChrFlags(0x8, 0x80)
    OP_4A(0x8, 255)
    OP_4A(0xA, 255)
    SetChrFlags(0x9, 0x80)
    SetChrPos(0x8, 400, 0, 10200, 270)
    SetChrPos(0x107, -630, 0, 10390, 90)
    SetChrPos(0x101, 640, 0, 800, 0)
    SetChrPos(0x102, -430, 0, 800, 0)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(    #138
        0x101,
        "We're back...\x02",
    )

    CloseMessageWindow()

    def lambda_2EAE():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_2EAE)

    def lambda_2EBC():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_2EBC)

    def lambda_2ECA():
        OP_8E(0xFE, 0x280, 0x0, 0x230A, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2ECA)
    Sleep(500)
    OP_8E(0x102, 0xFFFFFE52, 0x0, 0x2224, 0xBB8, 0x0)

    ChrTalk(    #139
        0x102,
        (
            "#010FAnd we've brought what\x01",
            "you asked for.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #140
        0x8,
        "#103F#6PExcellent.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #141
        0x107,
        "#560FThank you...\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #142
        "\x07\x00Handed over \x07\x02Combustion Engine\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #143
        "\x07\x00Handed over \x07\x02Gasoline Tank\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_3F(0x367, 1)
    OP_3F(0x368, 1)

    ChrTalk(    #144
        0x101,
        (
            "#007FYou weren't kidding about\x01",
            "how heavy this thing is.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #145
        0x8,
        (
            "#101F#6PYes, your brute strength\x01",
            "was most useful, girl!\x02\x03",

            "#100FPerfect timing, too, as I've\x01",
            "just finished preparing the\x01",
            "tools.\x02\x03",

            "All that's left is to set up the\x01",
            "engine and put gas in it.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x107, 400)

    ChrTalk(    #146
        0x8,
        (
            "#100FIf you'll go and put on the\x01",
            "finishing touches, Tita...?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x107, 0x8, 400)

    ChrTalk(    #147
        0x107,
        "#061FYes, sir!\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(500)
    OP_6D(-1390, 0, 11640, 0)
    SetChrPos(0x101, -2690, 0, 9810, 0)
    SetChrPos(0x102, -1580, 0, 9760, 0)
    SetChrPos(0x107, -3220, 0, 11360, 90)
    SetChrPos(0x8, -2350, 0, 13080, 180)
    OP_72(0x0, 0x4)
    FadeToBright(1500, 0)
    OP_0D()

    ChrTalk(    #148
        0x8,
        "#101FAnd it's all set!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #149
        0x101,
        (
            "#501F#2PWow... This thing is really\x01",
            "clunky-looking.\x02\x03",

            "Are all of these engines\x01",
            "like this?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #150
        0x107,
        (
            "#060FYeah...\x02\x03",

            "It converts the energy given\x01",
            "by the burning gas to power\x01",
            "the tools.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #151
        0x102,
        (
            "#010FSo this way, they don't\x01",
            "need orbal energy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #152
        0x8,
        (
            "#104FIndeed. Now let's not dawdle...\x01",
            "Let me flip the switch.\x02",
        )
    )

    CloseMessageWindow()
    OP_43(0x8, 0x1, 0x0, 0xC)
    OP_43(0x102, 0x1, 0x0, 0xD)
    OP_43(0x101, 0x1, 0x0, 0xE)
    OP_43(0x107, 0x1, 0x0, 0xF)
    OP_6D(1050, 0, 11840, 2000)
    WaitChrThread(0x107, 0x1)

    ChrTalk(    #153
        0x8,
        "#102F...aaaaand CLICK.\x02",
    )

    CloseMessageWindow()
    OP_22(0x9C, 0x0, 0x64)
    Sleep(400)
    OP_22(0x9F, 0x1, 0x64)

    def lambda_3375():

        label("loc_3375")

        OP_7C(0x0, 0xA, 0xBB8, 0x64)
        OP_48()
        Jump("loc_3375")

    QueueWorkItem2(0x101, 3, lambda_3375)
    OP_71(0x1, 0x20)
    OP_71(0x2, 0x20)
    OP_70(0x1, 0x3)
    OP_70(0x2, 0x3)
    Sleep(500)
    OP_8C(0x8, 180, 400)
    Sleep(500)

    ChrTalk(    #154
        0x101,
        (
            "#004FGeez. This thing sure makes\x01",
            "a racket.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #155
        0x102,
        (
            "#010FIt's definitely a lot louder than\x01",
            "orbal engines.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #156
        0x8,
        (
            "#102FThat's one of its drawbacks,\x01",
            "yes.\x02\x03",

            "But I doubt we need to\x01",
            "fear activating the Black\x01",
            "Orbment this way.\x02\x03",

            "Let's get started.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #157
        0x101,
        "#002F*gulp*\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #158
        0x107,
        "#560F#2POooo...\x02",
    )

    CloseMessageWindow()
    OP_72(0x1, 0x20)
    OP_72(0x2, 0x20)
    OP_6F(0x1, 3)
    OP_6F(0x2, 3)
    OP_70(0x1, 0x2D)
    OP_70(0x2, 0x2D)
    OP_73(0x1)
    OP_71(0x1, 0x20)
    OP_71(0x2, 0x20)
    OP_6F(0x1, 42)
    OP_6F(0x2, 42)
    OP_70(0x1, 0x2D)
    OP_70(0x2, 0x2D)
    OP_22(0xC7, 0x1, 0x64)
    LoadEffect(0x0, "map\\\\mp010_00.eff")
    PlayEffect(0x0, 0x0, 0xFF, -100, 1200, 11450, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    ChrTalk(    #159
        0x101,
        "#004FWhoa!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #160
        0x102,
        "#012FThat's some serious sparkage...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #161
        0x8,
        (
            "#102FOkay, shut it down for now.\x02\x03",

            "We've seen how much physical punishment\x01",
            "it can take...and how much punishment our\x01",
            "ears can take, as well!\x02",
        )
    )

    CloseMessageWindow()
    OP_72(0x1, 0x20)
    OP_72(0x2, 0x20)
    OP_82(0x0, 0x2)
    OP_23(0xC7)
    OP_44(0x101, 0x3)
    OP_22(0x9A, 0x0, 0x64)
    OP_23(0x9F)
    OP_7C(0x0, 0x64, 0xBB8, 0x64)
    OP_6F(0x1, 362)
    OP_6F(0x2, 362)
    OP_70(0x1, 0x16D)
    OP_70(0x2, 0x16D)
    OP_73(0x1)
    Sleep(1000)
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #162
        "\x07\x05Estelle and the others crowded around to get a closer look.\x02",
    )

    CloseMessageWindow()

    AnonymousTalk(    #163
        "\x07\x05A tiny scratch is faintly visible.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    ChrTalk(    #164
        0x101,
        "#505FThat's... That's IT?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #165
        0x107,
        (
            "#065F#2PThat's incredible...and with\x01",
            "the special alloy saw, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #166
        0x102,
        (
            "#012FWhatever it's made of, it's\x01",
            "tougher than anything I've\x01",
            "ever seen.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #167
        0x8,
        (
            "#101FBut if we keep at it, I\x01",
            "believe this would work.\x02\x03",

            "We're going to go through quite\x01",
            "a few saw blades, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #168
        0x101,
        (
            "#006FSo it's going to be a real\x01",
            "test of patience, then.\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, -800, 0, 800, 0)

    ChrTalk(    #169
        0xA,
        (
            "#1PHey, Professor, can I talk\x01",
            "to you for a second?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_38B7():
        TurnDirection(0xFE, 0xA, 400)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_38B7)

    def lambda_38C5():
        TurnDirection(0xFE, 0xA, 400)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_38C5)

    def lambda_38D3():
        TurnDirection(0xFE, 0xA, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_38D3)

    def lambda_38E1():
        TurnDirection(0xFE, 0xA, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_38E1)
    OP_8E(0xA, 0xFFFFFF6A, 0x0, 0x1F40, 0xBB8, 0x0)

    ChrTalk(    #170
        0xA,
        (
            "#801FOh, have you already finished\x01",
            "the modifications?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #171
        0x8,
        (
            "#104FOf course I have. Remember\x01",
            "who you're talking to.\x02\x03",

            "#100FAnyway, what is it?\x01",
            "Is something wrong?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #172
        0xA,
        (
            "#800FI just received a message from the hotel in\x01",
            "Elmo for you.\x02\x03",

            "The orbal-powered pump that\x01",
            "supplies the hot water for\x01",
            "their spa has broken down.\x02\x03",

            "Since they can't make any money\x01",
            "like this, they'd like for you\x01",
            "to come and try to fix it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #173
        0x8,
        (
            "#102FAgh, you must be kidding!\x02\x03",

            "Damn it! Of all the times\x01",
            "for this to happen...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #174
        0xA,
        (
            "#805FIf you're that busy, why don't\x01",
            "you send another engineer over?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #175
        0x8,
        (
            "#100FNo... That pile of junk is\x01",
            "at least forty years old.\x02\x03",

            "The younger techs have no idea\x01",
            "what to do with anything that's\x01",
            "not state-of-the-art.\x02\x03",

            "#104F*grumble*\x01",
            "What a pain in the--\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x107, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1200)
    OP_63(0x107)
    TurnDirection(0x107, 0x8, 400)

    ChrTalk(    #176
        0x107,
        (
            "#560F#2PGrandpa...\x02\x03",

            "Maybe I could go over and do\x01",
            "the repairs, you think...?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3C64():
        TurnDirection(0xFE, 0x107, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3C64)

    def lambda_3C72():
        TurnDirection(0xFE, 0x107, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3C72)
    TurnDirection(0x8, 0x107, 400)

    ChrTalk(    #177
        0x8,
        "#103FHmm?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #178
        0xA,
        "#802FTita?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #179
        0x107,
        (
            "#060F#2PYou took me there to help\x01",
            "with maintenance before.\x02\x03",

            "I think it'll be fine if just I go.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #180
        0x8,
        (
            "#100FMm. I'm sure you'd do a\x01",
            "fine job on the repairs...\x02\x03",

            "That's not what concerns me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #181
        0xA,
        (
            "#803FAgreed. There are monsters\x01",
            "out on the roads...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #182
        0x107,
        (
            "#063F#2PBut we can't just leave \x01",
            "Mrs. Mao like this.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3DD9():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3DD9)
    TurnDirection(0x101, 0x102, 400)
    OP_62(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_62(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1200)
    OP_63(0x101)
    OP_63(0x102)

    def lambda_3E1D():
        TurnDirection(0xFE, 0x107, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3E1D)
    TurnDirection(0x101, 0x107, 400)

    ChrTalk(    #183
        0x101,
        (
            "#006F#2PIf that's the problem, why \x01",
            "don't you let us handle this?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x107, 0x101, 400)

    ChrTalk(    #184
        0x107,
        "#064FHuh...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #185
        0x102,
        (
            "#010F#4PIt's a bracer's duty to ensure\x01",
            "the safety of Liberl's roadways.\x02\x03",

            "Therefore, seeing that Tita arrives\x01",
            "at her destination safely is\x01",
            "our responsibility.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #186
        0xA,
        (
            "#801FWell, that's another story. If\x01",
            "you're all with her, then we\x01",
            "don't need to worry.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #187
        0x8,
        (
            "#100FHm. All right, then.\x01",
            "Thank you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #188
        0x107,
        (
            "#065FUmm...\x01",
            "Are you sure this is okay?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #189
        0x101,
        (
            "#006F#2PDon't worry about it. Kids shouldn't\x01",
            "sweat the details so much.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #190
        0x102,
        "#019F#4PIf you're ready, then let's go.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #191
        0x107,
        (
            "#067FTh-Thank you...\x01",
            "Thank you both.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x107, 0x8, 400)
    Sleep(200)
    TurnDirection(0x107, 0xA, 400)
    Sleep(500)

    ChrTalk(    #192
        0x107,
        (
            "#560FOkay, Grandpa...and Mr. Murdock.\x02\x03",

            "We'll be back soon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #193
        0x8,
        "#101FTake care, dear.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #194
        0xA,
        "#801FBe careful out there.\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6D(-100, 0, 6770, 0)
    SetChrPos(0x101, -100, 0, 6770, 180)
    SetChrPos(0x102, -100, 0, 6770, 180)
    SetChrPos(0x107, -100, 0, 6770, 180)
    SetChrPos(0x8, 0, 0, 12740, 180)
    SetChrPos(0xA, -130, 0, 10450, 0)
    OP_4B(0x8, 255)
    OP_4B(0xA, 255)
    OP_6F(0x1, 0)
    OP_6F(0x2, 0)
    Sleep(500)
    FadeToBright(1000, 0)
    ClearMapFlags(0x10000000)
    OP_A2(0x51A)
    OP_28(0x3F, 0x4, 0x10)
    OP_28(0x3F, 0x4, 0x20)
    OP_28(0x40, 0x4, 0x2)
    OP_28(0x40, 0x4, 0x4)
    EventEnd(0x0)
    Return()

    # Function_11_2E1F end

    def Function_12_41CB(): pass

    label("Function_12_41CB")

    SetChrFlags(0xFE, 0x4)
    OP_8E(0xFE, 0xFFFFF876, 0x0, 0x348A, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFFFEF2, 0x0, 0x3674, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFFFF9C, 0x0, 0x319C, 0x7D0, 0x0)
    ClearChrFlags(0xFE, 0x4)
    OP_8C(0xFE, 90, 400)
    Return()

    # Function_12_41CB end

    def Function_13_4219(): pass

    label("Function_13_4219")

    Sleep(400)
    SetChrFlags(0xFE, 0x4)
    OP_8E(0xFE, 0x474, 0x0, 0x2774, 0x7D0, 0x0)
    ClearChrFlags(0xFE, 0x4)
    OP_8C(0xFE, 315, 400)
    Return()

    # Function_13_4219 end

    def Function_14_4244(): pass

    label("Function_14_4244")

    Sleep(800)
    SetChrFlags(0xFE, 0x4)
    OP_8E(0xFE, 0x78, 0x0, 0x26DE, 0x7D0, 0x0)
    ClearChrFlags(0xFE, 0x4)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_14_4244 end

    def Function_15_426F(): pass

    label("Function_15_426F")

    Sleep(1200)
    SetChrFlags(0xFE, 0x4)
    OP_8E(0xFE, 0xFFFFF448, 0x0, 0x268E, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFFFD1C, 0x0, 0x27E2, 0x7D0, 0x0)
    ClearChrFlags(0xFE, 0x4)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_15_426F end

    def Function_16_42AE(): pass

    label("Function_16_42AE")

    EventBegin(0x0)
    OP_6D(-180, 0, 2620, 0)
    SetMapFlags(0x40000000)
    AddParty(0x5, 0xFF)
    OP_31(0x5, 0x0, 0x1A)
    OP_B5(0x5, 0x0)
    OP_B5(0x5, 0x1)
    OP_B5(0x5, 0x2)
    OP_B5(0x5, 0x3)
    OP_41(0x5, 0x9B)
    OP_41(0x5, 0xF5)
    OP_41(0x5, 0x113)
    OP_41(0x5, 0x25F, 0x0)
    OP_41(0x5, 0x259, 0x1)
    OP_41(0x5, 0x262, 0x2)
    OP_35(0x5, 0xC8)
    OP_35(0x5, 0xC9)
    OP_35(0x5, 0xCA)
    OP_36(0x5, 0xFF)
    OP_36(0x5, 0x100)
    SetChrFlags(0x106, 0x80)
    SetChrPos(0x107, -850, 0, 2040, 0)
    SetChrPos(0x101, -1590, 0, 900, 0)
    SetChrPos(0x102, -260, 0, 1060, 0)
    OP_22(0x9F, 0x1, 0x64)

    def lambda_4350():

        label("loc_4350")

        OP_7C(0x0, 0xA, 0xBB8, 0x64)
        OP_48()
        Jump("loc_4350")

    QueueWorkItem2(0x101, 3, lambda_4350)
    OP_71(0x1, 0x20)
    OP_71(0x2, 0x20)
    OP_6F(0x1, 42)
    OP_6F(0x2, 42)
    OP_70(0x1, 0x2D)
    OP_70(0x2, 0x2D)
    FadeToBright(2000, 0)
    OP_0D()

    ChrTalk(    #195
        0x107,
        (
            "#062FGrandpa! We've got a big--\x02\x03",

            "#064FEr...\x02",
        )
    )

    CloseMessageWindow()
    OP_6D(1770, 0, 12830, 2000)

    def lambda_43DD():
        OP_8E(0xFE, 0x140, 0x0, 0x259E, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_43DD)

    def lambda_43F8():
        OP_8E(0xFE, 0xFFFFFCAE, 0x0, 0x21F2, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_43F8)

    def lambda_4413():
        OP_8E(0xFE, 0x3B6, 0x0, 0x2170, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_4413)
    WaitChrThread(0x101, 0x1)

    ChrTalk(    #196
        0x101,
        (
            "#004FThere's no one here...\x02\x03",

            "So why is the machine still on?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #197
        0x107,
        "#065FW-We should turn it off...\x02",
    )

    CloseMessageWindow()

    def lambda_449A():

        label("loc_449A")

        TurnDirection(0xFE, 0x107, 400)
        OP_48()
        Jump("loc_449A")

    QueueWorkItem2(0x101, 1, lambda_449A)

    def lambda_44AB():

        label("loc_44AB")

        TurnDirection(0xFE, 0x107, 400)
        OP_48()
        Jump("loc_44AB")

    QueueWorkItem2(0x102, 1, lambda_44AB)
    SetChrFlags(0x107, 0x4)
    OP_8E(0x107, 0x97E, 0x0, 0x271A, 0xFA0, 0x0)
    OP_8E(0x107, 0xA3C, 0x0, 0x326E, 0xFA0, 0x0)
    OP_8E(0x107, 0x50, 0x0, 0x350C, 0xFA0, 0x0)
    OP_8E(0x107, 0x8C, 0x0, 0x3200, 0xFA0, 0x0)
    OP_8C(0x107, 90, 400)
    Sleep(500)
    OP_72(0x1, 0x20)
    OP_72(0x2, 0x20)
    OP_23(0x9F)
    OP_44(0x101, 0x3)
    OP_22(0x9A, 0x0, 0x64)
    OP_7C(0x0, 0x64, 0xBB8, 0x64)
    OP_6F(0x1, 362)
    OP_6F(0x2, 362)
    OP_70(0x1, 0x16D)
    OP_70(0x2, 0x16D)
    OP_73(0x1)
    Sleep(1500)

    ChrTalk(    #198
        0x107,
        (
            "#561FWhew...\x02\x03",

            "#063FWhere could Grandpa\x01",
            "have gone...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #199
        0x102,
        (
            "#013FIt's not just him...\x01",
            "The Black Orbment is gone, too.\x02\x03",

            "You don't suppose...\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x106, -790, 0, 2500, 0)
    ClearChrFlags(0x106, 0x80)

    ChrTalk(    #200
        0x106,
        "#1PHeh. So here you are.\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_465E():
        TurnDirection(0xFE, 0x106, 400)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_465E)

    def lambda_466C():
        TurnDirection(0xFE, 0x106, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_466C)

    def lambda_467A():
        TurnDirection(0xFE, 0x106, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_467A)
    OP_6D(990, 0, 7840, 1000)

    ChrTalk(    #201
        0x101,
        "#004FAgate?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #202
        0x102,
        "#014FWhat are you doing here?\x02",
    )

    CloseMessageWindow()

    def lambda_46CE():

        label("loc_46CE")

        TurnDirection(0xFE, 0x106, 400)
        OP_48()
        Jump("loc_46CE")

    QueueWorkItem2(0x101, 1, lambda_46CE)

    def lambda_46DF():

        label("loc_46DF")

        TurnDirection(0xFE, 0x106, 400)
        OP_48()
        Jump("loc_46DF")

    QueueWorkItem2(0x102, 1, lambda_46DF)
    OP_8E(0x106, 0xFFFFFF2E, 0x0, 0x1B1C, 0xBB8, 0x0)
    OP_43(0x107, 0x2, 0x0, 0x11)

    ChrTalk(    #203
        0x106,
        (
            "#552FI should be asking you the\x01",
            "same thing.\x02\x03",

            "I heard about the disturbance here, so I came\x01",
            "to check it out. Lo and behold, you got here\x01",
            "before me. Will wonders never cease?\x02\x03",

            "You incompetents keep sticking your\x01",
            "noses where they don't belong, someone's\x01",
            "gonna come and cut them off.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #204
        0x101,
        (
            "#509FGrrrr...\x01",
            "Are you ever NOT a jerk?!\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x107, 0x2)
    TurnDirection(0x107, 0x106, 400)

    ChrTalk(    #205
        0x107,
        (
            "#064FUmm...\x01",
            "I guess you know him?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #206
        0x102,
        (
            "#010FHis name is Agate.\x01",
            "He's a senior bracer.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x106, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    TurnDirection(0x106, 0x107, 400)

    ChrTalk(    #207
        0x106,
        (
            "#052FHey, hold on a second.\x02\x03",

            "#057FWhat's a kid doing here?\x02",
        )
    )

    CloseMessageWindow()
    OP_8E(0x106, 0x55A, 0x0, 0x1D38, 0xBB8, 0x0)
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #208
        "\x07\x05Agate glared at Tita.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_62(0x107, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)

    ChrTalk(    #209
        0x107,
        "#065FEep...\x02",
    )

    OP_9E(0x107, 0xF, 0x0, 0x3E8, 0xBB8)
    CloseMessageWindow()
    OP_44(0x101, 0xFF)
    OP_8E(0x101, 0x186, 0x0, 0x1DF6, 0xBB8, 0x0)
    TurnDirection(0x101, 0x106, 0)

    ChrTalk(    #210
        0x101,
        (
            "#009FHey! She hasn't done anything,\x01",
            "so lay off!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #211
        0x106,
        (
            "#057F...\x02\x03",

            "#552FBah.\x02\x03",

            "So damn much I could say, but\x01",
            "I'll hold off...for now.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x106, 0x101, 400)

    ChrTalk(    #212
        0x106,
        "#050FSo what the hell's going on?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #213
        0x102,
        "#012FHere's the situation...\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #214
        "\x07\x05Joshua explained to Agate how Professor Russell had gone missing.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    ChrTalk(    #215
        0x106,
        (
            "#053FSmoke canisters, huh?\x01",
            "Certainly explains the\x01",
            "stench around here.\x02\x03",

            "#054FWe ain't got time to waste,\x01",
            "though. We've gotta find\x01",
            "the professor, and fast!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #216
        0x101,
        "#005FRight!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #217
        0x102,
        "#012FAcknowledged.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #218
        0x107,
        "#063FGrandpa...\x02",
    )

    CloseMessageWindow()
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_28(0x41, 0x1, 0x4)
    EventEnd(0x0)
    Return()

    # Function_16_42AE end

    def Function_17_4BD1(): pass

    label("Function_17_4BD1")

    OP_8E(0x107, 0x50, 0x0, 0x350C, 0xBB8, 0x0)
    OP_8E(0x107, 0x33E, 0x0, 0x3692, 0xBB8, 0x0)
    OP_8E(0x107, 0xA3C, 0x0, 0x326E, 0xBB8, 0x0)
    OP_8E(0x107, 0x8D4, 0x0, 0x1E14, 0xBB8, 0x0)
    TurnDirection(0x107, 0x101, 400)
    Return()

    # Function_17_4BD1 end

    SaveToFile()

Try(main)

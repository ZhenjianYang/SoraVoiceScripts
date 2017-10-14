from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 蔡斯

    CreateScenaFile(
        FileName            = 'C3100   ._SN',
        MapName             = 'Zeiss',
        Location            = 'C3100.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60016",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            '',
            'ED6_DT21/C3100_1 ._SN',
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
        'Kanone',                               # 9
        'Private Samuel',                       # 10
        'Cassius',                              # 11
        'Lt. Col. Cid',                         # 12
        'Measuring Instrument',                 # 13
        'Warrant Officer Belc',                 # 14
        'Soldier',                              # 15
        'Soldier',                              # 16
        'Soldier',                              # 17
        'Soldier',                              # 18
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
        'ED6_DT27/CH03125 ._CH',             # 00
        'ED6_DT27/CH03120 ._CH',             # 01
        'ED6_DT07/CH01640 ._CH',             # 02
        'ED6_DT27/CH03670 ._CH',             # 03
        'ED6_DT27/CH03590 ._CH',             # 04
        'ED6_DT06/CH20020 ._CH',             # 05
        'ED6_DT07/CH00065 ._CH',             # 06
        'ED6_DT07/CH01310 ._CH',             # 07
    )

    AddCharChipPat(
        'ED6_DT27/CH03125P._CP',             # 00
        'ED6_DT27/CH03120P._CP',             # 01
        'ED6_DT07/CH01640P._CP',             # 02
        'ED6_DT27/CH03670P._CP',             # 03
        'ED6_DT27/CH03590P._CP',             # 04
        'ED6_DT06/CH20020P._CP',             # 05
        'ED6_DT07/CH00065P._CP',             # 06
        'ED6_DT07/CH01310P._CP',             # 07
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = -3230,
        Direction           = 174,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
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
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
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
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
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
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
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
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
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
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
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
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclEvent(
        X                   = -4990,
        Y                   = 0,
        Z                   = -35710,
        Range               = 5060,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0xFFFF7D1A,
        Unknown_18          = 0x0,
        Unknown_1C          = 6,
    )


    DeclActor(
        TriggerX            = 5460,
        TriggerZ            = -60,
        TriggerY            = -46490,
        TriggerRange        = 2000,
        ActorX              = 5460,
        ActorZ              = -60,
        ActorY              = -46490,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 7,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 6000,
        TriggerZ            = 0,
        TriggerY            = -45540,
        TriggerRange        = 1500,
        ActorX              = 6000,
        ActorZ              = 1500,
        ActorY              = -45540,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 21,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 31750,
        TriggerZ            = -30,
        TriggerY            = -32759,
        TriggerRange        = 1000,
        ActorX              = 32009,
        ActorZ              = -1030,
        ActorY              = -29320,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 22,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_2B6",          # 00, 0
        "Function_1_32E",          # 01, 1
        "Function_2_386",          # 02, 2
        "Function_3_42D",          # 03, 3
        "Function_4_1402",         # 04, 4
        "Function_5_1CC8",         # 05, 5
        "Function_6_2124",         # 06, 6
        "Function_7_2700",         # 07, 7
        "Function_8_28CF",         # 08, 8
        "Function_9_5C39",         # 09, 9
        "Function_10_5C55",        # 0A, 10
        "Function_11_5C71",        # 0B, 11
        "Function_12_5C8D",        # 0C, 12
        "Function_13_5CA9",        # 0D, 13
        "Function_14_5F80",        # 0E, 14
        "Function_15_600F",        # 0F, 15
        "Function_16_6848",        # 10, 16
        "Function_17_6AB9",        # 11, 17
        "Function_18_722C",        # 12, 18
        "Function_19_72C4",        # 13, 19
        "Function_20_732A",        # 14, 20
        "Function_21_7383",        # 15, 21
        "Function_22_73E9",        # 16, 22
    )


    def Function_0_2B6(): pass

    label("Function_0_2B6")

    ClearChrFlags(0x9, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_2DA")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x51), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x10F0)
    SetMapFlags(0x10000000)
    Event(0, 13)
    Jump("loc_32D")

    label("loc_2DA")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x283, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2FB")
    SetMapFlags(0x10000000)
    Event(0, 4)
    Jump("loc_32D")

    label("loc_2FB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 1)), scpexpr(EXPR_END)), "loc_311")
    OP_A3(0x10F1)
    SetMapFlags(0x10000000)
    Event(1, 3)
    Jump("loc_32D")

    label("loc_311")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 2)), scpexpr(EXPR_END)), "loc_32D")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x74), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x10F2)
    SetMapFlags(0x10000000)
    Event(0, 14)

    label("loc_32D")

    Return()

    # Function_0_2B6 end

    def Function_1_32E(): pass

    label("Function_1_32E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_33C")
    OP_6F(0x0, 110)

    label("loc_33C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x283, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x283, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_34F")
    OP_65(0x0, 0x1)
    Jump("loc_353")

    label("loc_34F")

    OP_64(0x0, 0x1)

    label("loc_353")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x283, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_380")
    OP_72(0x2, 0x4)
    OP_72(0x3, 0x4)
    OP_72(0x4, 0x4)
    OP_72(0x5, 0x4)
    OP_22(0x9E, 0x1, 0x64)
    OP_24(0x9E, 0x4B)

    label("loc_380")

    OP_22(0x1CD, 0x1, 0x5A)
    Return()

    # Function_1_32E end

    def Function_2_386(): pass

    label("Function_2_386")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_END)),
        (0, "loc_3B7"),
        (1, "loc_3C3"),
        (2, "loc_3CF"),
        (3, "loc_3DB"),
        (4, "loc_3E7"),
        (5, "loc_3F3"),
        (6, "loc_3FF"),
        (SWITCH_DEFAULT, "loc_40B"),
    )


    label("loc_3B7")

    OP_99(0xFE, 0x0, 0x7, 0x5AA)
    Jump("loc_417")

    label("loc_3C3")

    OP_99(0xFE, 0x0, 0x7, 0x60E)
    Jump("loc_417")

    label("loc_3CF")

    OP_99(0xFE, 0x0, 0x7, 0x640)
    Jump("loc_417")

    label("loc_3DB")

    OP_99(0xFE, 0x0, 0x7, 0x578)
    Jump("loc_417")

    label("loc_3E7")

    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_417")

    label("loc_3F3")

    OP_99(0xFE, 0x0, 0x7, 0x546)
    Jump("loc_417")

    label("loc_3FF")

    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_417")

    label("loc_40B")

    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_417")

    label("loc_417")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_42C")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_417")

    label("loc_42C")

    Return()

    # Function_2_386 end

    def Function_3_42D(): pass

    label("Function_3_42D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_991")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x401, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_448")
    Call(0, 15)
    Jump("loc_98D")

    label("loc_448")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x402, 2)), scpexpr(EXPR_END)), "loc_607")
    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_573")

    ChrTalk(    #0
        0xFE,
        (
            "Communication with all stations has\x01",
            "been restored, and the Royal Army has\x01",
            "formed up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        (
            "Keeping order and the chain of command\x01",
            "solid is important. We need to put a stop to\x01",
            "this Orbal Shutdown Phenomenon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0xFE,
        (
            "Even General Bright is getting headaches\x01",
            "over the problem.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_601")

    label("loc_573")


    ChrTalk(    #3
        0xFE,
        (
            "Putting an end to the Orbal Shutdown\x01",
            "Phenomenon is our highest priority.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0xFE,
        (
            "Even General Bright is getting headaches\x01",
            "over the problem.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_601")

    TalkEnd(0x9)
    Jump("loc_98D")

    label("loc_607")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x401, 7)), scpexpr(EXPR_END)), "loc_8F7")
    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x401, 6)), scpexpr(EXPR_END)), "loc_81E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7A6")

    ChrTalk(    #5
        0xFE,
        (
            "Hey there. Did you find the engine you\x01",
            "wanted?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x101,
        "#1000FUh-huh! Sure did.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x102,
        (
            "#1040FThe men aboard the patrol ship were\x01",
            "unharmed, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0xFE,
        (
            "Excellent news! Thank you.\x01",
            "I'll be sure to pass that along.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0xFE,
        (
            "We should be able to get a rescue\x01",
            "squad out to pick them up soon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0xFE,
        "Good luck fixing the hot springs!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x101,
        "#1000FThanks for your help, sir!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x102,
        "#1040FExcuse us, then.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_81B")

    label("loc_7A6")


    ChrTalk(    #13
        0xFE,
        (
            "I'll be sure to report to headquarters\x01",
            "about the patrol ship and her crew.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0xFE,
        "Good luck with the hot springs.\x02",
    )

    CloseMessageWindow()

    label("loc_81B")

    Jump("loc_8F1")

    label("loc_81E")


    ChrTalk(    #15
        0xFE,
        (
            "General Bright is personally working\x01",
            "to reconstruct the Royal Army.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0xFE,
        (
            "The image of General Bright, giving orders\x01",
            "without a moment's rest, even in our darkest\x01",
            "hour... It's an inspiration for any soldier.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8F1")

    TalkEnd(0x9)
    Jump("loc_98D")

    label("loc_8F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x401, 6)), scpexpr(EXPR_END)), "loc_989")
    TalkBegin(0x9)

    ChrTalk(    #17
        0xFE,
        (
            "The patrol ship should've touched down\x01",
            "somewhere in the Tratt Plains.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0xFE,
        (
            "Go there to find out about the\x01",
            "combustion engine.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x9)
    Jump("loc_98D")

    label("loc_989")

    Call(0, 16)

    label("loc_98D")

    Return()

    label("loc_991")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x283, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x283, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9A2")
    Call(0, 5)
    Return()

    label("loc_9A2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x6D, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x6D, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x6D, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9D4")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x6D, 0x0, 0x4)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9CF")
    Call(1, 0)
    Return()

    label("loc_9CF")

    Call(1, 1)
    Return()

    label("loc_9D4")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_END)), "loc_BAB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_ABE")

    ChrTalk(    #19
        0x9,
        (
            "I suspect most of the actual patrolling\x01",
            "will be handled by the garrison here at\x01",
            "the fortress.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x9,
        (
            "Our charge is protecting the backbone\x01",
            "of the Royal Army. It's only natural we'd\x01",
            "shoulder such responsibility.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BA8")

    label("loc_ABE")


    ChrTalk(    #21
        0x9,
        (
            "Colonel Cid will be departing for\x01",
            "Grancel soon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x9,
        (
            "He'll be overseeing security for the signing\x01",
            "ceremony of the non-aggression pact.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x9,
        (
            "Even with Erebonians in town, Colonel Cid\x01",
            "will make sure it goes off without a hitch.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_BA8")

    Jump("loc_13FE")

    label("loc_BAB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 0)), scpexpr(EXPR_END)), "loc_D43")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_C3E")

    ChrTalk(    #24
        0x9,
        (
            "Thanks to the standby order, we suffered\x01",
            "little damage.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x9,
        (
            "I don't mind telling you--the timing on\x01",
            "that order was perfect.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D40")

    label("loc_C3E")


    ChrTalk(    #26
        0x9,
        (
            "We're currently evaluating the damage\x01",
            "done to the fortress.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x9,
        (
            "That was a pretty powerful earthquake,\x01",
            "but I doubt Leiston suffered any real damage.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x9,
        (
            "We were specifically ordered to stand by\x01",
            "and prep for an earthquake, so we were\x01",
            "well prepared.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_D40")

    Jump("loc_13FE")

    label("loc_D43")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x283, 7)), scpexpr(EXPR_END)), "loc_E47")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_D90")

    ChrTalk(    #29
        0x9,
        "You...talked to the general?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x9,
        "Damn! I'm jealous...\x02",
    )

    CloseMessageWindow()
    Jump("loc_E44")

    label("loc_D90")


    ChrTalk(    #31
        0x9,
        "Wasn't... Wasn't that General Bright?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x9,
        "You... What did you talk to him about?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x9,
        (
            "I've served for years and even I've\x01",
            "never spoken to him...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x9,
        "Damn! I'm jealous...\x02",
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_E44")

    Jump("loc_13FE")

    label("loc_E47")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x283, 5)), scpexpr(EXPR_END)), "loc_F3C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_EB0")

    ChrTalk(    #35
        0x9,
        (
            "Please avoid placing your device on the\x01",
            "road. It would be problematic for traffic.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F39")

    label("loc_EB0")


    ChrTalk(    #36
        0x9,
        (
            "Please avoid placing your device on the\x01",
            "road. It would be problematic for traffic.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0x9,
        "You may place it anywhere else you like.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_F39")

    Jump("loc_13FE")

    label("loc_F3C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 3)), scpexpr(EXPR_END)), "loc_124F")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x6D, 0x0, 0x40)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x6D, 0x0, 0x4)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x6D, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x6D, 0x1, 0x8000)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10F7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1082")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_FF9")

    ChrTalk(    #38
        0x9,
        (
            "There are earthquakes occurring all\x01",
            "over the Zeiss region.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0x9,
        (
            "The troops here at Leiston are ready for\x01",
            "anything, however!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_107F")

    label("loc_FF9")


    ChrTalk(    #40
        0x9,
        (
            "There are earthquakes occurring all\x01",
            "over the Zeiss region.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0x9,
        (
            "We of the fortress guard have been\x01",
            "strengthening our patrols.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_107F")

    Jump("loc_10F4")

    label("loc_1082")


    ChrTalk(    #42
        0xFE,
        "Unfortunately, training's over already.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0xFE,
        (
            "We're too busy preparing for the\x01",
            "earthquakes to have much time.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_10F4")

    Jump("loc_124C")

    label("loc_10F7")


    ChrTalk(    #44
        0xFE,
        "You lot are certainly late.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0xFE,
        "Training's been over for a while now.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0x101,
        (
            "#1000FAww! Figures...\x02\x03",

            "I guess it's our fault. You did put down\x01",
            "that it was urgent.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0xFE,
        (
            "Yes, but truth be told, we barely\x01",
            "have time for training, what with our\x01",
            "earthquake preparations.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0xFE,
        (
            "The top brass have been gathering to\x01",
            "analyze the situation.\x02",
        )
    )

    CloseMessageWindow()
    OP_28(0x6D, 0x1, 0x8000)
    OP_A2(0x2)

    label("loc_124C")

    Jump("loc_13FE")

    label("loc_124F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 2)), scpexpr(EXPR_END)), "loc_13FE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_12AD")

    ChrTalk(    #49
        0x9,
        "Good work in there.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0x9,
        (
            "They really put you through the\x01",
            "wringer today!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_13FE")

    label("loc_12AD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1363")

    ChrTalk(    #51
        0x9,
        (
            "This is an important military facility.\x01",
            "Photography is strictly prohibited.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0x9,
        (
            "I'm sorry, but we can't even permit\x01",
            "tourist or memorabilia photos.\x01",
            "Please move along.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_13FE")

    label("loc_1363")


    ChrTalk(    #53
        0x9,
        (
            "This is Leiston Fortress, headquarters\x01",
            "of Her Majesty's Royal Army.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0x9,
        "Civilians are currently barred from entry.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0x9,
        "Please leave immediately.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_13FE")

    TalkEnd(0x9)
    Return()

    # Function_3_42D end

    def Function_4_1402(): pass

    label("Function_4_1402")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1419")
    Call(0, 18)
    Call(0, 19)

    label("loc_1419")

    SetChrPos(0x101, -1130, 0, -60200, 0)
    SetChrPos(0x107, -120, 0, -61110, 0)
    SetChrPos(0xF7, -1370, 0, -61940, 0)
    SetChrPos(0xF9, -500, 0, -62650, 0)
    ClearMapFlags(0x10)
    OP_6D(560, 0, -4680, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(5110, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)

    def lambda_14A5():
        OP_6D(680, -140, -49070, 8000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_14A5)

    def lambda_14BD():
        OP_67(0, 9500, -10000, 8000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_14BD)
    OP_C8(0x200, 0x46, "C_PLAC10._CH", 0x0, 0x3E8)
    OP_DE("Leiston Fortress")
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(1000)

    def lambda_150B():
        OP_8E(0xFE, 0xFFFFFE98, 0xFFFFFFB0, 0xFFFF4098, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_150B)
    Sleep(100)

    def lambda_152B():
        OP_8E(0xFE, 0x30C, 0xFFFFFF88, 0xFFFF3F94, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 0, lambda_152B)
    Sleep(100)

    def lambda_154B():
        OP_8E(0xFE, 0xFFFFFD12, 0xFFFFFFBA, 0xFFFF3A62, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF7, 0, lambda_154B)
    Sleep(100)

    def lambda_156B():
        OP_8E(0xFE, 0x208, 0xFFFFFF92, 0xFFFF39AE, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF9, 0, lambda_156B)
    WaitChrThread(0x101, 0x2)
    WaitChrThread(0x101, 0x3)
    Fade(1000)
    StopSound(0x9470, 0x1FBD0, 0x0)
    OP_6D(190, -40, -49730, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_0D()
    WaitChrThread(0x101, 0x0)
    WaitChrThread(0x107, 0x0)
    WaitChrThread(0xF7, 0x0)
    WaitChrThread(0xF9, 0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x6D, 0x1, 0x1)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_163C")

    ChrTalk(    #56
        0x101,
        (
            "#1011F#6PLeiston Fortress...\x01",
            "Kind of nostalgic, in a way.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_16BF")

    label("loc_163C")


    ChrTalk(    #57
        0x101,
        (
            "#1011F#6PLeiston Fortress...\x02\x03",

            "I know we were just here to help with\x01",
            "the training, but it still makes me feel\x01",
            "kinda nostalgic.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_16BF")


    ChrTalk(    #58
        0x107,
        (
            "#067F#4PHeehee! I kinda thought that, too.\x02\x03",

            "#560FIt was night when we were here\x01",
            "last, so it feels different, though.\x01",
            "Happier, maybe?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_17C3")

    ChrTalk(    #59
        0x106,
        (
            "#051F#2PWell, we DID break in not that long ago.\x02\x03",

            "Looking back on how good we\x01",
            "did makes it all the better.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_187A")

    label("loc_17C3")


    ChrTalk(    #60
        0x103,
        (
            "#027F#2PThat's right, you actually broke\x01",
            "into Leiston to rescue the professor,\x01",
            "didn't you?\x02\x03",

            "Assailing the unassailable fortress...\x01",
            "You don't do things by half-measures,\x01",
            "Estelle.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_187A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_19BE")

    ChrTalk(    #61
        0x104,
        (
            "#032FWhy, really now. You planned\x01",
            "something that fun and you didn't\x01",
            "contact me at all?\x02\x03",

            "Such fickle friends!\x01",
            "Why wouldn't you extend an invitation\x01",
            "to something so thrilling?\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 180, 400)
    OP_8C(0x107, 225, 400)

    ChrTalk(    #62
        0x101,
        (
            "#1007F#6PAnd why, exactly, would we call\x01",
            "YOU of all...?\x02\x03",

            "#1006FANYWAY. Let's get the measuring\x01",
            "thingy set up!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1B19")

    label("loc_19BE")


    ChrTalk(    #63
        0x105,
        (
            "#542FErm, wait a moment...you actually...?\x02\x03",

            "I'm, um, a little amazed you managed to\x01",
            "break into the legendary Leiston Fortress!\x01",
            "(I'm also not sure I should be hearing that...)\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 180, 400)
    OP_8C(0x107, 225, 400)

    ChrTalk(    #64
        0x101,
        (
            "#1016F#6PEh-hehehe... Leeeeet's just say we had\x01",
            "a trick up our sleeves and leave it at that!\x02\x03",

            "#1006FAnyway, let's get this measuring\x01",
            "thingy set up!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B19")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_1BDB")

    ChrTalk(    #65
        0x106,
        (
            "#051F#2PAh, it might be a good idea to get\x01",
            "permission from the gate guard before\x01",
            "stickin' anything in front of the fort.\x02\x03",

            "Kilika should've called ahead,\x01",
            "so this should be a snap.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C9D")

    label("loc_1BDB")


    ChrTalk(    #66
        0x103,
        (
            "#020F#2PI think it would be wise to get permission\x01",
            "from the gate guard before placing anything\x01",
            "in front of the fort.\x02\x03",

            "Kilika should have called ahead of us,\x01",
            "so I doubt this will take long.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C9D")


    ChrTalk(    #67
        0x101,
        "#1006F#6PAll right, then!\x02",
    )

    CloseMessageWindow()
    OP_A2(0x141C)
    OP_28(0x87, 0x1, 0x40)
    EventEnd(0x0)
    Return()

    # Function_4_1402 end

    def Function_5_1CC8(): pass

    label("Function_5_1CC8")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1CE8")
    Call(0, 18)
    Call(0, 19)
    FadeToBright(0, 0)

    label("loc_1CE8")

    OP_4A(0x9, 255)
    Fade(1000)
    SetChrPos(0x101, -500, 0, -4790, 0)
    SetChrPos(0xF7, 900, 0, -4790, 0)
    SetChrPos(0x107, -540, 160, -6150, 0)
    SetChrPos(0xF9, 480, 160, -6270, 0)
    OP_6D(320, 0, -3840, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_0D()

    ChrTalk(    #68
        0x9,
        (
            "#6PThis is Leiston Fortress,\x01",
            "the headquarters of the Royal Army.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0x9,
        (
            "#6PI'm sorry, but civilians are not\x01",
            "permitted entry at this time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0x9,
        (
            "#6PI'll have to ask you to leave\x01",
            "the premises at once.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0x101,
        "#1015F#2PUm, but we're from the Bracer Guild...\x02",
    )

    CloseMessageWindow()
    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #72
        0x9,
        "#6POh, right, you folks.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0x9,
        (
            "#6PCommand already passed down word.\x01",
            "You need to place some form of measuring\x01",
            "device near the gate, right?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_1F77")

    ChrTalk(    #74
        0x106,
        (
            "#051F#4PTold you it'd be quick.\x02\x03",

            "So it's cool if we put this thing wherever?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1FE2")

    label("loc_1F77")


    ChrTalk(    #75
        0x103,
        (
            "#020F#4PKilika is quick and thorough,\x01",
            "as usual.\x02\x03",

            "So, do you mind if we go ahead\x01",
            "and place the device?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1FE2")


    ChrTalk(    #76
        0x9,
        (
            "#6PYou have permission, so go right\x01",
            "ahead. Wherever you want.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0x9,
        (
            "#6PWell, anywhere except the road\x01",
            "itself, if you don't mind.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0x9,
        (
            "#6PWe would prefer to keep that\x01",
            "open for vehicle traffic.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0x101,
        "#1006F#2PSure, no problem.\x02",
    )

    CloseMessageWindow()
    OP_8C(0x101, 180, 400)
    OP_8C(0xF7, 225, 400)

    ChrTalk(    #80
        0x101,
        "#1006F#5POkay, let's find a good place!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0x107,
        "#061F#2POkay!\x02",
    )

    CloseMessageWindow()
    OP_4B(0x9, 255)
    OP_A2(0x141D)
    OP_28(0x87, 0x1, 0x80)
    EventEnd(0x0)
    Return()

    # Function_5_1CC8 end

    def Function_6_2124(): pass

    label("Function_6_2124")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x283, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x283, 6)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2131")
    Return()

    label("loc_2131")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2151")
    Call(0, 18)
    Call(0, 19)
    FadeToBright(0, 0)

    label("loc_2151")

    OP_A2(0x141E)
    Fade(1000)
    SetChrPos(0x101, -910, 250, -36040, 180)
    SetChrPos(0x107, 140, 250, -36150, 180)
    SetChrPos(0xF7, 70, 250, -35070, 180)
    SetChrPos(0xF9, -910, 250, -34770, 180)
    OP_6D(-200, -230, -46450, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_0D()

    def lambda_21E1():
        OP_90(0xFE, 0x0, 0x0, 0xFFFFD508, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_21E1)
    Sleep(150)

    def lambda_2201():
        OP_90(0xFE, 0x0, 0x0, 0xFFFFD508, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_2201)
    Sleep(100)

    def lambda_2221():
        OP_90(0xFE, 0x0, 0x0, 0xFFFFD634, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_2221)
    Sleep(200)

    def lambda_2241():
        OP_90(0xFE, 0x0, 0x0, 0xFFFFD698, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_2241)
    WaitChrThread(0xF9, 0x1)
    OP_8C(0x101, 90, 400)
    OP_8C(0x107, 270, 400)

    ChrTalk(    #82
        0x101,
        (
            "#1006F#6PAll right, Tita.\x01",
            "Where should we put this thing?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0x107,
        "#560F#4PHmmmmm. Let me think...\x02",
    )

    CloseMessageWindow()
    OP_8C(0x107, 180, 400)

    def lambda_22DA():
        OP_6B(3270, 3000)
        ExitThread()

    QueueWorkItem(0x1, 0, lambda_22DA)

    def lambda_22EA():

        label("loc_22EA")

        TurnDirection(0xFE, 0x107, 400)
        OP_48()
        Jump("loc_22EA")

    QueueWorkItem2(0x101, 1, lambda_22EA)

    def lambda_22FB():

        label("loc_22FB")

        TurnDirection(0xFE, 0x107, 400)
        OP_48()
        Jump("loc_22FB")

    QueueWorkItem2(0xF7, 1, lambda_22FB)

    def lambda_230C():

        label("loc_230C")

        TurnDirection(0xFE, 0x107, 400)
        OP_48()
        Jump("loc_230C")

    QueueWorkItem2(0xF9, 1, lambda_230C)
    OP_8E(0x107, 0x2EE, 0xFFFFFF42, 0xFFFF41EC, 0x7D0, 0x0)
    Sleep(500)
    OP_8C(0x107, 270, 400)
    Sleep(500)
    OP_8C(0x107, 90, 400)
    Sleep(500)
    OP_8C(0x107, 180, 400)
    WaitChrThread(0x1, 0x0)

    ChrTalk(    #84
        0x107,
        (
            "#064F#5PSooo if we're not allowed to\x01",
            "put it on the road...\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x107, 45, 400)

    def lambda_23A1():
        OP_6D(2690, -160, -46040, 2500)
        ExitThread()

    QueueWorkItem(0x107, 2, lambda_23A1)
    Sleep(500)
    OP_8E(0x107, 0x1284, 0xFFFFFFD8, 0xFFFF46BA, 0x7D0, 0x0)
    Sleep(500)
    OP_8C(0x107, 0, 400)
    Sleep(500)
    OP_8C(0x107, 180, 400)
    Sleep(500)

    ChrTalk(    #85
        0x107,
        (
            "#060F#6PThere's a light nearby, but this should\x01",
            "be far enough away, I think!\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x107, 225, 400)
    Sleep(500)

    ChrTalk(    #86
        0x107,
        (
            "#060F#6PAnd Zeiss is in that direction, so\x01",
            "the angle... Yep! This'll be perfect!\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x107, 270, 400)
    Sleep(500)

    ChrTalk(    #87
        0x107,
        (
            "#061F#4PI know it's right in front of the sign,\x01",
            "but right here is the best spot for it!\x02\x03",

            "Should we set it up?\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x101, 0x1)
    OP_44(0xF7, 0x1)
    OP_44(0xF9, 0x1)
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "Set Up Instrument\x01",      # 0
            "Not Yet\x01",                # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_25D0")

    ChrTalk(    #88
        0x107,
        (
            "#560F#4POkay, I'll start setting it up.\x02\x03",

            "Gimme juuuust a minute...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_26FB")

    label("loc_25D0")


    ChrTalk(    #89
        0x107,
        (
            "#064F#4PUm, we're not gonna set it up yet?\x02\x03",

            "#060FWell, once you're ready,\x01",
            "just examine this area again.\x02\x03",

            "I'll set it up then!\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6D(-910, -140, -47040, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0, -910, -140, -47040, 90)
    SetChrPos(0x1, -910, -140, -47040, 90)
    SetChrPos(0x2, -910, -140, -47040, 90)
    SetChrPos(0x3, -910, -140, -47040, 90)
    OP_69(0x0, 0x0)
    OP_65(0x0, 0x1)
    Sleep(500)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    Return()

    label("loc_26FB")

    Call(0, 8)
    Return()

    # Function_6_2124 end

    def Function_7_2700(): pass

    label("Function_7_2700")

    EventBegin(0x0)
    Fade(1000)
    SetChrPos(0x101, 3460, -40, -46290, 90)
    SetChrPos(0x107, 4450, -20, -46910, 90)
    SetChrPos(0xF7, 3170, -40, -47550, 90)
    SetChrPos(0xF9, 4100, 70, -48420, 0)
    OP_6D(4450, -20, -46910, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_0D()
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "Set Up Instrument\x01",      # 0
            "Not Yet\x01",                # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2838")
    OP_8C(0x107, 270, 400)

    ChrTalk(    #90
        0x107,
        (
            "#061F#4POkay, I'll start setting it up.\x02\x03",

            "Gimme juuuust a minute...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_28CA")

    label("loc_2838")

    OP_8C(0x107, 270, 400)

    ChrTalk(    #91
        0x107,
        (
            "#064F#4PUm, we're not gonna set it up yet?\x02\x03",

            "#060FWell, once you're ready,\x01",
            "just examine this area again.\x02\x03",

            "I'll set it up then!\x02",
        )
    )

    CloseMessageWindow()
    Sleep(200)
    EventEnd(0x0)
    Return()

    label("loc_28CA")

    Call(0, 8)
    Return()

    # Function_7_2700 end

    def Function_8_28CF(): pass

    label("Function_8_28CF")

    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x101, 3460, -40, -46290, 90)
    SetChrPos(0x107, 4450, -20, -46910, 90)
    SetChrPos(0xF7, 3170, -40, -47550, 90)
    SetChrPos(0xF9, 4100, 70, -48420, 0)
    OP_6D(4450, -20, -46910, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_72(0x2, 0x4)
    OP_72(0x3, 0x4)
    Sleep(2000)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(    #92
        0x107,
        "#061FAll done!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2ACB")
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "Make this the first instrument set\x01",                               # 0
            "Make Tratt Plains instrument already set\x01",                         # 1
            "Make Kaldia Tunnel instrument already set\x01",                        # 2
            "Make Kaldia Tunnel and Tratt Plains instruments already set\x01",      # 3
            "No Change\x01",                                                        # 4
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2A9B"),
        (1, "loc_2AA7"),
        (2, "loc_2AB3"),
        (3, "loc_2ABF"),
        (SWITCH_DEFAULT, "loc_2ACB"),
    )


    label("loc_2A9B")

    OP_A3(0x1419)
    OP_A3(0x141B)
    OP_A3(0x141F)
    Jump("loc_2ACB")

    label("loc_2AA7")

    OP_A2(0x1419)
    OP_A3(0x141B)
    OP_A3(0x141F)
    Jump("loc_2ACB")

    label("loc_2AB3")

    OP_A3(0x1419)
    OP_A2(0x141B)
    OP_A3(0x141F)
    Jump("loc_2ACB")

    label("loc_2ABF")

    OP_A2(0x1419)
    OP_A2(0x141B)
    OP_A3(0x141F)
    Jump("loc_2ACB")

    label("loc_2ACB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x283, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x283, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_310F")

    ChrTalk(    #93
        0x101,
        (
            "#1004F#3PWhoa, so this is what it looks like\x01",
            "when it's all together? Wow!\x02\x03",

            "#1015FWhat's, um...this dish-like thing?\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x107, 270, 400)

    ChrTalk(    #94
        0x107,
        (
            "#060F#4POh, that's a kind of antenna for\x01",
            "broadcasting orbal-waves called\x01",
            "a parabolic antenna!\x02\x03",

            "It puts out really powerful orbal waves\x01",
            "that can cover really long distances...\x02\x03",

            "It can even broadcast from inside\x01",
            "a place like the Kaldia Tunnel!\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2E3E")

    ChrTalk(    #95
        0x104,
        (
            "#033F#2PHmmmm... A most impressive tool.\x02\x03",

            "#030FI don't recall seeing anything like\x01",
            "this at the corner tool shop...\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x107, 180, 400)

    ChrTalk(    #96
        0x107,
        (
            "#560FUm, well, I don't think it's\x01",
            "for sale anywhere yet.\x02\x03",

            "It's one of Grandpa's inventions, though,\x01",
            "so I bet the central factory will start\x01",
            "selling them pretty soon!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0x104,
        "#031F#2PMmm. Lovely.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_2E3B")

    ChrTalk(    #98
        0x103,
        (
            "#027FOh, Lenheim, is that your...\x01",
            "interest in technology showing?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0x104,
        (
            "#035F#2PWhy, whatever do you mean,\x01",
            "dear Schera? I certainly don't\x01",
            "know.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2E3B")

    Jump("loc_3009")

    label("loc_2E3E")


    ChrTalk(    #100
        0x105,
        (
            "#044F#2PUm, Tita?\x02\x03",

            "I'd heard that orbal waves weaken\x01",
            "as they pass through obstacles.\x02\x03",

            "Can this dish really transmit through\x01",
            "the Kaldia Tunnel?\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x107, 180, 400)

    ChrTalk(    #101
        0x107,
        (
            "#560FOh, um, according to Grandpa,\x01",
            "the antenna can direct orbal waves.\x02\x03",

            "So even if you're in a cave, you can\x01",
            "reflect it down the tunnel and bounce\x01",
            "it off the walls until it reaches the exit!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0x105,
        (
            "#040F#2PI see! My goodness...\x02\x03",

            "#041FProfessor Russell really is as much\x01",
            "of a genius as he's ever been.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3009")


    ChrTalk(    #103
        0x101,
        (
            "#1007F#3PI guess I'm too much of a country girl\x01",
            "to appreciate how incredible it is...\x02\x03",

            "#1006FThis thing'll transmit earthquake\x01",
            "info back to us, though, right?\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x107, 270, 400)

    ChrTalk(    #104
        0x107,
        (
            "#560F#4PUm, not yet.\x01",
            "I haven't started it up yet.\x02\x03",

            "Just need to flip the switch...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_316C")

    label("loc_310F")


    ChrTalk(    #105
        0x101,
        (
            "#1006F#3PWell, flip that switch\x01",
            "as hard as you can!\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x107, 270, 400)

    ChrTalk(    #106
        0x107,
        "#560F#4PFlipping...NOW!\x02",
    )

    CloseMessageWindow()

    label("loc_316C")

    OP_8C(0x107, 90, 400)
    OP_8C(0xF9, 0, 400)
    Sleep(500)
    Fade(500)
    SetChrSubChip(0x107, 0)
    SetChrChipByIndex(0x107, 6)
    OP_0D()
    Sleep(500)
    OP_22(0x9C, 0x0, 0x64)
    Sleep(1000)
    OP_72(0x4, 0x4)
    OP_72(0x5, 0x4)
    OP_22(0x9E, 0x1, 0x64)
    OP_24(0x9E, 0x4B)
    Sleep(2000)
    Fade(500)
    SetChrSubChip(0x107, 0)
    SetChrChipByIndex(0x107, 65535)
    OP_0D()
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x283, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x283, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_334D")
    OP_8C(0x107, 270, 400)

    ChrTalk(    #107
        0x107,
        "#061F#4PYay! Now it works!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #108
        0x101,
        (
            "#1006F#3PGreat work, Tita!\x02\x03",

            "That antenna looks kinda easy to break,\x01",
            "but I guess monsters aren't gonna be a\x01",
            "problem around here, huh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #109
        0x107,
        (
            "#560F#4PUh-huh, plus, this machine repels\x01",
            "monsters like the road lamps!\x02\x03",

            "I don't think there'll be a problem with\x01",
            "placing them anywhere else, either!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #110
        0x101,
        "#1011F#3PNo worries, then! Cool.\x02",
    )

    CloseMessageWindow()
    Jump("loc_33C4")

    label("loc_334D")

    OP_8C(0x107, 270, 400)

    ChrTalk(    #111
        0x107,
        "#061F#4PYay! Now it works!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_33A3")

    ChrTalk(    #112
        0x106,
        "#051F#5PGreat work, shortstuff.\x02",
    )

    CloseMessageWindow()
    Jump("loc_33C4")

    label("loc_33A3")


    ChrTalk(    #113
        0x103,
        "#021F#5PGood work, sweetie.\x02",
    )

    CloseMessageWindow()

    label("loc_33C4")

    SetChrPos(0xA, 1460, 250, -34530, 180)
    ClearChrFlags(0xA, 0x80)

    NpcTalk(    #114
        0xA,
        "Man's Voice",
        (
            "#4PWell, it looks like you're\x01",
            "certainly keeping busy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0x101,
        "#1004F#3PHuh...?\x02",
    )

    CloseMessageWindow()

    def lambda_343D():
        OP_6D(2480, -90, -43470, 2500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_343D)

    def lambda_3455():
        OP_67(0, 8500, -10000, 2500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3455)

    def lambda_346D():
        OP_8E(0xA, 0x5B4, 0xB4, 0xFFFF6636, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_346D)
    OP_8C(0x101, 0, 400)
    OP_8C(0x107, 0, 400)
    OP_8C(0xF7, 0, 400)
    WaitChrThread(0x101, 0x1)
    WaitChrThread(0x101, 0x2)
    WaitChrThread(0xA, 0x1)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0xF7, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0xF9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x107, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #116
        0x101,
        "#1004F#2P#3SDAD?!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_3546")

    ChrTalk(    #117
        0x106,
        "#052F#2PCassius...!\x02",
    )

    CloseMessageWindow()
    Jump("loc_3568")

    label("loc_3546")


    ChrTalk(    #118
        0x103,
        "#023F#2PWhy, Cassius! Hello!\x02",
    )

    CloseMessageWindow()

    label("loc_3568")


    def lambda_356E():
        OP_6D(1780, 0, -41760, 1000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_356E)
    OP_43(0x101, 0x0, 0x0, 0x9)
    Sleep(200)

    def lambda_3592():
        OP_8E(0xFE, 0x618, 0x0, 0xFFFF6064, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_3592)
    OP_43(0xF7, 0x0, 0x0, 0xB)
    Sleep(300)
    OP_43(0x107, 0x0, 0x0, 0xA)
    Sleep(200)
    OP_43(0xF9, 0x0, 0x0, 0xC)
    WaitChrThread(0x101, 0x0)
    WaitChrThread(0x101, 0x1)
    WaitChrThread(0x101, 0x2)
    WaitChrThread(0xA, 0x1)
    Sleep(500)

    ChrTalk(    #119
        0xA,
        (
            "#1120F#6PHello, Estelle, everyone.\x01",
            "It's been a while.\x02\x03",

            "I know it's a little late, but good\x01",
            "work with your training, Estelle.\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x107, 0x0)
    WaitChrThread(0xF7, 0x0)
    WaitChrThread(0xF9, 0x0)

    ChrTalk(    #120
        0x101,
        (
            "#1008F#4PHeeey! 'Good work'?!\x01",
            "You don't know the half of it!\x02\x03",

            "What are you doing here,\x01",
            "anyway, Dad?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #121
        0xA,
        (
            "#1120F#6PHaha! Well, I AM a member of the\x01",
            "military, just in case you forgot.\x02\x03",

            "This is the strategic headquarters for\x01",
            "the Royal Army, so most of the army\x01",
            "brass works here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #122
        0x101,
        "#1017F#4POh, okay.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_37E4")

    ChrTalk(    #123
        0x106,
        (
            "#051F#4PSo you WERE put in charge\x01",
            "of the army, huh?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3843")

    label("loc_37E4")


    ChrTalk(    #124
        0x103,
        (
            "#020F#4PAh, now I remember. You've been placed\x01",
            "in charge of the army as a whole, correct?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3843")


    ChrTalk(    #125
        0xA,
        (
            "#1123F#6PYes...thanks in no small part to Morgan\x01",
            "absolutely refusing to let go of the idea...\x02\x03",

            "In the end, let's say it came down to a\x01",
            "battle of wills, and I lost.\x02\x03",

            "Thanks to that, I've not had a moment's\x01",
            "rest in...days? Weeks? I can't even track\x01",
            "the passage of time anymore.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_3A78")

    ChrTalk(    #126
        0x106,
        (
            "#051F#4PHeh, for a workaholic like you,\x01",
            "what's the problem?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #127
        0x101,
        (
            "#1016F#4PHaha! Come on, Agate, be nice.\x02\x03",

            "#1006FI have to admit, though...seeing you\x01",
            "in a uniform again felt weird as heck\x01",
            "at first, but...\x02\x03",

            "Now that I've gotten used to it?\x01",
            "You really look at home in it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3B94")

    label("loc_3A78")


    ChrTalk(    #128
        0x103,
        "#021F#4PSorry to hear that, Cassius.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #129
        0x101,
        (
            "#1016F#4POh, you work like that because\x01",
            "you know you enjoy it, Dad.\x02\x03",

            "#1006FI have to admit, though...seeing you\x01",
            "in a uniform again felt weird as heck\x01",
            "at first, but...\x02\x03",

            "Now that I've gotten used to it?\x01",
            "You really look at home in it, Dad.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3B94")


    ChrTalk(    #130
        0xA,
        (
            "#1121F#6PHeheh! Naturally!\x02\x03",

            "You realize, of course, that you\x01",
            "gaze upon he who was once the\x01",
            "Great Dandy of the Royal Army!\x02\x03",

            "Even Richard wasn't half the\x01",
            "lady-killer I was! Knew it, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #131
        0x101,
        (
            "#1007F#4PI'm sure Mom would be thrilled\x01",
            "to hear that, Dad.\x02\x03",

            "#1017FHaha... I'm still glad.\x02\x03",

            "I'd heard you were really busy,\x01",
            "so I've been a little worried...\x01",
            "but it looks like you're okay.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #132
        0xA,
        (
            "#1125F#6PI'm surviving, at least.\x02\x03",

            "#1122FAnyway, Jean passed along the\x01",
            "report from the guild.\x02\x03",

            "So. They've begun moving already.\x01",
            "You found one in Ruan.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #133
        0x101,
        (
            "#1003F#4POh... Yeah.\x02\x03",

            "#1002FYeah, we found one.\x01",
            "A foot-soldier of Ouroboros.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_3EBA")

    ChrTalk(    #134
        0x106,
        (
            "#050F#4PLike the report said, those sons-of-dogs\x01",
            "are probably even more dangerous than\x01",
            "we'd figured.\x02\x03",

            "Any chance the military's got an ace\x01",
            "in the hole for those animals?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3F74")

    label("loc_3EBA")


    ChrTalk(    #135
        0x103,
        (
            "#022F#4PAs the report stated, their members are...\x01",
            "to be blunt, Cassius, they're absolutely\x01",
            "terrifying.\x02\x03",

            "Does the military have any contingencies\x01",
            "in place to deal with the society?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3F74")


    ChrTalk(    #136
        0xA,
        (
            "#1125F#6PHmmmph... Honestly, if I could put together\x01",
            "an agency to replace the Intelligence\x01",
            "Division, that'd help...\x02\x03",

            "I've only just gotten the regular army and\x01",
            "the border garrison welded back together and\x01",
            "cohesive, though. And that was a challenge.\x02\x03",

            "#1120FFor the moment, we've little choice but to\x01",
            "rely on the resources of the guild to investigate.\x02\x03",

            "I'm hoping you can look into these bizarre\x01",
            "earthquakes we've been having while you're\x01",
            "at it.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_4161")

    ChrTalk(    #137
        0x106,
        "#551F#4PSon of a... Figures.\x02",
    )

    CloseMessageWindow()
    Jump("loc_417F")

    label("loc_4161")


    ChrTalk(    #138
        0x103,
        "#027F#4PUnderstood, sir.\x02",
    )

    CloseMessageWindow()

    label("loc_417F")


    ChrTalk(    #139
        0x101,
        (
            "#1006F#4PSo you're relying on me for once, Dad?\x02\x03",

            "Don't worry, I'll shower you in filial piety!\x01",
            "And success, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #140
        0xA,
        (
            "#1120F#6PHaha. First time you've ever said\x01",
            "something like that, Estelle.\x02\x03",

            "You look very good, too. You really\x01",
            "have become much more of a true\x01",
            "bracer.\x02\x03",

            "I'm sure Joshua would be impressed\x01",
            "as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #141
        0x101,
        (
            "#1025F#4POh, uh...\x02\x03",

            "#1016FHaha, I, uh, guess so...\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0xB, 690, 250, -31680, 180)
    ClearChrFlags(0xB, 0x80)

    NpcTalk(    #142
        0xB,
        "Man's Voice",
        "#4PGeneral Bright!\x02",
    )

    CloseMessageWindow()
    OP_62(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(800)

    def lambda_434C():
        OP_6D(1780, 0, -39760, 1500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_434C)

    def lambda_4364():
        TurnDirection(0xA, 0xB, 400)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_4364)
    OP_8E(0xB, 0x1FE, 0xFA, 0xFFFF6898, 0x9C4, 0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x6D, 0x0, 0x8)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_43DD")

    ChrTalk(    #143
        0x101,
        "#1004F#2PHuh? Oh, Major Cid!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_43DA")

    ChrTalk(    #144
        0x106,
        "#052F#2PWell, hey. Been a while.\x02",
    )

    CloseMessageWindow()

    label("loc_43DA")

    Jump("loc_442E")

    label("loc_43DD")


    ChrTalk(    #145
        0x101,
        "#1011F#2POh, Major Cid.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_442E")

    ChrTalk(    #146
        0x106,
        (
            "#051F#2PYo, Cid.\x01",
            "Good to see you again.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_442E")


    def lambda_4434():
        OP_6D(1780, 0, -41760, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4434)

    def lambda_444C():
        OP_8E(0xB, 0x1FE, 0x0, 0xFFFF60C8, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_444C)
    Sleep(1000)
    TurnDirection(0xA, 0xF9, 400)
    WaitChrThread(0xB, 0x1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x6D, 0x0, 0x8)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_490B")

    NpcTalk(    #147
        0xB,
        "Cid",
        (
            "#701FIt certainly has been a while,\x01",
            "hasn't it?\x02\x03",

            "My apologies for all the trouble we\x01",
            "caused you during the kidnapping\x01",
            "of Professor Russell.\x02\x03",

            "You really deserve a much more formal\x01",
            "apology at some point, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #148
        0x101,
        (
            "#1016F#4PHaha, no, no, it's okay.\x01",
            "I mean, you let us get away.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #149
        0x107,
        (
            "#560F#2PUm, um, thank you so much for helping\x01",
            "us back there, Mr. Major!\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #150
        0xB,
        "Cid",
        (
            "#703FMmm... Your gratitude does me more\x01",
            "credit than I deserve, miss.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #151
        0xA,
        (
            "#1120F#6PI do feel the need to point out that\x01",
            "Cid here was promoted for his part\x01",
            "in defeating the coup d'etat.\x02\x03",

            "You should refer to him as lieutenant\x01",
            "colonel from now on.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0xA, 400)

    ChrTalk(    #152
        0xB,
        "#702F#6PEr, General...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #153
        0x101,
        (
            "#1011F#4POh, neat!\x02\x03",

            "#1001FCongratulations, Lieutenant Colonel!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #154
        0x107,
        "#061F#2PCongratulations!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_47CE")

    ChrTalk(    #155
        0x106,
        (
            "#051F#4PHah, that's great. Really.\x02\x03",

            "Good to see a good man getting\x01",
            "respect he deserves.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_47CE")

    TurnDirection(0xB, 0xF7, 400)

    ChrTalk(    #156
        0xB,
        (
            "#701FI... Thank you.\x02\x03",

            "To be honest, it's embarrassing.\x01",
            "I only did what my country and\x01",
            "duty asked of me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #157
        0x101,
        (
            "#1006F#4PHey, there's no need to be humble.\x01",
            "You earned it!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #158
        0xA,
        (
            "#1125F#6PIndeed. And I'll expect more\x01",
            "excellence from you, Colonel.\x02\x03",

            "Otherwise I'll never be able to\x01",
            "properly retire, after all.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4A8E")

    label("loc_490B")


    ChrTalk(    #159
        0xA,
        (
            "#1124F#6POh?\x02\x03",

            "It sounds like you've met recently.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #160
        0xB,
        (
            "#701FYes, sir. It was during the\x01",
            "special training I mentioned.\x02\x03",

            "It was a huge success thanks\x01",
            "to them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #161
        0xA,
        (
            "#1125F#6PI see. It's good you took the initiative\x01",
            "so well in my absence.\x02\x03",

            "Now that you're a lieutenant colonel,\x01",
            "I'll be expecting even greater things\x01",
            "from you, you know.\x02\x03",

            "Otherwise I'll never be able\x01",
            "to properly retire!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4A8E")

    OP_8C(0xB, 90, 400)

    ChrTalk(    #162
        0xB,
        (
            "#702F#6PWell, we can't have you retiring\x01",
            "too early, sir.\x02\x03",

            "At least wait until General Morgan\x01",
            "has retired first.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #163
        0xA,
        (
            "#1123F#6P*sigh* And that'll be when he keels\x01",
            "over at his desk, most likely...\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xA, 270, 400)

    ChrTalk(    #164
        0xA,
        (
            "#1124F#4PAnyway, Lieutenant Colonel. It sounded like you\x01",
            "had some business with me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #165
        0xB,
        (
            "#700F#6PYes, sir. General Morgan will be\x01",
            "arriving earlier than expected.\x02\x03",

            "He is due at the landing port\x01",
            "within the hour.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #166
        0xA,
        (
            "#1125F#4PFor the love... That man has\x01",
            "exactly zero patience, I swear...\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xA, 180, 400)
    OP_8C(0xB, 180, 400)

    ChrTalk(    #167
        0xA,
        (
            "#1120F#6PAs you can see, I've a meeting with\x01",
            "some of the brass to attend.\x02\x03",

            "I'm sorry we can't talk longer,\x01",
            "Estelle.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #168
        0x101,
        (
            "#1017F#4PNo, it's okay. I'm glad we got the\x01",
            "chance to chat, even for a little bit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #169
        0xA,
        "#1120F#6PSo am I.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0xF7, 400)
    Sleep(400)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_4E4E")

    ChrTalk(    #170
        0xA,
        (
            "#1120F#6PAgate, I'm sorry to ask it of you,\x01",
            "but please continue to watch over\x01",
            "Estelle.\x02\x03",

            "She's a senior bracer now, but she\x01",
            "still lacks experience.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #171
        0x106,
        "#051F#4PNo worries, Cassius.\x02",
    )

    CloseMessageWindow()
    Jump("loc_4F24")

    label("loc_4E4E")


    ChrTalk(    #172
        0xA,
        (
            "#1120F#6PSchera. I doubt I need to ask it of you,\x01",
            "but please continue to watch over\x01",
            "Estelle.\x02\x03",

            "She's a senior bracer now, but she still\x01",
            "lacks experience.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #173
        0x103,
        (
            "#027F#4PDon't worry, Cassius.\x01",
            "You can count on me.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4F24")

    TurnDirection(0xA, 0x101, 400)
    Sleep(400)

    ChrTalk(    #174
        0xA,
        (
            "#1121F#6PI see you're keeping up\x01",
            "the hard work too, Tita.\x02\x03",

            "I imagine she can be a dunderhead\x01",
            "of a sister sometimes, but help Estelle\x01",
            "out as best you can, okay?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #175
        0x107,
        (
            "#067F#2PHeehee! I will, I promise!\x02\x03",

            "#560FOh, oh! About the analysis\x01",
            "of the Gospel unit...\x02\x03",

            "Grandpa said he found, um,\x01",
            "an 'unexpected hint.' I think he'll\x01",
            "want to talk to you soon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #176
        0xA,
        (
            "#1120F#6PI see... Sounds like we can\x01",
            "expect some headway soon.\x02\x03",

            "Give my best to the professor\x01",
            "when you see him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #177
        0x107,
        "#061F#2PI will!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_52FF")

    ChrTalk(    #178
        0xA,
        (
            "#1120F#6POlivier's with you, too?\x01",
            "Thank you for helping my daughter.\x02\x03",

            "I know you have your own business.\x01",
            "Thank you for putting it aside for a moment.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #179
        0x104,
        (
            "#035F#2PHeh... Your thanks are unnecessary,\x01",
            "Mr. Bright.\x02\x03",

            "#030FI'd not miss the next chapter in\x01",
            "our little opera for all the world.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #180
        0xA,
        (
            "#1125F#6PHmm... Well, as you wish.\x02\x03",

            "#1120FJust be sure not to neglect\x01",
            "your own mission.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #181
        0x104,
        (
            "#031F#2PFear not, my friend.\x01",
            "I haven't forgotten.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #182
        0x101,
        "#1015F#4PWhat's all that--\x02",
    )

    CloseMessageWindow()
    Jump("loc_5580")

    label("loc_52FF")


    ChrTalk(    #183
        0xA,
        (
            "#1125F#6PAnd...Your Highness. You have my deepest\x01",
            "gratitude for helping my daughter.\x02\x03",

            "#1120FI'm aware of some of your other...concerns,\x01",
            "however. I think you should discuss them\x01",
            "with a few of the people you know.\x02\x03",

            "Not just Her Majesty, but Captain Schwarz\x01",
            "and General Morgan as well. They both worry\x01",
            "after you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #184
        0x105,
        (
            "#047F#2P...I know.\x02\x03",

            "#040FI intend to explain it to everyone soon,\x01",
            "and make them understand.\x02\x03",

            "This journey is something I need\x01",
            "to do in order to find myself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #185
        0xA,
        (
            "#1120F#6PHaha! I'm sure you'll find what\x01",
            "you're looking for, Your Highness.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #186
        0x105,
        (
            "#048F#2PThank you, General Bright.\x01",
            "It gives me strength to hear you say that.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5580")


    ChrTalk(    #187
        0xA,
        (
            "#1125F#6PWell, if you'll pardon me.\x02\x03",

            "#1120FI won't have time to do much to help you\x01",
            "directly, but if you find something too\x01",
            "big for the guild, contact me any time.\x02\x03",

            "I'll help you as much as I possibly can.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #188
        0x101,
        (
            "#1006F#4PYeah... I'm counting on you if\x01",
            "it happens, Dad.\x02\x03",

            "#1018FGood luck with your work!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #189
        0xA,
        (
            "#1121F#6PHaha, I'll need it to keep\x01",
            "Morgan off my back!\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xA, 270, 400)

    ChrTalk(    #190
        0xA,
        "#1120F#4PLet's go, Lieutenant Colonel.\x02",
    )

    CloseMessageWindow()
    OP_8C(0xB, 90, 400)

    ChrTalk(    #191
        0xB,
        "#701F#6PSir!\x02",
    )

    CloseMessageWindow()
    OP_8C(0xA, 0, 400)

    def lambda_5748():
        OP_90(0xFE, 0x0, 0x0, 0x36B0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_5748)
    Sleep(600)
    OP_8C(0xB, 0, 400)

    def lambda_576F():
        OP_90(0xFE, 0x0, 0x0, 0x36B0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_576F)

    def lambda_578A():
        OP_6D(1780, 250, -37820, 3000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_578A)
    WaitChrThread(0xA, 0x1)
    WaitChrThread(0x101, 0x0)
    WaitChrThread(0x101, 0x1)

    def lambda_57B1():
        OP_6D(1780, 0, -41540, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_57B1)

    def lambda_57C9():
        OP_67(0, 9500, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_57C9)
    WaitChrThread(0x101, 0x0)
    WaitChrThread(0x101, 0x1)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)

    ChrTalk(    #192
        0x101,
        (
            "#1017F#4PHmm. Looks like Dad's even\x01",
            "busier than I thought.\x02\x03",

            "We'll need to do our part\x01",
            "as the guild and more!\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_58BE")

    ChrTalk(    #193
        0x106,
        (
            "#051F#1PYou got it.\x02\x03",

            "Let's get some answers and leave\x01",
            "the old man speechless.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5922")

    label("loc_58BE")


    ChrTalk(    #194
        0x103,
        (
            "#021F#1PIndeed.\x02\x03",

            "#020FNow, then, let's find some\x01",
            "answers and show Cassius\x01",
            "just what we can do.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5922")

    OP_8C(0xF7, 90, 400)
    OP_8C(0x101, 270, 400)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x283, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x283, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_59FE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_5993")

    ChrTalk(    #195
        0x106,
        (
            "#051F#1PAnyway, we're all done here.\x02\x03",

            "Let's go set up the next device.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_59E6")

    label("loc_5993")


    ChrTalk(    #196
        0x103,
        (
            "#027F#1PWe should be all done here.\x02\x03",

            "We should go set up the\x01",
            "next instrument.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_59E6")


    ChrTalk(    #197
        0x101,
        "#1006F#4PRight!\x02",
    )

    CloseMessageWindow()
    Jump("loc_5C29")

    label("loc_59FE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x283, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x283, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_5AD4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_5A62")

    ChrTalk(    #198
        0x106,
        (
            "#051F#1PAnyway, that's two devices down.\x02\x03",

            "Let's go set up the last one.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5ABD")

    label("loc_5A62")


    ChrTalk(    #199
        0x103,
        (
            "#526F#1PThat's two instruments in place,\x01",
            "either way.\x02\x03",

            "Shall we go place the last one?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5ABD")


    ChrTalk(    #200
        0x101,
        "#1000F#4POkay!\x02",
    )

    CloseMessageWindow()
    Jump("loc_5C29")

    label("loc_5AD4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_5B58")

    ChrTalk(    #201
        0x106,
        (
            "#051F#1PWe've got all the devices in\x01",
            "place now, too.\x02\x03",

            "Let's get back to Gramps at\x01",
            "Operations in the central factory.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5BF2")

    label("loc_5B58")


    ChrTalk(    #202
        0x103,
        (
            "#026F#1PRight, then, that's the last instrument\x01",
            "in place.\x02\x03",

            "#020FLet's return to the Capel's room\x01",
            "at the factory and check in with\x01",
            "Professor Russell.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5BF2")


    ChrTalk(    #203
        0x101,
        "#1006F#4PRight. Fifth floor of the factory!\x02",
    )

    CloseMessageWindow()
    OP_28(0x87, 0x1, 0x200)

    label("loc_5C29")

    OP_64(0x0, 0x1)
    OP_A2(0x141F)
    OP_28(0x87, 0x1, 0x100)
    EventEnd(0x0)
    Return()

    # Function_8_28CF end

    def Function_9_5C39(): pass

    label("Function_9_5C39")

    OP_8E(0x101, 0x74E, 0x0, 0xFFFF5B78, 0x9C4, 0x0)
    OP_8C(0x101, 0, 400)
    Return()

    # Function_9_5C39 end

    def Function_10_5C55(): pass

    label("Function_10_5C55")

    OP_8E(0x107, 0x7BC, 0xFFFFFFBA, 0xFFFF5696, 0x7D0, 0x0)
    OP_8C(0x107, 0, 400)
    Return()

    # Function_10_5C55 end

    def Function_11_5C71(): pass

    label("Function_11_5C71")

    OP_8E(0xF7, 0x30C, 0x0, 0xFFFF5B00, 0x9C4, 0x0)
    OP_8C(0xF7, 0, 400)
    Return()

    # Function_11_5C71 end

    def Function_12_5C8D(): pass

    label("Function_12_5C8D")

    OP_8E(0xF9, 0x3CA, 0xFFFFFFCE, 0xFFFF566E, 0x7D0, 0x0)
    OP_8C(0xF9, 0, 400)
    Return()

    # Function_12_5C8D end

    def Function_13_5CA9(): pass

    label("Function_13_5CA9")

    EventBegin(0x0)
    OP_6D(7290, 8370, -11590, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(2880, 0)
    OP_6C(310000, 0)
    OP_6E(326, 0)
    OP_E5(0x9, 0x0, 0x0)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    SetChrFlags(0x8, 0x4)
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, 41020, 8200, -35260, 270)

    def lambda_5D21():
        OP_6D(38570, 8950, -35140, 8000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5D21)

    def lambda_5D39():
        OP_67(0, 3000, -10000, 8000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_5D39)

    def lambda_5D51():
        OP_6C(315000, 8000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_5D51)
    FadeToBright(2000, 0)
    OP_0D()
    WaitChrThread(0x101, 0x1)
    Sleep(500)

    ChrTalk(    #204
        0x8,
        (
            "#1182F#2PWatch towers...orbal sensors...\x02\x03",

            "A mined harbor, and gun emplacements\x01",
            "covering all approaches...\x02\x03",

            "A perfect defense in every way.\x02\x03",

            "#1322FIf that's the way you want to play,\x01",
            "Cassius Bright...\x02\x03",

            "I'll just have to change the rules of\x01",
            "the game a little, as suggested.\x02",
        )
    )

    CloseMessageWindow()
    Fade(500)
    SetChrChipByIndex(0x8, 1)
    SetChrSubChip(0x8, 0)
    OP_0D()
    OP_8C(0x8, 90, 400)
    Sleep(500)

    ChrTalk(    #205
        0x8,
        (
            "#1181F#5PSir...just wait a little bit longer.\x02\x03",

            "Your freedom is coming soon,\x01",
            "Colonel. I promise.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_24(0x1CD, 0x5A)
    Sleep(200)
    OP_24(0x1CD, 0x50)
    Sleep(200)
    OP_24(0x1CD, 0x46)
    Sleep(200)
    OP_24(0x1CD, 0x3C)
    Sleep(200)
    OP_24(0x1CD, 0x32)
    Sleep(200)
    OP_24(0x1CD, 0x28)
    Sleep(200)
    OP_24(0x1CD, 0x1E)
    Sleep(200)
    OP_23(0x1CD)
    OP_0D()
    OP_AD(0x2400A6, 0x0, 0x0, 0x64)
    Sleep(4000)
    OP_56(0x2)
    OP_AE(0xC8)
    Sleep(2000)
    OP_A2(0x10F0)
    OP_A2(0x1600)
    NewScene("ED6_DT21/T3100   ._SN", 110, 0, 0)
    IdleLoop()
    Return()

    # Function_13_5CA9 end

    def Function_14_5F80(): pass

    label("Function_14_5F80")

    EventBegin(0x0)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    OP_6D(40, 3450, -7970, 0)
    OP_67(0, 3180, -10000, 0)
    OP_6B(4019, 0)
    OP_6C(330000, 0)
    OP_6E(496, 0)
    OP_C8(0x200, 0x46, "C_PLAC10._CH", 0x0, 0x3E8)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(2000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x10F1)
    NewScene("ED6_DT21/C3110   ._SN", 106, 0, 0)
    IdleLoop()
    Return()

    # Function_14_5F80 end

    def Function_15_600F(): pass

    label("Function_15_600F")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_602F")
    Call(0, 18)
    Call(0, 20)
    FadeToBright(0, 0)

    label("loc_602F")

    OP_4A(0x9, 255)
    Fade(1000)
    SetChrPos(0x101, -440, 0, -4750, 0)
    SetChrPos(0x102, 590, 0, -4750, 0)
    SetChrPos(0xF8, -840, 150, -6050, 0)
    SetChrPos(0xF9, 480, 100, -6050, 0)
    OP_8C(0x9, 180, 0)
    OP_6D(800, 0, -3520, 0)
    OP_67(0, 7630, -10000, 0)
    OP_6B(2580, 0)
    OP_6C(45000, 0)
    OP_6E(291, 0)
    OP_0D()
    Sleep(300)

    ChrTalk(    #206
        0x9,
        (
            "#6PYou lot... You're bracers, right?\x02\x03",

            "Leiston Fortress is currently under\x01",
            "emergency alert.\x02\x03",

            "Unless your business is critical,\x01",
            "I'll have to ask you to leave.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #207
        0x101,
        (
            "#1015F#2PUm, excuse me...\x02\x03",

            "Is General Bright in the fortress?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #208
        0x9,
        (
            "#6POf course General Bright is here, but...\x01",
            "as a result of EVERYTHING not working,\x01",
            "the army's in chaos.\x02\x03",

            "The General's been working without rest,\x01",
            "sending orders out to all regions via\x01",
            "courier, rebuilding the chain of command.\x02\x03",

            "Even if you are bracers, I'm afraid\x01",
            "I can't let you see him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #209
        0x101,
        "#2P#1025FOkay...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #210
        0x102,
        (
            "#1035F#4PCould you potentially make an\x01",
            "exception this once?\x02\x03",

            "#1043FThis is actually General Bright's daughter.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #211
        0x9,
        (
            "#6PW-Wait, really?!\x01",
            "You're Ms. Estelle Bright?!\x02\x03",

            "I'd heard she was in the guild, but...\x02\x03",

            "Hells, then, of course you can come in!\x01",
            "I'll show you right to the general's--\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #212
        0x101,
        (
            "#1004F#2PAh, no, it's okay, really.\x02\x03",

            "#1008FI wouldn't want to get in the way\x01",
            "of his job if he's that busy.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #213
        0x102,
        "#1044F#4PEstelle...\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6514")
    TurnDirection(0x103, 0x101, 400)

    ChrTalk(    #214
        0x103,
        (
            "#524F#2PA little visit might help the\x01",
            "both of you, you know?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 400)
    Jump("loc_65D0")

    label("loc_6514")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6579")
    TurnDirection(0x106, 0x101, 400)

    ChrTalk(    #215
        0x106,
        (
            "#555F#2PI think buzzing the old man\x01",
            "a little is okay, don't you?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x106, 400)
    Jump("loc_65D0")

    label("loc_6579")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_65D0")
    TurnDirection(0x108, 0x101, 400)

    ChrTalk(    #216
        0x108,
        (
            "#072F#2PI doubt he would mind\x01",
            "a short visit, Estelle.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x108, 400)

    label("loc_65D0")


    ChrTalk(    #217
        0x101,
        (
            "#1011F#5PDad has his way, I have mine.\x02\x03",

            "#1012FI'm sure that Dad doing well in his\x01",
            "job will make mine easier, and...\x02\x03",

            "I think if I do the same, his\x01",
            "job will get easier, too.\x02\x03",

            "#1006FSo it's enough just knowing he's okay.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_66DD")
    TurnDirection(0x107, 0x101, 400)

    ChrTalk(    #218
        0x107,
        "#560F#2PEstelle...\x02",
    )

    CloseMessageWindow()

    label("loc_66DD")


    ChrTalk(    #219
        0x102,
        "#1053F#4PI see... Fair enough.\x02",
    )

    CloseMessageWindow()

    def lambda_6707():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_6707)
    Sleep(100)

    def lambda_671A():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_671A)
    Sleep(100)

    def lambda_672D():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_672D)
    Sleep(100)
    OP_8C(0xF8, 0, 400)
    Sleep(200)

    ChrTalk(    #220
        0x102,
        (
            "#1040F#4PWe'll be going, then.\x02\x03",

            "Please, give our best to the general\x01",
            "and let him know we stopped by if\x01",
            "you get a chance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #221
        0x9,
        (
            "#6POf course. I'll do what I can.\x02\x03",

            "I'll see if I can catch him\x01",
            "during mess or something.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #222
        0x101,
        "#1017F#2PThanks again!\x02",
    )

    CloseMessageWindow()
    OP_A2(0x200D)
    OP_4B(0x9, 255)
    EventEnd(0x0)
    Return()

    # Function_15_600F end

    def Function_16_6848(): pass

    label("Function_16_6848")

    TalkBegin(0x9)
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x401, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x401, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x401, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_68AA")

    Menu(
        0,
        10,
        100,
        0,
        (
            "Talk\x01",                                     # 0
            "Inquire about the Combustion Engine\x01",      # 1
            "Leave\x01",                                    # 2
        )
    )

    Jump("loc_68BE")

    label("loc_68AA")


    Menu(
        0,
        10,
        100,
        0,
        (
            "Talk\x01",       # 0
            "Leave\x01",      # 1
        )
    )


    label("loc_68BE")

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_69BB")

    ChrTalk(    #223
        0x9,
        (
            "General Bright is personally working\x01",
            "to reconstruct the Royal Army.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #224
        0x9,
        (
            "The image of General Bright, giving orders\x01",
            "without a moment's rest, even in our darkest\x01",
            "hour... It's an inspiration for any soldier.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6AB5")

    label("loc_69BB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x401, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x401, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x401, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_69DD")
    Call(0, 17)
    Jump("loc_6AB5")

    label("loc_69DD")


    ChrTalk(    #225
        0x9,
        (
            "Thanks to the Royal Guard's runners,\x01",
            "Leiston's communications with other units\x01",
            "has been restored to some degree.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #226
        0x9,
        (
            "Should any other emergency situations\x01",
            "arise, we will contact you via the Zeiss\x01",
            "guild branch.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6AB5")

    TalkEnd(0x9)
    Return()

    # Function_16_6848 end

    def Function_17_6AB9(): pass

    label("Function_17_6AB9")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6AD9")
    Call(0, 18)
    Call(0, 20)
    FadeToBright(0, 0)

    label("loc_6AD9")

    Fade(1000)
    SetChrPos(0x101, -440, 0, -4750, 0)
    SetChrPos(0x102, 590, 0, -4750, 0)
    SetChrPos(0xF8, -840, 150, -6050, 0)
    SetChrPos(0xF9, 480, 100, -6050, 0)
    SetChrPos(0x9, 500, 0, -3240, 0)
    OP_8C(0x9, 180, 0)
    SetChrSubChip(0x9, 0)
    OP_6D(800, 0, -3520, 0)
    OP_67(0, 7630, -10000, 0)
    OP_6B(2580, 0)
    OP_6C(45000, 0)
    OP_6E(291, 0)
    OP_0D()
    Sleep(300)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #227
        (
            "\x07\x05Estelle explained their situation and asked about the\x01",
            "combustion engine.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    ChrTalk(    #228
        0x9,
        (
            "#6PHmm. I'm not familiar with the device\x01",
            "in question, but I can tell it must be something\x01",
            "important.\x02\x03",

            "Wait here a moment. I'll go ask.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x9, 0, 400)

    def lambda_6C89():
        OP_90(0xFE, 0x0, 0x0, 0x1A90, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_6C89)
    Sleep(1000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    Sleep(2000)
    WaitChrThread(0x9, 0x1)
    FadeToBright(2000, 0)
    OP_8E(0x9, 0x1F4, 0x0, 0xFFFFF358, 0x7D0, 0x0)

    ChrTalk(    #229
        0x9,
        (
            "#6PAll right. I asked the quartermaster,\x01",
            "and there's a problem.\x02\x03",

            "It seems this 'combustion engine'\x01",
            "is not currently in the fortress walls.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(70)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6DBF")
    OP_62(0xF8, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_6DFD")

    label("loc_6DBF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6DE6")
    OP_62(0xF8, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_6DFD")

    label("loc_6DE6")

    OP_62(0xF8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_6DFD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6E24")
    OP_62(0xF9, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_6E62")

    label("loc_6E24")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6E4B")
    OP_62(0xF9, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_6E62")

    label("loc_6E4B")

    OP_62(0xF9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_6E62")

    Sleep(1000)

    ChrTalk(    #230
        0x101,
        (
            "#1009F#2PBut, but that can't be right!\x01",
            "Gustav said--\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #231
        0x9,
        (
            "#6PWait a moment, miss.\x01",
            "I said it isn't in the fortress walls.\x02\x03",

            "We loaded it onto a patrol ship a\x01",
            "short while ago for shipment back\x01",
            "to the central factory.\x02\x03",

            "Unfortunately, all THIS happened not long after\x01",
            "takeoff. The ship made an emergency landing\x01",
            "somewhere on the Tratt Plains as a result.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #232
        0x101,
        "#1004F#2POh! Oh, crap...\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_702F")

    ChrTalk(    #233
        0x108,
        (
            "#070F#2PWe have a real search ahead of us,\x01",
            "then.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_70C6")

    label("loc_702F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7076")

    ChrTalk(    #234
        0x103,
        (
            "#027F#2PWe have a real search ahead of us,\x01",
            "then.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_70C6")

    label("loc_7076")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_70C6")

    ChrTalk(    #235
        0x106,
        (
            "#051F#2PTime to go rescue an engine AND\x01",
            "a crew, sounds like.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_70C6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7127")

    ChrTalk(    #236
        0x107,
        (
            "#560F#2PSo we just need to talk to the guards\x01",
            "on the patrol ship about it?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_718F")

    label("loc_7127")


    ChrTalk(    #237
        0x102,
        (
            "#1040F#4PYes. We should look for the ship, ensure\x01",
            "the crew is safe, and ask them about the\x01",
            "engine.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_718F")


    ChrTalk(    #238
        0x9,
        (
            "#6PI know it's a pain, but that's the size of it.\x02\x03",

            "As I said, we think the ship landed\x01",
            "somewhere on the Tratt Plains. Good luck.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(200)
    OP_A2(0x200E)
    OP_28(0xC2, 0x1, 0x20)
    OP_28(0xC2, 0x1, 0x40)
    EventEnd(0x0)
    Return()

    # Function_17_6AB9 end

    def Function_18_722C(): pass

    label("Function_18_722C")

    FadeToDark(0, 0, -1)
    OP_A3(0x1200)
    OP_A3(0x1201)
    RemoveParty(0x2, 0xFF)
    RemoveParty(0x5, 0xFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "Set Scherazard as Partner\x01",      # 0
            "Set Agate as Partner\x01",           # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_72A5"),
        (1, "loc_72AB"),
        (SWITCH_DEFAULT, "loc_72B1"),
    )


    label("loc_72A5")

    OP_A2(0x1200)
    Jump("loc_72B1")

    label("loc_72AB")

    OP_A2(0x1201)
    Jump("loc_72B1")

    label("loc_72B1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_72BF")
    AddParty(0x2, 0xF7, 0xFF)
    Jump("loc_72C3")

    label("loc_72BF")

    AddParty(0x5, 0xF7, 0xFF)

    label("loc_72C3")

    Return()

    # Function_18_722C end

    def Function_19_72C4(): pass

    label("Function_19_72C4")

    ClearMapFlags(0x1)
    OP_6D(0, 0, 0, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_72FE")
    FadeToBright(0, 0)
    OP_C9(0x0, 0x4, 0x0, 0x2, 0x6, 0xFF, 0x3, 0x4, 0xFFFF)
    Jump("loc_7318")

    label("loc_72FE")

    FadeToBright(0, 0)
    OP_C9(0x0, 0x4, 0x0, 0x5, 0x6, 0xFF, 0x3, 0x4, 0xFFFF)

    label("loc_7318")

    FadeToDark(0, 0, -1)
    OP_69(0x0, 0x0)
    Return()

    # Function_19_72C4 end

    def Function_20_732A(): pass

    label("Function_20_732A")

    ClearMapFlags(0x1)
    OP_6D(106730, -1920, 53920, 0)
    Sleep(100)
    FadeToBright(0, 0)
    OP_C9(0x0, 0x4, 0x0, 0x1, 0xFF, 0xFF, 0x5, 0x2, 0x6, 0x7, 0xFFFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(0, 0, -1)
    OP_69(0x0, 0x0)
    Sleep(1000)
    Return()

    # Function_20_732A end

    def Function_21_7383(): pass

    label("Function_21_7383")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #239
        "\x07\x05   Warning! Restricted Area--Photography Prohibited\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_21_7383 end

    def Function_22_73E9(): pass

    label("Function_22_73E9")

    EventBegin(0x1)

    ChrTalk(    #240
        0x101,
        "#1001FI bet I could fish here!\x02",
    )

    CloseMessageWindow()

    def lambda_7415():
        OP_6D(32020, -50, -31290, 1500)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_7415)

    def lambda_742D():
        OP_67(0, 9500, -10000, 1500)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_742D)

    def lambda_7445():
        OP_6B(2800, 1500)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_7445)

    def lambda_7455():
        OP_6C(45000, 1500)
        ExitThread()

    QueueWorkItem(0x1, 2, lambda_7455)
    Sleep(1000)
    SetChrName("")

    AnonymousTalk(    #241
        "\x07\x05Try fishing?\x07\x00\x02",
    )

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        32,
        1,
        (
            "Hook, Line, and Sinker\x01",      # 0
            "Spare the Rod\x01",               # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    WaitChrThread(0x0, 0x1)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_74FB")
    OP_C0(0xE, 0x24, 0x7E71, 0xFFFFFFCE, 0xFFFF813E, 0x0, 0x7A08, 0xFFFFFE0C, 0xFFFF8AE4)
    OP_0D()
    EventEnd(0x1)
    Jump("loc_750A")

    label("loc_74FB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_750A")
    EventEnd(0x1)

    label("loc_750A")

    Return()

    # Function_22_73E9 end

    SaveToFile()

Try(main)

from ED6ScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 蔡斯

    CreateScenaFile(
        FileName            = 'T3223   ._SN',
        MapName             = 'Zeiss',
        Location            = 'T3223.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60084",
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
        'Dorothy',                              # 9
        'Mrs. Mao',                             # 10
        'Ed',                                   # 11
        'Percy',                                # 12
        'Lynn',                                 # 13
        'Recia',                                # 14
        'Cyril',                                # 15
        'Addy',                                 # 16
        'Lucky',                                # 17
        'Sima',                                 # 18
        'Quantay',                              # 19
        'Seagaro',                              # 20
        'Edel',                                 # 21
        'Ed',                                   # 22
        'Fruity Milk',                          # 23
        'Fruity Milk',                          # 24
        'Fruity Milk',                          # 25
        'Fruity Milk',                          # 26
        'Fruity Milk',                          # 27
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
        'ED6_DT07/CH02070 ._CH',             # 00
        'ED6_DT07/CH02430 ._CH',             # 01
        'ED6_DT07/CH01270 ._CH',             # 02
        'ED6_DT07/CH01460 ._CH',             # 03
        'ED6_DT07/CH01030 ._CH',             # 04
        'ED6_DT07/CH01150 ._CH',             # 05
        'ED6_DT07/CH01120 ._CH',             # 06
        'ED6_DT07/CH01130 ._CH',             # 07
        'ED6_DT07/CH01160 ._CH',             # 08
        'ED6_DT07/CH01020 ._CH',             # 09
        'ED6_DT07/CH01060 ._CH',             # 0A
        'ED6_DT07/CH01140 ._CH',             # 0B
        'ED6_DT07/CH01130 ._CH',             # 0C
        'ED6_DT07/CH01270 ._CH',             # 0D
        'ED6_DT06/CH20021 ._CH',             # 0E
    )

    AddCharChipPat(
        'ED6_DT07/CH02070P._CP',             # 00
        'ED6_DT07/CH02430P._CP',             # 01
        'ED6_DT07/CH01270P._CP',             # 02
        'ED6_DT07/CH01460P._CP',             # 03
        'ED6_DT07/CH01030P._CP',             # 04
        'ED6_DT07/CH01150P._CP',             # 05
        'ED6_DT07/CH01120P._CP',             # 06
        'ED6_DT07/CH01130P._CP',             # 07
        'ED6_DT07/CH01160P._CP',             # 08
        'ED6_DT07/CH01020P._CP',             # 09
        'ED6_DT07/CH01060P._CP',             # 0A
        'ED6_DT07/CH01140P._CP',             # 0B
        'ED6_DT07/CH01130P._CP',             # 0C
        'ED6_DT07/CH01270P._CP',             # 0D
        'ED6_DT06/CH20021P._CP',             # 0E
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
        TalkScenaIndex      = 13,
    )

    DeclNpc(
        X                   = 2590,
        Z                   = 250,
        Y                   = 5360,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 18,
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
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
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
        TalkScenaIndex      = 7,
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
        TalkScenaIndex      = 8,
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
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
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
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 12,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 14,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 9,
        ChipIndex           = 0x9,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 15,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 16,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 11,
        ChipIndex           = 0xB,
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
        Unknown3            = 12,
        ChipIndex           = 0xC,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 13,
        ChipIndex           = 0xD,
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
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 131086,
        ChipIndex           = 0xE,
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
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 196622,
        ChipIndex           = 0xE,
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
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 196622,
        ChipIndex           = 0xE,
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
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 196622,
        ChipIndex           = 0xE,
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
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 196622,
        ChipIndex           = 0xE,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclActor(
        TriggerX            = 2670,
        TriggerZ            = 250,
        TriggerY            = 3820,
        TriggerRange        = 400,
        ActorX              = 2590,
        ActorZ              = 1750,
        ActorY              = 5360,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 17,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 9940,
        TriggerZ            = 0,
        TriggerY            = 90,
        TriggerRange        = 400,
        ActorX              = 8490,
        ActorZ              = 1500,
        ActorY              = 340,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 11,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 8960,
        TriggerZ            = 250,
        TriggerY            = 13840,
        TriggerRange        = 1000,
        ActorX              = 9100,
        ActorZ              = 1750,
        ActorY              = 13840,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 21,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_3EE",          # 00, 0
        "Function_1_746",          # 01, 1
        "Function_2_747",          # 02, 2
        "Function_3_75D",          # 03, 3
        "Function_4_781",          # 04, 4
        "Function_5_A12",          # 05, 5
        "Function_6_C81",          # 06, 6
        "Function_7_13AD",         # 07, 7
        "Function_8_1735",         # 08, 8
        "Function_9_173C",         # 09, 9
        "Function_10_1743",        # 0A, 10
        "Function_11_1B7A",        # 0B, 11
        "Function_12_1B7F",        # 0C, 12
        "Function_13_20DC",        # 0D, 13
        "Function_14_2162",        # 0E, 14
        "Function_15_2169",        # 0F, 15
        "Function_16_2170",        # 10, 16
        "Function_17_2177",        # 11, 17
        "Function_18_217C",        # 12, 18
        "Function_19_3357",        # 13, 19
        "Function_20_34C5",        # 14, 20
        "Function_21_3765",        # 15, 21
    )


    def Function_0_3EE(): pass

    label("Function_0_3EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 2)), scpexpr(EXPR_END)), "loc_401")
    SetMapFlags(0x10000000)
    OP_A3(0x3FA)
    Event(0, 19)

    label("loc_401")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 3)), scpexpr(EXPR_END)), "loc_40F")
    OP_A3(0x3FB)
    Event(0, 20)

    label("loc_40F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_445")
    ClearChrFlags(0x15, 0x80)
    SetChrPos(0x15, -30310, -250, 8840, 81)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, 8490, 0, 340, 102)
    Jump("loc_745")

    label("loc_445")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_4C4")
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, 14330, 0, 1850, 182)
    ClearChrFlags(0x15, 0x80)
    SetChrPos(0x15, -30310, -250, 8840, 81)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, -1040, 0, 40770, 2)
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x13, -28880, 0, 43500, 9)
    ClearChrFlags(0x14, 0x80)
    SetChrPos(0x14, -28740, 0, 38750, 93)
    OP_43(0x14, 0x0, 0x0, 0x3)
    Jump("loc_745")

    label("loc_4C4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_52D")
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, 14330, 0, 1850, 182)
    ClearChrFlags(0x15, 0x80)
    SetChrPos(0x15, -30310, -250, 8840, 81)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, 8490, 0, 340, 102)
    ClearChrFlags(0x14, 0x80)
    SetChrPos(0x14, -28740, 0, 38750, 93)
    OP_43(0x14, 0x0, 0x0, 0x3)
    Jump("loc_745")

    label("loc_52D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_58F")
    ClearChrFlags(0x15, 0x80)
    SetChrPos(0x15, -30310, -250, 8840, 81)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, 8490, 0, 340, 102)
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x13, 11260, 0, 10650, 175)
    ClearChrFlags(0x14, 0x80)
    SetChrPos(0x14, 11070, 0, 8460, 358)
    Jump("loc_745")

    label("loc_58F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 6)), scpexpr(EXPR_END)), "loc_618")
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, -2470, 0, 39920, 270)
    ClearChrFlags(0x15, 0x80)
    SetChrPos(0x15, -30310, -250, 8840, 81)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, 8490, 0, 340, 102)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 7)), scpexpr(EXPR_END)), "loc_615")
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x4)
    SetChrFlags(0x8, 0x10)
    SetChrPos(0x8, 14070, 0, 2040, 180)
    ClearChrFlags(0x16, 0x80)
    SetChrPos(0x16, 14600, 750, 1030, 0)

    label("loc_615")

    Jump("loc_745")

    label("loc_618")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 2)), scpexpr(EXPR_END)), "loc_690")
    ClearChrFlags(0x15, 0x80)
    SetChrPos(0x15, -30310, -250, 8840, 81)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, 8490, 0, 340, 102)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, -1040, 0, 40770, 2)
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x13, 11260, 0, 10650, 175)
    ClearChrFlags(0x14, 0x80)
    SetChrPos(0x14, 11070, 0, 8460, 358)
    Jump("loc_745")

    label("loc_690")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 7)), scpexpr(EXPR_END)), "loc_6C6")
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, 14330, 0, 1850, 182)
    ClearChrFlags(0x15, 0x80)
    SetChrPos(0x15, 970, 0, -2050, 0)
    Jump("loc_745")

    label("loc_6C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_6FC")
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, 14330, 0, 1850, 182)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, -2080, 250, 6150, 195)
    Jump("loc_745")

    label("loc_6FC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_745")
    ClearChrFlags(0x15, 0x80)
    SetChrPos(0x15, -30310, -250, 8840, 81)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, 8490, 0, 340, 102)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, -2080, 250, 6150, 195)

    label("loc_745")

    Return()

    # Function_0_3EE end

    def Function_1_746(): pass

    label("Function_1_746")

    Return()

    # Function_1_746 end

    def Function_2_747(): pass

    label("Function_2_747")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_75C")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_747")

    label("loc_75C")

    Return()

    # Function_2_747 end

    def Function_3_75D(): pass

    label("Function_3_75D")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_780")
    OP_8D(0xFE, -30720, 37410, -25780, 40750, 3000)
    Jump("Function_3_75D")

    label("loc_780")

    Return()

    # Function_3_75D end

    def Function_4_781(): pass

    label("Function_4_781")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_78E")
    Jump("loc_A0E")

    label("loc_78E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_827")

    ChrTalk(    #0
        0xFE,
        (
            "My next target is the big\x01",
            "Birthday Celebration Sale\x01",
            "back at the capital!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        (
            "I'd better take it easy here\x01",
            "while I still have the chance.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A0E")

    label("loc_827")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_8E4")

    ChrTalk(    #2
        0xFE,
        (
            "I heard a little from the staff,\x01",
            "but was there some kind of\x01",
            "incident in Zeiss?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0xFE,
        (
            "News has spread this far just by\x01",
            "word of mouth, so it must be\x01",
            "quite an affair over there.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A0E")

    label("loc_8E4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_94E")

    ChrTalk(    #4
        0xFE,
        "Ah, relaxing in the hot springs...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0xFE,
        (
            "Gotta get my energy up for\x01",
            "the next shopping trip!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A0E")

    label("loc_94E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 6)), scpexpr(EXPR_END)), "loc_958")
    Jump("loc_A0E")

    label("loc_958")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 2)), scpexpr(EXPR_END)), "loc_9F3")

    ChrTalk(    #6
        0xFE,
        (
            "I bought a couple of the cutest\x01",
            "plates today without even\x01",
            "thinking about it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0xFE,
        (
            "There are still things to see in\x01",
            "that souvenir shop, too.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A0E")

    label("loc_9F3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 7)), scpexpr(EXPR_END)), "loc_9FD")
    Jump("loc_A0E")

    label("loc_9FD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_A07")
    Jump("loc_A0E")

    label("loc_A07")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_A0E")

    label("loc_A0E")

    TalkEnd(0xFE)
    Return()

    # Function_4_781 end

    def Function_5_A12(): pass

    label("Function_5_A12")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_A1F")
    Jump("loc_C7D")

    label("loc_A1F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_AC3")

    ChrTalk(    #8
        0xFE,
        (
            "After talking it over with my\x01",
            "wife, I've decided to stay here\x01",
            "a while longer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0xFE,
        (
            "I plan to get back just before the\x01",
            "queen's birthday celebrations.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C7D")

    label("loc_AC3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_ACD")
    Jump("loc_C7D")

    label("loc_ACD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_B4F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_B0A")

    ChrTalk(    #10
        0xFE,
        "I think I'll take a quick morning dip.\x02",
    )

    CloseMessageWindow()
    Jump("loc_B4C")

    label("loc_B0A")

    OP_A2(0xA)

    ChrTalk(    #11
        0xFE,
        "Are you leaving already?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0xFE,
        "We're going to stay longer.\x02",
    )

    CloseMessageWindow()

    label("loc_B4C")

    Jump("loc_C7D")

    label("loc_B4F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 6)), scpexpr(EXPR_END)), "loc_B59")
    Jump("loc_C7D")

    label("loc_B59")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 2)), scpexpr(EXPR_END)), "loc_C62")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_BD6")

    ChrTalk(    #13
        0xFE,
        (
            "Edel's already off shopping at\x01",
            "the souvenir shop.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0xFE,
        (
            "I can't take my eyes off her\x01",
            "for even a minute!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C5F")

    label("loc_BD6")

    OP_A2(0xA)

    ChrTalk(    #15
        0xFE,
        (
            "The minute I take my eyes off\x01",
            "her, my wife goes scurrying to\x01",
            "the gift shop.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0xFE,
        (
            "I can't take my eyes off her\x01",
            "for even a minute!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C5F")

    Jump("loc_C7D")

    label("loc_C62")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 7)), scpexpr(EXPR_END)), "loc_C6C")
    Jump("loc_C7D")

    label("loc_C6C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_C76")
    Jump("loc_C7D")

    label("loc_C76")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_C7D")

    label("loc_C7D")

    TalkEnd(0xFE)
    Return()

    # Function_5_A12 end

    def Function_6_C81(): pass

    label("Function_6_C81")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_E32")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_D57")

    ChrTalk(    #17
        0xFE,
        (
            "Ah, it's nice to have some down\x01",
            "time for a change.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0xFE,
        (
            "May as well make the most\x01",
            "of it and check my stock.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0xFE,
        (
            "You never know when the next\x01",
            "batch of customers will walk\x01",
            "through the door.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E2F")

    label("loc_D57")

    OP_A2(0x2)

    ChrTalk(    #20
        0xFE,
        (
            "Ah, it's nice to have some down\x01",
            "time for a change.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0xFE,
        (
            "Still though, why do people always\x01",
            "come on the same days?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0xFE,
        (
            "If they'd just stagger their visits\x01",
            "they'd have more room in the\x01",
            "springs for themselves.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E2F")

    Jump("loc_13A9")

    label("loc_E32")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_EAF")

    ChrTalk(    #23
        0xFE,
        (
            "So, is the investigation coming\x01",
            "along smoothly?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0xFE,
        (
            "I'm busy as usual here. Then again,\x01",
            "it's always just me.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_13A9")

    label("loc_EAF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_F72")

    ChrTalk(    #25
        0xFE,
        (
            "Oh, so it's my turn for\x01",
            "your questions?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0xFE,
        (
            "Word's spread already. Something was\x01",
            "stolen from the central factory, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0xFE,
        (
            "You bracers sure are a hard workin'\x01",
            "bunch of people.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_13A9")

    label("loc_F72")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_FCF")

    ChrTalk(    #28
        0xFE,
        "Are you leaving already?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0xFE,
        (
            "When you have some time off,\x01",
            "come and visit us!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_13A9")

    label("loc_FCF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 6)), scpexpr(EXPR_END)), "loc_10EA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_1070")

    ChrTalk(    #30
        0xFE,
        (
            "This Eastern cooking's not\x01",
            "only good, but healthy too!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0xFE,
        (
            "It takes more time to prepare,\x01",
            "but it's worth it when you sit\x01",
            "down and eat it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10E7")

    label("loc_1070")

    OP_A2(0x2)

    ChrTalk(    #32
        0xFE,
        "Off to the bath? Enjoy!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0xFE,
        (
            "I'll be preparing your exotic\x01",
            "Eastern dinner while you're\x01",
            "freshening up in there.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_10E7")

    Jump("loc_13A9")

    label("loc_10EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 2)), scpexpr(EXPR_END)), "loc_11FA")

    ChrTalk(    #34
        0xFE,
        (
            "Sorry about that little problem\x01",
            "we had before.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0xFE,
        (
            "I was relieved to hear that the\x01",
            "guest was okay.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0xFE,
        (
            "Which is all well and good, but\x01",
            "I should get dinner cooking.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0xFE,
        (
            "We're going to have much better\x01",
            "business now that we've finally\x01",
            "got customers coming.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_13A9")

    label("loc_11FA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 7)), scpexpr(EXPR_END)), "loc_128C")

    ChrTalk(    #38
        0xFE,
        (
            "I can't believe there are bracers here.\x01",
            "That makes me feel a lot better.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0xFE,
        (
            "I leave the customer's safety in\x01",
            "your capable hands!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_13A9")

    label("loc_128C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_1296")
    Jump("loc_13A9")

    label("loc_1296")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_13A9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_1319")

    ChrTalk(    #40
        0xFE,
        (
            "It's nice to have slow days like\x01",
            "this sometimes...but every day\x01",
            "would be bad.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0xFE,
        "People love their luxury.\x02",
    )

    CloseMessageWindow()
    Jump("loc_13A9")

    label("loc_1319")

    OP_A2(0x2)

    ChrTalk(    #42
        0xFE,
        "What a quiet day.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0xFE,
        (
            "Days like this are nice from\x01",
            "time to time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0xFE,
        (
            "If every day was like this though,\x01",
            "it would be bad for business.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_13A9")

    TalkEnd(0xFE)
    Return()

    # Function_6_C81 end

    def Function_7_13AD(): pass

    label("Function_7_13AD")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_13BA")
    Jump("loc_1731")

    label("loc_13BA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_1488")

    ChrTalk(    #45
        0xFE,
        "I feel all rested up!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0xFE,
        (
            "I get the feeling that if I cast\x01",
            "some bait, I'll catch the\x01",
            "biggest fish of my life.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0xFE,
        (
            "But it won't last. I better get\x01",
            "fishing while I still feel this\x01",
            "motivated!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1731")

    label("loc_1488")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_1504")

    ChrTalk(    #48
        0xFE,
        (
            "I heard you mention it, but was\x01",
            "there some kind of incident\x01",
            "in Zeiss?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0xFE,
        (
            "Hmph.\x01",
            "What's the world coming to?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1731")

    label("loc_1504")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_150E")
    Jump("loc_1731")

    label("loc_150E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 6)), scpexpr(EXPR_END)), "loc_15C1")

    ChrTalk(    #50
        0xFE,
        (
            "Are you all staying the night\x01",
            "here as well?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0xFE,
        (
            "If you haven't been in the outdoor\x01",
            "bath, I really recommend you go\x01",
            "try it right now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0xFE,
        "It made a fan out of me!\x02",
    )

    CloseMessageWindow()
    Jump("loc_1731")

    label("loc_15C1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 2)), scpexpr(EXPR_END)), "loc_15CB")
    Jump("loc_1731")

    label("loc_15CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_172A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_16A9")

    ChrTalk(    #53
        0xFE,
        (
            "Even when you can't get into the\x01",
            "bath, there's lots of stuff you can\x01",
            "go do around here!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0xFE,
        (
            "The big draw of the Maple Leaf\x01",
            "Inn is its cooking.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0xFE,
        (
            "It's heaven. I can hardly wait\x01",
            "for dinnertime!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1727")

    label("loc_16A9")

    OP_A2(0x1)

    ChrTalk(    #56
        0xFE,
        (
            "It seems like the pump that \x01",
            "carries the water is broken.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0xFE,
        (
            "Well, this is an old resort town.\x01",
            "Those things happen.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1727")

    Jump("loc_1731")

    label("loc_172A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_1731")

    label("loc_1731")

    TalkEnd(0xFE)
    Return()

    # Function_7_13AD end

    def Function_8_1735(): pass

    label("Function_8_1735")

    TalkBegin(0xFE)
    TalkEnd(0xFE)
    Return()

    # Function_8_1735 end

    def Function_9_173C(): pass

    label("Function_9_173C")

    TalkBegin(0xFE)
    TalkEnd(0xFE)
    Return()

    # Function_9_173C end

    def Function_10_1743(): pass

    label("Function_10_1743")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_1750")
    Jump("loc_1B76")

    label("loc_1750")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_1879")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_17EB")

    ChrTalk(    #58
        0xFE,
        (
            "I hope the criminals behind the\x01",
            "factory attack are found and\x01",
            "arrested soon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0xFE,
        (
            "We can't just let people like\x01",
            "that run around free!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1876")

    label("loc_17EB")

    OP_A2(0x5)

    ChrTalk(    #60
        0xFE,
        "Hello there. Still busy?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0xFE,
        (
            "I heard about you guys from Ed.\x01",
            "So, you're all bracers?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0xFE,
        (
            "Well, good luck. We're rooting\x01",
            "for you!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1876")

    Jump("loc_1B76")

    label("loc_1879")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_1883")
    Jump("loc_1B76")

    label("loc_1883")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_188D")
    Jump("loc_1B76")

    label("loc_188D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 6)), scpexpr(EXPR_END)), "loc_1897")
    Jump("loc_1B76")

    label("loc_1897")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 2)), scpexpr(EXPR_END)), "loc_19C0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 5)), scpexpr(EXPR_END)), "loc_18D8")

    ChrTalk(    #63
        0xFE,
        "Hi there!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0xFE,
        "The Yuzu room is next door.\x02",
    )

    CloseMessageWindow()
    Jump("loc_19BD")

    label("loc_18D8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_1948")

    ChrTalk(    #65
        0xFE,
        "I need to turn the beds down.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0xFE,
        (
            "And I need to get dinner ready\x01",
            "before the customers return...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_19BD")

    label("loc_1948")

    OP_A2(0x5)

    ChrTalk(    #67
        0xFE,
        (
            "The pump's been fixed?\x01",
            "That's wonderful news!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0xFE,
        (
            "We're so indebted to the people\x01",
            "from the central factory.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_19BD")

    Jump("loc_1B76")

    label("loc_19C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1B6F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_1AC3")

    ChrTalk(    #69
        0xFE,
        "I've got this problem...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0xFE,
        (
            "It seems the pump for the hot\x01",
            "springs is broken.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0xFE,
        (
            "If we don't hurry and fix it, we risk\x01",
            "losing a lot of our customers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0xFE,
        (
            "I mean, this IS a hot springs resort.\x01",
            "The operative word here being 'hot.'\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1B6C")

    label("loc_1AC3")

    OP_A2(0x5)

    ChrTalk(    #73
        0xFE,
        "Welcome to the Maple Leaf Inn!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0xFE,
        (
            "All of our rooms have special names.\x01",
            "This is the Yuzu room.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0xFE,
        (
            "I feel the names are so much more\x01",
            "personal than 'Room 201.'\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B6C")

    Jump("loc_1B76")

    label("loc_1B6F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_1B76")

    label("loc_1B76")

    TalkEnd(0xFE)
    Return()

    # Function_10_1743 end

    def Function_11_1B7A(): pass

    label("Function_11_1B7A")

    Call(0, 12)
    Return()

    # Function_11_1B7A end

    def Function_12_1B7F(): pass

    label("Function_12_1B7F")

    TalkBegin(0xF)
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "Talk\x01",                              # 0
            "Shop\x01",                              # 1
            "[Wild Veggie Pot] - 700 mira\x01",      # 2
            "Leave\x01",                             # 3
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1BFC")
    OP_0D()
    OP_A9(0x46)
    OP_56(0x0)
    TalkEnd(0xF)
    Return()

    label("loc_1BFC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1D0A")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x12), scpexpr(EXPR_PUSH_LONG, 0x2BC), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1CD0")
    SubMira(700)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetMessageWindowPos(-1, -1, -1, -1)
    OP_22(0xB, 0x0, 0x64)

    AnonymousTalk(    #76
        "\x06\x07\x00Ate \x07\x02Wild Veggie Pot\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_31(0x0, 0xFD, 0x2BC)
    OP_31(0x1, 0xFD, 0x2BC)
    OP_31(0x2, 0xFD, 0x2BC)
    OP_31(0x3, 0xFD, 0x2BC)
    OP_31(0x4, 0xFD, 0x2BC)
    OP_31(0x5, 0xFD, 0x2BC)
    OP_31(0x6, 0xFD, 0x2BC)
    OP_31(0x7, 0xFD, 0x2BC)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x20D)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1CC2")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_AC(0x4)"), scpexpr(EXPR_END)), "loc_1C91")
    Jump("loc_1CC2")

    label("loc_1C91")

    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #77
        "\x06\x07\x00Learned '\x07\x02Wild Veggie Pot\x07\x00' recipe.\x02",
    )

    CloseMessageWindow()

    label("loc_1CC2")

    OP_56(0x0)
    FadeToBright(1000, 0)
    Jump("loc_1CF8")

    label("loc_1CD0")

    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #78
        "Insufficient mira.\x02",
    )

    CloseMessageWindow()
    FadeToBright(300, 0)

    label("loc_1CF8")

    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xF)
    Return()

    label("loc_1D0A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1D1B")
    TalkEnd(0xF)
    Return()

    label("loc_1D1B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_1E20")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_1D98")

    ChrTalk(    #79
        0xF,
        (
            "Let's get this cleaning out of\x01",
            "the way right now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0xF,
        (
            "We'll be full of customers before\x01",
            "we can blink.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E1D")

    label("loc_1D98")

    OP_A2(0x6)

    ChrTalk(    #81
        0xF,
        (
            "Hello!\x01",
            "Welcome to the Maple Leaf Inn!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0xF,
        (
            "We welcome everyone, especially\x01",
            "those en route to the royal birthday\x01",
            "festivities!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E1D")

    Jump("loc_20D8")

    label("loc_1E20")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_1E2A")
    Jump("loc_20D8")

    label("loc_1E2A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_1EDD")

    ChrTalk(    #83
        0xF,
        (
            "All people wanted to talk about\x01",
            "today was that incident in Zeiss.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0xF,
        (
            "Here they are in a great resort\x01",
            "and that's what they all want\x01",
            "to discuss...how sad for them.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_20D8")

    label("loc_1EDD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_1F3E")

    ChrTalk(    #85
        0xF,
        (
            "Leaving so soon? You all are\x01",
            "awfully busy, aren't you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #86
        0xF,
        "Come back again soon!\x02",
    )

    CloseMessageWindow()
    Jump("loc_20D8")

    label("loc_1F3E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 6)), scpexpr(EXPR_END)), "loc_1FC7")

    ChrTalk(    #87
        0xF,
        (
            "Our exotic Eastern cooking tastes\x01",
            "even better after a long, hot bath!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0xF,
        (
            "Make sure you sweat yourselves\x01",
            "up an appetite!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_20D8")

    label("loc_1FC7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 2)), scpexpr(EXPR_END)), "loc_203E")

    ChrTalk(    #89
        0xF,
        "Hello there!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0xF,
        (
            "Rooms are on the second floor.\x01",
            "The front desk is over there,\x01",
            "just next to the stairs.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_20D8")

    label("loc_203E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 7)), scpexpr(EXPR_END)), "loc_2048")
    Jump("loc_20D8")

    label("loc_2048")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_2052")
    Jump("loc_20D8")

    label("loc_2052")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_20D8")

    ChrTalk(    #91
        0xF,
        (
            "Hello, and welcome to the\x01",
            "Maple Leaf Inn.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0xF,
        (
            "We also have authentic Eastern\x01",
            "cuisine. We hope you have a\x01",
            "wonderful time!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_20D8")

    TalkEnd(0xF)
    Return()

    # Function_12_1B7F end

    def Function_13_20DC(): pass

    label("Function_13_20DC")

    TalkBegin(0xFE)

    ChrTalk(    #93
        0xFE,
        (
            "#151FIsn't fruity milk after a soak in\x01",
            "the hot spring just DIVINE?\x02\x03",

            "I love the cool sweet taste after\x01",
            "all that hot steam.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_13_20DC end

    def Function_14_2162(): pass

    label("Function_14_2162")

    TalkBegin(0xFE)
    TalkEnd(0xFE)
    Return()

    # Function_14_2162 end

    def Function_15_2169(): pass

    label("Function_15_2169")

    TalkBegin(0xFE)
    TalkEnd(0xFE)
    Return()

    # Function_15_2169 end

    def Function_16_2170(): pass

    label("Function_16_2170")

    TalkBegin(0xFE)
    TalkEnd(0xFE)
    Return()

    # Function_16_2170 end

    def Function_17_2177(): pass

    label("Function_17_2177")

    Call(0, 18)
    Return()

    # Function_17_2177 end

    def Function_18_217C(): pass

    label("Function_18_217C")

    TalkBegin(0x9)
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "Talk\x01",       # 0
            "Rest\x01",       # 1
            "Leave\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_21DC")
    OP_0D()
    OP_A9(0x45)
    OP_56(0x0)
    TalkEnd(0x9)
    Return()

    label("loc_21DC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_21ED")
    TalkEnd(0x9)
    Return()

    label("loc_21ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2825")
    ClearMapFlags(0x1)
    OP_66(0x0)
    OP_69(0x9, 0x3E8)
    OP_A2(0x525)
    OP_28(0x40, 0x1, 0x800)
    OP_28(0x40, 0x4, 0x10)

    ChrTalk(    #94
        0x9,
        (
            "#680FThank you, Tita!\x02\x03",

            "The pump's pumping like it was\x01",
            "just installed yesterday!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0x107,
        (
            "#060FHee hee. Really?\x02\x03",

            "Please think nothing of it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #96
        0x9,
        (
            "#680FWell, haven't you grown into such\x01",
            "a well mannered young lady?\x02\x03",

            "And thank you two for that\x01",
            "last time as well.\x02\x03",

            "You guys know everyone,\x01",
            "it seems.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0x101,
        "#000FHa ha, I guess we do...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0x107,
        (
            "#060F???\x02\x03",

            "What happened?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0x102,
        "#010FA little bracer business.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0x9,
        (
            "#680FYou two have my thanks.\x02\x03",

            "As a way to pay you back, I'd\x01",
            "like you to stay here free.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0x101,
        "#000FNo way! Really?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0x107,
        (
            "#060FMa'am?\x02\x03",

            "We didn't tell my grandfather we\x01",
            "were going to stay here...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0x9,
        (
            "#680FNonsense. I heard from Russell\x01",
            "a little earlier.\x02\x03",

            "He said the job would take him\x01",
            "until tomorrow to finish, and he\x01",
            "asked if you could stay here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0x107,
        "#060FGrandpa said that?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0x101,
        "#000FWhat a sweet old guy!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #106
        0x102,
        (
            "#010FWell, if he said that, then I'm\x01",
            "afraid we have no choice but\x01",
            "to impose for the night.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0x9,
        (
            "#680FCome right in.\x02\x03",

            "You can put your things in the\x01",
            "Yuzu room on the second floor.\x02\x03",

            "It'll be some time before dinner,\x01",
            "so go take a dip in the hot springs.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #108
        0x101,
        (
            "#000FYou want us to take a bath\x01",
            "before dinner?\x02\x03",

            "I thought people took their baths\x01",
            "before they went to sleep.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #109
        0x9,
        (
            "#680FWhat are you talking about?\x01",
            "This is a HOT SPRINGS resort!\x02\x03",

            "People expect you to jump\x01",
            "in the bath in the morning,\x01",
            "at lunch...whenever!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #110
        0x107,
        (
            "#060FI'd be okay with three baths\x01",
            "a day here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0x101,
        (
            "#000FR-Really?\x02\x03",

            "Well, I like baths as much as\x01",
            "anybody, but it sounds a little\x01",
            "bit much for me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #112
        0x102,
        (
            "#010FHa ha. Shall we go put our bags\x01",
            "in our room, then?\x02",
        )
    )

    CloseMessageWindow()
    OP_69(0x0, 0x3E8)
    SetMapFlags(0x1)
    OP_66(0x1)
    Jump("loc_3353")

    label("loc_2825")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_2ACE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_2890")

    ChrTalk(    #113
        0x9,
        (
            "#680FCome back and stay with us\x01",
            "any time you want!\x02\x03",

            "Have a safe trip to the capital!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2ACB")

    label("loc_2890")

    OP_A2(0x0)

    ChrTalk(    #114
        0x9,
        (
            "#680FHello, you all. Any luck catching\x01",
            "your target?\x02\x03",

            "If so, why not take a break and\x01",
            "stay for a while?\x02\x03",

            "We have a reservation only\x01",
            "outdoor bath for customers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0x101,
        (
            "#000FThat sounds so lovely, but...\x02\x03",

            "We've got to get to the\x01",
            "capital right away.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #116
        0x102,
        (
            "#010FAs always, we appreciate\x01",
            "your hospitality.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #117
        0x9,
        (
            "#680FDon't worry about it! It's our\x01",
            "thanks for fixing the pump.\x02\x03",

            "And Tita's off to help Russell\x01",
            "again, no doubt?\x02\x03",

            "You tell him I said not to\x01",
            "overwork that poor girl.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #118
        0x101,
        (
            "#000FUh...\x02\x03",

            "...Okay!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #119
        0x102,
        "#010FWe'll tell him.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #120
        0x9,
        "#680FHave a safe trip to the capital!\x02",
    )

    CloseMessageWindow()

    label("loc_2ACB")

    Jump("loc_3353")

    label("loc_2ACE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_2B9F")

    ChrTalk(    #121
        0x9,
        (
            "#680FHello again, everybody.\x02\x03",

            "Just running all over looking\x01",
            "for your criminals, aren't you?\x02\x03",

            "I'm sorry to say we haven't\x01",
            "got any clues or heard any\x01",
            "more information.\x02\x03",

            "I wish we could help more.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3353")

    label("loc_2B9F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_2D40")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_2C8C")

    ChrTalk(    #122
        0x9,
        (
            "#680FTita dear, what's wrong?\x02\x03",

            "You look awfully pale.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #123
        0x107,
        (
            "#060FIt's nothing.\x02\x03",

            "I'm just a little tired.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #124
        0x9,
        (
            "#680FWell, don't overdo it.\x02\x03",

            "You're just like Russell. I worry\x01",
            "you get too caught up in things\x01",
            "sometimes.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2D3D")

    label("loc_2C8C")

    OP_A2(0x0)

    ChrTalk(    #125
        0x9,
        (
            "#680FHello! How have you been?\x02\x03",

            "I heard about the burglary at\x01",
            "the central factory. It had\x01",
            "me a little bit worried.\x02\x03",

            "Still, these things do happen.\x01",
            "A shame, but still...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2D3D")

    Jump("loc_3353")

    label("loc_2D40")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_2DA0")

    ChrTalk(    #126
        0x9,
        (
            "#680FWell, that was quick.\x02\x03",

            "Did you want to have another\x01",
            "dip in the hot springs?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3353")

    label("loc_2DA0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 6)), scpexpr(EXPR_END)), "loc_2E36")

    ChrTalk(    #127
        0x9,
        (
            "#680FThe bath is separate from the\x01",
            "hotel. Go through the restaurant\x01",
            "to get there.\x02\x03",

            "We're especially proud of that\x01",
            "outdoor bath. Enjoy!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3353")

    label("loc_2E36")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 2)), scpexpr(EXPR_END)), "loc_31D5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 4)), scpexpr(EXPR_END)), "loc_2EBC")

    ChrTalk(    #128
        0x9,
        (
            "#680FYou're all in the Yuzu room,\x01",
            "on the second floor.\x02\x03",

            "Drop off your things and go enjoy\x01",
            "a bath before dinner.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_31D2")

    label("loc_2EBC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB1, 5)), scpexpr(EXPR_END)), "loc_2F75")

    ChrTalk(    #129
        0x9,
        (
            "#680FThat girl is just like Russell...\x01",
            "Put her in front of a machine\x01",
            "and she just won't stop.\x02\x03",

            "Sorry to be an imposition,\x01",
            "but could you go check\x01",
            "on the pump shed for me?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_31D2")

    label("loc_2F75")

    OP_A2(0x58D)

    ChrTalk(    #130
        0x9,
        (
            "#680FGood work, you all.\x02\x03",

            "Did you know that guest?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #131
        0x101,
        (
            "#000FAh...ha...ha...\x01",
            "Unfortunately...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #132
        0x102,
        (
            "#010FIt looks like the pump repairs\x01",
            "are complete.\x02\x03",

            "The front well should fill back\x01",
            "up with hot water soon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #133
        0x9,
        (
            "#680FIs that right, now?\x02\x03",

            "But Tita hasn't come back.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #134
        0x101,
        (
            "#000FAh, yeah. Guess we should've\x01",
            "gone to the pump shed first,\x01",
            "before reporting back here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #135
        0x102,
        "#010FWell, let's go, then!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #136
        0x9,
        (
            "#680FPlease do.\x02\x03",

            "That girl is just like Russell...\x01",
            "Put her in front of a machine\x01",
            "and she just won't stop.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #137
        0x101,
        "#000FIsn't that the truth!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #138
        0x102,
        "#010FWe'll go have a look.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #139
        0x9,
        "#680FOkay. Thanks again.\x02",
    )

    CloseMessageWindow()

    label("loc_31D2")

    Jump("loc_3353")

    label("loc_31D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 7)), scpexpr(EXPR_END)), "loc_323E")

    ChrTalk(    #140
        0x9,
        (
            "#680FI'll trust you two to fix it.\x02\x03",

            "Head on out and see if you can\x01",
            "bring that guest back.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3353")

    label("loc_323E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_32BE")

    ChrTalk(    #141
        0x9,
        (
            "#680FWhat, did you forget where the\x01",
            "pump is?\x02\x03",

            "It's in a shed up north past the\x01",
            "town square.\x02\x03",

            "Good luck, you all.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3353")

    label("loc_32BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_3353")

    ChrTalk(    #142
        0x9,
        (
            "#680FWelcome, everyone! This is the\x01",
            "famous Maple Leaf Inn.\x02\x03",

            "We have many fine springs,\x01",
            "including our famous Eastern-\x01",
            "style outdoor bath!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3353")

    TalkEnd(0x9)
    Return()

    # Function_18_217C end

    def Function_19_3357(): pass

    label("Function_19_3357")

    EventBegin(0x0)
    ClearMapFlags(0x1)
    OP_6D(10910, 0, 69600, 0)
    SetChrPos(0x101, 11690, 0, 68340, 180)
    SetChrPos(0x102, 11420, 0, 67000, 45)
    SetChrPos(0x107, 12710, 0, 66950, 315)
    FadeToBright(2000, 0)
    OP_0D()

    ChrTalk(    #143
        0x101,
        (
            "#502F#2POkay...\x01",
            "The luggage is secure!\x02\x03",

            "#505FSo, where's this spa, now?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #144
        0x107,
        (
            "#560F#5POh, there's a separate bath\x01",
            "behind the building.\x02\x03",

            "It's a big open-air bath.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #145
        0x102,
        (
            "#010F#1PYou mean it's basically\x01",
            "outside, then?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #146
        0x101,
        (
            "#006F#2POooohh, that sounds neat!\x02\x03",

            "#001FLet's go!\x02",
        )
    )

    CloseMessageWindow()
    ClearMapFlags(0x10000000)
    EventEnd(0x0)
    Return()

    # Function_19_3357 end

    def Function_20_34C5(): pass

    label("Function_20_34C5")

    EventBegin(0x0)
    ClearMapFlags(0x1)
    OP_6D(12630, 0, 1940, 0)
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x102, 0x80)
    SetChrFlags(0x107, 0x80)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x14, 0x80)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x4)
    SetChrPos(0x8, 14070, 0, 2040, 180)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x19, 0x80)
    ClearChrFlags(0x1A, 0x80)
    SetChrPos(0x16, 14600, 750, 1030, 0)
    SetChrPos(0x17, 13500, 700, 950, 0)
    SetChrPos(0x18, 13380, 700, 500, 0)
    SetChrPos(0x19, 13870, 700, 660, 0)
    SetChrPos(0x1A, 13800, 700, 310, 0)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(    #147
        0x8,
        (
            "#152F#4PMan... They're sooooo late.\x02\x03",

            "Ugh... I drank too much fruity milk.\x01",
            "Now my stomach's all messed up...\x02",
        )
    )

    CloseMessageWindow()
    OP_20(0xBB8)
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(500)

    AnonymousTalk(    #148
        (
            "\x07\x05After getting out of the spa, Estelle and company tried to soothe Dorothy's\x01",
            "annoyance with some of the inn's fine Eastern cuisine.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #149
        (
            "\x07\x05This was followed by an enjoyable game of cards, after which they returned\x01",
            "to the spa.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #150
        "\x07\x05And so, the evening wore on comfortably...\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_22(0xD, 0x0, 0x64)
    OP_31(0x0, 0xFE, 0x0)
    OP_31(0x1, 0xFE, 0x0)
    OP_31(0x2, 0xFE, 0x0)
    OP_31(0x3, 0xFE, 0x0)
    OP_31(0x4, 0xFE, 0x0)
    OP_31(0x5, 0xFE, 0x0)
    OP_31(0x6, 0xFE, 0x0)
    OP_31(0x7, 0xFE, 0x0)
    Sleep(5000)
    OP_21()
    OP_A2(0x3FA)
    NewScene("ED6_DT01/T3200   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_20_34C5 end

    def Function_21_3765(): pass

    label("Function_21_3765")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #151
        "\x07\x05Open-Air Bath ⇒\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_21_3765 end

    SaveToFile()

Try(main)

from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'U7003   ._SN',
        MapName             = 'Gaiden2',
        Location            = 'U7003.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60210",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            '',
            '',
            '',
            '',
            'ED6_DT21/U7003_4 ._SN',
            'ED6_DT21/U7003_5 ._SN',
            'ED6_DT21/SUB000  ._SN',
            ''
        ],
    )

    BuildStringList(
        '@FileName',                            # 8
        '凯文',                                 # 9
        '莉丝',                                 # 10
        '提妲',                                 # 11
        '尤莉亚\u3000\u3000\u3000\u3000\u3000\u3000\u3000',# 12
        '穆拉',                                 # 13
        '乔丝特',                               # 14
        '约修亚',                               # 15
        '科洛丝',                               # 16
        '基库',                                 # 17
        '奥利维尔',                             # 18
        '金',                                   # 19
        '亚妮拉丝',                             # 20
        '雪拉扎德',                             # 21
        '阿加特',                               # 22
        '艾丝蒂尔',                             # 23
        '理查德',                               # 24
        '玲',                                   # 25
        '亚妮拉丝',                             # 26
        '',                                     # 27
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


    AddCharChip(
        'ED6_DT26/CH20625 ._CH',             # 00
        'ED6_DT27/CH03080 ._CH',             # 01
        'ED6_DT27/CH03150 ._CH',             # 02
        'ED6_DT07/CH00060 ._CH',             # 03
        'ED6_DT27/CH03580 ._CH',             # 04
        'ED6_DT27/CH03570 ._CH',             # 05
        'ED6_DT27/CH03100 ._CH',             # 06
        'ED6_DT27/CH03250 ._CH',             # 07
        'ED6_DT27/CH03210 ._CH',             # 08
        'ED6_DT07/CH02323 ._CH',             # 09
        'ED6_DT27/CH03260 ._CH',             # 0A
        'ED6_DT07/CH00070 ._CH',             # 0B
        'ED6_DT07/CH01630 ._CH',             # 0C
        'ED6_DT27/CH03240 ._CH',             # 0D
        'ED6_DT06/CH20053 ._CH',             # 0E
        'ED6_DT26/CH20255 ._CH',             # 0F
        'ED6_DT07/CH02030 ._CH',             # 10
        'ED6_DT27/CH03510 ._CH',             # 11
        'ED6_DT27/CH03263 ._CH',             # 12
        'ED6_DT27/CH03573 ._CH',             # 13
        'ED6_DT27/CH03213 ._CH',             # 14
        'ED6_DT27/CH03264 ._CH',             # 15
        'ED6_DT27/CH03513 ._CH',             # 16
        'ED6_DT26/CH20607 ._CH',             # 17
        'ED6_DT27/CH03153 ._CH',             # 18
        'ED6_DT07/CH00063 ._CH',             # 19
        'ED6_DT27/CH03470 ._CH',             # 1A
        'ED6_DT27/CH03473 ._CH',             # 1B
        'ED6_DT07/CH00073 ._CH',             # 1C
        'ED6_DT07/CH00053 ._CH',             # 1D
        'ED6_DT26/CH20822 ._CH',             # 1E
        'ED6_DT27/CH03000 ._CH',             # 1F
        'ED6_DT27/CH03001 ._CH',             # 20
        'ED6_DT26/CH20822 ._CH',             # 21
        'ED6_DT07/CH02093 ._CH',             # 22
    )

    AddCharChipPat(
        'ED6_DT26/CH20625P._CP',             # 00
        'ED6_DT27/CH03080P._CP',             # 01
        'ED6_DT27/CH03150P._CP',             # 02
        'ED6_DT07/CH00060P._CP',             # 03
        'ED6_DT27/CH03580P._CP',             # 04
        'ED6_DT27/CH03570P._CP',             # 05
        'ED6_DT27/CH03100P._CP',             # 06
        'ED6_DT27/CH03250P._CP',             # 07
        'ED6_DT27/CH03210P._CP',             # 08
        'ED6_DT07/CH02323P._CP',             # 09
        'ED6_DT27/CH03260P._CP',             # 0A
        'ED6_DT07/CH00070P._CP',             # 0B
        'ED6_DT07/CH01630P._CP',             # 0C
        'ED6_DT27/CH03240P._CP',             # 0D
        'ED6_DT06/CH20053P._CP',             # 0E
        'ED6_DT26/CH20255P._CP',             # 0F
        'ED6_DT07/CH02030P._CP',             # 10
        'ED6_DT27/CH03510P._CP',             # 11
        'ED6_DT27/CH03263P._CP',             # 12
        'ED6_DT27/CH03573P._CP',             # 13
        'ED6_DT27/CH03213P._CP',             # 14
        'ED6_DT27/CH03264P._CP',             # 15
        'ED6_DT27/CH03513P._CP',             # 16
        'ED6_DT26/CH20607P._CP',             # 17
        'ED6_DT27/CH03153P._CP',             # 18
        'ED6_DT07/CH00063P._CP',             # 19
        'ED6_DT27/CH03470P._CP',             # 1A
        'ED6_DT27/CH03473P._CP',             # 1B
        'ED6_DT07/CH00073P._CP',             # 1C
        'ED6_DT07/CH00053P._CP',             # 1D
        'ED6_DT26/CH20822P._CP',             # 1E
        'ED6_DT27/CH03000P._CP',             # 1F
        'ED6_DT27/CH03001P._CP',             # 20
        'ED6_DT26/CH20822P._CP',             # 21
        'ED6_DT07/CH02093P._CP',             # 22
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
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 5,
        TalkScenaIndex      = 2,
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
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 5,
        TalkScenaIndex      = 8,
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
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 5,
        TalkScenaIndex      = 11,
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
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 5,
        TalkScenaIndex      = 12,
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
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 5,
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
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 5,
        TalkScenaIndex      = 4,
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
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 5,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 9,
        ChipIndex           = 0x9,
        NpcIndex            = 0x185,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 15,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
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
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 5,
        TalkScenaIndex      = 5,
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
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 4,
        TalkScenaIndex      = 2,
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
        InitScenaIndex      = 18,
        TalkFunctionIndex   = 5,
        TalkScenaIndex      = 9,
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
        Unknown3            = 14,
        ChipIndex           = 0xE,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 5,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 31,
        ChipIndex           = 0x1F,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 5,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 16,
        ChipIndex           = 0x10,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 4,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 17,
        ChipIndex           = 0x11,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 5,
        TalkScenaIndex      = 13,
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
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclEvent(
        X                   = 4930,
        Y                   = 0,
        Z                   = -3270,
        Range               = 4000,
        Unknown_10          = 0x3E80,
        Unknown_14          = 0x0,
        Unknown_18          = 0x40,
        Unknown_1C          = 26,
    )

    DeclEvent(
        X                   = 48310,
        Y                   = 0,
        Z                   = -46340,
        Range               = 4000,
        Unknown_10          = 0x2710,
        Unknown_14          = 0x0,
        Unknown_18          = 0x40,
        Unknown_1C          = 2,
    )

    DeclEvent(
        X                   = 0,
        Y                   = 0,
        Z                   = 0,
        Range               = 0,
        Unknown_10          = 0x0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x2,
        Unknown_1C          = 8,
    )

    DeclEvent(
        X                   = 83340,
        Y                   = -15000,
        Z                   = -48360,
        Range               = 85140,
        Unknown_10          = 0xFFFFD508,
        Unknown_14          = 0xFFFF2522,
        Unknown_18          = 0x0,
        Unknown_1C          = 20,
    )

    DeclEvent(
        X                   = 85340,
        Y                   = -15000,
        Z                   = -48360,
        Range               = 87140,
        Unknown_10          = 0xFFFFD508,
        Unknown_14          = 0xFFFF2522,
        Unknown_18          = 0x0,
        Unknown_1C          = 21,
    )


    DeclActor(
        TriggerX            = 54440,
        TriggerZ            = 1800,
        TriggerY            = -47860,
        TriggerRange        = 1000,
        ActorX              = 54440,
        ActorZ              = 3000,
        ActorY              = -47860,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 7,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 52420,
        TriggerZ            = 2000,
        TriggerY            = -48240,
        TriggerRange        = 1500,
        ActorX              = 52420,
        ActorZ              = 2500,
        ActorY              = -48240,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 16,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 59580,
        TriggerZ            = 1000,
        TriggerY            = -41040,
        TriggerRange        = 1500,
        ActorX              = 57260,
        ActorZ              = 2500,
        ActorY              = -41880,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 17,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 63660,
        TriggerZ            = -11000,
        TriggerY            = -56430,
        TriggerRange        = 1800,
        ActorX              = 63660,
        ActorZ              = -10000,
        ActorY              = -56430,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 22,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 64129,
        TriggerZ            = -11000,
        TriggerY            = -49610,
        TriggerRange        = 1800,
        ActorX              = 64129,
        ActorZ              = -10000,
        ActorY              = -49610,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 25,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_556",          # 00, 0
        "Function_1_5E3",          # 01, 1
        "Function_2_7CF",          # 02, 2
        "Function_3_D84",          # 03, 3
        "Function_4_DC8",          # 04, 4
        "Function_5_DFD",          # 05, 5
        "Function_6_105B",         # 06, 6
        "Function_7_1B85",         # 07, 7
        "Function_8_1C3E",         # 08, 8
        "Function_9_1D0A",         # 09, 9
        "Function_10_2D0E",        # 0A, 10
        "Function_11_2D5F",        # 0B, 11
        "Function_12_3273",        # 0C, 12
        "Function_13_32A4",        # 0D, 13
        "Function_14_3357",        # 0E, 14
        "Function_15_339B",        # 0F, 15
        "Function_16_33F8",        # 10, 16
        "Function_17_33FD",        # 11, 17
        "Function_18_3402",        # 12, 18
        "Function_19_3442",        # 13, 19
        "Function_20_3466",        # 14, 20
        "Function_21_3495",        # 15, 21
        "Function_22_34C4",        # 16, 22
        "Function_23_3F0E",        # 17, 23
        "Function_24_3F90",        # 18, 24
        "Function_25_410B",        # 19, 25
        "Function_26_42D5",        # 1A, 26
        "Function_27_4315",        # 1B, 27
    )


    def Function_0_556(): pass

    label("Function_0_556")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5BE")
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (100, "loc_56E"),
        (SWITCH_DEFAULT, "loc_5BE"),
    )


    label("loc_56E")

    SetChrPos(0x0, 16880, 1000, -14940, 135)
    SetChrPos(0x1, 16880, 1000, -14940, 135)
    SetChrPos(0x2, 16880, 1000, -14940, 135)
    SetChrPos(0x3, 16880, 1000, -14940, 135)
    OP_30(0x1)
    OP_69(0x0, 0x0)
    Jump("loc_5BE")

    label("loc_5BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 4)), scpexpr(EXPR_END)), "loc_5DA")
    OP_A3(0x2504)
    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0xB8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 5)

    label("loc_5DA")

    Call(0, 11)
    Call(0, 9)
    Return()

    # Function_0_556 end

    def Function_1_5E3(): pass

    label("Function_1_5E3")

    OP_16(0x2, 0xFA0, 0xFFFE2082, 0xFFFD8D0C, 0x23007B)
    OP_10(0x0, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x584, 0)), scpexpr(EXPR_END)), "loc_60D")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0xD5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapFlags(0x2000000)

    label("loc_60D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x521, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x521, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_62B")
    OP_65(0x1, 0x1)
    Jump("loc_62F")

    label("loc_62B")

    OP_64(0x1, 0x1)

    label("loc_62F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x562, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x564, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_64D")
    OP_65(0x2, 0x1)
    Jump("loc_651")

    label("loc_64D")

    OP_64(0x2, 0x1)

    label("loc_651")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x581, 7)), scpexpr(EXPR_END)), "loc_6AB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4CE, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6A8")
    LoadEffect(0x1, "map\\mp257_00.eff")
    PlayEffect(0x1, 0x0, 0xFF, 63660, -10000, -56430, 0, 0, 0, 800, 800, 800, 0xFF, 0, 0, 0, 0)

    label("loc_6A8")

    Jump("loc_71B")

    label("loc_6AB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x500, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x501, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_70A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4CE, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_707")
    LoadEffect(0x1, "map\\mp257_00.eff")
    PlayEffect(0x1, 0x0, 0xFF, 63660, -10000, -56430, 0, 0, 0, 800, 800, 800, 0xFF, 0, 0, 0, 0)

    label("loc_707")

    Jump("loc_71B")

    label("loc_70A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4CE, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4CE, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_71B")
    OP_64(0x3, 0x1)

    label("loc_71B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x562, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x581, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_77A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4CE, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_777")
    LoadEffect(0x1, "map\\mp257_00.eff")
    PlayEffect(0x1, 0x0, 0xFF, 64129, -10000, -49610, 0, 0, 0, 800, 800, 800, 0xFF, 0, 0, 0, 0)

    label("loc_777")

    Jump("loc_786")

    label("loc_77A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4CE, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_786")
    OP_64(0x4, 0x1)

    label("loc_786")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7C1")
    OP_64(0x0, 0x1)
    OP_E5(0x1, 0xFF, 0x10, 262144)
    OP_E5(0x1, 0xFF, 0x11, 262144)
    OP_E5(0x1, 0xFF, 0x12, 262144)
    OP_E5(0x1, 0xFF, 0x13, 262144)
    OP_82(0x81, 0x0)
    OP_82(0x82, 0x0)
    OP_82(0x83, 0x0)
    OP_82(0x84, 0x0)
    OP_82(0x85, 0x0)

    label("loc_7C1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4E1, 0)), scpexpr(EXPR_END)), "loc_7CE")
    OP_C4(0x0, 0x200)

    label("loc_7CE")

    Return()

    # Function_1_5E3 end

    def Function_2_7CF(): pass

    label("Function_2_7CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C0, 4)), scpexpr(EXPR_END)), "loc_7D7")
    Return()

    label("loc_7D7")

    EventBegin(0x0)
    OP_8C(0x0, 135, 400)
    OP_62(0x0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    Fade(1000)
    SetChrPos(0x109, 39490, 1000, -38490, 135)
    SetChrPos(0x10F, 39420, 1000, -37080, 135)
    SetChrChipByIndex(0x109, 65535)
    SetChrSubChip(0x109, 0)
    SetChrChipByIndex(0x10F, 65535)
    SetChrSubChip(0x10F, 0)
    OP_6D(54910, 6000, -43800, 0)
    OP_67(0, 10110, -10000, 0)
    OP_6B(2700, 0)
    OP_6C(20000, 0)
    OP_6E(463, 0)
    OP_43(0x109, 0x0, 0x0, 0x3)
    OP_43(0x10F, 0x0, 0x0, 0x4)
    OP_0D()
    Sleep(1000)

    def lambda_88E():
        OP_6D(53620, 4350, -46260, 6000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_88E)

    def lambda_8A6():
        OP_67(0, 5190, -10000, 6000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_8A6)

    def lambda_8BE():
        OP_6B(3030, 6000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_8BE)

    def lambda_8CE():
        OP_6C(8000, 6000)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_8CE)

    def lambda_8DE():
        OP_6E(432, 6000)
        ExitThread()

    QueueWorkItem(0x10F, 2, lambda_8DE)
    WaitChrThread(0x109, 0x0)
    WaitChrThread(0x10F, 0x0)
    WaitChrThread(0x109, 0x1)
    Sleep(300)

    ChrTalk(    #0
        0x109,
        (
            "#1079F#5P这个……\x01",
            "生长在这里也很不自然。\x02\x03",

            "#1067F虽然这枝叶非常繁盛，\x01",
            "可是为什么在这种地方……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x10F,
        (
            "#1443F#5P………………………………\x02\x03",

            "#1445F……很遗憾。\x01",
            "好像不是能够结果实的树。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x109,
        (
            "#1840F#5P显然不会\x01",
            "这么随你的意吧……\x02",
        )
    )

    CloseMessageWindow()

    def lambda_A06():
        OP_6D(50190, 1000, -47300, 2000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_A06)

    def lambda_A1E():
        OP_67(0, 5190, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_A1E)

    def lambda_A36():
        OP_6B(2400, 2000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_A36)

    def lambda_A46():
        OP_6C(8000, 2000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_A46)

    def lambda_A56():
        OP_6E(406, 2000)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_A56)
    Sleep(1000)
    OP_8C(0x109, 315, 400)
    WaitChrThread(0x109, 0x0)
    Sleep(300)

    ChrTalk(    #3
        0x109,
        (
            "#1063F#6P对了，莉丝。\x01",
            "你对药草和植物应该很熟悉吧？\x02\x03",

            "你见过这种树吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x10F, 135, 400)
    Sleep(300)

    ChrTalk(    #4
        0x10F,
        (
            "#1446F#5P……不知道。\x02\x03",

            "#1802F至少不是大陆西部\x01",
            "野生的品种。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x109,
        "#1067F#6P唔……原来如此啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x10F,
        (
            "#1440F#5P……？\x02\x03",

            "明白什么了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x109,
        (
            "#1065F#6P不……\x01",
            "只是有些想法罢了。\x02\x03",

            "#1060F总之，\x01",
            "到别的地方看看去吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x10F,
        (
            "#1444F#5P啊……好。\x02\x03",

            "………………………………\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x10F, 45, 400)
    Sleep(500)

    ChrTalk(    #9
        0x10F,
        (
            "#1446F#5P不过，\x01",
            "也许和枫树一样有甜的树液呢。\x02\x03",

            "#1448F……要在树干上\x01",
            "稍微割一下试试吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #10
        0x109,
        "#1068F#6P还是算了吧。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2604)
    Sleep(300)
    OP_30(0x0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D01")

    def lambda_CEC():
        OP_6D(50070, 1000, -50210, 1000)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_CEC)
    Jump("loc_D25")

    label("loc_D01")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D25")

    def lambda_D13():
        OP_6D(49080, 1000, -49390, 1000)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_D13)

    label("loc_D25")


    def lambda_D2B():
        OP_67(0, 7900, -10000, 1000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_D2B)

    def lambda_D43():
        OP_6B(2530, 1000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_D43)

    def lambda_D53():
        OP_6C(0, 1000)
        ExitThread()

    QueueWorkItem(0x0, 3, lambda_D53)

    def lambda_D63():
        OP_6E(450, 1000)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_D63)
    Sleep(1000)
    SetMapFlags(0x1)
    ClearMapFlags(0x80)
    EventEnd(0x2)
    SetMapFlags(0x2000000)
    Return()

    # Function_2_7CF end

    def Function_3_D84(): pass

    label("Function_3_D84")

    OP_8E(0xFE, 0xB2A2, 0x3E8, 0xFFFF51AA, 0x7D0, 0x0)
    OP_8E(0xFE, 0xC396, 0x3E8, 0xFFFF3BDE, 0x7D0, 0x0)
    OP_8E(0xFE, 0xC396, 0x3E8, 0xFFFF3BDE, 0x7D0, 0x0)
    OP_8C(0xFE, 45, 400)
    Return()

    # Function_3_D84 end

    def Function_4_DC8(): pass

    label("Function_4_DC8")

    Sleep(200)
    OP_8E(0xFE, 0xB25C, 0x3E8, 0xFFFF5650, 0x7D0, 0x0)
    OP_8E(0xFE, 0xBFB8, 0x3E8, 0xFFFF3F12, 0x7D0, 0x0)
    OP_8C(0xFE, 45, 400)
    Return()

    # Function_4_DC8 end

    def Function_5_DFD(): pass

    label("Function_5_DFD")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrFlags(0x109, 0x80)
    SetChrFlags(0x10F, 0x80)
    OP_6D(54810, 3500, -44170, 0)
    OP_67(0, 4680, -10000, 0)
    OP_6B(2410, 0)
    OP_6C(300000, 0)
    OP_6E(591, 0)
    OP_E5(0x1, 0xFF, 0x10, 262144)
    OP_E5(0x1, 0xFF, 0x11, 262144)
    OP_E5(0x1, 0xFF, 0x12, 262144)
    OP_E5(0x1, 0xFF, 0x13, 262144)
    OP_82(0x81, 0x0)
    OP_82(0x82, 0x0)
    OP_82(0x83, 0x0)
    OP_82(0x84, 0x0)
    OP_82(0x85, 0x0)

    def lambda_E85():
        OP_6D(54810, 4750, -44170, 6000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_E85)

    def lambda_E9D():
        OP_67(0, 6610, -10000, 6000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_E9D)

    def lambda_EB5():
        OP_6B(2510, 6000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_EB5)

    def lambda_EC5():
        OP_6C(0, 6000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_EC5)

    def lambda_ED5():
        OP_6E(600, 6000)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_ED5)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(4000)
    OP_22(0x15F, 0x0, 0x64)
    Fade(1000)
    OP_E5(0x0, 0xFF, 0x10, 262144)
    OP_E5(0x0, 0xFF, 0x11, 262144)
    OP_E5(0x0, 0xFF, 0x12, 262144)
    OP_E5(0x0, 0xFF, 0x13, 262144)
    PlayEffect(0x81, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x82, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x83, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x84, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x85, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_1027():
        OP_6B(2200, 8000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_1027)
    OP_0D()
    WaitChrThread(0x109, 0x0)
    Sleep(2000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetMapFlags(0x2000000)
    OP_A2(0x2504)
    NewScene("ED6_DT21/U7002   ._SN", 100, 0, 0)
    IdleLoop()
    EventEnd(0x0)
    Return()

    # Function_5_DFD end

    def Function_6_105B(): pass

    label("Function_6_105B")

    EventBegin(0x0)
    Fade(1000)
    OP_6D(54290, 1000, -43900, 0)
    OP_67(0, 3960, -10000, 0)
    OP_6B(3600, 0)
    OP_6C(0, 0)
    OP_6E(349, 0)
    SetChrPos(0x109, 54420, 1000, -51530, 0)
    SetChrPos(0x10F, 53160, 1000, -52020, 45)
    SetChrChipByIndex(0x109, 65535)
    SetChrSubChip(0x109, 0)
    SetChrChipByIndex(0x10F, 65535)
    SetChrSubChip(0x10F, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #11
        0x109,
        (
            "#1078F#6P这……\x01",
            "又是不得了的光景呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x10F,
        (
            "#1442F#6P………嗯…………\x02\x03",

            "就像发光的花瓣\x01",
            "到处飞舞一样……\x02",
        )
    )

    CloseMessageWindow()
    OP_C4(0x0, 0x800)
    Sleep(150)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, 120, -1, -1)

    AnonymousTalk(    #13
        "\x07\x05#2S#40W    欢迎，诸位来客……\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    FadeToBright(300, 0)
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x10F, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #14
        0x109,
        "#1079F#6P难道……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x10F,
        "#1444F#6P这棵树在说话……？\x02",
    )

    CloseMessageWindow()
    Sleep(150)
    FadeToDark(300, 0, 100)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(-1, 100, -1, -1)

    AnonymousTalk(    #16
        (
            "\x07\x05#2S#40W  ……响应吾主之愿望……\x01",
            "#800W\x01",
            "#40W ……赐予汝等大地之恩惠……\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(-1, 100, -1, -1)

    AnonymousTalk(    #17
        (
            "\x07\x05#2S#40W但吾之力量并非万能……\x01",
            "#800W\x01",
            "#40W    汝等须付出相应代价……\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    FadeToBright(300, 0)
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_133B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_13B6")

    Menu(
        1,
        -1,
        150,
        1,
        (
            "获得食材\x01",      # 0
            "结束\x01",          # 1
        )
    )

    Jump("loc_1371")

    label("loc_1371")

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x1)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1397"),
        (SWITCH_DEFAULT, "loc_13A6"),
    )


    label("loc_1397")

    OP_A9(0xF)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_13B3")

    label("loc_13A6")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_13B3")

    label("loc_13B3")

    Jump("loc_133B")

    label("loc_13B6")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(500)
    Sleep(150)
    FadeToDark(300, 0, 100)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(-1, 100, -1, -1)

    AnonymousTalk(    #18
        (
            "\x07\x05#2S#40W    待吾主之力恢复之时……\x01",
            "#800W\x01",
            "#40W   吾等之恩惠将愈加丰富……\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(-1, 120, -1, -1)

    AnonymousTalk(    #19
        "\x07\x05#2S#40W………愿汝等得到大地祝福………\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    FadeToBright(300, 0)
    OP_62(0x109, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_62(0x10F, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x109)
    OP_63(0x10F)
    Sleep(300)
    WaitChrThread(0x109, 0x0)

    ChrTalk(    #20
        0x109,
        (
            "#1840F#6P哈哈……怎么回事……\x02\x03",

            "#1068F……树竟然会说话，\x01",
            "还卖起了食材，\x01",
            "这到底是开得什么玩笑……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x10F,
        "#1443F#6P#40W…………………………………\x02",
    )

    CloseMessageWindow()

    def lambda_1573():
        OP_6D(53990, 1000, -49500, 1200)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_1573)

    def lambda_158B():
        OP_67(0, 4960, -10000, 1200)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_158B)

    def lambda_15A3():
        OP_6B(2850, 1200)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_15A3)
    OP_8C(0x109, 225, 400)
    WaitChrThread(0x109, 0x1)

    ChrTalk(    #22
        0x109,
        (
            "#1079F#2P莉丝……？\x02\x03",

            "#1063F喂，你怎么了？\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    Fade(250)
    OP_22(0x8F, 0x0, 0x64)
    SetChrChipByIndex(0x10F, 0)
    SetChrSubChip(0x10F, 0)
    SetChrFlags(0x10F, 0x2)
    OP_0D()
    Sleep(500)

    ChrTalk(    #23
        0x10F,
        (
            "#1442F#6P『……此大树\x01",
            "  植根于七色泉之畔，\x01",
            "  施舍恩惠和喜悦……』\x02\x03",

            "──来自创世纪第七节，\x01",
            "《始源之地》。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    Fade(250)
    SetChrChipByIndex(0x10F, 0)
    SetChrSubChip(0x10F, 1)
    OP_0D()
    Sleep(300)
    OP_99(0x10F, 0x2, 0x4, 0x5DC)
    Sleep(300)

    ChrTalk(    #24
        0x10F,
        (
            "#1447F#6P女神啊……\x02\x03",

            "感谢您伟大的\x01",
            "慈悲与保佑。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #25
        0x109,
        (
            "#1840F#2P你好像很高兴嘛……\x02\x03",

            "不过，我觉得这和\x01",
            "女神的保佑没什么关系嘛。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    Fade(250)
    SetChrChipByIndex(0x10F, 65535)
    SetChrSubChip(0x10F, 0)
    ClearChrFlags(0x10F, 0x2)
    OP_0D()
    Sleep(300)

    ChrTalk(    #26
        0x10F,
        (
            "#1443F#6P……不对。\x02\x03",

            "#1446F『条条大路通食物』，\x01",
            "女神在圣典中也是这么说的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x109,
        "#1068F#2P才没有这回事吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x10F,
        (
            "#1440F#6P对了……\x01",
            "凯文，这个给你。\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0x11, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #29
        "\x07\x00得到了\x1F\x0D\x02\x07\x00。\x02",
    )

    Jump("loc_1879")

    label("loc_1879")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x20D, 1)
    OP_AC(0x16)
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #30
        0x109,
        (
            "#1064F#2P哎……\x02\x03",

            "为什么给我这个？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x10F,
        (
            "#1446F#6P凯文，你的信仰太浅了……\x01",
            "亏你还是守护骑士。\x02\x03",

            "#1801F我要让你通过料理\x01",
            "把对女神大人的信仰找回来。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x109,
        (
            "#1068F#2P哎呀，\x01",
            "这理论也太奇怪了吧！\x02\x03",

            "#1063F而且要做饭的话，\x01",
            "你来做不就行了吗！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x10F,
        (
            "#1447F#6P凯文，\x01",
            "你以前做饭就比我强……\x02\x03",

            "食材也会希望自己\x01",
            "被做成更美味的料理吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x109,
        "#1060F#2P不，可是……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x10F,
        (
            "#1802F#6P………………………………\x02\x03",

            "#1445F………不行吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x109, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(    #36
        0x109,
        (
            "#1079F#2P呜……\x02\x03",

            "#1068F（唉……我太没用了。）\x02\x03",

            "#1840F……话说在前面，\x01",
            "你可也得认真帮忙哦？\x02\x03",

            "还有，\x01",
            "不能在做饭的过程中偷吃。\x02",
        )
    )

    Jump("loc_1B53")

    label("loc_1B53")

    CloseMessageWindow()

    ChrTalk(    #37
        0x10F,
        "#1442F#6P呵呵……我知道。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2609)
    Sleep(500)
    EventEnd(0x0)
    Return()

    # Function_6_105B end

    def Function_7_1B85(): pass

    label("Function_7_1B85")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C0, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1B96")
    Call(0, 6)
    Return()

    label("loc_1B96")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1BB6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1C31")

    Menu(
        1,
        -1,
        150,
        1,
        (
            "获得食材\x01",      # 0
            "结束\x01",          # 1
        )
    )

    Jump("loc_1BEC")

    label("loc_1BEC")

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x1)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1C12"),
        (SWITCH_DEFAULT, "loc_1C21"),
    )


    label("loc_1C12")

    OP_A9(0xF)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1C2E")

    label("loc_1C21")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1C2E")

    label("loc_1C2E")

    Jump("loc_1BB6")

    label("loc_1C31")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkEnd(0xFF)
    Return()

    # Function_7_1B85 end

    def Function_8_1C3E(): pass

    label("Function_8_1C3E")

    OP_A3(0x10)
    Call(0, 11)
    Call(0, 9)
    Call(0, 12)
    OP_C0(0x27, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x45), scpexpr(EXPR_END)), "loc_1C79")
    Call(0, 12)

    label("loc_1C79")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1D09")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x564, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x564, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1CA6")
    NewScene("ED6_DT21/U7000   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    label("loc_1CA6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x562, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x562, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_42(0xB)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1CC7")
    NewScene("ED6_DT21/U7000   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    label("loc_1CC7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x561, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x561, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1CE8")
    NewScene("ED6_DT21/U7000   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    label("loc_1CE8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x560, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x560, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1D09")
    NewScene("ED6_DT21/U7000   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    label("loc_1D09")

    Return()

    # Function_8_1C3E end

    def Function_9_1D0A(): pass

    label("Function_9_1D0A")

    OP_64(0x1, 0x1)
    OP_64(0x2, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x584, 0)), scpexpr(EXPR_END)), "loc_1DF7")
    SetChrPos(0x1E, 55220, 1800, -49210, 0)
    SetChrPos(0x11, 54510, 1220, -50260, 0)
    SetChrPos(0x16, 58670, 1000, -49340, 177)
    SetChrPos(0x20, 52150, 1000, -53260, 322)
    SetChrPos(0x12, 50890, 1000, -51800, 142)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1D86")
    OP_43(0x12, 0x0, 0x0, 0x13)
    Jump("loc_1D8D")

    label("loc_1D86")

    OP_43(0x12, 0x0, 0x6, 0x2)

    label("loc_1D8D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1DA5")
    OP_43(0x20, 0x0, 0x0, 0x13)
    Jump("loc_1DAC")

    label("loc_1DA5")

    OP_43(0x20, 0x0, 0x6, 0x2)

    label("loc_1DAC")

    SetChrChipByIndex(0x1A, 28)
    SetChrSubChip(0x1A, 0)
    OP_44(0x1A, 0x0)
    SetChrFlags(0x1A, 0x4)
    SetChrPos(0x1A, 76920, -11300, -53500, 90)
    SetChrChipByIndex(0x1D, 29)
    SetChrSubChip(0x1D, 0)
    OP_44(0x1D, 0x0)
    SetChrFlags(0x1D, 0x4)
    SetChrPos(0x1D, 77120, -11300, -52420, 90)
    Jump("loc_2D09")

    label("loc_1DF7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x565, 3)), scpexpr(EXPR_END)), "loc_203E")
    SetChrChipByIndex(0x12, 25)
    SetChrSubChip(0x12, 0)
    OP_44(0x12, 0x0)
    SetChrFlags(0x12, 0x4)
    SetChrPos(0x12, 98770, -13900, -52140, 90)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1E35")
    SetChrSubChip(0x12, 2)

    label("loc_1E35")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1E62")
    SetChrPos(0x1B, 100250, -14000, -51650, 66)
    Jump("loc_1EBB")

    label("loc_1E62")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4CC, 4)), scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1E88")
    SetChrPos(0x1B, 100250, -14000, -51650, 199)
    Jump("loc_1EBB")

    label("loc_1E88")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1EAA")
    SetChrPos(0x1B, 100240, -14000, -52310, 230)
    Jump("loc_1EBB")

    label("loc_1EAA")

    SetChrPos(0x1B, 100250, -14000, -51650, 230)

    label("loc_1EBB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x565, 4)), scpexpr(EXPR_END)), "loc_1EE9")
    SetChrChipByIndex(0x11, 24)
    SetChrSubChip(0x11, 0)
    OP_44(0x11, 0x0)
    SetChrFlags(0x11, 0x4)
    SetChrPos(0x11, 98770, -13900, -53060, 90)
    Jump("loc_1F7E")

    label("loc_1EE9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4CC, 4)), scpexpr(EXPR_END)), "loc_1F13")
    SetChrChipByIndex(0x11, 23)
    SetChrPos(0x11, 99670, -14000, -53130, 90)
    OP_43(0x11, 0x0, 0x0, 0xE)
    OP_A2(0x10)
    Jump("loc_1F7E")

    label("loc_1F13")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1F5A")
    SetChrChipByIndex(0x11, 2)
    SetChrSubChip(0x11, 0)
    OP_44(0x11, 0x0)
    SetChrFlags(0x11, 0x4)
    SetChrPos(0x11, 100490, -14000, -55300, 133)
    OP_43(0x11, 0x0, 0x6, 0x2)
    Jump("loc_1F7E")

    label("loc_1F5A")

    SetChrChipByIndex(0x11, 24)
    SetChrSubChip(0x11, 0)
    OP_44(0x11, 0x0)
    SetChrFlags(0x11, 0x4)
    SetChrPos(0x11, 98770, -13900, -53060, 90)

    label("loc_1F7E")

    SetChrPos(0x1A, 51210, 1000, -60260, 205)
    SetChrPos(0x14, 57200, 1000, -49150, 148)
    SetChrPos(0x1F, 60170, 1000, -46660, 176)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xB)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1FD3")
    SetChrPos(0x13, 62820, 1000, -45530, 27)
    Jump("loc_1FE4")

    label("loc_1FD3")

    SetChrPos(0x13, 60350, 1000, -49000, 356)

    label("loc_1FE4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2006")
    SetChrPos(0x15, 59210, 1000, -56500, 127)
    Jump("loc_203B")

    label("loc_2006")

    SetChrChipByIndex(0x17, 20)
    SetChrSubChip(0x17, 0)
    OP_44(0x17, 0x0)
    SetChrFlags(0x17, 0x4)
    SetChrPos(0x17, 59340, 1300, -57340, 315)
    SetChrPos(0x15, 58310, 1000, -56210, 135)

    label("loc_203B")

    Jump("loc_2D09")

    label("loc_203E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x564, 0)), scpexpr(EXPR_END)), "loc_209F")
    SetChrPos(0x1B, 95180, -14000, -52580, 126)
    SetChrPos(0x14, 60170, 1000, -46660, 180)
    SetChrPos(0x1F, 54480, 1000, -52730, 0)
    SetChrChipByIndex(0x1A, 28)
    SetChrSubChip(0x1A, 0)
    OP_44(0x1A, 0x0)
    SetChrFlags(0x1A, 0x4)
    SetChrPos(0x1A, 54410, 1300, -59300, 0)
    Jump("loc_2D09")

    label("loc_209F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x562, 5)), scpexpr(EXPR_END)), "loc_2262")
    SetChrChipByIndex(0x21, 33)
    SetChrSubChip(0x21, 0)
    OP_44(0x21, 0x0)
    SetChrFlags(0x21, 0x4)
    SetChrPos(0x21, 57260, 2000, -41880, 225)
    SetChrFlags(0x1B, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_20E5")
    SetChrFlags(0x21, 0x80)
    Jump("loc_20EE")

    label("loc_20E5")

    ClearChrFlags(0x21, 0x80)
    OP_65(0x2, 0x1)

    label("loc_20EE")

    SetChrChipByIndex(0x1A, 28)
    SetChrSubChip(0x1A, 0)
    OP_44(0x1A, 0x0)
    SetChrFlags(0x1A, 0x4)
    SetChrPos(0x1A, 54410, 1300, -59300, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2189")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2142")
    SetChrPos(0x14, 52280, 1000, -61100, 192)
    Jump("loc_2186")

    label("loc_2142")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2164")
    SetChrPos(0x13, 56320, 1000, -59850, 171)
    Jump("loc_2186")

    label("loc_2164")

    SetChrPos(0x14, 53410, 1000, -57430, 90)
    SetChrPos(0x13, 55360, 1000, -57610, 275)

    label("loc_2186")

    Jump("loc_21EF")

    label("loc_2189")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_21AB")
    SetChrPos(0x14, 54420, 1000, -56910, 179)
    Jump("loc_21EF")

    label("loc_21AB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_21CD")
    SetChrPos(0x13, 54420, 1000, -56910, 179)
    Jump("loc_21EF")

    label("loc_21CD")

    SetChrPos(0x14, 53410, 1000, -57430, 150)
    SetChrPos(0x13, 55360, 1000, -57610, 219)

    label("loc_21EF")

    SetChrPos(0x1E, 55220, 1800, -49210, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4CD, 0)), scpexpr(EXPR_END)), "loc_221B")
    SetChrPos(0x20, 97450, -14000, -47720, 37)
    Jump("loc_225F")

    label("loc_221B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_224E")
    SetChrPos(0x11, 93410, -14000, -52280, 96)
    SetChrPos(0x20, 97090, -14000, -52560, 264)
    Jump("loc_225F")

    label("loc_224E")

    SetChrPos(0x11, 65290, -11000, -47010, 30)

    label("loc_225F")

    Jump("loc_2D09")

    label("loc_2262")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x561, 0)), scpexpr(EXPR_END)), "loc_2471")
    SetChrPos(0x13, 61630, 1000, -50010, 313)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_42(0xB)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_22B8")
    SetChrPos(0x1B, 61330, 1000, -57980, 214)
    SetChrPos(0x1F, 60450, 1000, -59270, 54)
    Jump("loc_22F9")

    label("loc_22B8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_22DA")
    SetChrPos(0x1F, 61200, 1000, -59080, 134)
    Jump("loc_22F9")

    label("loc_22DA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xB)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_22F9")
    SetChrPos(0x1B, 61200, 1000, -59080, 134)

    label("loc_22F9")

    SetChrPos(0x11, 65290, -11000, -47010, 30)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_232C")
    SetChrChipByIndex(0x11, 23)
    SetChrSubChip(0x11, 0)
    OP_43(0x11, 0x0, 0x0, 0xD)
    Jump("loc_2336")

    label("loc_232C")

    OP_43(0x11, 0x0, 0x6, 0x2)
    OP_63(0x11)

    label("loc_2336")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2374")
    SetChrPos(0x14, 47340, 1000, -58740, 129)
    SetChrPos(0x19, 48290, 1000, -59730, 299)
    Jump("loc_23A7")

    label("loc_2374")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2396")
    SetChrPos(0x19, 49980, 1000, -56720, 50)
    Jump("loc_23A7")

    label("loc_2396")

    SetChrPos(0x14, 41330, 1000, -53920, 250)

    label("loc_23A7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2415")
    SetChrChipByIndex(0x20, 22)
    SetChrSubChip(0x20, 0)
    OP_44(0x20, 0x0)
    SetChrFlags(0x20, 0x4)
    SetChrPos(0x20, 98730, -13900, -52200, 90)
    SetChrChipByIndex(0x12, 25)
    SetChrSubChip(0x12, 0)
    OP_44(0x12, 0x0)
    SetChrFlags(0x12, 0x4)
    SetChrPos(0x12, 98830, -13900, -53010, 90)
    SetChrSubChip(0x12, 1)
    SetChrSubChip(0x20, 2)
    Jump("loc_246E")

    label("loc_2415")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_244A")
    SetChrChipByIndex(0x20, 22)
    SetChrSubChip(0x20, 0)
    OP_44(0x20, 0x0)
    SetChrFlags(0x20, 0x4)
    SetChrPos(0x20, 98770, -13900, -52490, 90)
    Jump("loc_246E")

    label("loc_244A")

    SetChrChipByIndex(0x12, 25)
    SetChrSubChip(0x12, 0)
    OP_44(0x12, 0x0)
    SetChrFlags(0x12, 0x4)
    SetChrPos(0x12, 98770, -13900, -52490, 90)

    label("loc_246E")

    Jump("loc_2D09")

    label("loc_2471")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x560, 0)), scpexpr(EXPR_END)), "loc_2594")
    SetChrPos(0x14, 41330, 1000, -53920, 250)
    SetChrChipByIndex(0x19, 18)
    SetChrSubChip(0x19, 0)
    OP_44(0x19, 0x0)
    SetChrFlags(0x19, 0x4)
    SetChrPos(0x19, 61420, 1200, -52290, 267)
    SetChrPos(0x13, 54410, 1000, -57870, 1)
    SetChrChipByIndex(0x20, 22)
    SetChrSubChip(0x20, 0)
    OP_44(0x20, 0x0)
    SetChrFlags(0x20, 0x4)
    SetChrPos(0x20, 97610, -13900, -53060, 269)
    SetChrChipByIndex(0x12, 25)
    SetChrSubChip(0x12, 0)
    OP_44(0x12, 0x0)
    SetChrFlags(0x12, 0x4)
    SetChrPos(0x12, 97600, -13900, -52140, 269)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2524")
    SetChrSubChip(0x12, 1)

    label("loc_2524")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2542")
    SetChrSubChip(0x20, 2)

    label("loc_2542")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_256F")
    SetChrPos(0x1B, 99110, -14000, -49420, 55)
    Jump("loc_2580")

    label("loc_256F")

    SetChrPos(0x1B, 95970, -14000, -52590, 79)

    label("loc_2580")

    SetChrPos(0x1F, 51740, 1000, -48810, 220)
    Jump("loc_2D09")

    label("loc_2594")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x540, 7)), scpexpr(EXPR_END)), "loc_26FA")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_25D9")
    SetChrPos(0x17, 61440, 1000, -58160, 221)
    SetChrPos(0x16, 60340, 1000, -59400, 47)
    Jump("loc_261A")

    label("loc_25D9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_25FB")
    SetChrPos(0x16, 61140, 1000, -59050, 132)
    Jump("loc_261A")

    label("loc_25FB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_261A")
    SetChrPos(0x17, 61140, 1000, -59050, 132)

    label("loc_261A")

    SetChrChipByIndex(0x13, 34)
    SetChrSubChip(0x13, 0)
    OP_44(0x13, 0x0)
    SetChrFlags(0x13, 0x4)
    SetChrPos(0x13, 54350, 1300, -59320, 0)
    SetChrPos(0x14, 41330, 1000, -53920, 250)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_26A0")
    SetChrPos(0x12, 96280, -14000, -52650, 90)
    SetChrChipByIndex(0x20, 22)
    SetChrSubChip(0x20, 0)
    OP_44(0x20, 0x0)
    SetChrFlags(0x20, 0x4)
    SetChrPos(0x20, 97700, -13900, -52560, 269)
    Jump("loc_26E6")

    label("loc_26A0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_26D5")
    SetChrChipByIndex(0x20, 22)
    SetChrSubChip(0x20, 0)
    OP_44(0x20, 0x0)
    SetChrFlags(0x20, 0x4)
    SetChrPos(0x20, 98920, -13900, -52540, 90)
    Jump("loc_26E6")

    label("loc_26D5")

    SetChrPos(0x12, 96280, -14000, -52650, 90)

    label("loc_26E6")

    SetChrPos(0x1F, 63520, 1000, -42950, 42)
    Jump("loc_2D09")

    label("loc_26FA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x540, 4)), scpexpr(EXPR_END)), "loc_2813")
    SetChrPos(0x1F, 54780, 1000, -51140, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xB)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_273F")
    SetChrPos(0x14, 54410, 1000, -57870, 15)
    Jump("loc_2750")

    label("loc_273F")

    SetChrPos(0x14, 54410, 1000, -57870, 0)

    label("loc_2750")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xB)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_277D")
    SetChrPos(0x17, 55790, 1000, -57780, 335)
    Jump("loc_278E")

    label("loc_277D")

    SetChrPos(0x17, 55790, 1000, -57780, 0)

    label("loc_278E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xB)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_27B0")
    SetChrPos(0x13, 55820, 1000, -53090, 332)
    Jump("loc_2810")

    label("loc_27B0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_27DD")
    SetChrPos(0x13, 54950, 1000, -56000, 180)
    Jump("loc_2810")

    label("loc_27DD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_27FF")
    SetChrPos(0x13, 54950, 1000, -56000, 155)
    Jump("loc_2810")

    label("loc_27FF")

    SetChrPos(0x13, 54950, 1000, -56000, 195)

    label("loc_2810")

    Jump("loc_2D09")

    label("loc_2813")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x540, 0)), scpexpr(EXPR_END)), "loc_2874")
    SetChrChipByIndex(0x14, 19)
    SetChrSubChip(0x14, 0)
    OP_44(0x14, 0x0)
    SetChrFlags(0x14, 0x4)
    SetChrPos(0x14, 54350, 1300, -59320, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2860")
    SetChrPos(0x13, 55700, 1000, -58390, 281)
    Jump("loc_2871")

    label("loc_2860")

    SetChrPos(0x13, 56970, 1000, -59720, 160)

    label("loc_2871")

    Jump("loc_2D09")

    label("loc_2874")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x521, 6)), scpexpr(EXPR_END)), "loc_28F5")
    SetChrPos(0x14, 54440, 1000, -61430, 180)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_28AE")
    SetChrPos(0x17, 50110, 1000, -48610, 145)
    Jump("loc_28BF")

    label("loc_28AE")

    SetChrPos(0x17, 50110, 1000, -48610, 34)

    label("loc_28BF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_28E1")
    SetChrPos(0x13, 51570, 1000, -50010, 316)
    Jump("loc_28F2")

    label("loc_28E1")

    SetChrPos(0x13, 51250, 1000, -51050, 38)

    label("loc_28F2")

    Jump("loc_2D09")

    label("loc_28F5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x521, 2)), scpexpr(EXPR_END)), "loc_29AA")
    SetChrChipByIndex(0x14, 19)
    SetChrSubChip(0x14, 0)
    OP_44(0x14, 0x0)
    SetChrFlags(0x14, 0x4)
    SetChrPos(0x14, 61460, 1400, -52370, 271)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2942")
    SetChrPos(0x13, 50180, 1000, -48600, 90)
    Jump("loc_2953")

    label("loc_2942")

    SetChrPos(0x13, 51640, 1000, -49210, 212)

    label("loc_2953")

    SetChrChipByIndex(0x17, 20)
    SetChrSubChip(0x17, 1)
    OP_44(0x17, 0x0)
    SetChrFlags(0x17, 0x4)
    SetChrPos(0x17, 51970, 1500, -47860, 209)
    SetChrPos(0x18, 52240, 1600, -48050, 283)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_299E")
    SetChrFlags(0x18, 0x80)
    Jump("loc_29A7")

    label("loc_299E")

    ClearChrFlags(0x18, 0x80)
    OP_65(0x1, 0x1)

    label("loc_29A7")

    Jump("loc_2D09")

    label("loc_29AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x520, 5)), scpexpr(EXPR_END)), "loc_2C2A")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_29ED")
    SetChrChipByIndex(0x19, 10)
    SetChrSubChip(0x19, 0)
    OP_44(0x19, 0x0)
    SetChrFlags(0x19, 0x4)
    SetChrPos(0x19, 96290, -14000, -51540, 180)
    OP_43(0x19, 0x0, 0x6, 0x2)
    Jump("loc_2A11")

    label("loc_29ED")

    SetChrChipByIndex(0x19, 18)
    SetChrSubChip(0x19, 0)
    OP_44(0x19, 0x0)
    SetChrFlags(0x19, 0x4)
    SetChrPos(0x19, 97800, -13900, -52620, 264)

    label("loc_2A11")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2A4D")
    SetChrChipByIndex(0x14, 5)
    SetChrSubChip(0x14, 0)
    OP_44(0x14, 0x0)
    SetChrFlags(0x14, 0x4)
    SetChrPos(0x14, 96290, -14000, -53640, 0)
    OP_43(0x14, 0x0, 0x6, 0x2)
    Jump("loc_2A71")

    label("loc_2A4D")

    SetChrChipByIndex(0x14, 19)
    SetChrSubChip(0x14, 0)
    OP_44(0x14, 0x0)
    SetChrFlags(0x14, 0x4)
    SetChrPos(0x14, 97800, -13900, -52620, 264)

    label("loc_2A71")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2AA9")
    SetChrPos(0x17, 54450, 1000, -58360, 6)
    Jump("loc_2C27")

    label("loc_2AA9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2AE1")
    SetChrPos(0x13, 54450, 1000, -58360, 6)
    Jump("loc_2C27")

    label("loc_2AE1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2B19")
    SetChrPos(0x1A, 54450, 1000, -58360, 6)
    Jump("loc_2C27")

    label("loc_2B19")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2B62")
    SetChrPos(0x13, 55340, 1000, -57810, 248)
    SetChrPos(0x17, 53840, 1000, -57840, 94)
    Jump("loc_2C27")

    label("loc_2B62")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2BAB")
    SetChrPos(0x17, 55340, 1000, -57810, 248)
    SetChrPos(0x1A, 53840, 1000, -57840, 94)
    Jump("loc_2C27")

    label("loc_2BAB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2BF4")
    SetChrPos(0x13, 55340, 1000, -57810, 248)
    SetChrPos(0x1A, 53840, 1000, -57840, 94)
    Jump("loc_2C27")

    label("loc_2BF4")

    SetChrPos(0x1A, 53340, 1000, -57770, 39)
    SetChrPos(0x13, 55020, 1000, -57740, 305)
    SetChrPos(0x17, 54170, 1000, -56200, 185)

    label("loc_2C27")

    Jump("loc_2D09")

    label("loc_2C2A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x520, 0)), scpexpr(EXPR_END)), "loc_2D02")
    SetChrPos(0x14, 60400, 1000, -49520, 180)
    SetChrChipByIndex(0x19, 18)
    SetChrSubChip(0x19, 0)
    OP_44(0x19, 0x0)
    SetChrFlags(0x19, 0x4)
    SetChrPos(0x19, 61420, 1200, -52290, 267)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2C88")
    SetChrPos(0x17, 59530, 1000, -52170, 315)
    Jump("loc_2C99")

    label("loc_2C88")

    SetChrPos(0x17, 59530, 1000, -52170, 90)

    label("loc_2C99")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2CBB")
    SetChrPos(0x13, 58300, 1000, -53260, 45)
    Jump("loc_2CCC")

    label("loc_2CBB")

    SetChrPos(0x13, 55340, 1000, -57810, 248)

    label("loc_2CCC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2CEE")
    SetChrPos(0x1A, 53840, 1000, -57840, 180)
    Jump("loc_2CFF")

    label("loc_2CEE")

    SetChrPos(0x1A, 53840, 1000, -57840, 94)

    label("loc_2CFF")

    Jump("loc_2D09")

    label("loc_2D02")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x500, 0)), scpexpr(EXPR_END)), "loc_2D09")

    label("loc_2D09")

    Call(0, 10)
    Return()

    # Function_9_1D0A end

    def Function_10_2D0E(): pass

    label("Function_10_2D0E")

    OP_BC(0xE, 0x1, 0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x16), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2D5E")
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x11, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_PUSH_LONG, 0x40), scpexpr(EXPR_ADD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2D3F")
    OP_51(0x11, 0xA, (scpexpr(EXPR_PUSH_LONG, 0x1A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2D3F")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x11, 0xA), scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_PUSH_LONG, 0x40), scpexpr(EXPR_ADD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2D5E")
    OP_51(0x11, 0xA, (scpexpr(EXPR_PUSH_LONG, 0x1B), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2D5E")

    Return()

    # Function_10_2D0E end

    def Function_11_2D5F(): pass

    label("Function_11_2D5F")

    OP_C0(0x23, 0x10, 0x181, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_C0(0x23, 0x11, 0x181, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_C0(0x23, 0x12, 0x181, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_C0(0x23, 0x13, 0x181, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_C0(0x23, 0x14, 0x181, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_C0(0x23, 0x15, 0x181, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_C0(0x23, 0x16, 0x181, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_C0(0x23, 0x17, 0x181, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_C0(0x23, 0x18, 0x181, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_C0(0x23, 0x19, 0x181, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_C0(0x23, 0x1A, 0x181, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_C0(0x23, 0x1B, 0x181, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_C0(0x23, 0x1C, 0x181, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_C0(0x23, 0x1D, 0x181, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_C0(0x23, 0x1E, 0x181, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_C0(0x23, 0x1F, 0x181, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_C0(0x23, 0x20, 0x181, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    SetChrPos(0x10, 9000000, 9000000, 0, 0)
    SetChrPos(0x11, 9000000, 9000000, 0, 0)
    SetChrPos(0x12, 9000000, 9000000, 0, 0)
    SetChrPos(0x13, 9000000, 9000000, 0, 0)
    SetChrPos(0x14, 9000000, 9000000, 0, 0)
    SetChrPos(0x15, 9000000, 9000000, 0, 0)
    SetChrPos(0x16, 9000000, 9000000, 0, 0)
    SetChrPos(0x17, 9000000, 9000000, 0, 0)
    SetChrPos(0x18, 9000000, 9000000, 0, 0)
    SetChrPos(0x19, 9000000, 9000000, 0, 0)
    SetChrPos(0x1A, 9000000, 9000000, 0, 0)
    SetChrPos(0x1B, 9000000, 9000000, 0, 0)
    SetChrPos(0x1C, 9000000, 9000000, 0, 0)
    SetChrPos(0x1D, 9000000, 9000000, 0, 0)
    SetChrPos(0x1E, 9000000, 9000000, 0, 0)
    SetChrPos(0x1F, 9000000, 9000000, 0, 0)
    SetChrPos(0x20, 9000000, 9000000, 0, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_30D8")
    SetChrFlags(0x12, 0x80)
    Jump("loc_30DD")

    label("loc_30D8")

    ClearChrFlags(0x12, 0x80)

    label("loc_30DD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_30F3")
    SetChrFlags(0x13, 0x80)
    Jump("loc_30F8")

    label("loc_30F3")

    ClearChrFlags(0x13, 0x80)

    label("loc_30F8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_310E")
    SetChrFlags(0x14, 0x80)
    Jump("loc_3113")

    label("loc_310E")

    ClearChrFlags(0x14, 0x80)

    label("loc_3113")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3129")
    SetChrFlags(0x15, 0x80)
    Jump("loc_312E")

    label("loc_3129")

    ClearChrFlags(0x15, 0x80)

    label("loc_312E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3144")
    SetChrFlags(0x16, 0x80)
    Jump("loc_3149")

    label("loc_3144")

    ClearChrFlags(0x16, 0x80)

    label("loc_3149")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_315F")
    SetChrFlags(0x17, 0x80)
    Jump("loc_3164")

    label("loc_315F")

    ClearChrFlags(0x17, 0x80)

    label("loc_3164")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_317A")
    SetChrFlags(0x19, 0x80)
    Jump("loc_317F")

    label("loc_317A")

    ClearChrFlags(0x19, 0x80)

    label("loc_317F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3195")
    SetChrFlags(0x1A, 0x80)
    Jump("loc_319A")

    label("loc_3195")

    ClearChrFlags(0x1A, 0x80)

    label("loc_319A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_31B0")
    SetChrFlags(0x1B, 0x80)
    Jump("loc_31B5")

    label("loc_31B0")

    ClearChrFlags(0x1B, 0x80)

    label("loc_31B5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_31CB")
    SetChrFlags(0x1C, 0x80)
    Jump("loc_31D0")

    label("loc_31CB")

    ClearChrFlags(0x1C, 0x80)

    label("loc_31D0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_31E6")
    SetChrFlags(0x1D, 0x80)
    Jump("loc_31EB")

    label("loc_31E6")

    ClearChrFlags(0x1D, 0x80)

    label("loc_31EB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3201")
    SetChrFlags(0x1E, 0x80)
    Jump("loc_3206")

    label("loc_3201")

    ClearChrFlags(0x1E, 0x80)

    label("loc_3206")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xB)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_321C")
    SetChrFlags(0x1F, 0x80)
    Jump("loc_3221")

    label("loc_321C")

    ClearChrFlags(0x1F, 0x80)

    label("loc_3221")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3237")
    SetChrFlags(0x20, 0x80)
    Jump("loc_323C")

    label("loc_3237")

    ClearChrFlags(0x20, 0x80)

    label("loc_323C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3252")
    SetChrFlags(0x11, 0x80)
    Jump("loc_3257")

    label("loc_3252")

    ClearChrFlags(0x11, 0x80)

    label("loc_3257")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_326D")
    SetChrFlags(0x10, 0x80)
    Jump("loc_3272")

    label("loc_326D")

    ClearChrFlags(0x10, 0x80)

    label("loc_3272")

    Return()

    # Function_11_2D5F end

    def Function_12_3273(): pass

    label("Function_12_3273")

    OP_A3(0x0)
    OP_A3(0x1)
    OP_A3(0x2)
    OP_A3(0x3)
    OP_A3(0x4)
    OP_A3(0x5)
    OP_A3(0x6)
    OP_A3(0x7)
    OP_A3(0x8)
    OP_A3(0x9)
    OP_A3(0xA)
    OP_A3(0xB)
    OP_A3(0xC)
    OP_A3(0xD)
    OP_A3(0xE)
    OP_A3(0xF)
    Return()

    # Function_12_3273 end

    def Function_13_32A4(): pass

    label("Function_13_32A4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x561, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x562, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3352")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_334F")
    Sleep(500)

    label("loc_32C3")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_334F")
    OP_8C(0xFE, 30, 400)
    SetChrChipByIndex(0xFE, 23)
    SetChrSubChip(0xFE, 0)
    Sleep(50)
    SetChrSubChip(0xFE, 1)
    Sleep(50)
    SetChrSubChip(0xFE, 2)
    Sleep(1500)
    OP_62(0xFE, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0xFE)
    SetChrSubChip(0xFE, 1)
    Sleep(50)
    SetChrChipByIndex(0xFE, 23)
    SetChrSubChip(0xFE, 0)
    Sleep(50)
    SetChrSubChip(0xFE, 1)
    Sleep(50)
    SetChrSubChip(0xFE, 2)
    Sleep(1500)
    Sleep(1500)
    SetChrSubChip(0xFE, 1)
    Sleep(50)
    Jump("loc_32C3")

    label("loc_334F")

    Jump("loc_3356")

    label("loc_3352")

    Call(6, 2)

    label("loc_3356")

    Return()

    # Function_13_32A4 end

    def Function_14_3357(): pass

    label("Function_14_3357")

    Sleep(500)

    label("loc_335C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_339A")
    SetChrChipByIndex(0xFE, 23)
    SetChrSubChip(0xFE, 0)
    Sleep(50)
    SetChrSubChip(0xFE, 1)
    Sleep(50)
    SetChrSubChip(0xFE, 2)
    Sleep(1500)
    Sleep(2000)
    SetChrSubChip(0xFE, 1)
    Sleep(50)
    Jump("loc_335C")

    label("loc_339A")

    Return()

    # Function_14_3357 end

    def Function_15_339B(): pass

    label("Function_15_339B")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_33F7")
    SetChrSubChip(0xFE, 0)
    Sleep(100)
    SetChrSubChip(0xFE, 1)
    Sleep(100)
    SetChrSubChip(0xFE, 0)
    Sleep(100)
    SetChrSubChip(0xFE, 2)
    Sleep(2000)
    SetChrSubChip(0xFE, 0)
    Sleep(100)
    SetChrSubChip(0xFE, 1)
    Sleep(1000)
    SetChrSubChip(0xFE, 0)
    Sleep(100)
    SetChrSubChip(0xFE, 2)
    Sleep(1500)
    Jump("Function_15_339B")

    label("loc_33F7")

    Return()

    # Function_15_339B end

    def Function_16_33F8(): pass

    label("Function_16_33F8")

    Call(5, 15)
    Return()

    # Function_16_33F8 end

    def Function_17_33FD(): pass

    label("Function_17_33FD")

    Call(5, 9)
    Return()

    # Function_17_33FD end

    def Function_18_3402(): pass

    label("Function_18_3402")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x565, 3)), scpexpr(EXPR_END)), "loc_3410")
    Call(6, 2)
    Jump("loc_3441")

    label("loc_3410")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x564, 0)), scpexpr(EXPR_END)), "loc_343D")

    label("loc_3417")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_343A")
    OP_8D(0xFE, 92770, -50060, 96780, -55920, 1500)
    Jump("loc_3417")

    label("loc_343A")

    Jump("loc_3441")

    label("loc_343D")

    Call(6, 2)

    label("loc_3441")

    Return()

    # Function_18_3402 end

    def Function_19_3442(): pass

    label("Function_19_3442")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3465")
    OP_8D(0xFE, 49060, -49630, 53360, -54740, 1500)
    Jump("Function_19_3442")

    label("loc_3465")

    Return()

    # Function_19_3442 end

    def Function_20_3466(): pass

    label("Function_20_3466")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x562, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x564, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4CD, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3494")
    OP_A2(0x11)
    Call(5, 13)

    label("loc_3494")

    Return()

    # Function_20_3466 end

    def Function_21_3495(): pass

    label("Function_21_3495")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x562, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x564, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4CD, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_34C3")
    OP_A2(0x12)
    Call(5, 13)

    label("loc_34C3")

    Return()

    # Function_21_3495 end

    def Function_22_34C4(): pass

    label("Function_22_34C4")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4CE, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x581, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_351F")
    OP_22(0x17, 0x0, 0x64)
    OP_82(0x0, 0x2)
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #38
        "\x07\x05在书柜上发现了《利贝尔通讯》。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_A2(0x2676)
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Jump("loc_3EED")

    label("loc_351F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4CE, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x501, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3578")
    OP_22(0x17, 0x0, 0x64)
    OP_82(0x0, 0x2)
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #39
        "\x07\x05在书柜上发现了《利贝尔通讯》。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_A2(0x2671)
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Jump("loc_3EED")

    label("loc_3578")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4CE, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4CE, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_39F7")
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #40
        "\x07\x05书柜上放着《利贝尔通讯》。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        10,
        1,
        (
            "【０２年度前期～０２年度中期】\x01",      # 0
            "【０２年度后期～０３年度前期】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_3622"),
        (1, "loc_37D0"),
        (SWITCH_DEFAULT, "loc_39E5"),
    )


    label("loc_3622")

    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        10,
        1,
        (
            "【阅读第１号】\x01",      # 0
            "【阅读第２号】\x01",      # 1
            "【阅读第３号】\x01",      # 2
            "【阅读第４号】\x01",      # 3
            "【阅读第５号】\x01",      # 4
            "【阅读第６号】\x01",      # 5
            "【阅读第７号】\x01",      # 6
            "【阅读第８号】\x01",      # 7
            "【阅读第９号】\x01",      # 8
            "【阅读特別号】\x01",      # 9
            "【放弃】\x01",            # 10
        )
    )

    Jump("loc_36F3")

    label("loc_36F3")

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_5F(0x1)
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_372B")
    OP_B8(0xD2, 0x0)

    label("loc_372B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_373D")
    OP_B8(0xD3, 0x0)

    label("loc_373D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_374F")
    OP_B8(0xD4, 0x0)

    label("loc_374F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3761")
    OP_B8(0xD5, 0x0)

    label("loc_3761")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3773")
    OP_B8(0xD6, 0x0)

    label("loc_3773")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3785")
    OP_B8(0xD7, 0x0)

    label("loc_3785")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3797")
    OP_B8(0xD8, 0x0)

    label("loc_3797")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_37A9")
    OP_B8(0xD9, 0x0)

    label("loc_37A9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_37BB")
    OP_B8(0xDA, 0x0)

    label("loc_37BB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_37CD")
    OP_B8(0xDB, 0x0)

    label("loc_37CD")

    Jump("loc_39E5")

    label("loc_37D0")

    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        10,
        1,
        (
            "【阅读第１号】\x01",        # 0
            "【阅读第２号】\x01",        # 1
            "【阅读第３号】\x01",        # 2
            "【阅读第４号】\x01",        # 3
            "【阅读第５号】\x01",        # 4
            "【阅读第６号】\x01",        # 5
            "【阅读第７号】\x01",        # 6
            "【阅读特別号①】\x01",      # 7
            "【阅读第８号】\x01",        # 8
            "【阅读第９号】\x01",        # 9
            "【阅读第10号】\x01",        # 10
            "【阅读第11号】\x01",        # 11
            "【阅读特別号②】\x01",      # 12
            "【放弃】\x01",              # 13
        )
    )

    Jump("loc_38D2")

    label("loc_38D2")

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_5F(0x1)
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_390A")
    OP_B8(0xF1, 0x0)

    label("loc_390A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_391C")
    OP_B8(0xF2, 0x0)

    label("loc_391C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_392E")
    OP_B8(0xF3, 0x0)

    label("loc_392E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3940")
    OP_B8(0xF4, 0x0)

    label("loc_3940")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3952")
    OP_B8(0xF5, 0x0)

    label("loc_3952")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3964")
    OP_B8(0xF6, 0x0)

    label("loc_3964")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3976")
    OP_B8(0xF7, 0x0)

    label("loc_3976")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3988")
    OP_B8(0xF8, 0x0)

    label("loc_3988")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_399A")
    OP_B8(0xF9, 0x0)

    label("loc_399A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_39AC")
    OP_B8(0xFA, 0x0)

    label("loc_39AC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_39BE")
    OP_B8(0xFB, 0x0)

    label("loc_39BE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_39D0")
    OP_B8(0xFC, 0x0)

    label("loc_39D0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_39E2")
    OP_B8(0x326, 0x0)

    label("loc_39E2")

    Jump("loc_39E5")

    label("loc_39E5")

    FadeToBright(300, 0)
    OP_5F(0x0)
    TalkEnd(0xFF)
    Jump("loc_3EED")

    label("loc_39F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4CE, 6)), scpexpr(EXPR_END)), "loc_3CAD")
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #41
        "\x07\x05书柜上放着《利贝尔通讯》。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        10,
        1,
        "【０２年度后期～０３年度前期】\x01",
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_3A83"),
        (1, "loc_3C98"),
        (SWITCH_DEFAULT, "loc_3C9B"),
    )


    label("loc_3A83")

    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        10,
        1,
        (
            "【阅读第１号】\x01",        # 0
            "【阅读第２号】\x01",        # 1
            "【阅读第３号】\x01",        # 2
            "【阅读第４号】\x01",        # 3
            "【阅读第５号】\x01",        # 4
            "【阅读第６号】\x01",        # 5
            "【阅读第７号】\x01",        # 6
            "【阅读特別号①】\x01",      # 7
            "【阅读第８号】\x01",        # 8
            "【阅读第９号】\x01",        # 9
            "【阅读第10号】\x01",        # 10
            "【阅读第11号】\x01",        # 11
            "【阅读特別号②】\x01",      # 12
            "【放弃】\x01",              # 13
        )
    )

    Jump("loc_3B85")

    label("loc_3B85")

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_5F(0x1)
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3BBD")
    OP_B8(0xF1, 0x0)

    label("loc_3BBD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3BCF")
    OP_B8(0xF2, 0x0)

    label("loc_3BCF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3BE1")
    OP_B8(0xF3, 0x0)

    label("loc_3BE1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3BF3")
    OP_B8(0xF4, 0x0)

    label("loc_3BF3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3C05")
    OP_B8(0xF5, 0x0)

    label("loc_3C05")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3C17")
    OP_B8(0xF6, 0x0)

    label("loc_3C17")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3C29")
    OP_B8(0xF7, 0x0)

    label("loc_3C29")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3C3B")
    OP_B8(0xF8, 0x0)

    label("loc_3C3B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3C4D")
    OP_B8(0xF9, 0x0)

    label("loc_3C4D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3C5F")
    OP_B8(0xFA, 0x0)

    label("loc_3C5F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3C71")
    OP_B8(0xFB, 0x0)

    label("loc_3C71")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3C83")
    OP_B8(0xFC, 0x0)

    label("loc_3C83")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3C95")
    OP_B8(0x326, 0x0)

    label("loc_3C95")

    Jump("loc_3C9B")

    label("loc_3C98")

    Jump("loc_3C9B")

    label("loc_3C9B")

    FadeToBright(300, 0)
    OP_5F(0x0)
    TalkEnd(0xFF)
    Jump("loc_3EED")

    label("loc_3CAD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4CE, 1)), scpexpr(EXPR_END)), "loc_3EED")
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #42
        "\x07\x05书柜上放着《利贝尔通讯》。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        10,
        1,
        "【０２年度前期～０２年度中期】\x01",
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_3D30"),
        (SWITCH_DEFAULT, "loc_3EDE"),
    )


    label("loc_3D30")

    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        10,
        1,
        (
            "【阅读第１号】\x01",      # 0
            "【阅读第２号】\x01",      # 1
            "【阅读第３号】\x01",      # 2
            "【阅读第４号】\x01",      # 3
            "【阅读第５号】\x01",      # 4
            "【阅读第６号】\x01",      # 5
            "【阅读第７号】\x01",      # 6
            "【阅读第８号】\x01",      # 7
            "【阅读第９号】\x01",      # 8
            "【阅读特別号】\x01",      # 9
            "【放弃】\x01",            # 10
        )
    )

    Jump("loc_3E01")

    label("loc_3E01")

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_5F(0x1)
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3E39")
    OP_B8(0xD2, 0x0)

    label("loc_3E39")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3E4B")
    OP_B8(0xD3, 0x0)

    label("loc_3E4B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3E5D")
    OP_B8(0xD4, 0x0)

    label("loc_3E5D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3E6F")
    OP_B8(0xD5, 0x0)

    label("loc_3E6F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3E81")
    OP_B8(0xD6, 0x0)

    label("loc_3E81")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3E93")
    OP_B8(0xD7, 0x0)

    label("loc_3E93")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3EA5")
    OP_B8(0xD8, 0x0)

    label("loc_3EA5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3EB7")
    OP_B8(0xD9, 0x0)

    label("loc_3EB7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3EC9")
    OP_B8(0xDA, 0x0)

    label("loc_3EC9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3EDB")
    OP_B8(0xDB, 0x0)

    label("loc_3EDB")

    Jump("loc_3EDE")

    label("loc_3EDE")

    FadeToBright(300, 0)
    OP_5F(0x0)
    TalkEnd(0xFF)

    label("loc_3EED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4CE, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3F0D")
    Call(0, 23)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_3F0D")
    Call(0, 24)
    Jump("loc_3F0D")

    label("loc_3F0D")

    Return()

    # Function_22_34C4 end

    def Function_23_3F0E(): pass

    label("Function_23_3F0E")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4CE, 0)), scpexpr(EXPR_END)), "loc_3F29")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_3F29")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4CE, 1)), scpexpr(EXPR_END)), "loc_3F3A")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_3F3A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4CE, 2)), scpexpr(EXPR_END)), "loc_3F4B")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_3F4B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4CE, 3)), scpexpr(EXPR_END)), "loc_3F5C")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_3F5C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4CE, 4)), scpexpr(EXPR_END)), "loc_3F6D")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_3F6D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4CE, 5)), scpexpr(EXPR_END)), "loc_3F7E")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_3F7E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4CE, 6)), scpexpr(EXPR_END)), "loc_3F8F")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_3F8F")

    Return()

    # Function_23_3F0E end

    def Function_24_3F90(): pass

    label("Function_24_3F90")

    EventBegin(0x0)
    OP_22(0x222, 0x0, 0x64)
    Fade(500)
    SetChrPos(0x0, 65110, -11000, -56600, 289)
    SetChrPos(0x1, 64519, -11000, -57970, 313)
    SetChrPos(0x2, 66560, -11000, -56870, 282)
    SetChrPos(0x3, 65570, -11000, -59420, 294)
    FadeToDark(300, 0, 100)
    OP_C4(0x0, 0x800)
    SetChrName("")
    SetMessageWindowPos(-1, 60, -1, -1)
    OP_6D(65560, -10000, -57380, 0)
    OP_67(0, 5230, -10000, 0)
    OP_6B(2110, 0)
    OP_6C(339000, 0)
    OP_6E(450, 0)
    OP_0D()
    Sleep(500)

    AnonymousTalk(    #43
        (
            "\x07\x05#40W 吾赠予之知识碎片，\x01",
            "既已全部阅览完毕……\x01",
            "#500W\x01",
            "#40W　赞赏汝等探究之心，\x01",
            "在此赐予汝等祝福……\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    Sleep(500)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    OP_3E(0x15D, 1)

    AnonymousTalk(    #44
        "\x07\x00得到了\x1F\x5D\x01\x07\x00。\x02",
    )

    Jump("loc_40EB")

    label("loc_40EB")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_A2(0x2677)
    FadeToBright(300, 0)
    EventEnd(0x0)
    SetMapFlags(0x2000000)
    Return()

    # Function_24_3F90 end

    def Function_25_410B(): pass

    label("Function_25_410B")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4CE, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4164")
    OP_22(0x17, 0x0, 0x64)
    OP_82(0x0, 0x2)
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #45
        "\x07\x05在书柜上发现了似乎很难看懂的书。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_A2(0x2675)
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Jump("loc_42D4")

    label("loc_4164")

    FadeToDark(300, 0, 100)

    AnonymousTalk(    #46
        "\x07\x05书柜上放着似乎很难看懂的书。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        10,
        1,
        (
            "【阅读《实录百日战役》】\x01",        # 0
            "【阅读《卢安经济史·上》】\x01",      # 1
            "【阅读《卢安经济史·中》】\x01",      # 2
            "【阅读《卢安经济史·下》】\x01",      # 3
            "【阅读《结晶光学论集》】\x01",        # 4
            "【放弃】\x01",                        # 5
        )
    )

    Jump("loc_4248")

    label("loc_4248")

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_427D")
    OP_B8(0xDC, 0x0)

    label("loc_427D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_428F")
    OP_B8(0xDD, 0x0)

    label("loc_428F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_42A1")
    OP_B8(0xDE, 0x0)

    label("loc_42A1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_42B3")
    OP_B8(0xDF, 0x0)

    label("loc_42B3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_42C5")
    OP_B8(0xE0, 0x0)

    label("loc_42C5")

    FadeToBright(300, 0)
    OP_5F(0x0)
    TalkEnd(0xFF)

    label("loc_42D4")

    Return()

    # Function_25_410B end

    def Function_26_42D5(): pass

    label("Function_26_42D5")

    SetMapFlags(0x80)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(500, 0, -1)

    def lambda_42F3():
        OP_90(0x0, 0xFFFFFC18, 0x0, 0x3E8, 0x514, 0x0)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_42F3)
    OP_0D()
    NewScene("ED6_DT21/U7000   ._SN", 102, 0, 0)
    IdleLoop()
    EventEnd(0x0)
    Return()

    # Function_26_42D5 end

    def Function_27_4315(): pass

    label("Function_27_4315")

    SetMapFlags(0x80)
    FadeToDark(0, 0, -1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0x0, 16880, 1000, -14940, 135)
    SetChrPos(0x1, 16880, 1000, -14940, 135)
    SetChrPos(0x2, 16880, 1000, -14940, 135)
    SetChrPos(0x3, 16880, 1000, -14940, 135)
    OP_69(0x0, 0x0)
    Sleep(1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToBright(300, 0)
    ClearMapFlags(0x80)
    EventEnd(0x2)
    Return()

    # Function_27_4315 end

    SaveToFile()

Try(main)

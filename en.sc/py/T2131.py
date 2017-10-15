from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 卢安

    CreateScenaFile(
        FileName            = 'T2131   ._SN',
        MapName             = 'Ruan',
        Location            = 'T2131.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60012",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            'ED6_DT21/T2131   ._SN',
            'ED6_DT21/T2131_1 ._SN',
            'ED6_DT21/T2131_2 ._SN',
            '',
            '',
            '',
            'ED6_DT21/SUB000  ._SN',
            ''
        ],
    )

    BuildStringList(
        '@FileName',                            # 8
        'Primo',                                # 9
        'Spiridon',                             # 10
        'Lottelio',                             # 11
        'Fuego',                                # 12
        'Alund',                                # 13
        'Phelio',                               # 14
        'Lakeisha',                             # 15
        'Deen',                                 # 16
        'Squaro',                               # 17
        'Hardt',                                # 18
        'ランチ',                               # 19
        '茶',                                   # 20
        'Portos',                               # 21
        'Bolle',                                # 22
        'Pesca',                                # 23
        'Zecalte',                              # 24
        'Gunter',                               # 25
        'Targeting Camera',                     # 26
        'Targeting Camera2',                    # 27
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
        'ED6_DT07/CH01270 ._CH',             # 00
        'ED6_DT07/CH01560 ._CH',             # 01
        'ED6_DT27/CH03930 ._CH',             # 02
        'ED6_DT07/CH01570 ._CH',             # 03
        'ED6_DT07/CH01120 ._CH',             # 04
        'ED6_DT07/CH01040 ._CH',             # 05
        'ED6_DT07/CH01030 ._CH',             # 06
        'ED6_DT07/CH01123 ._CH',             # 07
        'ED6_DT06/CH20020 ._CH',             # 08
        'ED6_DT07/CH01680 ._CH',             # 09
        'ED6_DT07/CH01120 ._CH',             # 0A
        'ED6_DT07/CH01463 ._CH',             # 0B
        'ED6_DT07/CH02510 ._CH',             # 0C
        'ED6_DT07/CH01460 ._CH',             # 0D
        'ED6_DT07/CH01443 ._CH',             # 0E
    )

    AddCharChipPat(
        'ED6_DT07/CH01270P._CP',             # 00
        'ED6_DT07/CH01560P._CP',             # 01
        'ED6_DT27/CH03930P._CP',             # 02
        'ED6_DT07/CH01570P._CP',             # 03
        'ED6_DT07/CH01120P._CP',             # 04
        'ED6_DT07/CH01040P._CP',             # 05
        'ED6_DT07/CH01030P._CP',             # 06
        'ED6_DT07/CH01123P._CP',             # 07
        'ED6_DT06/CH20020P._CP',             # 08
        'ED6_DT07/CH01680P._CP',             # 09
        'ED6_DT07/CH01120P._CP',             # 0A
        'ED6_DT07/CH01463P._CP',             # 0B
        'ED6_DT07/CH02510P._CP',             # 0C
        'ED6_DT07/CH01460P._CP',             # 0D
        'ED6_DT07/CH01443P._CP',             # 0E
    )

    DeclNpc(
        X                   = -5500,
        Z                   = 300,
        Y                   = 33800,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 22,
    )

    DeclNpc(
        X                   = 26000,
        Z                   = 0,
        Y                   = 27230,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 18,
    )

    DeclNpc(
        X                   = 33420,
        Z                   = 0,
        Y                   = 35300,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 14,
    )

    DeclNpc(
        X                   = 35010,
        Z                   = 0,
        Y                   = 30340,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
    )

    DeclNpc(
        X                   = 24900,
        Z                   = 250,
        Y                   = 35290,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = 24900,
        Z                   = 250,
        Y                   = 35290,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = 24900,
        Z                   = 250,
        Y                   = 35290,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 1,
        TalkScenaIndex      = 0,
    )

    DeclNpc(
        X                   = -3510,
        Z                   = 250,
        Y                   = 31610,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 12,
        ChipIndex           = 0xC,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 23,
    )

    DeclNpc(
        X                   = -2940,
        Z                   = 0,
        Y                   = 5590,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 20,
    )

    DeclNpc(
        X                   = -1860,
        Z                   = 200,
        Y                   = 305,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x195,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = -2860,
        Z                   = 750,
        Y                   = 300,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 655368,
        ChipIndex           = 0x8,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -2920,
        Z                   = 750,
        Y                   = -220,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1638408,
        ChipIndex           = 0x8,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -17250,
        Z                   = 0,
        Y                   = 1960,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 9,
        ChipIndex           = 0x9,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = -22080,
        Z                   = 0,
        Y                   = 2720,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = -300,
        Z                   = 200,
        Y                   = 2126,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 11,
        ChipIndex           = 0xB,
        NpcIndex            = 0x115,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = -17650,
        Z                   = 200,
        Y                   = 3320,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 14,
        ChipIndex           = 0xE,
        NpcIndex            = 0x1D5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 24,
    )

    DeclNpc(
        X                   = 35040,
        Z                   = 0,
        Y                   = 27960,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 12,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x80,
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
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x80,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclActor(
        TriggerX            = -4000,
        TriggerZ            = 250,
        TriggerY            = 33700,
        TriggerRange        = 400,
        ActorX              = -5500,
        ActorZ              = 1800,
        ActorY              = 33800,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 21,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 33310,
        TriggerZ            = 0,
        TriggerY            = 33689,
        TriggerRange        = 400,
        ActorX              = 33420,
        ActorZ              = 1700,
        ActorY              = 35300,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 14,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 33190,
        TriggerZ            = 0,
        TriggerY            = 30422,
        TriggerRange        = 1000,
        ActorX              = 35010,
        ActorZ              = 1700,
        ActorY              = 30340,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 10,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 33190,
        TriggerZ            = 0,
        TriggerY            = 27980,
        TriggerRange        = 1000,
        ActorX              = 35040,
        ActorZ              = 1700,
        ActorY              = 27960,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 12,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 25610,
        TriggerZ            = 0,
        TriggerY            = 28960,
        TriggerRange        = 1700,
        ActorX              = 26000,
        ActorZ              = 1700,
        ActorY              = 27230,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 18,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 27820,
        TriggerZ            = 0,
        TriggerY            = 28620,
        TriggerRange        = 1700,
        ActorX              = 26000,
        ActorZ              = 1700,
        ActorY              = 27230,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 18,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 25000,
        TriggerZ            = 250,
        TriggerY            = 36880,
        TriggerRange        = 700,
        ActorX              = 25150,
        ActorZ              = 1500,
        ActorY              = 37640,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 17,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 27030,
        TriggerZ            = 250,
        TriggerY            = 36880,
        TriggerRange        = 700,
        ActorX              = 27030,
        ActorZ              = 1500,
        ActorY              = 37640,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 16,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 28730,
        TriggerZ            = 0,
        TriggerY            = 37220,
        TriggerRange        = 800,
        ActorX              = 28730,
        ActorZ              = 1800,
        ActorY              = 37220,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 25,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_4C6",          # 00, 0
        "Function_1_647",          # 01, 1
        "Function_2_725",          # 02, 2
        "Function_3_72C",          # 03, 3
        "Function_4_D52",          # 04, 4
        "Function_5_1520",         # 05, 5
        "Function_6_1E37",         # 06, 6
        "Function_7_1F0A",         # 07, 7
        "Function_8_22A5",         # 08, 8
        "Function_9_27A6",         # 09, 9
        "Function_10_2B69",        # 0A, 10
        "Function_11_2C2F",        # 0B, 11
        "Function_12_3353",        # 0C, 12
        "Function_13_341D",        # 0D, 13
        "Function_14_3A74",        # 0E, 14
        "Function_15_3B35",        # 0F, 15
        "Function_16_43B2",        # 10, 16
        "Function_17_4468",        # 11, 17
        "Function_18_451F",        # 12, 18
        "Function_19_45E8",        # 13, 19
        "Function_20_51C2",        # 14, 20
        "Function_21_5D78",        # 15, 21
        "Function_22_5D7D",        # 16, 22
        "Function_23_66AD",        # 17, 23
        "Function_24_67C2",        # 18, 24
        "Function_25_6A84",        # 19, 25
    )


    def Function_0_4C6(): pass

    label("Function_0_4C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_523")
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0x14, 0x80)
    SetChrPos(0x16, -1030, 0, 2240, 0)
    SetChrChipByIndex(0x16, 13)
    ClearChrFlags(0x16, 0x10)
    ClearChrFlags(0x16, 0x4)
    OP_43(0x16, 0x0, 0x6, 0x2)
    ClearChrFlags(0x17, 0x80)
    OP_8C(0x15, 180, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_END)), "loc_520")
    ClearChrFlags(0xF, 0x80)
    SetChrFlags(0xC, 0x80)

    label("loc_520")

    Jump("loc_646")

    label("loc_523")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_END)), "loc_580")
    SetChrPos(0xC, -6569, 0, 32668, 270)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x68, 0x0, 0x10)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x68, 0x0, 0x40)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_54F")
    Jump("loc_565")

    label("loc_54F")

    SetChrPos(0xD, 32520, 0, 29800, 90)
    SetChrFlags(0xD, 0x10)

    label("loc_565")

    SetChrPos(0xE, 5386, 250, 34285, 180)
    OP_8C(0x9, 90, 0)
    Jump("loc_646")

    label("loc_580")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 5)), scpexpr(EXPR_END)), "loc_5AF")
    SetChrFlags(0xC, 0x80)
    SetChrPos(0xE, 4570, 250, 30488, 90)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    Jump("loc_646")

    label("loc_5AF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 4)), scpexpr(EXPR_END)), "loc_5FB")
    SetChrFlags(0x8, 0x80)
    SetChrPos(0xC, 32603, 0, 29644, 67)
    SetChrPos(0xD, 33180, 0, 31996, 135)
    SetChrFlags(0xD, 0x10)
    SetChrFlags(0xC, 0x10)
    SetChrPos(0xE, -2350, 250, 33680, 270)
    Jump("loc_646")

    label("loc_5FB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x242, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_635")
    SetChrPos(0xC, 32603, 0, 29644, 67)
    SetChrPos(0xD, 33180, 0, 31996, 135)
    SetChrFlags(0xD, 0x10)
    SetChrFlags(0xC, 0x10)
    Jump("loc_646")

    label("loc_635")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 6)), scpexpr(EXPR_END)), "loc_646")
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xE, 0x80)

    label("loc_646")

    Return()

    # Function_0_4C6 end

    def Function_1_647(): pass

    label("Function_1_647")

    OP_71(0x3, 0x8)
    OP_71(0x3, 0x20)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_661")
    OP_64(0x0, 0x1)

    label("loc_661")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_695")
    OP_72(0x0, 0x20)
    OP_72(0x0, 0x8)
    OP_72(0x1, 0x20)
    OP_72(0x1, 0x8)
    OP_72(0x2, 0x20)
    OP_72(0x2, 0x8)
    OP_72(0x3, 0x20)
    OP_72(0x3, 0x8)

    label("loc_695")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6E4")
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (105, "loc_6B5"),
        (106, "loc_6C5"),
        (107, "loc_6C5"),
        (SWITCH_DEFAULT, "loc_6D5"),
    )


    label("loc_6B5")

    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 2)
    Jump("loc_6E1")

    label("loc_6C5")

    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x19), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 2)
    Jump("loc_6E1")

    label("loc_6D5")

    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_6E1")

    label("loc_6E1")

    Jump("loc_724")

    label("loc_6E4")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (105, "loc_6F8"),
        (106, "loc_708"),
        (107, "loc_708"),
        (SWITCH_DEFAULT, "loc_718"),
    )


    label("loc_6F8")

    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 2)
    Jump("loc_724")

    label("loc_708")

    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x19), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 2)
    Jump("loc_724")

    label("loc_718")

    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_724")

    label("loc_724")

    Return()

    # Function_1_647 end

    def Function_2_725(): pass

    label("Function_2_725")

    OP_20(0x3E8)
    OP_21()
    Return()

    # Function_2_725 end

    def Function_3_72C(): pass

    label("Function_3_72C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_END)), "loc_863")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7F7")

    ChrTalk(    #0
        0xFE,
        (
            "Aaaagh! Won't the orbments start\x01",
            "working again, already?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        (
            "If I could just launch my pride and\x01",
            "joy--my ship!--I'd catch a hundred\x01",
            "times the fish I normally could! *sigh*\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xC)
    Jump("loc_85C")

    label("loc_7F7")


    ChrTalk(    #2
        0xFE,
        (
            "Aaaagh! Won't the orbments start\x01",
            "working again, already?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0xFE,
        "Snacks are off limits till then.\x02",
    )

    CloseMessageWindow()

    label("loc_85C")

    TalkEnd(0xFE)
    Return()

    label("loc_863")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_A59")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9AC")

    ChrTalk(    #4
        0xFE,
        (
            "I can't put out my normal ship,\x01",
            "so I can't do much else but try and\x01",
            "catch fish on my old boat for now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0xFE,
        (
            "It's not the best, though. No way to\x01",
            "catch more than a few fish at a time\x01",
            "with it, so things are getting tough...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0xFE,
        (
            "Even if I work all day, I barely make\x01",
            "enough mira for a single Azelia Kiss!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xC)
    Jump("loc_A55")

    label("loc_9AC")


    ChrTalk(    #7
        0xFE,
        (
            "If I can't put out my ship, I guess\x01",
            "I'm out of a job as a fisherman...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0xFE,
        (
            "I can work all damn day and still\x01",
            "come home with barely enough\x01",
            "mira for a single drink.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A55")

    TalkEnd(0xFE)
    Return()

    label("loc_A59")

    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    Jc((scpexpr(EXPR_PUSH_LONG, 0x1E), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_LSS), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x96), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A86")
    SetChrSubChip(0xFE, 2)
    Jump("loc_AAC")

    label("loc_A86")

    Jc((scpexpr(EXPR_PUSH_LONG, 0xD2), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_LSS), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x14A), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_AA7")
    SetChrSubChip(0xFE, 1)
    Jump("loc_AAC")

    label("loc_AA7")

    SetChrSubChip(0xFE, 0)

    label("loc_AAC")

    OP_8C(0xFE, 0, 0)
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_END)), "loc_B56")

    ChrTalk(    #9
        0xFE,
        (
            "I wonder if those guys in the\x01",
            "warehouse even care about\x01",
            "the election.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0xFE,
        (
            "Don't they know they're out on\x01",
            "their asses if Norman becomes\x01",
            "mayor?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D49")

    label("loc_B56")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 5)), scpexpr(EXPR_END)), "loc_BB7")

    ChrTalk(    #11
        0xFE,
        "Everyone's on edge.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0xFE,
        (
            "I don't think fighting over election\x01",
            "stuff helps anyone.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D49")

    label("loc_BB7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x242, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_C79")

    ChrTalk(    #13
        0xFE,
        (
            "True, I don't know much about\x01",
            "the nitty-gritty stuff...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0xFE,
        (
            "But even I know as much as anyone\x01",
            "that Mayor Dalmore never did much\x01",
            "for us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0xFE,
        "He never even fixed the crane...\x02",
    )

    CloseMessageWindow()
    Jump("loc_D49")

    label("loc_C79")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 6)), scpexpr(EXPR_END)), "loc_D49")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_END)), "loc_CD5")

    ChrTalk(    #16
        0xFE,
        (
            "I'm thinkin' of helping to distribute\x01",
            "fliers when I've got free time.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D49")

    label("loc_CD5")

    OP_A2(0xC)

    ChrTalk(    #17
        0xFE,
        (
            "I'm a fisherman, you know? If we\x01",
            "lose the harbor, I'm in big trouble.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0xFE,
        "I'm wishin' Portos all the best!\x02",
    )

    CloseMessageWindow()

    label("loc_D49")

    SetChrSubChip(0xFE, 0)
    TalkEnd(0xFE)
    Return()

    # Function_3_72C end

    def Function_4_D52(): pass

    label("Function_4_D52")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_END)), "loc_E6D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DFB")

    ChrTalk(    #19
        0xFE,
        (
            "As long as these orbments ain't\x01",
            "workin', we sailors ain't got shit to\x01",
            "do.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0xFE,
        (
            "I'm sure the airship crews're bored\x01",
            "outta their skulls, too.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xB)
    Jump("loc_E6A")

    label("loc_DFB")


    ChrTalk(    #21
        0xFE,
        (
            "As long as these orbments ain't\x01",
            "workin', we sailors ain't got shit to\x01",
            "do.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0xFE,
        "We're like a fish on land.\x02",
    )

    CloseMessageWindow()

    label("loc_E6A")

    Jump("loc_151C")

    label("loc_E6D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_FF3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F58")

    ChrTalk(    #23
        0xFE,
        (
            "It's gotten better, but the city's still\x01",
            "a hell of a mess.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0xFE,
        (
            "But the all-important Mayor Norman's\x01",
            "stuck up in his big, fancy mansion, so...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0xFE,
        (
            "Damn it! This is why we should've\x01",
            "had Portos as the mayor...\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xB)
    Jump("loc_FF0")

    label("loc_F58")


    ChrTalk(    #26
        0xFE,
        (
            "Norman wins the election and this\x01",
            "is what we get.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0xFE,
        (
            "A pack of idiots, the whole lot of\x01",
            "Ruanians. Not a one of 'em know\x01",
            "how to judge a real man.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_FF0")

    Jump("loc_151C")

    label("loc_FF3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_END)), "loc_10D6")

    ChrTalk(    #28
        0xFE,
        (
            "We gotta let those folks on the other\x01",
            "side of the bridge know about all the\x01",
            "problems with the harbor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0xFE,
        (
            "They may THINK it's got nothin' to\x01",
            "do with them, but they'll be singin' a\x01",
            "different tune if Norman wins.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_151C")

    label("loc_10D6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 5)), scpexpr(EXPR_END)), "loc_11AD")

    ChrTalk(    #30
        0xFE,
        (
            "What a mess... I'm just glad no one\x01",
            "was hurt.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0xFE,
        (
            "It's 'cause Portos knows how to\x01",
            "keep his cool, even when things're\x01",
            "about to get ugly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0xFE,
        (
            "He's the kinda guy you can count\x01",
            "on when times are rough.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_151C")

    label("loc_11AD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x242, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_133B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_121D")

    ChrTalk(    #33
        0xFE,
        (
            "Problems with the harbor ain't\x01",
            "just about the mira.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0xFE,
        "It's about this town's soul.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1338")

    label("loc_121D")

    OP_A2(0xB)

    ChrTalk(    #35
        0xFE,
        (
            "Hey there! Welcome to the office\x01",
            "for Portos' election campaign.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0xFE,
        (
            "I'm a sailor, just like him--and I know\x01",
            "he's the man to change things at the\x01",
            "harbor for the better.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0xFE,
        (
            "You know what'll happen if we let\x01",
            "Norman win? The harbor'll become\x01",
            "even shoddier than it already is!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1338")

    Jump("loc_151C")

    label("loc_133B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 6)), scpexpr(EXPR_END)), "loc_151C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_1410")

    ChrTalk(    #38
        0xFE,
        (
            "Portos may be on the shy side, but\x01",
            "damn it if he ain't a real man of the\x01",
            "sea.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0xFE,
        (
            "We're gonna need all the votes we\x01",
            "can get, so I hope you'll give him your\x01",
            "full backing during the election!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_151C")

    label("loc_1410")

    OP_A2(0xB)

    ChrTalk(    #40
        0xFE,
        (
            "Hey there! Welcome to the office\x01",
            "for Portos' election campaign.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0xFE,
        (
            "Portos may be on the shy side, but\x01",
            "damn it if he ain't a real man of the\x01",
            "sea.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0xFE,
        (
            "We're gonna need all the votes we\x01",
            "can get, so I hope you'll give him your\x01",
            "full backing during the election!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_151C")

    TalkEnd(0xFE)
    Return()

    # Function_4_D52 end

    def Function_5_1520(): pass

    label("Function_5_1520")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_END)), "loc_1818")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_1601")

    ChrTalk(    #43
        0xFE,
        (
            "We need to start putting more effort\x01",
            "into campaigning on the north side\x01",
            "of the city. \x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0xFE,
        (
            "We'll never get those who believe in\x01",
            "expanding tourism to understand our\x01",
            "cause without getting the word out.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1815")

    label("loc_1601")

    OP_A2(0xA)

    ChrTalk(    #45
        0xFE,
        (
            "We need to start putting more effort\x01",
            "into campaigning on the north side\x01",
            "of the city. \x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0xFE,
        (
            "We'll never get those who believe in\x01",
            "expanding tourism to understand our\x01",
            "cause without getting the word out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0xFE,
        (
            "It's not that we're against expanding\x01",
            "the tourism industry--far from it, even.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0xFE,
        (
            "But think: we had virtually no funds to\x01",
            "help run the harbor with our last mayor.\x01",
            "We need to better balance our budget!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0xFE,
        (
            "The logic behind my campaign is\x01",
            "clear enough, and yet we're still having\x01",
            "trouble coming to an understanding...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1815")

    Jump("loc_1E33")

    label("loc_1818")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 5)), scpexpr(EXPR_END)), "loc_19FB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_18FA")

    ChrTalk(    #50
        0xFE,
        (
            "I love the people of the harbor, but they\x01",
            "can be far too blunt and confrontational\x01",
            "for their own good.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0xFE,
        (
            "It's a testament to how good and\x01",
            "honest they are as people, however.\x01",
            "I couldn't ask for better.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_19F8")

    label("loc_18FA")

    OP_A2(0xA)

    ChrTalk(    #52
        0xFE,
        (
            "*pheeew* I'm just glad things\x01",
            "didn't go too far in the end...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0xFE,
        (
            "I have every intention of making the\x01",
            "one responsible for this fuss march\x01",
            "right over and apologize to Mr. Norman.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0xFE,
        (
            "I don't want any bad blood to remain\x01",
            "between our supporters.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_19F8")

    Jump("loc_1E33")

    label("loc_19FB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x242, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1C7C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_1AFD")

    ChrTalk(    #55
        0xFE,
        (
            "I won't deny that the center of Ruan's\x01",
            "economy is tourism, but we can't let\x01",
            "the harbor be sacrificed for it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0xFE,
        (
            "If we let some of the older buildings\x01",
            "continue to deteriorate like this, we're\x01",
            "in real danger of accidents occurring.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C79")

    label("loc_1AFD")

    OP_A2(0xA)

    ChrTalk(    #57
        0xFE,
        (
            "As Mr. Norman says, the center\x01",
            "of Ruan's economy is tourism.\x01",
            "There's no denying that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0xFE,
        (
            "That doesn't mean we can just ignore\x01",
            "the harbor in the condition it's currently\x01",
            "in, however.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0xFE,
        (
            "We pose a real risk of accidents that\x01",
            "could be easily prevented if we don't\x01",
            "make an effort to restore out harbor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0xFE,
        (
            "We have to act now: It'll be too late\x01",
            "once someone's been hurt.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C79")

    Jump("loc_1E33")

    label("loc_1C7C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 6)), scpexpr(EXPR_END)), "loc_1E33")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_1D11")

    ChrTalk(    #61
        0xFE,
        (
            "To be honest, I've always felt out\x01",
            "of my league just representing the\x01",
            "harbor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0xFE,
        (
            "But now I'm a mayoral candidate!\x01",
            "Oh, man...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E33")

    label("loc_1D11")

    OP_A2(0xA)

    ChrTalk(    #63
        0xFE,
        (
            "Man, oh, man. To be honest, I'm still\x01",
            "not sure I have what it takes to run for\x01",
            "mayor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0xFE,
        (
            "But with everyone pushing me to do\x01",
            "it, well, I didn't have much choice but\x01",
            "to announce my candidacy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0xFE,
        (
            "And I won't run halfheartedly, either.\x01",
            "I'm going to give this election all I've\x01",
            "got!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E33")

    TalkEnd(0xFE)
    Return()

    # Function_5_1520 end

    def Function_6_1E37(): pass

    label("Function_6_1E37")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_1E89")

    ChrTalk(    #66
        0x11,
        (
            "It sure was loud outside earlier...\x02\x03",

            "Do you know what happened?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F06")

    label("loc_1E89")

    OP_A2(0x8)

    ChrTalk(    #67
        0x11,
        (
            "Nice! The price is about right\x01",
            "and the flavor's certainly good\x01",
            "enough.\x02\x03",

            "I'm sure this'll be a hit with the\x01",
            "tourists!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F06")

    TalkEnd(0xFE)
    Return()

    # Function_6_1E37 end

    def Function_7_1F0A(): pass

    label("Function_7_1F0A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_END)), "loc_20D7")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x68, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_1FAE")

    ChrTalk(    #68
        0xFE,
        (
            "Ha...haha. This loss is but a small\x01",
            "stepping stone on my path to glory!\x01",
            "This is NOTHING.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0xFE,
        (
            "Time to win a bunch and earn it\x01",
            "all back!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_20D4")

    label("loc_1FAE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x68, 0x0, 0x40)"), scpexpr(EXPR_END)), "loc_2062")

    ChrTalk(    #70
        0xFE,
        "Hahaha! You guys weren't half bad.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0xFE,
        (
            "You just chose the wrong guy to\x01",
            "mess with.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0xFE,
        (
            "All right. I think I could win a little\x01",
            "more mira if I just tried this...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_20D4")

    label("loc_2062")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_20CD")

    ChrTalk(    #73
        0xD,
        (
            "Fear not, friends! You fought well.\x01",
            "You just chose the wrong guy to\x01",
            "mess with.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0xD,
        "Hahaha!\x02",
    )

    CloseMessageWindow()
    Jump("loc_20D4")

    label("loc_20CD")

    OP_A2(0x6)
    Call(0, 9)

    label("loc_20D4")

    Jump("loc_22A1")

    label("loc_20D7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 5)), scpexpr(EXPR_END)), "loc_224B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_2193")

    ChrTalk(    #75
        0xFE,
        (
            "Everyone's so intimidated by my\x01",
            "flawless skill that they won't even\x01",
            "play me at cards.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0xFE,
        (
            "*sigh* Nothing for it, I guess. Might\x01",
            "as well play some slots for a while.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2248")

    label("loc_2193")

    OP_A2(0x6)

    ChrTalk(    #77
        0xFE,
        "MAN! I even win big playing slots!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0xFE,
        (
            "Is this a message from the Goddess\x01",
            "telling me to quit my job and become\x01",
            "a gambler?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0xFE,
        (
            "Yes! This much be the divine will\x01",
            "of Aidios!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2248")

    Jump("loc_22A1")

    label("loc_224B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x242, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_22A1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_229A")

    ChrTalk(    #80
        0xFE,
        "WHOO HOOOO! I won again!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0xFE,
        "I'm a gambling GENIUS!\x02",
    )

    CloseMessageWindow()
    Jump("loc_22A1")

    label("loc_229A")

    OP_A2(0x6)
    Call(0, 9)

    label("loc_22A1")

    TalkEnd(0xFE)
    Return()

    # Function_7_1F0A end

    def Function_8_22A5(): pass

    label("Function_8_22A5")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_24BD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2419")

    ChrTalk(    #82
        0xFE,
        (
            "I finally got my pay for washing\x01",
            "dishes downstairs.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0xFE,
        "So now I'm here for another challenge!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0xFE,
        (
            "You know how it is. Gotta make a little\x01",
            "mira to beef up that travel fund before\x01",
            "the scheduled liners resume, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0xFE,
        (
            "I totally sucked when I'd started, but now\x01",
            "that I'm starting to get the hang of things,\x01",
            "it should be easy enough to win.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x5)
    Jump("loc_24BA")

    label("loc_2419")


    ChrTalk(    #86
        0xFE,
        (
            "I just gotta win enough to replenish\x01",
            "my travel funds before the scheduled\x01",
            "liners resume.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0xFE,
        (
            "Phew! All right! Time to kick it into\x01",
            "high gear at the slots!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_24BA")

    Jump("loc_27A2")

    label("loc_24BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_END)), "loc_25A8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_252B")

    ChrTalk(    #88
        0xFE,
        (
            "Nothing like good, ol' fashioned\x01",
            "hard labor to give you a real sense\x01",
            "of accomplishment.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_25A5")

    label("loc_252B")

    OP_A2(0x5)

    ChrTalk(    #89
        0xFE,
        (
            "I lost all my travel money to go\x01",
            "home at the casino...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0xFE,
        (
            "So I ended up having to take on\x01",
            "a part-time job here.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_25A5")

    Jump("loc_27A2")

    label("loc_25A8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 5)), scpexpr(EXPR_END)), "loc_25B2")
    Jump("loc_27A2")

    label("loc_25B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x242, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2661")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_2657")

    ChrTalk(    #91
        0xFE,
        "Whaaaaaaaat? I lost? AGAIN?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0xFE,
        (
            "N-No, there must be some mistake!\x01",
            "I couldn't lose to an amateur like\x01",
            "this! How can my luck be this bad?!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_265E")

    label("loc_2657")

    OP_A2(0x5)
    Call(0, 9)

    label("loc_265E")

    Jump("loc_27A2")

    label("loc_2661")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 6)), scpexpr(EXPR_END)), "loc_27A2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_2707")

    ChrTalk(    #93
        0xFE,
        (
            "It doesn't seem like my mojo at\x01",
            "the slots is gonna come back...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0xFE,
        (
            "Guess I'll just have to find a few\x01",
            "suckers to play a around of cards\x01",
            "with.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_27A2")

    label("loc_2707")

    OP_A2(0x5)

    ChrTalk(    #95
        0xFE,
        (
            "Man, these slots are old and\x01",
            "rickety as all hell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #96
        0xFE,
        (
            "They're not nearly as nice as\x01",
            "the modern ones.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0xFE,
        "...Which is totally why I lost. Yeah...\x02",
    )

    CloseMessageWindow()

    label("loc_27A2")

    TalkEnd(0xFE)
    Return()

    # Function_8_22A5 end

    def Function_9_27A6(): pass

    label("Function_9_27A6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_END)), "loc_2902")
    OP_A2(0x3)
    OP_A2(0x6)
    OP_4A(0xD, 255)
    OP_4A(0xB, 255)

    ChrTalk(    #98
        0xD,
        "...All right, come on, come on!\x02",
    )

    CloseMessageWindow()
    OP_62(0xD, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_63(0xD)
    OP_62(0xD, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(400)
    RunExpression(0x5, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2845")

    ChrTalk(    #99
        0xD,
        "Got it! Jack!\x02",
    )

    CloseMessageWindow()
    Jump("loc_287F")

    label("loc_2845")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2869")

    ChrTalk(    #100
        0xD,
        "Got it! Joker!\x02",
    )

    CloseMessageWindow()
    Jump("loc_287F")

    label("loc_2869")


    ChrTalk(    #101
        0xD,
        "Here we go! Ace!\x02",
    )

    CloseMessageWindow()

    label("loc_287F")


    ChrTalk(    #102
        0xB,
        "...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0xB,
        "...It is your win, sir.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0xD,
        (
            "You fought well, my good man!\x01",
            "Just not well enough to face ME.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0xD,
        "Hahaha!!\x02",
    )

    CloseMessageWindow()
    OP_4B(0xD, 255)
    OP_4B(0xB, 255)
    Jump("loc_2B68")

    label("loc_2902")

    OP_A2(0x5)
    OP_A2(0x3)
    OP_A2(0x6)
    OP_4A(0xD, 255)
    OP_4A(0xB, 255)
    OP_4A(0xC, 255)

    ChrTalk(    #106
        0xB,
        "It is your turn, sir.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0xC,
        "Hmm...\x02",
    )

    CloseMessageWindow()
    RunExpression(0x5, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2982")

    ChrTalk(    #108
        0xC,
        "A-All right! I'll call your bluff.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2A04")

    label("loc_2982")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_29AD")

    ChrTalk(    #109
        0xC,
        "Of course! I'll call!\x02",
    )

    CloseMessageWindow()
    Jump("loc_2A04")

    label("loc_29AD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_29E4")

    ChrTalk(    #110
        0xC,
        "This one's in the bag! I'll call.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2A04")

    label("loc_29E4")


    ChrTalk(    #111
        0xC,
        "All or nothing! I'll call!\x02",
    )

    CloseMessageWindow()

    label("loc_2A04")


    ChrTalk(    #112
        0xD,
        "Heh heh, you sure?\x02",
    )

    CloseMessageWindow()
    RunExpression(0x5, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2A5C")

    ChrTalk(    #113
        0xD,
        "I've got three aces over here.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2B36")

    label("loc_2A5C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2A93")

    ChrTalk(    #114
        0xD,
        "I've got an easy full house here.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2B36")

    label("loc_2A93")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2AC8")

    ChrTalk(    #115
        0xD,
        "I've got a four of a kind here.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2B36")

    label("loc_2AC8")


    ChrTalk(    #116
        0xD,
        "I've got a flush here.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #117
        0xD,
        (
            "Huh? You know, now that I look closely,\x01",
            "this might even be a straight flush.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2B36")


    ChrTalk(    #118
        0xC,
        "Aaaaaaaaahhhhhhh! I lose AGAIN?!\x02",
    )

    CloseMessageWindow()
    OP_4B(0xD, 255)
    OP_4B(0xB, 255)
    OP_4B(0xC, 255)

    label("loc_2B68")

    Return()

    # Function_9_27A6 end

    def Function_10_2B69(): pass

    label("Function_10_2B69")

    TalkBegin(0xB)
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "Talk\x01",            # 0
            "Play Poker\x01",      # 1
            "Leave\x01",           # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2C14")
    FadeToDark(300, 0, -1)
    OP_0D()
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_C0(0xF, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_56(0x0)
    FadeToBright(300, 0)
    TalkEnd(0xB)
    Return()

    label("loc_2C14")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2C27")
    OP_56(0x0)
    TalkEnd(0xB)
    Return()

    label("loc_2C27")

    Call(0, 11)
    TalkEnd(0xB)
    Return()

    # Function_10_2B69 end

    def Function_11_2C2F(): pass

    label("Function_11_2C2F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_3093")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x68, 0x0, 0x10)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x68, 0x0, 0x80)"), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x416, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2DC3")

    ChrTalk(    #119
        0xB,
        "Oh, hello. It's been some time.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #120
        0xB,
        (
            "You were in a most impressive\x01",
            "match when last we met.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #121
        0x101,
        (
            "#1016FAhaha... Oh, yeah. Guess we were,\x01",
            "weren't we?\x02\x03",

            "Not that I was all that big a help\x01",
            "during said match...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0x101, 400)

    ChrTalk(    #122
        0xB,
        "My, no need to be so humble.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #123
        0xB,
        (
            "If I may, I would be glad to serve\x01",
            "as your opponent at any time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #124
        0xB,
        (
            "Please enjoy our games at your\x01",
            "leisure.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)
    OP_A2(0x20B6)
    Jump("loc_3090")

    label("loc_2DC3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_2E40")

    ChrTalk(    #125
        0xB,
        (
            "If I may, I would be glad to serve\x01",
            "as your opponent at any time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #126
        0xB,
        (
            "Please enjoy our games at your\x01",
            "leisure.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3090")

    label("loc_2E40")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_END)), "loc_303C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2F79")

    ChrTalk(    #127
        0xB,
        (
            "The south block was a large part of\x01",
            "our clientele, but now it's become\x01",
            "difficult to cross with the bridge down.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #128
        0xB,
        (
            "The sailors used to visit often in\x01",
            "particular, but their numbers have\x01",
            "dwindled by the day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #129
        0xB,
        (
            "The bridge being closed has started\x01",
            "to take quite a toll on our business.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)
    Jump("loc_3039")

    label("loc_2F79")


    ChrTalk(    #130
        0xB,
        (
            "The south block was a large part\x01",
            "of our clientele, but now it's become\x01",
            "difficult to cross.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #131
        0xB,
        (
            "The sailors used to visit often in\x01",
            "particular, but their numbers have\x01",
            "dwindled by the day.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3039")

    Jump("loc_3090")

    label("loc_303C")


    ChrTalk(    #132
        0xB,
        "Welcome.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #133
        0xB,
        (
            "If I may, I would be glad to serve\x01",
            "as your opponent at any time.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3090")

    Jump("loc_3352")

    label("loc_3093")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_END)), "loc_31FD")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x68, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_311F")

    ChrTalk(    #134
        0xB,
        (
            "Your match was splendid. If you\x01",
            "would, please let us take care of\x01",
            "the rest.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #135
        0xB,
        "We'll take excellent care of him.\x02",
    )

    CloseMessageWindow()
    Jump("loc_31FA")

    label("loc_311F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x68, 0x0, 0x40)"), scpexpr(EXPR_END)), "loc_319D")

    ChrTalk(    #136
        0xB,
        (
            "If even bracers couldn't stop him,\x01",
            "then we have no other choice...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #137
        0xB,
        "Time to bring out our final weapon.\x02",
    )

    CloseMessageWindow()
    Jump("loc_31FA")

    label("loc_319D")


    ChrTalk(    #138
        0xB,
        (
            "Why, this guest appears to be\x01",
            "MOST lucky.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #139
        0xB,
        (
            "Would you like to take up the\x01",
            "challenge?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_31FA")

    Jump("loc_3352")

    label("loc_31FD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 5)), scpexpr(EXPR_END)), "loc_3281")

    ChrTalk(    #140
        0xB,
        (
            "I wonder why the supporters got\x01",
            "so worked up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #141
        0xB,
        (
            "Do they have mira riding on the\x01",
            "outcome of the election, perhaps?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3352")

    label("loc_3281")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x242, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_32B7")

    ChrTalk(    #142
        0xB,
        "Have you been enjoying yourselves?\x02",
    )

    CloseMessageWindow()
    Jump("loc_3352")

    label("loc_32B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 6)), scpexpr(EXPR_END)), "loc_3352")

    ChrTalk(    #143
        0xB,
        (
            "Welcome to a world of chance--a world\x01",
            "where, for a lucky few, a single game of\x01",
            "cards could change their destiny...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #144
        0xB,
        "I shall be your match.\x02",
    )

    CloseMessageWindow()

    label("loc_3352")

    Return()

    # Function_11_2C2F end

    def Function_12_3353(): pass

    label("Function_12_3353")

    TalkBegin(0x18)
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "Talk\x01",                # 0
            "Play Blackjack\x01",      # 1
            "Leave\x01",               # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3402")
    FadeToDark(300, 0, -1)
    OP_0D()
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_C0(0xD, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_56(0x0)
    FadeToBright(300, 0)
    TalkEnd(0x18)
    Return()

    label("loc_3402")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3415")
    OP_56(0x0)
    TalkEnd(0x18)
    Return()

    label("loc_3415")

    Call(0, 13)
    TalkEnd(0x18)
    Return()

    # Function_12_3353 end

    def Function_13_341D(): pass

    label("Function_13_341D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_END)), "loc_3537")

    ChrTalk(    #145
        0x18,
        (
            "It was the owner's eccentric tastes that\x01",
            "made him include non-orbal machines.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #146
        0x18,
        (
            "Didn't know what to make of it at first,\x01",
            "but it ended up being a smart move after\x01",
            "all. They work even with the power down.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #147
        0x18,
        (
            "The owner's instincts are right on the\x01",
            "mira, as always.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3A73")

    label("loc_3537")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_3601")

    ChrTalk(    #148
        0x18,
        (
            "Hey, it's a dark and harsh world out\x01",
            "there now. Why not play a few games\x01",
            "to ease your troubles before you go?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #149
        0x18,
        (
            "It's times like this where you need to\x01",
            "make sure you have a little fun.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3A73")

    label("loc_3601")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_END)), "loc_36C8")

    ChrTalk(    #150
        0x18,
        (
            "It's important to know when to ride\x01",
            "the wave and win, and that if you ride\x01",
            "it too far, you can get hurt.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #151
        0x18,
        (
            "Being able to read the flow of\x01",
            "the game is the key to winning\x01",
            "any gamble.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3A73")

    label("loc_36C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 5)), scpexpr(EXPR_END)), "loc_3849")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_END)), "loc_3747")

    ChrTalk(    #152
        0x18,
        (
            "I don't ever want to get involved\x01",
            "with politics as long as I live.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #153
        0x18,
        "Yeah, I'm not gonna vote either!\x02",
    )

    CloseMessageWindow()
    Jump("loc_3846")

    label("loc_3747")

    OP_A2(0xE)

    ChrTalk(    #154
        0x18,
        (
            "There was some argument going\x01",
            "down between the supports on the\x01",
            "bridge.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #155
        0x18,
        (
            "It's only once you take away the fancy\x01",
            "speeches and podiums that you see\x01",
            "what people in politics are really like.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #156
        0x18,
        (
            "I never want to get involved\x01",
            "for as long as I live.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3846")

    Jump("loc_3A73")

    label("loc_3849")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x242, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_38EC")

    ChrTalk(    #157
        0x18,
        (
            "The most important thing in gambling\x01",
            "is knowing when to leave.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #158
        0x18,
        (
            "As long as you don't overstay your\x01",
            "luck, gambling can make you filthy\x01",
            "rich!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3A73")

    label("loc_38EC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 6)), scpexpr(EXPR_END)), "loc_3A73")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_END)), "loc_3984")

    ChrTalk(    #159
        0x18,
        (
            "Blackjack's a game that almost\x01",
            "always guarantees a win of some\x01",
            "kind, if you play your cards right.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #160
        0x18,
        "Go ahead, give it a shot.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3A73")

    label("loc_3984")

    OP_A2(0xE)

    ChrTalk(    #161
        0x18,
        "Hey, welcome!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #162
        0x18,
        "You can play blackjack here at this table.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #163
        0x18,
        (
            "It's one of the few games where you're\x01",
            "practically guaranteed to make a little\x01",
            "mira, so long as you play your cards right.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #164
        0x18,
        "Sit back, relax, and have some fun.\x02",
    )

    CloseMessageWindow()

    label("loc_3A73")

    Return()

    # Function_13_341D end

    def Function_14_3A74(): pass

    label("Function_14_3A74")

    TalkBegin(0xA)
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "Talk\x01",                 # 0
            "Exchange Medals\x01",      # 1
            "Leave\x01",                # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3B1A")
    OP_0D()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3AF2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x455, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3AED")
    OP_A9(0x6C)
    Jump("loc_3AEF")

    label("loc_3AED")

    OP_A9(0x80)

    label("loc_3AEF")

    Jump("loc_3B01")

    label("loc_3AF2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x455, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3AFF")
    OP_A9(0x69)
    Jump("loc_3B01")

    label("loc_3AFF")

    OP_A9(0x7D)

    label("loc_3B01")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x23B, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_3B13")
    OP_A2(0x10B6)

    label("loc_3B13")

    TalkEnd(0xA)
    Return()

    label("loc_3B1A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3B2D")
    OP_56(0x0)
    TalkEnd(0xA)
    Return()

    label("loc_3B2D")

    Call(0, 15)
    TalkEnd(0xA)
    Return()

    # Function_14_3A74 end

    def Function_15_3B35(): pass

    label("Function_15_3B35")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_END)), "loc_3C4A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3BB6")

    ChrTalk(    #165
        0xA,
        (
            "The casino's been sooo boring\x01",
            "without anybody visiting.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #166
        0xA,
        (
            "I hope orbments start working again\x01",
            "soon.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)
    Jump("loc_3C47")

    label("loc_3BB6")


    ChrTalk(    #167
        0xA,
        (
            "The casino's been sooo boring\x01",
            "without anybody visiting.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #168
        0xA,
        (
            "The owner's acting like he doesn't\x01",
            "care, like, as usual, but I'm freaking\x01",
            "out!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3C47")

    Jump("loc_43B1")

    label("loc_3C4A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_3D60")

    ChrTalk(    #169
        0xA,
        (
            "The owner's been completely chill\x01",
            "about the whole orbment-shutdown\x01",
            "situation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #170
        0xA,
        (
            "Seriously, the guy has a poker face\x01",
            "like you wouldn't BELIEVE.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #171
        0xA,
        (
            "It'd be kinda funny if he was actually\x01",
            "freaking out and just wasn't letting it\x01",
            "show on his face, though, right?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_43B1")

    label("loc_3D60")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_END)), "loc_3FC6")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x68, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_3E77")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_3DF9")

    ChrTalk(    #172
        0xA,
        (
            "All work and no play's SO boring.\x01",
            "Why don't you guys come here for\x01",
            "fun next time?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #173
        0xA,
        "I'll be glad to be your match. ㈱\x02",
    )

    CloseMessageWindow()
    Jump("loc_3E74")

    label("loc_3DF9")

    OP_A2(0x2)

    ChrTalk(    #174
        0xA,
        (
            "Everyone, that was SOOO cool!\x01",
            "I'm, like, seriously impressed!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #175
        0xA,
        (
            "I had no idea bracers were so good\x01",
            "at gambling!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3E74")

    Jump("loc_3FC3")

    label("loc_3E77")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x68, 0x0, 0x40)"), scpexpr(EXPR_END)), "loc_3F3A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_3EE7")

    ChrTalk(    #176
        0xA,
        (
            "Oh, yes, yes, YES... Looks like I'm up\x01",
            "for a real match this time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #177
        0xA,
        "La la la... ♪\x02",
    )

    CloseMessageWindow()
    Jump("loc_3F37")

    label("loc_3EE7")

    OP_A2(0x2)

    ChrTalk(    #178
        0xA,
        "Too bad, guys.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #179
        0xA,
        (
            "Don't worry, though. I'm WAY good.\x01",
            "I got your back.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3F37")

    Jump("loc_3FC3")

    label("loc_3F3A")


    ChrTalk(    #180
        0xA,
        (
            "You see over there? Fuego and\x01",
            "the owner have been talking with\x01",
            "their eyes for, like, ever now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #181
        0xA,
        "Could it be...? Is it MY turn?!\x02",
    )

    CloseMessageWindow()

    label("loc_3FC3")

    Jump("loc_43B1")

    label("loc_3FC6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 5)), scpexpr(EXPR_END)), "loc_40C3")

    ChrTalk(    #182
        0xA,
        (
            "The owner never flips out, no matter\x01",
            "HOW much a guest wins.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #183
        0xA,
        (
            "He'll talk about the weather like he's\x01",
            "totally not just losing a ton of dough\x01",
            "right before his eyes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #184
        0xA,
        (
            "He wouldn't be so good at what he\x01",
            "does if not for that poker face.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_43B1")

    label("loc_40C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x242, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_42C3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_4209")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4199")

    ChrTalk(    #185
        0xA,
        (
            "Awww, you wanna know? Do you?\x01",
            "You guys sure are persistent!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #186
        0xA,
        "Okay, okay. Just an itty-bitty hint. ㈱\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #187
        0xA,
        (
            "...The one with the longer hair's\x01",
            "gonna win.\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4206")

    label("loc_4199")


    ChrTalk(    #188
        0xA,
        (
            "Actually, I already know.\x01",
            "Who's gonna win the election, I mean.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #189
        0xA,
        "I haven't told anyone yet, though.\x02",
    )

    CloseMessageWindow()

    label("loc_4206")

    Jump("loc_42C0")

    label("loc_4209")

    OP_A2(0x2)

    ChrTalk(    #190
        0xA,
        (
            "Most people don't realize it, but I'm,\x01",
            "like, WAY good at gambling.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #191
        0xA,
        (
            "I just KNOW somehow, you know?\x01",
            "I know what cards are coming, what\x01",
            "side of the dice is gonna face up...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_42C0")

    Jump("loc_43B1")

    label("loc_42C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 6)), scpexpr(EXPR_END)), "loc_43B1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_4323")

    ChrTalk(    #192
        0xA,
        (
            "If you're not sure how to play,\x01",
            "let me know and I'll be happy to\x01",
            "help. ㈱\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_43B1")

    label("loc_4323")

    OP_A2(0x2)

    ChrTalk(    #193
        0xA,
        "I just joined this place, actually.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #194
        0xA,
        (
            "It's super-mega relaxing here!\x01",
            "Where else can I earn some mira\x01",
            "AND have fun while I'm at it?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_43B1")

    Return()

    # Function_15_3B35 end

    def Function_16_43B2(): pass

    label("Function_16_43B2")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        10,
        1,
        (
            "Play 1-Medal Slots\x01",      # 0
            "Stop\x01",                    # 1
        )
    )

    MenuEnd(0x0)
    OP_5F(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_56(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4464")
    FadeToDark(300, 0, -1)
    OP_0D()
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_C0(0xC, 0x1, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_4464")

    TalkEnd(0xFF)
    Return()

    # Function_16_43B2 end

    def Function_17_4468(): pass

    label("Function_17_4468")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        10,
        1,
        (
            "Play 10-Medal Slots\x01",      # 0
            "Stop\x01",                     # 1
        )
    )

    MenuEnd(0x0)
    OP_5F(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_56(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_451B")
    FadeToDark(300, 0, -1)
    OP_0D()
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_C0(0xC, 0xA, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_451B")

    TalkEnd(0xFF)
    Return()

    # Function_17_4468 end

    def Function_18_451F(): pass

    label("Function_18_451F")

    TalkBegin(0x9)
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "Talk\x01",               # 0
            "Play Roulette\x01",      # 1
            "Leave\x01",              # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_45CD")
    FadeToDark(300, 0, -1)
    OP_0D()
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_C0(0xB, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_56(0x0)
    FadeToBright(300, 0)
    TalkEnd(0x9)
    Return()

    label("loc_45CD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_45E0")
    OP_56(0x0)
    TalkEnd(0x9)
    Return()

    label("loc_45E0")

    Call(0, 19)
    TalkEnd(0x9)
    Return()

    # Function_18_451F end

    def Function_19_45E8(): pass

    label("Function_19_45E8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_END)), "loc_47FD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_473E")

    ChrTalk(    #195
        0x9,
        (
            "I just came out to the balcony for\x01",
            "a breather.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #196
        0x9,
        (
            "...That object floating over there in\x01",
            "the sky has the most beautiful gold\x01",
            "shimmer, doesn't it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #197
        0x9,
        (
            "It's so odd for it to even exist,\x01",
            "and yet now I can gaze at it from\x01",
            "here without batting an eye.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #198
        0x9,
        (
            "It's a tad frightening, our ability to\x01",
            "adjust to the unknown.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)
    Jump("loc_47FA")

    label("loc_473E")


    ChrTalk(    #199
        0x9,
        (
            "The mere existence of such a\x01",
            "thing should be a constant marvel.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #200
        0x9,
        (
            "And yet we as humans can grow used\x01",
            "to just about anything, even that. A tad\x01",
            "frightening, when you think about it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_47FA")

    Jump("loc_51C1")

    label("loc_47FD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_49A0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_48EA")

    ChrTalk(    #201
        0x9,
        (
            "Welcome to my establishment,\x01",
            "Lavantar Casino & Bar!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #202
        0x9,
        (
            "Even in such difficult times as these,\x01",
            "my doors are always open.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #203
        0x9,
        (
            "We pride ourselves on antique\x01",
            "machines that require no orbal\x01",
            "power to run properly.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)
    Jump("loc_499D")

    label("loc_48EA")


    ChrTalk(    #204
        0x9,
        (
            "Even in such difficult times as these,\x01",
            "my doors are always open.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #205
        0x9,
        (
            "In fact, it's when things are at their\x01",
            "most dire that the people demand\x01",
            "distractions and entertainment.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_499D")

    Jump("loc_51C1")

    label("loc_49A0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_END)), "loc_4BA1")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x68, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_4A28")

    ChrTalk(    #206
        0x9,
        (
            "Once someone's winning streak\x01",
            "comes to an end, the rest is easy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #207
        0x9,
        (
            "He'll pay out what he's won soon\x01",
            "enough.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4B9E")

    label("loc_4A28")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x68, 0x0, 0x40)"), scpexpr(EXPR_END)), "loc_4A99")

    ChrTalk(    #208
        0x9,
        (
            "Don't think we have any other\x01",
            "choice here...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #209
        0x9,
        (
            "It's about time we play our hand,\x01",
            "I suppose.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4B9E")

    label("loc_4A99")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_4B26")

    ChrTalk(    #210
        0x9,
        (
            "He doesn't yet have the self-control to keep\x01",
            "from going overboard and prevent his\x01",
            "winnings from collapsing right beneath him.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4B9E")

    label("loc_4B26")

    OP_A2(0x1)

    ChrTalk(    #211
        0x9,
        (
            "That guest's been on quite the\x01",
            "winning streak.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #212
        0x9,
        (
            "All I can do it pray that he doesn't\x01",
            "take things too far...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4B9E")

    Jump("loc_51C1")

    label("loc_4BA1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 5)), scpexpr(EXPR_END)), "loc_4D22")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_4BFC")

    ChrTalk(    #213
        0x9,
        (
            "I would hope our new mayor continues\x01",
            "to assist the tourism industry.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4D1F")

    label("loc_4BFC")

    OP_A2(0x1)

    ChrTalk(    #214
        0x9,
        (
            "Despite supporting the tourism industry\x01",
            "to a great degree, our last mayor ended\x01",
            "up being...well, an embarrassment.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #215
        0x9,
        (
            "Our last mayor's focus on the\x01",
            "tourism industry was of great\x01",
            "benefit to this establishment.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #216
        0x9,
        (
            "I would hope our new mayor continues\x01",
            "to assist in the same manner.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4D1F")

    Jump("loc_51C1")

    label("loc_4D22")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x242, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4F17")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_4DE0")

    ChrTalk(    #217
        0x9,
        (
            "Have you given the slot machines\x01",
            "a go yet? They're the pride of this\x01",
            "establishment!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #218
        0x9,
        (
            "All of them are antiques that operate\x01",
            "on non-orbal systems. Marvelous, no?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4F14")

    label("loc_4DE0")

    OP_A2(0x1)

    ChrTalk(    #219
        0x9,
        (
            "Have you given the slot machines\x01",
            "a go yet? They're the pride of this\x01",
            "establishment!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #220
        0x9,
        (
            "All of them are antiques that operate\x01",
            "on non-orbal systems. Marvelous, no?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #221
        0x9,
        (
            "Feel the weight of the lever in your hands!\x01",
            "It would bring me no shortage of joy if you\x01",
            "were to appreciate its fine craftsmanship.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4F14")

    Jump("loc_51C1")

    label("loc_4F17")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 6)), scpexpr(EXPR_END)), "loc_51C1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_4FC2")

    ChrTalk(    #222
        0x9,
        (
            "Welcome to my establishment,\x01",
            "Lavantar Casino & Bar!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #223
        0x9,
        (
            "The wait for our grand reopening was\x01",
            "a long one, yes, but at last we are open\x01",
            "for business.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_51C1")

    label("loc_4FC2")

    OP_A2(0x1)

    ChrTalk(    #224
        0x9,
        (
            "Welcome to my establishment,\x01",
            "Lavantar Casino & Bar!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #225
        0x9,
        (
            "There are times in life when one is\x01",
            "forced to make decisions without the\x01",
            "help of logic.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #226
        0x9,
        (
            "However, Aidios, ever merciful, has\x01",
            "granted humanity a gift to trump such\x01",
            "trying moments.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #227
        0x9,
        "...I speak of intuition, of course.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #228
        0x9,
        (
            "Just as with choices in life, there is\x01",
            "no logic behind winning and losing\x01",
            "in gambling.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #229
        0x9,
        (
            "But once you've learned to sense the\x01",
            "danger intuitively...THAT, friend, is when\x01",
            "you've captured the true spirit of gambling.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_51C1")

    Return()

    # Function_19_45E8 end

    def Function_20_51C2(): pass

    label("Function_20_51C2")

    TalkBegin(0x10)
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
            "[Sea Breeze Soup] - 400 mira\x01",      # 2
            "Leave\x01",                             # 3
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_523F")
    OP_0D()
    OP_A9(0x6A)
    OP_56(0x0)
    TalkEnd(0x10)
    Return()

    label("loc_523F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5353")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x12), scpexpr(EXPR_PUSH_LONG, 0x190), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_5319")
    SubMira(400)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetMessageWindowPos(-1, -1, -1, -1)
    OP_22(0xB, 0x0, 0x64)

    AnonymousTalk(    #230
        "\x06Ate #2CSea Breeze Soup#0C.\x02",
    )

    CloseMessageWindow()
    OP_31(0x0, 0xFD, 0x320)
    OP_31(0x1, 0xFD, 0x320)
    OP_31(0x2, 0xFD, 0x320)
    OP_31(0x3, 0xFD, 0x320)
    OP_31(0x4, 0xFD, 0x320)
    OP_31(0x5, 0xFD, 0x320)
    OP_31(0x6, 0xFD, 0x320)
    OP_31(0x7, 0xFD, 0x320)
    OP_31(0x8, 0xFD, 0x320)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x20D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_530B")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_AC(0x3)"), scpexpr(EXPR_END)), "loc_52DA")
    Jump("loc_530B")

    label("loc_52DA")

    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #231
        "\x06Learned [#2CSea Breeze Soup#0C] recipe.\x02",
    )

    CloseMessageWindow()

    label("loc_530B")

    OP_56(0x0)
    FadeToBright(1000, 0)
    Jump("loc_5341")

    label("loc_5319")

    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #232
        "Insufficient mira.\x02",
    )

    CloseMessageWindow()
    FadeToBright(300, 0)

    label("loc_5341")

    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0x10)
    Return()

    label("loc_5353")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5364")
    TalkEnd(0x10)
    Return()

    label("loc_5364")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_END)), "loc_5549")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_54C0")

    ChrTalk(    #233
        0xFE,
        "The fishermen are in a bad way, too.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #234
        0xFE,
        (
            "All the ships loaded with orbal engines\x01",
            "are toast, so their only option is to put out\x01",
            "these dinky, old boats.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #235
        0xFE,
        (
            "Well, they've still got their jobs, at least.\x01",
            "That's better than some folks out there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #236
        0xFE,
        (
            "Look at the sailors. They're all slumped\x01",
            "over there on the second floor.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x9)
    Jump("loc_5546")

    label("loc_54C0")


    ChrTalk(    #237
        0xFE,
        "The fishermen are in a bad way, too.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #238
        0xFE,
        (
            "Well, they've still got their jobs, at least.\x01",
            "That's better than some folks out there.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5546")

    Jump("loc_5D74")

    label("loc_5549")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_5700")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_561C")

    ChrTalk(    #239
        0xFE,
        "Welcome!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #240
        0xFE,
        (
            "We've got our furnace loaded with\x01",
            "firewood so we can stay open as long\x01",
            "as we can during all this craziness.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #241
        0xFE,
        (
            "We've still got the same menu as\x01",
            "always, too, thankfully.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x9)
    Jump("loc_56FD")

    label("loc_561C")


    ChrTalk(    #242
        0xFE,
        (
            "We've got our furnace loaded with\x01",
            "firewood so we can stay open as long\x01",
            "as we can during all this craziness.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #243
        0xFE,
        (
            "Thanks to that, the kitchen's a sauna,\x01",
            "but any cook worth his salt can suck it\x01",
            "up with a little willpower.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_56FD")

    Jump("loc_5D74")

    label("loc_5700")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_END)), "loc_58B4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_57B9")

    ChrTalk(    #244
        0xFE,
        (
            "They went all that way to fight in the\x01",
            "Martial Arts Competition, only to go back\x01",
            "to bumming around the warehouse...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #245
        0xFE,
        "Those kids don't have a lick of ambition!\x02",
    )

    CloseMessageWindow()
    Jump("loc_58B1")

    label("loc_57B9")

    OP_A2(0x9)

    ChrTalk(    #246
        0xFE,
        (
            "Oh, yeah, I heard the Ravens were\x01",
            "in this year's Martial Arts Competition.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #247
        0xFE,
        (
            "I even saw a picture of 'em in the\x01",
            "Liberl News!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #248
        0xFE,
        (
            "But instead of making something out\x01",
            "of themselves, they're back to bumming\x01",
            "around the warehouse, as usual.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_58B1")

    Jump("loc_5D74")

    label("loc_58B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 5)), scpexpr(EXPR_END)), "loc_5A5E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_5959")

    ChrTalk(    #249
        0xFE,
        (
            "Not too smart to incite a riot\x01",
            "in front of the voters.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #250
        0xFE,
        (
            "Bein' quick to start a fight's not\x01",
            "exactly going to do wonders for\x01",
            "anyone's image.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5A5B")

    label("loc_5959")

    OP_A2(0x9)

    ChrTalk(    #251
        0xFE,
        "I heard about the fight.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #252
        0xFE,
        (
            "Pickin' a fight's bad enough, but you're\x01",
            "no better if you try to take 'em up on it.\x01",
            "Both sides hold a share of the blame.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #253
        0xFE,
        (
            "With the eyes of the voters on 'em,\x01",
            "man, I wish they'd use their damned\x01",
            "heads a little more!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5A5B")

    Jump("loc_5D74")

    label("loc_5A5E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x242, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_5C46")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_5B2A")

    ChrTalk(    #254
        0xFE,
        (
            "People who live as one with the\x01",
            "sea have an attached to the harbor\x01",
            "like no other in this city.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #255
        0xFE,
        (
            "Portos is the best mayoral candidate\x01",
            "to explain those feelings to the people.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5C43")

    label("loc_5B2A")

    OP_A2(0x9)

    ChrTalk(    #256
        0xFE,
        (
            "I was a fisherman back in my day,\x01",
            "too, so I've always had a soft spot for\x01",
            "the harbor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #257
        0xFE,
        (
            "Portos is the best mayoral candidate\x01",
            "to explain the passion we hold for the\x01",
            "harbor to the people.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #258
        0xFE,
        (
            "Don't you dare vote for some upstart\x01",
            "bastard like Norman! Don't even think it!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5C43")

    Jump("loc_5D74")

    label("loc_5C46")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 6)), scpexpr(EXPR_END)), "loc_5D74")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_5C80")

    ChrTalk(    #259
        0xFE,
        "Hey! Welcome to the Aqua Rossa Bar!\x02",
    )

    CloseMessageWindow()
    Jump("loc_5D74")

    label("loc_5C80")

    OP_A2(0x9)

    ChrTalk(    #260
        0xFE,
        "Hey! Welcome to the Aqua Rossa Bar!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #261
        0xFE,
        (
            "The second floor's serving as Portos'\x01",
            "election headquarters, but my place\x01",
            "is as open for business as always.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #262
        0xFE,
        (
            "Why not have a seat and take a look\x01",
            "at our menu? We got the best seafood\x01",
            "around!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5D74")

    TalkEnd(0x10)
    Return()

    # Function_20_51C2 end

    def Function_21_5D78(): pass

    label("Function_21_5D78")

    Call(0, 22)
    Return()

    # Function_21_5D78 end

    def Function_22_5D7D(): pass

    label("Function_22_5D7D")

    TalkBegin(0x8)
    Call(6, 4)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5D9A")
    OP_A9(0x68)
    TalkEnd(0x8)
    Return()

    label("loc_5D9A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5DAB")
    TalkEnd(0x8)
    Return()

    label("loc_5DAB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_END)), "loc_5F59")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5EBE")

    ChrTalk(    #263
        0x8,
        (
            "I wonder how long it's been since\x01",
            "my little brother started working.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #264
        0x8,
        (
            "If he's serious about turning over\x01",
            "a new leaf and actually working, then\x01",
            "I'll support him every step of the way.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #265
        0x8,
        (
            "He's my only brother, you know?\x01",
            "We gotta stick together.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_5F56")

    label("loc_5EBE")


    ChrTalk(    #266
        0x8,
        (
            "I wonder how long it's been since\x01",
            "my little brother started working.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #267
        0x8,
        (
            "It wasn't easy, but I think it was well\x01",
            "worth staying open for business.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5F56")

    Jump("loc_66A9")

    label("loc_5F59")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_60EE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6041")

    ChrTalk(    #268
        0x8,
        (
            "The bridge is stuck up, we can't use\x01",
            "the stove... It's pure chaos.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #269
        0x8,
        (
            "We're keeping the store open,\x01",
            "but I'm still not sure if this is a\x01",
            "good idea or not.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #270
        0x8,
        (
            "I'm not sure how long we can\x01",
            "keep this up...\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_60EB")

    label("loc_6041")


    ChrTalk(    #271
        0x8,
        (
            "The bridge is stuck up, we can't use\x01",
            "the stove... It's pure chaos.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #272
        0x8,
        (
            "I don't care if it's the army or bracers,\x01",
            "or...whoever! I just want someone to\x01",
            "do SOMETHING.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_60EB")

    Jump("loc_66A9")

    label("loc_60EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_END)), "loc_61FD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_6171")

    ChrTalk(    #273
        0x8,
        (
            "Can you believe this guy? He gambled\x01",
            "away all his traveling mira, just like that!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #274
        0x8,
        "Has he lost his mind?\x02",
    )

    CloseMessageWindow()
    Jump("loc_61FA")

    label("loc_6171")

    OP_A2(0x0)

    ChrTalk(    #275
        0x8,
        (
            "I hired a part-timer who gambled\x01",
            "away too much at the casino.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #276
        0x8,
        (
            "Works out for me, too. I could use\x01",
            "an extra hand around here.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_61FA")

    Jump("loc_66A9")

    label("loc_61FD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 5)), scpexpr(EXPR_END)), "loc_62D2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6220")

    ChrTalk(    #277
        0x8,
        "Heya, bracers.\x02",
    )

    CloseMessageWindow()

    label("loc_6220")

    OP_A2(0x0)

    ChrTalk(    #278
        0x8,
        (
            "I'm glad everything worked itself\x01",
            "out peacefully enough.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #279
        0x8,
        (
            "You can be passionate about your\x01",
            "beliefs without resorting to fights.\x01",
            "They've got some growing up to do.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_66A9")

    label("loc_62D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x242, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_6406")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_6396")

    ChrTalk(    #280
        0x8,
        (
            "The hotel not too far from here's\x01",
            "Norman's office.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #281
        0x8,
        (
            "You'll see plenty of campaigners going\x01",
            "in an out of there. Our business is\x01",
            "booming thanks to all the orders, too!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6403")

    label("loc_6396")

    OP_A2(0x0)

    ChrTalk(    #282
        0x8,
        (
            "All the business owners are voting\x01",
            "for Norman, of course.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #283
        0x8,
        "Without tourists, we're out of a job.\x02",
    )

    CloseMessageWindow()

    label("loc_6403")

    Jump("loc_66A9")

    label("loc_6406")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 6)), scpexpr(EXPR_END)), "loc_66A9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_652D")

    ChrTalk(    #284
        0x8,
        (
            "My younger brother, Deen, was a\x01",
            "participant in this year's Martial Arts\x01",
            "Competition.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #285
        0x8,
        (
            "And just when I thought he was going\x01",
            "to try and make something of himself,\x01",
            "he's back to being lazy as ever.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #286
        0x8,
        (
            "It's so frustrating! Why doesn't he have\x01",
            "the motivation to change...?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_66A9")

    label("loc_652D")

    OP_A2(0x0)

    ChrTalk(    #287
        0x8,
        (
            "Do you know Deen? He's my younger\x01",
            "brother, and one of those Raven punks\x01",
            "down at the harbor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #288
        0x8,
        (
            "Apparently, he and his friends\x01",
            "participated in the Martial Arts\x01",
            "Competition this year.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #289
        0x8,
        (
            "But just when I thought he was going\x01",
            "to try and make something of himself,\x01",
            "he's back to being lazy as ever.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #290
        0x8,
        (
            "It's so frustrating! Why doesn't he have\x01",
            "the motivation to change...?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_66A9")

    TalkEnd(0x8)
    Return()

    # Function_22_5D7D end

    def Function_23_66AD(): pass

    label("Function_23_66AD")

    TalkBegin(0xF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_END)), "loc_67BE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_676C")

    ChrTalk(    #291
        0xFE,
        (
            "#1740FHeh heh, I decided to swing by my\x01",
            "brother's restaurant and have a bite.\x02\x03",

            "Been a long time since we met up,\x01",
            "actually.\x02\x03",

            "Maybe I'll come by from time to time.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xD)
    Jump("loc_67BE")

    label("loc_676C")


    ChrTalk(    #292
        0xFE,
        (
            "#1740FPrimo's food is so damn good!\x02\x03",

            "#1746FHeh. Reminds me of Mom's cooking.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_67BE")

    TalkEnd(0xF)
    Return()

    # Function_23_66AD end

    def Function_24_67C2(): pass

    label("Function_24_67C2")

    TalkBegin(0x17)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_END)), "loc_6938")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_68BB")

    ChrTalk(    #293
        0xFE,
        (
            "Phew! When you're out to sea,\x01",
            "you sometimes can't wait to get\x01",
            "back on land...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #294
        0xFE,
        (
            "But when you can't leave the port,\x01",
            "suddenly it's the sea that you long\x01",
            "for.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #295
        0xFE,
        (
            "We're always longing for what we\x01",
            "can't have, aren't we?\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xF)
    Jump("loc_6935")

    label("loc_68BB")


    ChrTalk(    #296
        0xFE,
        (
            "When you can't leave the port,\x01",
            "suddenly it's the sea that you\x01",
            "long for.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #297
        0xFE,
        "Sailors just can't stand still on land.\x02",
    )

    CloseMessageWindow()

    label("loc_6935")

    Jump("loc_6A80")

    label("loc_6938")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_6A80")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_69F3")

    ChrTalk(    #298
        0xFE,
        (
            "It's not too bad to come in from the sea,\x01",
            "but now we can't leave port.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #299
        0xFE,
        (
            "At least I've got liquor to keep\x01",
            "me company. I'll never say no\x01",
            "to a break with beer.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xF)
    Jump("loc_6A80")

    label("loc_69F3")


    ChrTalk(    #300
        0xFE,
        (
            "It's not too bad to come in from the sea,\x01",
            "but now we can't leave port.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #301
        0xFE,
        (
            "What the hell could cause all the\x01",
            "orbments to stop working?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6A80")

    TalkEnd(0x17)
    Return()

    # Function_24_67C2 end

    def Function_25_6A84(): pass

    label("Function_25_6A84")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_6AF5")
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #302
        (
            "\x07\x05Forever gambling in the heart.\x01",
            "-Lavantar Casino & Bar\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Jump("loc_6B79")

    label("loc_6AF5")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #303
        (
            "\x07\x05Newly open after renovations! Thrills and excitement await.\x01",
            "-Lavantar Casino & Bar\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)

    label("loc_6B79")

    Return()

    # Function_25_6A84 end

    SaveToFile()

Try(main)

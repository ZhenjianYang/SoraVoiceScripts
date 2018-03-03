from ED63RDScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'M7408   ._SN',
        MapName             = 'Gaiden3',
        Location            = 'M7408.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60000",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            'ED6_DT21/M7408   ._SN',
            'ED6_DT21/M7408_1 ._SN',
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
        'Rufina',                               # 9
        'Tita',                                 # 10
        'Captain Schwarz',                      # 11
        'Major Vander',                         # 12
        'Josette',                              # 13
        'Joshua',                               # 14
        'Princess Klaudia',                     # 15
        'Sieg',                                 # 16
        'Prince Olivert',                       # 17
        'Zin',                                  # 18
        'Anelace',                              # 19
        'Scherazard',                           # 20
        'Agate',                                # 21
        'Estelle',                              # 22
        'Richard',                              # 23
        'Renne',                                # 24
        'Sister Ries',                          # 25
        'Father Kevin',                         # 26
        'Celeste',                              # 27
        'Gilbert',                              # 28
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
        'ED6_DT07/CH02930 ._CH',             # 00
        'ED6_DT07/CH02940 ._CH',             # 01
        'ED6_DT27/CH03080 ._CH',             # 02
        'ED6_DT27/CH03470 ._CH',             # 03
        'ED6_DT07/CH00060 ._CH',             # 04
        'ED6_DT27/CH03580 ._CH',             # 05
        'ED6_DT27/CH03570 ._CH',             # 06
        'ED6_DT27/CH03100 ._CH',             # 07
        'ED6_DT27/CH03250 ._CH',             # 08
        'ED6_DT27/CH03210 ._CH',             # 09
        'ED6_DT07/CH02320 ._CH',             # 0A
        'ED6_DT27/CH03260 ._CH',             # 0B
        'ED6_DT07/CH00070 ._CH',             # 0C
        'ED6_DT07/CH01630 ._CH',             # 0D
        'ED6_DT27/CH03240 ._CH',             # 0E
        'ED6_DT06/CH20053 ._CH',             # 0F
        'ED6_DT27/CH03000 ._CH',             # 10
        'ED6_DT07/CH02030 ._CH',             # 11
        'ED6_DT27/CH03510 ._CH',             # 12
        'ED6_DT07/CH02891 ._CH',             # 13
        'ED6_DT27/CH03750 ._CH',             # 14
        'ED6_DT06/CH20113 ._CH',             # 15
        'ED6_DT26/CH20219 ._CH',             # 16
        'ED6_DT26/CH20747 ._CH',             # 17
        'ED6_DT27/CH03085 ._CH',             # 18
        'ED6_DT27/CH03475 ._CH',             # 19
        'ED6_DT07/CH02895 ._CH',             # 1A
        'ED6_DT26/CH20254 ._CH',             # 1B
    )

    AddCharChipPat(
        'ED6_DT07/CH02930P._CP',             # 00
        'ED6_DT07/CH02940P._CP',             # 01
        'ED6_DT27/CH03080P._CP',             # 02
        'ED6_DT27/CH03470P._CP',             # 03
        'ED6_DT07/CH00060P._CP',             # 04
        'ED6_DT27/CH03580P._CP',             # 05
        'ED6_DT27/CH03570P._CP',             # 06
        'ED6_DT27/CH03100P._CP',             # 07
        'ED6_DT27/CH03250P._CP',             # 08
        'ED6_DT27/CH03210P._CP',             # 09
        'ED6_DT07/CH02320P._CP',             # 0A
        'ED6_DT27/CH03260P._CP',             # 0B
        'ED6_DT07/CH00070P._CP',             # 0C
        'ED6_DT07/CH01630P._CP',             # 0D
        'ED6_DT27/CH03240P._CP',             # 0E
        'ED6_DT06/CH20053P._CP',             # 0F
        'ED6_DT27/CH03000P._CP',             # 10
        'ED6_DT07/CH02030P._CP',             # 11
        'ED6_DT27/CH03510P._CP',             # 12
        'ED6_DT07/CH02891P._CP',             # 13
        'ED6_DT27/CH03750P._CP',             # 14
        'ED6_DT06/CH20113P._CP',             # 15
        'ED6_DT26/CH20219P._CP',             # 16
        'ED6_DT26/CH20747P._CP',             # 17
        'ED6_DT27/CH03085P._CP',             # 18
        'ED6_DT27/CH03475P._CP',             # 19
        'ED6_DT07/CH02895P._CP',             # 1A
        'ED6_DT26/CH20254P._CP',             # 1B
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x1C5,
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
        NpcIndex            = 0x1C1,
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
        NpcIndex            = 0x1C1,
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
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x1C1,
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
        NpcIndex            = 0x1C1,
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
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x1C1,
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
        Unknown3            = 9,
        ChipIndex           = 0x9,
        NpcIndex            = 0x1C1,
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
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x1C1,
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
        Unknown3            = 11,
        ChipIndex           = 0xB,
        NpcIndex            = 0x1C1,
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
        Unknown3            = 12,
        ChipIndex           = 0xC,
        NpcIndex            = 0x1C1,
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
        Unknown3            = 13,
        ChipIndex           = 0xD,
        NpcIndex            = 0x1C1,
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
        NpcIndex            = 0x1C1,
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
        Unknown3            = 15,
        ChipIndex           = 0xF,
        NpcIndex            = 0x1C1,
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
        Unknown3            = 16,
        ChipIndex           = 0x10,
        NpcIndex            = 0x1C1,
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
        Unknown3            = 17,
        ChipIndex           = 0x11,
        NpcIndex            = 0x1C1,
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
        Unknown3            = 18,
        ChipIndex           = 0x12,
        NpcIndex            = 0x1C1,
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
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x1C1,
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
        NpcIndex            = 0x1C1,
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
        Unknown3            = 19,
        ChipIndex           = 0x13,
        NpcIndex            = 0x1C1,
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
        Unknown3            = 20,
        ChipIndex           = 0x14,
        NpcIndex            = 0x1C1,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    ScpFunction(
        "Function_0_40A",          # 00, 0
        "Function_1_4A6",          # 01, 1
        "Function_2_60E",          # 02, 2
        "Function_3_2FC0",         # 03, 3
        "Function_4_41EC",         # 04, 4
        "Function_5_432D",         # 05, 5
        "Function_6_45E2",         # 06, 6
    )


    def Function_0_40A(): pass

    label("Function_0_40A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A1, 1)), scpexpr(EXPR_END)), "loc_42F")
    OP_A3(0x2509)
    SetMapFlags(0x10000000)
    OP_C4(0x0, 0x100000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(1, 3)
    Jump("loc_4A5")

    label("loc_42F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A1, 0)), scpexpr(EXPR_END)), "loc_454")
    OP_A3(0x2508)
    SetMapFlags(0x10000000)
    OP_C4(0x0, 0x100000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 6)
    Jump("loc_4A5")

    label("loc_454")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 7)), scpexpr(EXPR_END)), "loc_46A")
    OP_A3(0x2507)
    SetMapFlags(0x10000000)
    Event(0, 4)
    Jump("loc_4A5")

    label("loc_46A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 5)), scpexpr(EXPR_END)), "loc_489")
    OP_A3(0x2505)
    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0xB1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 3)
    Jump("loc_4A5")

    label("loc_489")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 4)), scpexpr(EXPR_END)), "loc_4A5")
    OP_A3(0x2504)
    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0xD4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 2)

    label("loc_4A5")

    Return()

    # Function_0_40A end

    def Function_1_4A6(): pass

    label("Function_1_4A6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_4B6")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x9C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4B6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_4C6")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x9C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_4D6")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x9C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4D6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B0, 2)), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4EF")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4EF")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x29), scpexpr(EXPR_PUSH_LONG, 0x334), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_504")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x9C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_504")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x29), scpexpr(EXPR_PUSH_LONG, 0x335), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_519")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x9C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_519")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x29), scpexpr(EXPR_PUSH_LONG, 0x336), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_52E")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x9C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_52E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x29), scpexpr(EXPR_PUSH_LONG, 0xE16), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_565")
    FadeToDark(0, 16777215, -1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x49), scpexpr(EXPR_PUSH_LONG, 0x9B), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_55C")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x9B), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_565")

    label("loc_55C")

    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0xA0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_565")

    OP_71(0x400, 0x0)
    ExitThread()
    OP_71(0x401, 0x0)
    ExitThread()
    OP_71(0x40A, 0x0)
    ExitThread()
    OP_71(0x40B, 0x0)
    ExitThread()
    OP_71(0x40C, 0x0)
    ExitThread()
    OP_71(0x40D, 0x0)
    ExitThread()
    OP_71(0x40E, 0x0)
    ExitThread()
    OP_71(0x40F, 0x0)
    ExitThread()
    OP_71(0x410, 0x0)
    ExitThread()
    OP_71(0x411, 0x0)
    ExitThread()
    OP_71(0x412, 0x0)
    ExitThread()
    OP_71(0x413, 0x0)
    ExitThread()
    OP_71(0x414, 0x0)
    ExitThread()
    OP_71(0x414, 0x0)
    ExitThread()
    OP_71(0x415, 0x0)
    ExitThread()
    OP_71(0x416, 0x0)
    ExitThread()
    OP_71(0x417, 0x0)
    ExitThread()
    OP_71(0x418, 0x0)
    ExitThread()
    OP_71(0x419, 0x0)
    ExitThread()
    OP_71(0x41A, 0x0)
    ExitThread()
    OP_71(0x41B, 0x0)
    ExitThread()
    OP_71(0x41C, 0x0)
    ExitThread()
    OP_71(0x41D, 0x0)
    ExitThread()
    OP_71(0x41E, 0x0)
    ExitThread()
    OP_71(0x41F, 0x0)
    ExitThread()
    OP_71(0x420, 0x0)
    ExitThread()
    OP_71(0x421, 0x0)
    ExitThread()
    OP_71(0x422, 0x0)
    ExitThread()
    Return()

    # Function_1_4A6 end

    def Function_2_60E(): pass

    label("Function_2_60E")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadEffect(0x0, "map\\mp261_00.eff")
    LoadEffect(0x1, "map\\mp272_00.eff")
    LoadEffect(0x2, "map\\mp260_00.eff")
    OP_E0(250, 0x5C, 0x2)
    OP_E0(250, 0x5D, 0x3)
    OP_E0(251, 0x5E, 0x2)
    OP_E0(251, 0x5F, 0x3)
    OP_E0(252, 0x60, 0x2)
    OP_E0(252, 0x61, 0x3)
    OP_E0(253, 0x62, 0x2)
    OP_E0(253, 0x63, 0x3)
    OP_E6(0x0, 0x3)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 0, 0, 25130, 180)
    SetChrPos(0xFA, -700, 0, -62170, 0)
    SetChrPos(0xFB, 800, 0, -62900, 0)
    SetChrPos(0xFC, -1000, 0, -64250, 0)
    SetChrPos(0xFD, 1160, 0, -65319, 0)
    OP_6D(0, 850, -50000, 0)
    OP_67(0, 6760, -10000, 0)
    OP_6B(5560, 0)
    OP_6C(0, 0)
    OP_6E(467, 0)

    def lambda_71B():
        OP_6D(0, 3300, 18260, 10000)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_71B)

    def lambda_733():
        OP_67(0, 14860, -10000, 10000)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_733)

    def lambda_74B():
        OP_6B(5070, 10000)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_74B)

    def lambda_75B():
        OP_6E(521, 10000)
        ExitThread()

    QueueWorkItem(0x10, 3, lambda_75B)

    def lambda_76B():
        OP_8E(0xFE, 0xFFFFFD44, 0x0, 0x38C2, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFA, 0, lambda_76B)
    Sleep(50)

    def lambda_78B():
        OP_8E(0xFE, 0x320, 0x0, 0x38AE, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFB, 0, lambda_78B)
    Sleep(50)

    def lambda_7AB():
        OP_8E(0xFE, 0xFFFFFC18, 0x0, 0x2FE4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFC, 0, lambda_7AB)
    Sleep(50)

    def lambda_7CB():
        OP_8E(0xFE, 0xFFFFFB78, 0x0, 0x30A2, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFD, 0, lambda_7CB)
    FadeToBright(2000, 0)
    OP_0D()
    WaitChrThread(0x10, 0x0)

    def lambda_7F5():
        OP_6D(0, 3000, 17760, 5000)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_7F5)

    def lambda_80D():
        OP_6B(3270, 5000)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_80D)

    def lambda_81D():
        OP_6E(521, 5000)
        ExitThread()

    QueueWorkItem(0x10, 3, lambda_81D)
    Sleep(2000)
    Fade(1000)
    OP_44(0x10, 0x0)
    OP_44(0x10, 0x1)
    OP_44(0x10, 0x2)
    OP_44(0x10, 0x3)
    OP_6D(0, -550, 28610, 0)
    OP_67(0, 4040, -10000, 0)
    OP_6B(3120, 0)
    OP_6C(0, 0)
    OP_6E(332, 0)

    def lambda_884():
        OP_6B(2800, 1000)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_884)
    OP_0D()
    WaitChrThread(0x10, 0x0)
    Sleep(500)

    ChrTalk(    #0
        0x10,
        (
            "\x07\x02#1586F#5PHeehee... Welcome.\x02\x03",

            "#1582FI'm impressed you were able to make it all\x01",
            "this way to me.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(500)
    OP_6D(1200, 0, 25840, 0)
    OP_67(0, 5070, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(323, 0)

    def lambda_94D():
        OP_6D(1000, 0, 19200, 3500)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_94D)

    def lambda_965():
        OP_67(0, 4910, -10000, 3500)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_965)

    def lambda_97D():
        OP_6B(3000, 3500)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_97D)

    def lambda_98D():
        OP_6E(370, 3500)
        ExitThread()

    QueueWorkItem(0x10, 3, lambda_98D)
    Sleep(1000)
    OP_44(0xFA, 0x0)
    OP_44(0xFB, 0x0)
    OP_44(0xFC, 0x0)
    OP_44(0xFD, 0x0)
    SetChrPos(0xFA, -1380, 0, 10530, 0)
    SetChrPos(0xFB, 280, 0, 10510, 0)
    SetChrPos(0xFC, -2160, 0, 8260, 0)
    SetChrPos(0xFD, -60, 0, 8450, 0)

    def lambda_9F6():
        OP_8E(0xFE, 0xFFFFFA9C, 0x0, 0x34DA, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFA, 0, lambda_9F6)
    Sleep(150)

    def lambda_A16():
        OP_8E(0xFE, 0x118, 0x0, 0x34C6, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFB, 0, lambda_A16)
    Sleep(150)

    def lambda_A36():
        OP_8E(0xFE, 0xFFFFF830, 0x0, 0x2D8C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFC, 0, lambda_A36)
    Sleep(150)

    def lambda_A56():
        OP_8E(0xFE, 0xFFFFFFC4, 0x0, 0x2DE6, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFD, 0, lambda_A56)
    WaitChrThread(0xFA, 0x0)
    WaitChrThread(0xFB, 0x0)
    WaitChrThread(0xFC, 0x0)
    WaitChrThread(0xFD, 0x0)
    WaitChrThread(0x10, 0x0)
    Sleep(150)

    ChrTalk(    #1
        0x10F,
        "#1935F#12PRufina...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x109,
        "#1063F#6PDarn right, we did.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x10,
        (
            "\x07\x02#1586F#5PFor the record, I saw all that happened down in\x01",
            "Gehenna from here.\x02\x03",

            "#1587FI wasn't expecting you to have the will to resist\x01",
            "Weissmann's proposal.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x109,
        (
            "#1841F#6PI'll be honest. If Ries hadn't been with me,\x01",
            "he might've swayed me.\x02\x03",

            "#1067FSo don't give me too much credit. I'm still\x01",
            "the same cowardly loser I always was.\x02\x03",

            "#1840FPeople don't change their ways that easily.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x10F,
        "#1942F#12PDon't say that...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x10,
        (
            "\x07\x02#1586F#5PYou look surprisingly relaxed for someone\x01",
            "talking about how hopeless they are.\x02\x03",

            "#1582FIf you have so little confidence in yourself,\x01",
            "you might be in for some trouble.\x02\x03",

            "Remember, Kevin: if you can't defeat me,\x01",
            "Phantasma isn't going anywhere.\x02\x03",

            "You do understand that, right?\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x109,
        (
            "#1067F#6PYeah. I know.\x02\x03",

            "#1065FWorse still, it'll probably start affecting the real\x01",
            "world soon...\x02\x03",

            "Right now, its effects are limited to Phantasma's\x01",
            "own borders, but that might not stay that way\x01",
            "forever.\x02\x03",

            "#1063FRight?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xFB)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E8F")
    OP_62(0xFB, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_EF6")

    label("loc_E8F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xFB)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_EB7")
    OP_62(0xFB, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_EF6")

    label("loc_EB7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xFB)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_EDF")
    OP_62(0xFB, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_EF6")

    label("loc_EDF")

    OP_62(0xFB, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_EF6")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xFC)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F23")
    OP_62(0xFC, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_F8A")

    label("loc_F23")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xFC)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F4B")
    OP_62(0xFC, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_F8A")

    label("loc_F4B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xFC)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F73")
    OP_62(0xFC, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_F8A")

    label("loc_F73")

    OP_62(0xFC, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_F8A")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xFD)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FB7")
    OP_62(0xFD, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_101E")

    label("loc_FB7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xFD)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FDF")
    OP_62(0xFD, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_101E")

    label("loc_FDF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xFD)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1007")
    OP_62(0xFD, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_101E")

    label("loc_1007")

    OP_62(0xFD, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_101E")

    Sleep(1000)

    ChrTalk(    #8
        0x10F,
        "#1934F#12PWhat?!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1064")

    ChrTalk(    #9
        0x101,
        "#1005F#12PS-Seriously?!\x02",
    )

    CloseMessageWindow()

    label("loc_1064")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_108B")

    ChrTalk(    #10
        0x10A,
        "#1317F#12PN-No way!\x02",
    )

    CloseMessageWindow()

    label("loc_108B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_10B9")

    ChrTalk(    #11
        0x106,
        "#055F#12PYou're kidding...\x02",
    )

    CloseMessageWindow()

    label("loc_10B9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_10E0")

    ChrTalk(    #12
        0x107,
        "#065F#12PR-Really?!\x02",
    )

    CloseMessageWindow()

    label("loc_10E0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1116")

    ChrTalk(    #13
        0x10B,
        "#216F#12PTh-This is a joke, right?\x02",
    )

    CloseMessageWindow()

    label("loc_1116")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1162")

    ChrTalk(    #14
        0x102,
        "#1503F#12PUnfortunately, I think he's right on track.\x02",
    )

    CloseMessageWindow()
    Jump("loc_119C")

    label("loc_1162")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_119C")

    ChrTalk(    #15
        0x110,
        "#1305F#12PI suppose that is plausible.\x02",
    )

    CloseMessageWindow()

    label("loc_119C")


    ChrTalk(    #16
        0x10,
        (
            "\x07\x02#1586F#5PWell, well. You noticed.\x02\x03",

            "#1587FPhantasma has been taking in people's desires\x01",
            "for thousands of years now, and it's starting to\x01",
            "hit the limits of its own capacity.\x02\x03",

            "In order to release some of the pressure that's\x01",
            "been building up within, it's likely it will start\x01",
            "to erode away the real world.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x109,
        "#1065F#6PThought so...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x10,
        (
            "\x07\x02#1586F#5PIt won't be something that happens overnight...\x02\x03",

            "...but slowly, its influence will start to extend\x01",
            "across the land, blurring the line between this\x01",
            "world and yours.\x02\x03",

            "#1582FUntil eventually, the real world will be filled with\x01",
            "devils and ghosts like this one.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x10F,
        "#1949F#12PN-No way...\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1456")

    ChrTalk(    #20
        0x10E,
        "#175F#12PThat sounds terrifying...\x02",
    )

    CloseMessageWindow()
    Jump("loc_1485")

    label("loc_1456")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1485")

    ChrTalk(    #21
        0x103,
        "#1532F#12PHow terrifying...\x02",
    )

    CloseMessageWindow()

    label("loc_1485")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_14C1")

    ChrTalk(    #22
        0x108,
        "#074F#12PThat sounds like a bad joke.\x02",
    )

    CloseMessageWindow()
    Jump("loc_14FA")

    label("loc_14C1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_14FA")

    ChrTalk(    #23
        0x10D,
        "#272F#12PThat sounds like a bad joke.\x02",
    )

    CloseMessageWindow()

    label("loc_14FA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1551")

    ChrTalk(    #24
        0x105,
        "#1162F#12PI had no idea the situation was quite that perilous...\x02",
    )

    CloseMessageWindow()
    Jump("loc_15A4")

    label("loc_1551")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xB)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_15A4")

    ChrTalk(    #25
        0x10C,
        "#112F#12PI had no idea the situation was quite that perilous...\x02",
    )

    CloseMessageWindow()

    label("loc_15A4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_15E4")

    ChrTalk(    #26
        0x104,
        "#1544F#12POh, my... That doesn't sound good.\x02",
    )

    CloseMessageWindow()

    label("loc_15E4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1664")

    ChrTalk(    #27
        0x110,
        (
            "#263F#12PReality becomes a fairy tale, and fairy tales\x01",
            "become reality...\x02\x03",

            "#1306FWhat a fascinating prospect.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1664")


    ChrTalk(    #28
        0x10,
        (
            "\x07\x02#1581F#5PI would ask that you not despair at the thought.\x02\x03",

            "#1586FThe real world could be easily influenced by\x01",
            "people's wishes and desires.\x02\x03",

            "If all the world's population genuinely wished\x01",
            "for a better, more peaceful world...maybe it\x01",
            "would actually happen.\x02\x03",

            "#1582FPerhaps being taken over by Phantasma may\x01",
            "even be in the real world's best interests.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x109,
        "#1075F#6P...Screw that. There's no way that's true.\x02",
    )

    CloseMessageWindow()
    OP_62(0x10, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #30
        0x10,
        "\x07\x02#1584FIs that so?\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_20(0x5DC)
    Sleep(300)
    Fade(500)
    OP_6D(700, 0, 10800, 0)
    OP_67(0, 4170, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(140000, 0)
    OP_6E(346, 0)
    SetChrPos(0xFA, -1380, 0, 13530, 0)
    SetChrPos(0xFB, 280, 0, 13210, 0)
    SetChrPos(0xFC, -1300, 0, 11600, 0)
    SetChrPos(0xFD, 560, 0, 11350, 0)

    def lambda_18CF():
        OP_6B(2600, 30000)
        ExitThread()

    QueueWorkItem(0xFA, 0, lambda_18CF)
    OP_0D()
    OP_21()
    OP_1D(0xB2)
    Sleep(500)

    ChrTalk(    #31
        0x109,
        (
            "#1067F#11PNo one who knows the first thing about life before\x01",
            "the Aureole could believe it would be that simple.\x02\x03",

            "#1065FThe people back in those days were able to make\x01",
            "their desires reality using it.\x02\x03",

            "And all it did was lead people down a path toward\x01",
            "ruin and force them to lock it away in order to\x01",
            "ensure humanity's future.\x02\x03",

            "#1063FLetting Phantasma take over the continent would\x01",
            "no doubt be a repeat of the same thing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x10,
        "\x07\x02#1583F#2P...\x07\x00\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x109,
        (
            "#1067F#11PI know you don't believe for a second that's how\x01",
            "people should live, Rufina.\x02\x03",

            "#1065FEven after becoming a knight, you never relied on\x01",
            "force to solve problems. You were always thinking.\x01",
            "Always trying to find the best solution.\x02\x03",

            "When I was ready to give up on life and wallow in\x01",
            "my own despair, you were the one who made me\x01",
            "face reality.\x02\x03",

            "#1840FIt was because you knew that life doesn't always\x01",
            "go the way people want it to that you were strong\x01",
            "enough to do that for me.\x02\x03",

            "You knew that the only way to make the world a\x01",
            "better place was for people to be strong together\x01",
            "and MAKE it that way.\x02\x03",

            "Am I wrong?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x10,
        "\x07\x02#1585F#2P...\x07\x00\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x109,
        (
            "#1065F#11PIt took me falling down to Gehenna with Ries\x01",
            "for me to finally realize that, but I did.\x02\x03",

            "#1840FI realized all over again just how pitiful a man\x01",
            "I used to be.\x02\x03",

            "#1076FI never stopped to think what your final thoughts\x01",
            "must have been when you gave your life to save\x01",
            "me...\x02\x03",

            "I never stopped to think whether I could've done\x01",
            "something for Mom instead of running away from\x01",
            "her...\x02\x03",

            "I just acted like a spoiled brat trying to find a way\x01",
            "to be 'punished,' because I thought by doing that,\x01",
            "maybe I could finally be forgiven.\x02\x03",

            "#1065FIt's taken me a long time to see that, but here I am.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x10F, 270, 400)
    Sleep(300)

    ChrTalk(    #36
        0x10F,
        "#1942F#5PKevin...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0x109,
        (
            "#1075F#11PYou know what, though? I'm fine with how long it\x01",
            "took.\x02\x03",

            "I'm a long ways off from being able to compare to\x01",
            "you, but at least I know what direction I should be\x01",
            "walking now.\x02\x03",

            "Maybe if I start walking today, one day, I'll actually\x01",
            "be able to reach the place where you used to stand.\x02\x03",

            "#1840FSo that's why...I feel like I can finally start accepting\x01",
            "myself for how I am.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2133")

    ChrTalk(    #38
        0x102,
        "#1501F#11PKevin...\x02",
    )

    CloseMessageWindow()
    Jump("loc_21FA")

    label("loc_2133")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_215B")

    ChrTalk(    #39
        0x107,
        "#560F#11PKevin...\x02",
    )

    CloseMessageWindow()
    Jump("loc_21FA")

    label("loc_215B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2184")

    ChrTalk(    #40
        0x10A,
        "#1314F#11PKevin...\x02",
    )

    CloseMessageWindow()
    Jump("loc_21FA")

    label("loc_2184")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_21AD")

    ChrTalk(    #41
        0x105,
        "#1382F#11PKevin...\x02",
    )

    CloseMessageWindow()
    Jump("loc_21FA")

    label("loc_21AD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_21D5")

    ChrTalk(    #42
        0x10E,
        "#171F#11PKevin...\x02",
    )

    CloseMessageWindow()
    Jump("loc_21FA")

    label("loc_21D5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_21FA")

    ChrTalk(    #43
        0x10B,
        "#210F#11PKevin...\x02",
    )

    CloseMessageWindow()

    label("loc_21FA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2243")

    ChrTalk(    #44
        0x101,
        "#1008F#11PHeehee. You sound like a new man, Kevin.\x02",
    )

    CloseMessageWindow()
    Jump("loc_239A")

    label("loc_2243")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_228A")

    ChrTalk(    #45
        0x103,
        "#1536F#11PHaha. You sound like a new man, Kevin.\x02",
    )

    CloseMessageWindow()
    Jump("loc_239A")

    label("loc_228A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_22C1")

    ChrTalk(    #46
        0x106,
        "#051F#11PHeh. Well said, my man.\x02",
    )

    CloseMessageWindow()
    Jump("loc_239A")

    label("loc_22C1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_230B")

    ChrTalk(    #47
        0x108,
        "#071F#11PHaha. You sound so much more positive now.\x02",
    )

    CloseMessageWindow()
    Jump("loc_239A")

    label("loc_230B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2353")

    ChrTalk(    #48
        0x10D,
        "#275F#11PYou're sounding a lot more positive now.\x02",
    )

    CloseMessageWindow()
    Jump("loc_239A")

    label("loc_2353")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xB)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_239A")

    ChrTalk(    #49
        0x10C,
        "#111F#11PHaha. You sound so much more positive now.\x02",
    )

    CloseMessageWindow()

    label("loc_239A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_23C7")

    ChrTalk(    #50
        0x104,
        "#1541F#11PHeh. Well said.\x02",
    )

    CloseMessageWindow()

    label("loc_23C7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2417")

    ChrTalk(    #51
        0x110,
        (
            "#1307F#11PYou're accepting yourself for how you are,\x01",
            "huh...?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2417")

    Sleep(300)
    OP_44(0xFA, 0x0)
    Fade(500)
    OP_6D(1000, 0, 19200, 0)
    OP_67(0, 4910, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(370, 0)
    SetChrPos(0xFA, -1380, 0, 13530, 0)
    SetChrPos(0xFB, 280, 0, 13510, 270)
    SetChrPos(0xFC, -2000, 0, 11660, 0)
    SetChrPos(0xFD, -60, 0, 11750, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #52
        0x10,
        (
            "\x07\x02#1583F#5P...\x02\x03",

            "#1586FIt looks like my attempts to punish you ended\x01",
            "up having quite an unintended result.\x02\x03",

            "#1582FMind you, Kevin, I wouldn't put me on a pedestal\x01",
            "if I were you.\x02\x03",

            "The world we stand in is one affected by the will\x01",
            "of those within.\x02\x03",

            "If you're convinced that you are inferior to me...\x02\x03",

            "...how do you expect to defeat me?\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x10F, 0, 400)
    Sleep(300)

    ChrTalk(    #53
        0x10F,
        "#1935F#12PThat's true...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0x109,
        (
            "#1065F#6PWell, you're right.\x02\x03",

            "#1840FOr you would be if you weren't\x01",
            "just a copy of her.\x02",
        )
    )

    CloseMessageWindow()
    OP_20(0x5DC)
    OP_62(0x10, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #55
        0x10,
        "\x07\x02#1584F#5P...What?\x07\x00\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0x10F,
        "#1934F#12PShe is?!\x02",
    )

    CloseMessageWindow()
    OP_1D(0xB1)
    Sleep(500)

    ChrTalk(    #57
        0x109,
        (
            "#1063F#6PThe game's up. I know exactly what you are now.\x02\x03",

            "#1065FYou're this world's core--the reason it can operate\x01",
            "autonomously...\x02\x03",

            "...but you're not Rufina.\x02\x03",

            "#1069FYou're the copy of my Stigma that was made here\x01",
            "half a year ago!\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(500)
    OP_6D(1720, 0, 26480, 0)
    OP_67(0, 4370, -10000, 0)
    OP_6B(2440, 0)
    OP_6C(45000, 0)
    OP_6E(359, 0)
    SetChrPos(0xFA, -1380, 0, 13530, 0)
    SetChrPos(0xFB, 280, 0, 13510, 0)
    SetChrPos(0xFC, -2000, 0, 11660, 0)
    SetChrPos(0xFD, -60, 0, 11750, 0)
    OP_0D()
    Sleep(300)

    ChrTalk(    #58
        0x10,
        "\x07\x02#1583F#3S#5P...!!\x07\x00\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    OP_22(0x1C0, 0x0, 0x64)
    OP_22(0x137, 0x0, 0x64)
    PlayEffect(0x1, 0x0, 0x10, 0, 0, 0, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    Sleep(2000)
    OP_22(0x117, 0x0, 0x64)
    OP_22(0x2F2, 0x1, 0x3C)
    OP_22(0x32E, 0x1, 0x3C)
    PlayEffect(0x2, 0x1, 0x10, 0, -500, 0, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    Sleep(300)
    OP_82(0x0, 0x2)

    def lambda_2914():
        OP_6D(1170, 0, 28620, 3000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_2914)

    def lambda_292C():

        label("loc_292C")

        OP_9E(0xFE, 0x14, 0x0, 0x1388, 0x1F4)
        OP_48()
        Jump("loc_292C")

    QueueWorkItem2(0x10, 3, lambda_292C)

    def lambda_2949():
        OP_8F(0xFE, 0x0, 0x0, 0x6AB8, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_2949)
    WaitChrThread(0x10, 0x0)

    def lambda_2969():
        OP_6D(3880, 1500, 39000, 5000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_2969)

    def lambda_2981():
        OP_67(0, 3770, -10000, 5000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_2981)

    def lambda_2999():
        OP_6B(2920, 5000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_2999)

    def lambda_29A9():
        OP_6E(350, 5000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_29A9)
    Fade(250)

    def lambda_29BE():
        OP_8F(0xFE, 0x0, 0xBB8, 0x89F8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_29BE)
    SetChrChipByIndex(0x10, 1)
    SetChrSubChip(0x10, 0)

    def lambda_29E3():

        label("loc_29E3")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_29E3")

    QueueWorkItem2(0x10, 3, lambda_29E3)
    OP_0D()
    WaitChrThread(0x10, 0x0)
    Sleep(1000)

    ChrTalk(    #59
        0x10,
        (
            "\x07\x02#5PHow...?\x02\x03",

            "How did you work that out?!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(500)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_6D(110, 2650, 36260, 0)
    OP_67(0, 2400, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(0, 0)
    OP_6E(344, 0)
    SetChrPos(0x10, 0, 2500, 35320, 180)
    OP_0D()
    OP_22(0x99, 0x0, 0x64)
    Fade(1000)
    SetChrFlags(0x10, 0x80)
    OP_82(0x1, 0x2)
    OP_23(0x2F2)
    OP_23(0x32E)
    OP_0D()
    Sleep(500)
    Fade(1000)

    def lambda_2AB7():
        OP_6B(3050, 500)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_2AB7)
    OP_22(0x1BF, 0x0, 0x64)
    OP_22(0x14F, 0x0, 0x64)
    PlayEffect(0x0, 0x2, 0x10, 0, 500, 0, 0, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)
    OP_0D()
    Sleep(1000)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xFC)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2B3A")

    NpcTalk(    #60
        0xFD,
        "Estelle",
        "#1002F#5PThere it is!\x02",
    )

    CloseMessageWindow()
    Jump("loc_2DB6")

    label("loc_2B3A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xFC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2B6B")

    NpcTalk(    #61
        0xFD,
        "Joshua",
        "#1502F#5PThat's it!\x02",
    )

    CloseMessageWindow()
    Jump("loc_2DB6")

    label("loc_2B6B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xFC)"), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2B9C")

    NpcTalk(    #62
        0xFD,
        "Josette",
        "#212F#5PThat's it!\x02",
    )

    CloseMessageWindow()
    Jump("loc_2DB6")

    label("loc_2B9C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xFC)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2BCD")

    NpcTalk(    #63
        0xFD,
        "Renne",
        "#262F#5PThere it is!\x02",
    )

    CloseMessageWindow()
    Jump("loc_2DB6")

    label("loc_2BCD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xFC)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2BFB")

    NpcTalk(    #64
        0xFD,
        "Tita",
        "#062F#5PThat's it!\x02",
    )

    CloseMessageWindow()
    Jump("loc_2DB6")

    label("loc_2BFB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xFC)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2C2E")

    NpcTalk(    #65
        0xFD,
        "Anelace",
        "#812F#5PThere it is!\x02",
    )

    CloseMessageWindow()
    Jump("loc_2DB6")

    label("loc_2C2E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xFC)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2C5F")

    NpcTalk(    #66
        0xFD,
        "Kloe",
        "#1162F#5PThere it is!\x02",
    )

    CloseMessageWindow()
    Jump("loc_2DB6")

    label("loc_2C5F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xFC)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2C94")

    NpcTalk(    #67
        0xFD,
        "Scherazard",
        "#1522F#5PThat's it!\x02",
    )

    CloseMessageWindow()
    Jump("loc_2DB6")

    label("loc_2C94")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xFC)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2CC5")

    NpcTalk(    #68
        0xFD,
        "Agate",
        "#057F#5PThere it is!\x02",
    )

    CloseMessageWindow()
    Jump("loc_2DB6")

    label("loc_2CC5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xFC)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2CF2")

    NpcTalk(    #69
        0xFD,
        "Zin",
        "#072F#5PThat's it!\x02",
    )

    CloseMessageWindow()
    Jump("loc_2DB6")

    label("loc_2CF2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xFC)"), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2D23")

    NpcTalk(    #70
        0xFD,
        "Julia",
        "#172F#5PThere it is!\x02",
    )

    CloseMessageWindow()
    Jump("loc_2DB6")

    label("loc_2D23")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xFC)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2D55")

    NpcTalk(    #71
        0xFD,
        "Olivier",
        "#1542F#5PThat's it!\x02",
    )

    CloseMessageWindow()
    Jump("loc_2DB6")

    label("loc_2D55")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xFC)"), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2D88")

    NpcTalk(    #72
        0xFD,
        "Mueller",
        "#270F#5PThere it is!\x02",
    )

    CloseMessageWindow()
    Jump("loc_2DB6")

    label("loc_2D88")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xFC)"), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2DB6")

    NpcTalk(    #73
        0xFD,
        "Richard",
        "#112F#5PThat's it!\x02",
    )

    CloseMessageWindow()

    label("loc_2DB6")


    ChrTalk(    #74
        0x10F,
        "#1931F#5PKevin's Stigma!\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #75
        0xFD,
        "Kevin",
        (
            "#1063F#5PMaybe I can't match up to Rufina, but I'm not\x01",
            "fighting her. I'm fighting YOU.\x02\x03",

            "#1065FI'm not gonna lose to my own Stigma, and I'm\x01",
            "gonna set her free from you!\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)

    NpcTalk(    #76
        0xFD,
        "Kevin",
        "#1069F#5P#3SSo get ready for one hell of a beatdown!\x02",
    )

    OP_7C(0x0, 0x12C, 0xBB8, 0x64)
    CloseMessageWindow()
    Sleep(500)
    FadeToDark(300, 0, 100)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #77 op#A
        (
            "\x07\x02#60W#55AHahaha...\x01",
            "Go ahead and try, Kevin Graham!\x02\x03",

            "#60ABy devouring you, my original, I will be able\x01",
            "to become fully complete!\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    FadeToBright(300, 0)
    Sleep(500)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_DC(0x0, 0x0)
    SetMapFlags(0x2000000)
    OP_A2(0x2504)
    NewScene("ED6_DT21/M7402   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_2_60E end

    def Function_3_2FC0(): pass

    label("Function_3_2FC0")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadEffect(0x0, "map\\mp282_00.eff")
    LoadEffect(0x1, "map\\mp282_01.eff")
    OP_E0(250, 0x5C, 0x2)
    OP_E0(250, 0x5D, 0x3)
    OP_E0(251, 0x5E, 0x2)
    OP_E0(251, 0x5F, 0x3)
    OP_E0(252, 0x60, 0x2)
    OP_E0(252, 0x61, 0x3)
    OP_E0(253, 0x62, 0x2)
    OP_E0(253, 0x63, 0x3)
    SetChrPos(0xFA, -500, 0, 26340, 0)
    SetChrPos(0xFB, 780, 0, 26300, 0)
    SetChrPos(0xFC, -1150, 0, 24200, 0)
    SetChrPos(0xFD, 1450, 0, 24270, 0)
    SetChrPos(0x10, 0, 4000, 35320, 180)
    PlayEffect(0x0, 0x0, 0x10, 0, 0, 0, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    OP_6D(0, 3200, 37890, 0)
    OP_67(0, 2720, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(0, 0)
    OP_6E(378, 0)
    Sleep(1000)
    FadeToBright(1500, 0)
    OP_6B(3500, 1500)
    OP_0D()
    OP_22(0x85, 0x1, 0x3C)

    def lambda_3104():

        label("loc_3104")

        OP_7C(0x5, 0x5, 0xBB8, 0x12C)
        OP_48()
        Jump("loc_3104")

    QueueWorkItem2(0xFB, 3, lambda_3104)
    Sleep(500)
    OP_22(0x85, 0x1, 0x50)

    def lambda_3129():

        label("loc_3129")

        OP_7C(0xA, 0xA, 0xBB8, 0x12C)
        OP_48()
        Jump("loc_3129")

    QueueWorkItem2(0xFB, 3, lambda_3129)
    Sleep(500)
    OP_22(0x85, 0x1, 0x64)

    def lambda_314E():

        label("loc_314E")

        OP_7C(0x14, 0x14, 0xBB8, 0x12C)
        OP_48()
        Jump("loc_314E")

    QueueWorkItem2(0xFB, 3, lambda_314E)
    Fade(500)
    OP_22(0x32E, 0x1, 0x64)
    OP_22(0x2F2, 0x1, 0x64)
    OP_22(0x137, 0x1, 0x64)
    Sleep(100)
    PlayEffect(0x1, 0x1, 0x10, 0, 0, 0, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    OP_0D()
    Sleep(1000)
    OP_43(0x10, 0x0, 0x1, 0x2)
    WaitChrThread(0xFA, 0x0)
    FadeToDark(300, 0, 100)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #78 op#A
        (
            "\x07\x02#60W#75AMy name is Anima... I am this world's center,\x01",
            "its core, its very essence!\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    FadeToBright(300, 0)
    OP_20(0x7D0)
    OP_21()
    OP_1D(0x9C)

    def lambda_325B():
        OP_6D(0, 3050, 33290, 5000)
        ExitThread()

    QueueWorkItem(0xFA, 0, lambda_325B)

    def lambda_3273():
        OP_67(0, 1620, -10000, 5000)
        ExitThread()

    QueueWorkItem(0xFA, 1, lambda_3273)

    def lambda_328B():
        OP_6B(5170, 5000)
        ExitThread()

    QueueWorkItem(0xFA, 2, lambda_328B)

    def lambda_329B():
        OP_6E(270, 5000)
        ExitThread()

    QueueWorkItem(0xFA, 3, lambda_329B)
    WaitChrThread(0xFA, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xFD)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3308")

    ChrTalk(    #79
        0x101,
        (
            "#1002F#5P#40WThat's not gonna stop us beating the crap out\x01",
            "of you!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_36F0")

    label("loc_3308")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xFD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3355")

    ChrTalk(    #80
        0x102,
        "#1502F#5P#40WI guess we've got no choice but to fight.\x02",
    )

    CloseMessageWindow()
    Jump("loc_36F0")

    label("loc_3355")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xFD)"), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_33AB")

    ChrTalk(    #81
        0x10B,
        (
            "#210F#5P#40WHeh. We'll see how long you can keep talking\x01",
            "tough!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_36F0")

    label("loc_33AB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xFD)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_342F")

    ChrTalk(    #82
        0x110,
        (
            "#263F#5P#40WFor the essence of a world, you sure are naive.\x02\x03",

            "#1306FYou honestly think you can win against us?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_36F0")

    label("loc_342F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xFD)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_346C")

    ChrTalk(    #83
        0x107,
        "#062F#5P#40WWe won't lose! Not to you!\x02",
    )

    CloseMessageWindow()
    Jump("loc_36F0")

    label("loc_346C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xFD)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_34B5")

    ChrTalk(    #84
        0x10A,
        "#815F#5P#40WWell, we're not gonna let you beat us!\x02",
    )

    CloseMessageWindow()
    Jump("loc_36F0")

    label("loc_34B5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xFD)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3501")

    ChrTalk(    #85
        0x105,
        "#1162F#5P#40W...Seems we have no choice but to fight.\x02",
    )

    CloseMessageWindow()
    Jump("loc_36F0")

    label("loc_3501")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xFD)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3531")

    ChrTalk(    #86
        0x103,
        "#1524F#5P#40WBring it on!\x02",
    )

    CloseMessageWindow()
    Jump("loc_36F0")

    label("loc_3531")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xFD)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_357F")

    ChrTalk(    #87
        0x106,
        "#057F#5P#40WBah. Looks like fighting's our only option.\x02",
    )

    CloseMessageWindow()
    Jump("loc_36F0")

    label("loc_357F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xFD)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_35CF")

    ChrTalk(    #88
        0x108,
        "#070F#5P#40WWell, looks like fighting is the only option.\x02",
    )

    CloseMessageWindow()
    Jump("loc_36F0")

    label("loc_35CF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xFD)"), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3620")

    ChrTalk(    #89
        0x10E,
        "#172F#5P#40WIf fighting is our only option, then so be it!\x02",
    )

    CloseMessageWindow()
    Jump("loc_36F0")

    label("loc_3620")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xFD)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_366E")

    ChrTalk(    #90
        0x104,
        "#1545F#5P#40WHeh. Seems we have no choice but to fight.\x02",
    )

    CloseMessageWindow()
    Jump("loc_36F0")

    label("loc_366E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xFD)"), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_36BF")

    ChrTalk(    #91
        0x10D,
        "#270F#5P#40WIf fighting is our only option, then so be it!\x02",
    )

    CloseMessageWindow()
    Jump("loc_36F0")

    label("loc_36BF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xFD)"), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_36F0")

    ChrTalk(    #92
        0x10C,
        "#111F#5P#40WWe will overcome!\x02",
    )

    CloseMessageWindow()

    label("loc_36F0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xFC)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3759")

    ChrTalk(    #93
        0x101,
        (
            "#1005F#5P#40WIf those are the rules of this game, we'll be \x01",
            "happy to play by them!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3CBE")

    label("loc_3759")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xFC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_37C2")

    ChrTalk(    #94
        0x102,
        (
            "#1502F#5P#40WIf those are the rules of this game, we'll be \x01",
            "happy to play by them!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3CBE")

    label("loc_37C2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xFC)"), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_382A")

    ChrTalk(    #95
        0x10B,
        (
            "#214F#5P#40WIf those are the rules of this game, we'll be \x01",
            "happy to play by them!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3CBE")

    label("loc_382A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xFC)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_38AE")

    ChrTalk(    #96
        0x110,
        (
            "#263F#5P#40WFor the essence of a world, you sure are naive.\x02\x03",

            "#1306FYou honestly think you can win against us?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3CBE")

    label("loc_38AE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xFC)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3916")

    ChrTalk(    #97
        0x107,
        (
            "#062F#5P#40WIf those are the rules of this game, we'll be \x01",
            "happy to play by them!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3CBE")

    label("loc_3916")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xFC)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_397E")

    ChrTalk(    #98
        0x10A,
        (
            "#815F#5P#40WIf those are the rules of this game, we'll be \x01",
            "happy to play by them!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3CBE")

    label("loc_397E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xFC)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_39E7")

    ChrTalk(    #99
        0x105,
        (
            "#1166F#5P#40WIf those are the rules of this game, we'll be \x01",
            "happy to play by them!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3CBE")

    label("loc_39E7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xFC)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3A50")

    ChrTalk(    #100
        0x103,
        (
            "#1524F#5P#40WIf those are the rules of this game, we'll be \x01",
            "happy to play by them!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3CBE")

    label("loc_3A50")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xFC)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3AB8")

    ChrTalk(    #101
        0x106,
        (
            "#054F#5P#40WIf those are the rules of this game, we'll be \x01",
            "happy to play by them!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3CBE")

    label("loc_3AB8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xFC)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3B20")

    ChrTalk(    #102
        0x108,
        (
            "#076F#5P#40WIf those are the rules of this game, we'll be \x01",
            "happy to play by them!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3CBE")

    label("loc_3B20")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xFC)"), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3B88")

    ChrTalk(    #103
        0x10E,
        (
            "#177F#5P#40WIf those are the rules of this game, we'll be \x01",
            "happy to play by them!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3CBE")

    label("loc_3B88")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xFC)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3BF1")

    ChrTalk(    #104
        0x104,
        (
            "#1550F#5P#40WIf those are the rules of this game, we'll be \x01",
            "happy to play by them!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3CBE")

    label("loc_3BF1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xFC)"), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3C59")

    ChrTalk(    #105
        0x10D,
        (
            "#271F#5P#40WIf those are the rules of this game, we'll be \x01",
            "happy to play by them!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3CBE")

    label("loc_3C59")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xFC)"), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3CBE")

    ChrTalk(    #106
        0x10C,
        (
            "#114F#5P#40WIf those are the rules of this game, we'll be \x01",
            "happy to play by them!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3CBE")

    Sleep(300)
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0xFA, 28)
    SetChrSubChip(0xFA, 0)
    Sleep(50)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0xFB, 30)
    SetChrSubChip(0xFB, 0)
    Sleep(50)
    OP_22(0xD8, 0x0, 0x64)
    SetChrChipByIndex(0xFC, 32)
    SetChrSubChip(0xFC, 0)
    Sleep(50)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0xFD, 34)
    SetChrSubChip(0xFD, 0)
    OP_0D()
    Sleep(1000)

    ChrTalk(    #107
        0x109,
        (
            "#1065F#5P#40WSo I can finally take that first true step\x01",
            "towards accepting myself...\x02\x03",

            "#1069F...and so all of us can be reunited again--\x01",
            "so we return safely to our world...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #108
        0x10F,
        "#1939F#5P#40W...we ARE going to defeat you!\x02",
    )

    CloseMessageWindow()
    Sleep(1000)
    ClearMapFlags(0x2000000)
    OP_C0(0x14, 0x1F40, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_24(0x85, 0x5A)
    Sleep(400)
    OP_24(0x85, 0x50)
    Sleep(400)
    OP_24(0x85, 0x46)
    Sleep(400)
    OP_24(0x85, 0x3C)
    Sleep(400)
    OP_24(0x85, 0x32)
    Sleep(400)
    OP_24(0x85, 0x28)
    Sleep(400)
    OP_24(0x85, 0x1E)
    Sleep(400)
    OP_24(0x85, 0x14)
    Sleep(400)
    OP_23(0x85)
    OP_0D()
    Jc((scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3E87")
    OP_DC(0x0, 0x0)
    OP_E6(0x1, 0x0)
    Jump("loc_3EAE")

    label("loc_3E87")

    Jc((scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3E9C")
    OP_DC(0x0, 0x1)
    OP_E6(0x1, 0x1)
    Jump("loc_3EAE")

    label("loc_3E9C")

    Jc((scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3EAE")
    OP_DC(0x0, 0x2)
    OP_E6(0x1, 0x2)

    label("loc_3EAE")

    OP_A2(0x0)
    OP_4F(0x31, (scpexpr(EXPR_PUSH_LONG, 0x1A3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_C4(0x0, 0x10)
    OP_C0(0x16, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_C4(0x1, 0x10)
    OP_A3(0x0)
    OP_4F(0x30, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3F10")
    Battle(0x334, 0x300002, 0x0, 0x0, 0xFF)
    Jump("loc_3F45")

    label("loc_3F10")

    Jc((scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3F2C")
    Battle(0x335, 0x300002, 0x0, 0x0, 0xFF)
    Jump("loc_3F45")

    label("loc_3F2C")

    Jc((scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3F45")
    Battle(0x336, 0x300002, 0x0, 0x0, 0xFF)

    label("loc_3F45")

    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3F5A")
    OP_DC(0x0, 0x0)
    OP_E6(0x1, 0x0)
    Jump("loc_3F81")

    label("loc_3F5A")

    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3F6F")
    OP_DC(0x0, 0x1)
    OP_E6(0x1, 0x1)
    Jump("loc_3F81")

    label("loc_3F6F")

    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3F81")
    OP_DC(0x0, 0x2)
    OP_E6(0x1, 0x2)

    label("loc_3F81")

    OP_A2(0x1)
    OP_4F(0x31, (scpexpr(EXPR_PUSH_LONG, 0x1A3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_C4(0x0, 0x10)
    OP_C0(0x16, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_C4(0x1, 0x10)
    OP_A3(0x1)
    FadeToDark(0, 0, -1)
    EventBegin(0x0)
    OP_4F(0x30, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3FEF")
    Battle(0x334, 0x300002, 0x0, 0x0, 0xFF)
    Jump("loc_4024")

    label("loc_3FEF")

    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_400B")
    Battle(0x335, 0x300002, 0x0, 0x0, 0xFF)
    Jump("loc_4024")

    label("loc_400B")

    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4024")
    Battle(0x336, 0x300002, 0x0, 0x0, 0xFF)

    label("loc_4024")

    Jc((scpexpr(EXPR_23, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4039")
    OP_DC(0x0, 0x0)
    OP_E6(0x1, 0x0)
    Jump("loc_4060")

    label("loc_4039")

    Jc((scpexpr(EXPR_23, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_404E")
    OP_DC(0x0, 0x1)
    OP_E6(0x1, 0x1)
    Jump("loc_4060")

    label("loc_404E")

    Jc((scpexpr(EXPR_23, 0x5), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4060")
    OP_DC(0x0, 0x2)
    OP_E6(0x1, 0x2)

    label("loc_4060")

    OP_A2(0x2)
    OP_4F(0x31, (scpexpr(EXPR_PUSH_LONG, 0x1A3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_C4(0x0, 0x10)
    OP_C0(0x16, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_C4(0x1, 0x10)
    OP_A3(0x2)
    FadeToDark(0, 0, -1)
    EventBegin(0x0)
    OP_4F(0x30, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_23, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_40CE")
    Battle(0x334, 0x300002, 0x0, 0x0, 0xFF)
    Jump("loc_4103")

    label("loc_40CE")

    Jc((scpexpr(EXPR_23, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_40EA")
    Battle(0x335, 0x300002, 0x0, 0x0, 0xFF)
    Jump("loc_4103")

    label("loc_40EA")

    Jc((scpexpr(EXPR_23, 0x5), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4103")
    Battle(0x336, 0x300002, 0x0, 0x0, 0xFF)

    label("loc_4103")

    FadeToDark(0, 0, -1)
    EventBegin(0x0)
    OP_20(0x1388)
    OP_21()
    OP_DC(0x0, 0x3)
    OP_E6(0x1, 0x3)
    Sleep(500)
    OP_A2(0x2582)
    OP_4F(0x31, (scpexpr(EXPR_PUSH_LONG, 0x1A3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_C4(0x0, 0x10)
    SetMessageWindowPos(-1, 100, -1, -1)
    SetChrName("")

    AnonymousTalk(    #109
        "\x07\x05Save your current progress?\x18\x02",
    )

    FadeToDark(0, 0, -1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        240,
        180,
        0,
        (
            "Save\x01",         # 0
            "Proceed\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_5F(0x0)
    OP_56(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_419D")
    ShowSaveMenu()

    label("loc_419D")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(0, 0, -1)
    Sleep(2000)
    OP_C4(0x1, 0x10)
    OP_A3(0x2582)
    OP_4F(0x30, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Battle(0xE16, 0x300001, 0x0, 0x0, 0xFF)
    SetMapFlags(0x80)
    OP_20(0x1388)
    OP_21()
    OP_A2(0x2504)
    NewScene("ED6_DT21/M7499   ._SN", 100, 20, 0)
    IdleLoop()
    Return()

    # Function_3_2FC0 end

    def Function_4_41EC(): pass

    label("Function_4_41EC")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadEffect(0x0, "map\\mp261_00.eff")
    OP_E0(250, 0x5C, 0x2)
    OP_E0(250, 0x5D, 0x3)
    OP_E0(251, 0x5E, 0x2)
    OP_E0(251, 0x5F, 0x3)
    OP_E0(252, 0x60, 0x2)
    OP_E0(252, 0x61, 0x3)
    OP_E0(253, 0x62, 0x2)
    OP_E0(253, 0x63, 0x3)
    SetChrPos(0xFA, -1710, 0, 27030, 0)
    SetChrPos(0xFB, -210, 0, 26760, 0)
    SetChrPos(0xFC, -2210, 0, 25040, 0)
    SetChrPos(0xFD, -430, 0, 24930, 0)
    SetChrChipByIndex(0xFA, 28)
    SetChrSubChip(0xFA, 0)
    SetChrChipByIndex(0xFB, 30)
    SetChrSubChip(0xFB, 0)
    SetChrChipByIndex(0xFC, 32)
    SetChrSubChip(0xFC, 0)
    SetChrChipByIndex(0xFD, 34)
    SetChrSubChip(0xFD, 0)
    PlayEffect(0x0, 0x0, 0xFF, -630, 2000, 34430, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_6D(910, 0, 30370, 0)
    OP_67(0, 5830, -10000, 0)
    OP_6B(3280, 0)
    OP_6C(45000, 0)
    OP_6E(346, 0)
    FadeToBright(500, 0)
    OP_0D()
    Battle(0xE16, 0x0, 0x0, 0x0, 0xFF)
    Call(0, 5)
    Return()

    # Function_4_41EC end

    def Function_5_432D(): pass

    label("Function_5_432D")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadEffect(0x0, "map\\mp261_00.eff")
    OP_E0(250, 0x5C, 0x2)
    OP_E0(250, 0x5D, 0x3)
    OP_E0(251, 0x5E, 0x2)
    OP_E0(251, 0x5F, 0x3)
    OP_E0(252, 0x60, 0x2)
    OP_E0(252, 0x61, 0x3)
    OP_E0(253, 0x62, 0x2)
    OP_E0(253, 0x63, 0x3)
    SetChrPos(0xFA, -1710, 0, 27030, 0)
    SetChrPos(0xFB, -210, 0, 26760, 0)
    SetChrPos(0xFC, -2210, 0, 25040, 0)
    SetChrPos(0xFD, -430, 0, 24930, 0)
    PlayEffect(0x0, 0x0, 0xFF, -630, 2000, 34430, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_6D(910, 0, 30370, 0)
    OP_67(0, 5830, -10000, 0)
    OP_6B(3280, 0)
    OP_6C(45000, 0)
    OP_6E(346, 0)
    FadeToBright(500, 0)
    OP_0D()
    Sleep(300)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #110
        "\x07\x00◆Carry out events on another dimension map.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #111
        (
            "\x07\x00◆After battle, the last boss disappears while\x01",
            "howling in another dimension. The Stigma remains,\x01",
            "but its red glow is lost, replaced by a blue one.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)

    ChrTalk(    #112
        0x109,
        "#1060FOh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0x10F,
        "#1930FIts color changed...\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #114
        "\x07\x00◆The Stigma shines, giving off a blue light.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToDark(1000, 16777215, -1)
    OP_0D()
    OP_C4(0x0, 0x10)
    FadeToBright(3000, 16777215)
    OP_0D()
    FadeToDark(0, 0, -1)
    OP_0D()
    OP_C4(0x1, 0x10)
    OP_A2(0x2506)
    NewScene("ED6_DT21/M5415   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_5_432D end

    def Function_6_45E2(): pass

    label("Function_6_45E2")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_71(0x400, 0x0)
    ExitThread()
    LoadEffect(0x0, "map\\mp259_01.eff")
    LoadEffect(0x1, "map\\mp263_05.eff")
    LoadEffect(0x2, "map\\mp276_00.eff")
    LoadEffect(0x3, "map\\mp277_00.eff")
    LoadEffect(0x4, "map\\mp278_00.eff")
    LoadEffect(0x5, "map\\mp277_01.eff")
    OP_DF(0x0, 0x1, 0x1)
    Sleep(1000)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0xC, 0x8)
    ClearChrFlags(0xD, 0x8)
    ClearChrFlags(0xE, 0x8)
    ClearChrFlags(0xF, 0x8)
    SetChrPos(0xFA, 390, 0, 13390, 0)
    SetChrPos(0xFB, -1280, 0, 13610, 45)
    SetChrPos(0xFC, -710, 0, 15710, 180)
    SetChrPos(0xFD, 910, 0, 15860, 180)
    SetChrChipByIndex(0xFA, 22)
    SetChrSubChip(0xFA, 0)
    SetChrFlags(0xFA, 0x800)
    ClearChrFlags(0xFA, 0x1)
    SetChrChipByIndex(0xFB, 23)
    SetChrSubChip(0xFB, 0)
    SetChrFlags(0xFB, 0x800)
    ClearChrFlags(0xFB, 0x1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xFC)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xFD)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4737")
    ClearChrFlags(0x101, 0x8)
    ClearChrFlags(0x101, 0x80)
    SetChrPos(0x101, -1280, 0, 16700, 180)

    label("loc_4737")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xFC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xFD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_476B")
    ClearChrFlags(0x102, 0x8)
    ClearChrFlags(0x102, 0x80)
    SetChrPos(0x102, 440, 0, 17500, 180)

    label("loc_476B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xFC)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xFD)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_479F")
    ClearChrFlags(0x110, 0x8)
    ClearChrFlags(0x110, 0x80)
    SetChrPos(0x110, -2300, 0, 17150, 180)

    label("loc_479F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xFC)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xFD)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_47D3")
    ClearChrFlags(0x107, 0x8)
    ClearChrFlags(0x107, 0x80)
    SetChrPos(0x107, 2600, 0, 13870, 270)

    label("loc_47D3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xFC)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xFD)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4807")
    ClearChrFlags(0x106, 0x8)
    ClearChrFlags(0x106, 0x80)
    SetChrPos(0x106, 3050, 0, 12840, 270)

    label("loc_4807")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xFC)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xFD)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_483B")
    ClearChrFlags(0x105, 0x8)
    ClearChrFlags(0x105, 0x80)
    SetChrPos(0x105, 2550, 0, 16340, 225)

    label("loc_483B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xFC)"), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xFD)"), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_486F")
    ClearChrFlags(0x10E, 0x8)
    ClearChrFlags(0x10E, 0x80)
    SetChrPos(0x10E, 3150, 0, 15430, 225)

    label("loc_486F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xFC)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xFD)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_48A3")
    ClearChrFlags(0x103, 0x8)
    ClearChrFlags(0x103, 0x80)
    SetChrPos(0x103, -4180, 0, 11880, 45)

    label("loc_48A3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xFC)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xFD)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_48D7")
    ClearChrFlags(0x10A, 0x8)
    ClearChrFlags(0x10A, 0x80)
    SetChrPos(0x10A, -3520, 0, 10710, 45)

    label("loc_48D7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xFC)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xFD)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_490B")
    ClearChrFlags(0x104, 0x8)
    ClearChrFlags(0x104, 0x80)
    SetChrPos(0x104, -3180, 0, 14760, 90)

    label("loc_490B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xFC)"), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xFD)"), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_493F")
    ClearChrFlags(0x10D, 0x8)
    ClearChrFlags(0x10D, 0x80)
    SetChrPos(0x10D, -3800, 0, 13380, 90)

    label("loc_493F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xFC)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xFD)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4973")
    ClearChrFlags(0x108, 0x8)
    ClearChrFlags(0x108, 0x80)
    SetChrPos(0x108, 1390, 0, 10890, 315)

    label("loc_4973")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xFC)"), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xFD)"), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_49A7")
    ClearChrFlags(0x10C, 0x8)
    ClearChrFlags(0x10C, 0x80)
    SetChrPos(0x10C, -490, 0, 10260, 0)

    label("loc_49A7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xFC)"), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xFD)"), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_49DB")
    ClearChrFlags(0x10B, 0x8)
    ClearChrFlags(0x10B, 0x80)
    SetChrPos(0x10B, -1900, 0, 10500, 0)

    label("loc_49DB")

    OP_6D(800, 0, 14690, 0)
    OP_67(0, 5810, -10000, 0)
    OP_6B(3450, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    SetMessageWindowPos(60, 120, -1, -1)
    SetChrName("Girl's Voice")

    AnonymousTalk(    #115
        "\x07\x00Kevin! Ries!\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(200, 60, -1, -1)
    SetChrName("Boy's Voice")

    AnonymousTalk(    #116
        "\x07\x00Please...wake up!\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(330, 250, -1, -1)
    SetChrName("Kevin")

    AnonymousTalk(    #117
        "\x07\x00#1067F#60WMm...\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(160, 300, -1, -1)
    SetChrName("Ries")

    AnonymousTalk(    #118
        "\x07\x00#1955F#60WHmm...?\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_1D(0xAD)

    def lambda_4AD2():
        OP_6B(3220, 3000)
        ExitThread()

    QueueWorkItem(0x22, 0, lambda_4AD2)
    FadeToBright(3000, 0)
    OP_0D()
    WaitChrThread(0x22, 0x0)
    Sleep(1000)

    def lambda_4AF6():
        OP_9E(0xFE, 0xF, 0x0, 0x12C, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFA, 3, lambda_4AF6)
    Sleep(100)
    Fade(250)
    OP_22(0x8F, 0x0, 0x64)
    SetChrChipByIndex(0xFA, 24)
    SetChrSubChip(0xFA, 0)
    OP_0D()
    Sleep(100)

    def lambda_4B2F():
        OP_9E(0xFE, 0xF, 0x0, 0x12C, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFB, 3, lambda_4B2F)
    Sleep(100)
    Fade(250)
    OP_22(0x8F, 0x0, 0x64)
    SetChrChipByIndex(0xFB, 25)
    SetChrSubChip(0xFB, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #119
        0x109,
        "#1079F#12P#40WHuh...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #120
        0x10F,
        "#1949F#6P#40WWhere are we...?\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xFC)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xFD)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4C31")

    ChrTalk(    #121
        0x101,
        (
            "#1007F#5PTh-Thank Aidios...\x02\x03",

            "#1025FYou scared us half to death when you passed\x01",
            "out the second the battle ended.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5381")

    label("loc_4C31")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xFC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xFD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4CB2")

    ChrTalk(    #122
        0x102,
        (
            "#1513F#5PThank goodness...\x02\x03",

            "#1514FYou scared us half to death when you\x01",
            "fainted all of a sudden.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5381")

    label("loc_4CB2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xFC)"), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xFD)"), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4D57")

    ChrTalk(    #123
        0x10B,
        (
            "#413F#5P*sigh* You really scared the crap out of us,\x01",
            "you know?\x02\x03",

            "#210FAs soon as the battle ended, you two conked\x01",
            "out outta nowhere.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5381")

    label("loc_4D57")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xFC)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xFD)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4DF2")

    ChrTalk(    #124
        0x110,
        (
            "#268F#5P*sigh* You really scared us, you know?\x02\x03",

            "#262FAfter the battle finished, you two suddenly\x01",
            "fainted without warning.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5381")

    label("loc_4DF2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xFC)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xFD)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4E84")

    ChrTalk(    #125
        0x107,
        (
            "#562F#5PTh-Thank Aidios...\x02\x03",

            "#063FYou really scared us when you suddenly\x01",
            "fainted the second the fight was over...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5381")

    label("loc_4E84")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xFC)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xFD)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4F11")

    ChrTalk(    #126
        0x10A,
        (
            "#1311F#5PWhew... Thank goodness.\x02\x03",

            "#1314FYou really freaked us out when you just\x01",
            "passed out after the fight.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5381")

    label("loc_4F11")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xFC)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xFD)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4FAD")

    ChrTalk(    #127
        0x105,
        (
            "#1165F#5PThank goodness you're all right...\x02\x03",

            "#1382FWe were really worried when you two\x01",
            "fainted as soon as the fight ended.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5381")

    label("loc_4FAD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xFC)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xFD)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_5075")

    ChrTalk(    #128
        0x104,
        (
            "#1541F#5PYou gave us quite the surprise when you\x01",
            "fainted after the battle ended.\x02\x03",

            "#1547FWere you enjoying a romantic getaway in\x01",
            "a different land of dreams, perchance?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5381")

    label("loc_5075")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xFC)"), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xFD)"), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_510D")

    ChrTalk(    #129
        0x10E,
        (
            "#179F#5PThank goodness you're all right...\x02\x03",

            "#171FWe were really worried when you fainted\x01",
            "so suddenly after the battle.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5381")

    label("loc_510D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xFC)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xFD)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_51A8")

    ChrTalk(    #130
        0x103,
        (
            "#1525F#5PYou two gave us a real scare, there...\x02\x03",

            "#1527FThe second we finished fighting, you just\x01",
            "fainted all of a sudden.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5381")

    label("loc_51A8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xFC)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xFD)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_5240")

    ChrTalk(    #131
        0x106,
        (
            "#551F#5PYou two scared the shit out of us, you know.\x02\x03",

            "#555FThe second we finished fighting, you fainted\x01",
            "outta nowhere.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5381")

    label("loc_5240")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xFC)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xFD)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_52E7")

    ChrTalk(    #132
        0x108,
        (
            "#074F#5PWhew... Looks like you're okay.\x01",
            "Talk about a relief.\x02\x03",

            "#070FThe second we finished fighting,\x01",
            "you just fainted all of a sudden.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5381")

    label("loc_52E7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xFC)"), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xFD)"), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_5381")

    ChrTalk(    #133
        0x10D,
        (
            "#278F#5P...I'm glad you're both awake.\x02\x03",

            "#277FYou gave us quite the scare when you fainted\x01",
            "all of a sudden after the battle.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5381")

    OP_62(0x109, 0xFFFFFED4, 1800, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(100)
    OP_62(0x10F, 0x0, 1600, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    Fade(250)
    SetChrChipByIndex(0xFA, 2)
    SetChrSubChip(0xFA, 0)
    ClearChrFlags(0xFA, 0x800)
    SetChrFlags(0xFA, 0x1)
    Sleep(500)
    Fade(250)
    SetChrChipByIndex(0xFB, 3)
    SetChrSubChip(0xFB, 0)
    ClearChrFlags(0xFB, 0x800)
    SetChrFlags(0xFB, 0x1)
    OP_0D()
    Sleep(500)

    ChrTalk(    #134
        0x109,
        "#1847F#12PWe fainted?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #135
        0x10F,
        "#1950F#6PB-But...\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    FadeToDark(300, 0, 100)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(-1, 60, -1, -1)
    SetChrName("")

    AnonymousTalk(    #136
        (
            "\x07\x0CI imagine she summoned your spirits to an area\x01",
            "of her creation, leaving your bodies behind.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    FadeToBright(300, 0)
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x10F, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x107, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x10B, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x10C, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x10D, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x10E, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x110, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x10A, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x106, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x108, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_564F():
        OP_6D(3060, 300, 16610, 1500)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_564F)

    def lambda_5667():
        OP_67(0, 4500, -10000, 1500)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_5667)

    def lambda_567F():
        OP_6B(3320, 1500)
        ExitThread()

    QueueWorkItem(0xEE, 2, lambda_567F)

    def lambda_568F():
        OP_6E(316, 1500)
        ExitThread()

    QueueWorkItem(0xEE, 3, lambda_568F)
    WaitChrThread(0xEE, 0x0)
    ClearChrFlags(0x22, 0x80)
    SetChrPos(0x22, 4770, 500, 18110, 225)
    SetChrFlags(0x22, 0x4)
    OP_9F(0x22, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_56CA():

        label("loc_56CA")

        OP_99(0xFE, 0x0, 0x7, 0x3E8)
        OP_48()
        Jump("loc_56CA")

    QueueWorkItem2(0x22, 0, lambda_56CA)
    OP_22(0xD7, 0x0, 0x64)
    PlayEffect(0x1, 0x0, 0x22, 0, 800, 0, 0, 0, 0, 900, 900, 900, 0xFF, 0, 0, 0, 0)
    Sleep(500)

    def lambda_571C():
        OP_8C(0xFE, 45, 400)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_571C)

    def lambda_572A():
        OP_8C(0xFE, 45, 400)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_572A)
    Sleep(50)

    def lambda_573D():
        TurnDirection(0xFE, 0x22, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_573D)

    def lambda_574B():
        TurnDirection(0xFE, 0x22, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_574B)
    Sleep(50)

    def lambda_575E():
        TurnDirection(0xFE, 0x22, 400)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_575E)

    def lambda_576C():
        TurnDirection(0xFE, 0x22, 400)
        ExitThread()

    QueueWorkItem(0x10E, 1, lambda_576C)
    Sleep(50)

    def lambda_577F():
        TurnDirection(0xFE, 0x22, 400)
        ExitThread()

    QueueWorkItem(0x110, 1, lambda_577F)

    def lambda_578D():
        TurnDirection(0xFE, 0x22, 400)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_578D)
    Sleep(50)

    def lambda_57A0():
        TurnDirection(0xFE, 0x22, 400)
        ExitThread()

    QueueWorkItem(0x110, 1, lambda_57A0)

    def lambda_57AE():
        TurnDirection(0xFE, 0x22, 400)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_57AE)
    Sleep(50)

    def lambda_57C1():
        TurnDirection(0xFE, 0x22, 400)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_57C1)

    def lambda_57CF():
        TurnDirection(0xFE, 0x22, 400)
        ExitThread()

    QueueWorkItem(0x10D, 1, lambda_57CF)
    Sleep(50)

    def lambda_57E2():
        TurnDirection(0xFE, 0x22, 400)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_57E2)

    def lambda_57F0():
        TurnDirection(0xFE, 0x22, 400)
        ExitThread()

    QueueWorkItem(0x10C, 1, lambda_57F0)
    Sleep(50)

    def lambda_5803():
        TurnDirection(0xFE, 0x22, 400)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_5803)

    def lambda_5811():
        TurnDirection(0xFE, 0x22, 400)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_5811)
    Sleep(50)

    def lambda_5824():
        TurnDirection(0xFE, 0x22, 400)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_5824)

    def lambda_5832():
        TurnDirection(0xFE, 0x22, 400)
        ExitThread()

    QueueWorkItem(0x10B, 1, lambda_5832)
    Sleep(100)
    PlayEffect(0x0, 0x7, 0x22, 0, 900, 0, 0, 0, 0, 1600, 3300, 0, 0xFF, 0, 0, 0, 0)

    def lambda_587A():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xB4, 0x3E8)
        ExitThread()

    QueueWorkItem(0x22, 1, lambda_587A)
    OP_22(0x99, 0x0, 0x64)
    WaitChrThread(0x22, 0x1)
    OP_82(0x0, 0x2)
    Sleep(1000)

    ChrTalk(    #137
        0x105,
        "#1164F#6PThere you are...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #138
        0x109,
        "#1079F#6PCeleste...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #139
        0x22,
        (
            "\x07\x0C#1615F#5PI felt the return of all of my power a short\x01",
            "while ago.\x02\x03",

            "#1612FDid something happen, Kevin?\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #140
        0x10F,
        "#1935F#6POh...\x02",
    )

    CloseMessageWindow()

    def lambda_5959():
        TurnDirection(0xFE, 0x109, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5959)

    def lambda_5967():
        TurnDirection(0xFE, 0x109, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_5967)
    Sleep(50)

    def lambda_597A():
        TurnDirection(0xFE, 0x109, 400)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_597A)

    def lambda_5988():
        TurnDirection(0xFE, 0x109, 400)
        ExitThread()

    QueueWorkItem(0x10E, 1, lambda_5988)
    Sleep(50)

    def lambda_599B():
        TurnDirection(0xFE, 0x109, 400)
        ExitThread()

    QueueWorkItem(0x110, 1, lambda_599B)

    def lambda_59A9():
        TurnDirection(0xFE, 0x109, 400)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_59A9)
    Sleep(50)

    def lambda_59BC():
        TurnDirection(0xFE, 0x109, 400)
        ExitThread()

    QueueWorkItem(0x110, 1, lambda_59BC)

    def lambda_59CA():
        TurnDirection(0xFE, 0x109, 400)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_59CA)
    Sleep(50)

    def lambda_59DD():
        TurnDirection(0xFE, 0x109, 400)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_59DD)

    def lambda_59EB():
        TurnDirection(0xFE, 0x109, 400)
        ExitThread()

    QueueWorkItem(0x10D, 1, lambda_59EB)
    Sleep(50)

    def lambda_59FE():
        TurnDirection(0xFE, 0x109, 400)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_59FE)

    def lambda_5A0C():
        TurnDirection(0xFE, 0x109, 400)
        ExitThread()

    QueueWorkItem(0x10C, 1, lambda_5A0C)
    Sleep(50)

    def lambda_5A1F():
        TurnDirection(0xFE, 0x109, 400)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_5A1F)

    def lambda_5A2D():
        TurnDirection(0xFE, 0x109, 400)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_5A2D)
    Sleep(50)

    def lambda_5A40():
        TurnDirection(0xFE, 0x109, 400)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_5A40)

    def lambda_5A4E():
        TurnDirection(0xFE, 0x109, 400)
        ExitThread()

    QueueWorkItem(0x10B, 1, lambda_5A4E)
    Sleep(500)

    ChrTalk(    #141
        0x109,
        "#1065F#6PActually...\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #142
        (
            "\x07\x05Kevin explained to her that they had said farewell to Rufina, and that the\x01",
            "Stigma that once ruled the land of Phantasma had completely disappeared.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    Sleep(500)

    ChrTalk(    #143
        0x10E,
        "#176F#5PI see...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #144
        0x105,
        "#1169F#5PShe must have been an incredibly strong person...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #145
        0x22,
        (
            "\x07\x0C#1616F#5PI may have never had the chance to meet her...\x02\x03",

            "...but she sounds like someone I would have\x01",
            "liked to talk to.\x02\x03",

            "#1613FThat being said, there's no longer any time to\x01",
            "waste.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #146
        0x109,
        "#1079F#6PHuh?\x02",
    )

    CloseMessageWindow()

    def lambda_5C5F():
        TurnDirection(0xFE, 0x22, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5C5F)

    def lambda_5C6D():
        TurnDirection(0xFE, 0x22, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_5C6D)
    Sleep(50)

    def lambda_5C80():
        TurnDirection(0xFE, 0x22, 400)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_5C80)

    def lambda_5C8E():
        TurnDirection(0xFE, 0x22, 400)
        ExitThread()

    QueueWorkItem(0x10E, 1, lambda_5C8E)
    Sleep(50)

    def lambda_5CA1():
        TurnDirection(0xFE, 0x22, 400)
        ExitThread()

    QueueWorkItem(0x110, 1, lambda_5CA1)

    def lambda_5CAF():
        TurnDirection(0xFE, 0x22, 400)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_5CAF)
    Sleep(50)

    def lambda_5CC2():
        TurnDirection(0xFE, 0x22, 400)
        ExitThread()

    QueueWorkItem(0x110, 1, lambda_5CC2)

    def lambda_5CD0():
        TurnDirection(0xFE, 0x22, 400)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_5CD0)
    Sleep(50)

    def lambda_5CE3():
        TurnDirection(0xFE, 0x22, 400)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_5CE3)

    def lambda_5CF1():
        TurnDirection(0xFE, 0x22, 400)
        ExitThread()

    QueueWorkItem(0x10D, 1, lambda_5CF1)
    Sleep(50)

    def lambda_5D04():
        TurnDirection(0xFE, 0x22, 400)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_5D04)

    def lambda_5D12():
        TurnDirection(0xFE, 0x22, 400)
        ExitThread()

    QueueWorkItem(0x10C, 1, lambda_5D12)
    Sleep(50)

    def lambda_5D25():
        TurnDirection(0xFE, 0x22, 400)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_5D25)

    def lambda_5D33():
        TurnDirection(0xFE, 0x22, 400)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_5D33)
    Sleep(50)

    def lambda_5D46():
        TurnDirection(0xFE, 0x22, 400)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_5D46)

    def lambda_5D54():
        TurnDirection(0xFE, 0x22, 400)
        ExitThread()

    QueueWorkItem(0x10B, 1, lambda_5D54)
    Sleep(300)

    ChrTalk(    #147
        0x10F,
        "#1942F#6PWhy not?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #148
        0x22,
        (
            "\x07\x0C#1615F#5PNow that Phantasma has once again lost its\x01",
            "master, it will revert to being unstable once\x01",
            "more.\x02\x03",

            "#1612FThis castle will be no exception. I imagine it\x01",
            "will disappear before long, unable to retain its\x01",
            "current form any longer.\x02\x03",

            "The same will likely be true of all the planes,\x01",
            "even. Only the garden will remain.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x10F, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x107, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x10D, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x10B, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x10E, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x10C, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x108, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x10A, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x106, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #149
        0x101,
        "#1005FY-You're kidding!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x110, 0x101, 400)
    Sleep(300)

    ChrTalk(    #150
        0x110,
        (
            "#263FAre you really so surprised, Estelle?\x02\x03",

            "#260FWe know about how this world works.\x01",
            "This was always a likely possibility.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x110, 400)
    Sleep(300)

    ChrTalk(    #151
        0x101,
        (
            "#1007FI-It sure wasn't one I was thinking about...\x02\x03",

            "#1019FBesides, if you knew all of this already,\x01",
            "why is this the first time we're hearing\x01",
            "about it?!\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)

    ChrTalk(    #152
        0x102,
        (
            "#1502FWe should hurry to the Arseille and make\x01",
            "our escape at once.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_61CF():
        TurnDirection(0xFE, 0x22, 400)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_61CF)

    def lambda_61DD():
        TurnDirection(0xFE, 0x22, 400)
        ExitThread()

    QueueWorkItem(0x110, 0, lambda_61DD)
    Sleep(500)

    ChrTalk(    #153
        0x22,
        (
            "\x07\x0C#1615F#5PThere's no need.\x02\x03",

            "#1610FI can open the gates of heaven from here.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x10F, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x107, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x10D, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x10B, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x10E, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x10C, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x110, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x108, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x10A, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x106, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #154
        0x10F,
        "#1934F#6PYou can...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #155
        0x109,
        "#1064F#6PAs in the ones in the Testaments?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #156
        0x22,
        (
            "\x07\x0C#1616F#5PI believe so.\x02\x03",

            "To my recollection, they are the counterpart to\x01",
            "the gates of Gehenna, connecting the world in\x01",
            "which you reside to heaven above.\x02\x03",

            "#1611FA replica was prepared for us in the area we\x01",
            "stand.\x02\x03",

            "I can only assume the one who created them was\x01",
            "the woman who you bade farewell to--the one\x01",
            "who was assimilated into the Lord of Phantasma.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #157
        0x109,
        "#1840F#6PHaha...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #158
        0x10F,
        "#1952F#6PShe did...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #159
        0x104,
        "#1545FHmm... I see.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #160
        0x10D,
        (
            "#277FThen if we pass through there, we can return\x01",
            "to our own world?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #161
        0x22,
        (
            "\x07\x0C#1616F#5PPrecisely.\x02\x03",

            "#1610FThough perhaps seeing is believing.\x01",
            "Allow me to open the gates.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_22(0xD7, 0x0, 0x64)
    PlayEffect(0x1, 0x0, 0x22, 0, 800, 0, 0, 0, 0, 900, 900, 900, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    Fade(1000)

    def lambda_66B9():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x22, 1, lambda_66B9)
    OP_82(0x0, 0x0)
    OP_82(0x7, 0x0)
    OP_22(0x99, 0x0, 0x64)
    WaitChrThread(0x22, 0x1)
    OP_0D()
    Sleep(500)
    Fade(500)
    SetChrPos(0x22, 0, 4500, 23000, 0)
    OP_6D(0, 0, 33270, 0)
    OP_67(0, 4110, -10000, 0)
    OP_6B(3200, 0)
    OP_6C(0, 0)
    OP_6E(400, 0)
    OP_0D()
    Sleep(500)
    OP_22(0xD7, 0x0, 0x64)
    PlayEffect(0x1, 0x0, 0x22, 0, 800, 0, 0, 0, 0, 900, 900, 900, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    PlayEffect(0x0, 0x7, 0x22, 0, 900, 0, 0, 0, 0, 1600, 3300, 0, 0xFF, 0, 0, 0, 0)

    def lambda_67AE():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x22, 1, lambda_67AE)
    OP_22(0x99, 0x0, 0x64)
    WaitChrThread(0x22, 0x1)
    OP_82(0x0, 0x2)
    Sleep(500)
    Fade(250)
    SetChrChipByIndex(0x22, 26)
    SetChrSubChip(0x22, 0)
    OP_0D()
    Sleep(300)
    Fade(1000)
    OP_22(0x138, 0x0, 0x64)
    OP_22(0x146, 0x1, 0x46)
    PlayEffect(0x2, 0x6, 0x22, 0, 500, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_0D()
    Fade(500)
    OP_82(0x7, 0x2)
    OP_0D()
    Sleep(1500)

    def lambda_683A():
        OP_6D(0, 15300, 41770, 5000)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_683A)

    def lambda_6852():
        OP_67(0, -1500, -10000, 5000)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_6852)

    def lambda_686A():
        OP_6B(3850, 5000)
        ExitThread()

    QueueWorkItem(0xEE, 2, lambda_686A)

    def lambda_687A():
        OP_6E(437, 5000)
        ExitThread()

    QueueWorkItem(0xEE, 3, lambda_687A)
    WaitChrThread(0xEE, 0x0)

    def lambda_688F():
        OP_6B(3500, 4000)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_688F)
    OP_72(0x200C, 0x0)
    ExitThread()
    OP_6F(0xC, 0)
    OP_70(0xC, 0x0)
    OP_72(0x200D, 0x0)
    ExitThread()
    OP_6F(0xD, 0)
    OP_70(0xD, 0x0)
    OP_72(0x200E, 0x0)
    ExitThread()
    OP_6F(0xE, 0)
    OP_70(0xE, 0x0)
    OP_22(0x233, 0x0, 0x64)
    Fade(1000)
    OP_72(0x40C, 0x0)
    ExitThread()
    OP_0D()
    OP_22(0x233, 0x0, 0x64)
    Fade(1000)
    OP_72(0x40D, 0x0)
    ExitThread()
    OP_0D()
    OP_22(0x233, 0x0, 0x64)
    Fade(1000)
    OP_72(0x40E, 0x0)
    ExitThread()
    OP_0D()
    WaitChrThread(0xEE, 0x0)

    def lambda_6913():
        OP_6D(0, 14550, 41420, 5000)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_6913)
    OP_22(0x150, 0x0, 0x64)
    PlayEffect(0x3, 0x0, 0xFF, 0, 14500, 56000, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    PlayEffect(0x5, 0x1, 0xFF, 0, 15500, 56000, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    Sleep(1500)
    OP_7A(0x20, 0x2)
    OP_7A(0x1E, 0x2)
    OP_7B()
    Fade(2000)
    OP_22(0x138, 0x0, 0x64)
    OP_72(0x40A, 0x0)
    ExitThread()
    OP_72(0x40B, 0x0)
    ExitThread()

    def lambda_69C3():
        OP_6D(0, 14550, 41420, 3000)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_69C3)

    def lambda_69DB():
        OP_67(0, -1230, -10000, 3000)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_69DB)

    def lambda_69F3():
        OP_6B(4340, 3000)
        ExitThread()

    QueueWorkItem(0xEE, 2, lambda_69F3)

    def lambda_6A03():
        OP_6E(420, 3000)
        ExitThread()

    QueueWorkItem(0xEE, 3, lambda_6A03)
    OP_E5(0x2, 0x1, 0x0, 200)
    OP_E5(0x2, 0x1, 0x1, 100)
    OP_E5(0x2, 0x1, 0x2, 100)
    OP_E5(0x2, 0xA, 0x0, 300)
    OP_E5(0x2, 0xA, 0x1, 300)
    OP_E5(0x2, 0xA, 0x2, 300)
    OP_E5(0x2, 0xA, 0x3, 300)
    OP_E5(0x2, 0xB, 0x0, 300)
    OP_E5(0x2, 0xB, 0x1, 300)
    OP_E5(0x2, 0xB, 0x2, 300)
    OP_E5(0x2, 0xB, 0x3, 300)
    OP_0D()
    OP_82(0x0, 0x2)
    OP_82(0x1, 0x2)
    Sleep(3000)
    Fade(500)
    OP_6D(790, 5450, 42830, 0)
    OP_67(0, 5970, -10000, 0)
    OP_6B(5200, 0)
    OP_6C(69000, 0)
    OP_6E(475, 0)
    OP_0D()
    Sleep(500)

    def lambda_6ABF():
        OP_6D(790, 5450, 42830, 2000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_6ABF)

    def lambda_6AD7():
        OP_67(0, 5970, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_6AD7)

    def lambda_6AEF():
        OP_6B(4960, 2000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_6AEF)

    def lambda_6AFF():
        OP_6C(69000, 2000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_6AFF)

    def lambda_6B0F():
        OP_6E(455, 2000)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_6B0F)
    Fade(2000)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_22(0x2D8, 0x0, 0x64)
    OP_72(0x401, 0x0)
    ExitThread()
    Sleep(50)
    OP_72(0x40F, 0x0)
    ExitThread()
    Sleep(50)
    OP_72(0x410, 0x0)
    ExitThread()
    Sleep(50)
    OP_72(0x411, 0x0)
    ExitThread()
    Sleep(50)
    OP_72(0x412, 0x0)
    ExitThread()
    Sleep(50)
    OP_72(0x413, 0x0)
    ExitThread()
    Sleep(50)
    OP_72(0x414, 0x0)
    ExitThread()
    Sleep(50)
    OP_72(0x415, 0x0)
    ExitThread()
    Sleep(50)
    OP_72(0x416, 0x0)
    ExitThread()
    Sleep(50)
    OP_72(0x417, 0x0)
    ExitThread()
    Sleep(50)
    OP_72(0x418, 0x0)
    ExitThread()
    Sleep(50)
    OP_72(0x419, 0x0)
    ExitThread()
    Sleep(50)
    OP_72(0x41A, 0x0)
    ExitThread()
    Sleep(50)
    OP_72(0x41B, 0x0)
    ExitThread()
    Sleep(50)
    OP_72(0x41C, 0x0)
    ExitThread()
    Sleep(50)
    OP_72(0x41D, 0x0)
    ExitThread()
    Sleep(50)
    OP_72(0x41E, 0x0)
    ExitThread()
    Sleep(50)
    OP_72(0x41F, 0x0)
    ExitThread()
    Sleep(50)
    OP_72(0x420, 0x0)
    ExitThread()
    Sleep(50)
    OP_72(0x421, 0x0)
    ExitThread()
    Sleep(50)
    OP_72(0x422, 0x0)
    ExitThread()
    OP_0D()
    WaitChrThread(0x109, 0x0)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(1000)
    Fade(500)
    OP_6D(-1160, 14950, 54720, 0)
    OP_67(0, 3310, -10000, 0)
    OP_6B(5710, 0)
    OP_6C(45000, 0)
    OP_6E(365, 0)

    def lambda_6C6A():
        OP_6D(0, 15500, 47600, 10000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_6C6A)

    def lambda_6C82():
        OP_67(0, 200, -10000, 10000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_6C82)

    def lambda_6C9A():
        OP_6B(4000, 10000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_6C9A)

    def lambda_6CAA():
        OP_6C(0, 10000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_6CAA)

    def lambda_6CBA():
        OP_6E(533, 10000)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_6CBA)
    OP_71(0x200C, 0x0)
    ExitThread()
    OP_6F(0xC, 0)
    OP_70(0xC, 0x258)
    OP_71(0x200D, 0x0)
    ExitThread()
    OP_6F(0xD, 0)
    OP_70(0xD, 0x320)
    OP_71(0x200E, 0x0)
    ExitThread()
    OP_6F(0xE, 0)
    OP_70(0xE, 0x12C)
    OP_22(0x85, 0x1, 0x3C)

    def lambda_6D0B():

        label("loc_6D0B")

        OP_7C(0x5, 0x5, 0xBB8, 0x12C)
        OP_48()
        Jump("loc_6D0B")

    QueueWorkItem2(0x10F, 3, lambda_6D0B)
    Sleep(300)
    OP_22(0x85, 0x1, 0x50)

    def lambda_6D30():

        label("loc_6D30")

        OP_7C(0xA, 0xA, 0xBB8, 0x12C)
        OP_48()
        Jump("loc_6D30")

    QueueWorkItem2(0x10F, 3, lambda_6D30)
    Sleep(300)
    OP_22(0x85, 0x1, 0x64)

    def lambda_6D55():

        label("loc_6D55")

        OP_7C(0x14, 0x14, 0xBB8, 0x12C)
        OP_48()
        Jump("loc_6D55")

    QueueWorkItem2(0x10F, 3, lambda_6D55)
    PlayEffect(0x4, 0x1, 0xFF, 0, 14500, 56500, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    OP_72(0x100B, 0x0)
    ExitThread()
    OP_B0(0xB, 0x32)
    OP_6F(0xB, 0)
    OP_70(0xB, 0x226)
    OP_73(0xB)
    OP_44(0x10F, 0x3)
    OP_23(0x85)

    def lambda_6DC7():
        OP_7C(0x28, 0x28, 0xBB8, 0x12C)
        ExitThread()

    QueueWorkItem(0x10F, 3, lambda_6DC7)
    OP_22(0x88, 0x0, 0x64)
    OP_6F(0xB, 550)
    OP_70(0xB, 0x258)
    WaitChrThread(0x109, 0x0)
    Sleep(500)
    SetChrPos(0x22, 4000, 500, 28500, 225)
    OP_82(0x6, 0x0)
    PlayEffect(0x0, 0x7, 0x22, 0, 900, 0, 0, 0, 0, 1600, 3300, 0, 0xFF, 0, 0, 0, 0)

    def lambda_6E45():

        label("loc_6E45")

        OP_99(0xFE, 0x0, 0x7, 0x3E8)
        OP_48()
        Jump("loc_6E45")

    QueueWorkItem2(0x22, 0, lambda_6E45)
    OP_23(0x146)
    SetChrChipByIndex(0x22, 19)
    SetChrSubChip(0x22, 0)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    SetChrFlags(0x0, 0x8)
    SetChrFlags(0x1, 0x8)
    SetChrFlags(0x2, 0x8)
    SetChrFlags(0x3, 0x8)
    SetChrFlags(0x4, 0x80)
    SetChrFlags(0x5, 0x80)
    SetChrFlags(0x6, 0x80)
    SetChrFlags(0x7, 0x80)
    SetChrFlags(0x4, 0x8)
    SetChrFlags(0x5, 0x8)
    SetChrFlags(0x6, 0x8)
    SetChrFlags(0x7, 0x8)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0x8, 0x8)
    SetChrFlags(0x9, 0x8)
    SetChrFlags(0xA, 0x8)
    SetChrFlags(0xB, 0x8)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0xC, 0x8)
    SetChrFlags(0xD, 0x8)
    SetChrFlags(0xE, 0x8)
    SetChrFlags(0xF, 0x8)
    ClearChrFlags(0x21, 0x80)
    ClearChrFlags(0x20, 0x80)
    ClearChrFlags(0x1D, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x19, 0x80)
    ClearChrFlags(0x1A, 0x80)
    ClearChrFlags(0x1B, 0x80)
    ClearChrFlags(0x1C, 0x80)
    ClearChrFlags(0x1E, 0x80)
    ClearChrFlags(0x1F, 0x80)
    SetChrPos(0x21, -390, 0, 22360, 0)
    SetChrPos(0x20, -1870, 0, 22010, 0)
    SetChrPos(0x1D, -360, 0, 25440, 0)
    SetChrPos(0x15, 60, 0, 24000, 0)
    SetChrPos(0x1F, -1230, 0, 23590, 0)
    SetChrPos(0x11, 2600, 0, 25000, 0)
    SetChrPos(0x12, 1240, 0, 23940, 0)
    SetChrPos(0x13, -4120, 0, 22470, 0)
    SetChrPos(0x14, 1050, 0, 22440, 0)
    SetChrPos(0x16, 1210, 0, 25280, 0)
    SetChrPos(0x18, -3430, 0, 24010, 0)
    SetChrPos(0x19, 2960, 0, 22470, 0)
    SetChrPos(0x1A, -2620, 0, 23250, 0)
    SetChrPos(0x1B, -2040, 0, 24850, 0)
    SetChrPos(0x1C, 2270, 0, 23590, 0)
    SetChrPos(0x1E, 3520, 0, 24000, 0)
    Sleep(1000)
    SetMessageWindowPos(150, 320, -1, -1)
    SetChrName("Estelle")

    AnonymousTalk(    #162
        "\x07\x00#1004FWow...\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(250, 320, -1, -1)
    SetChrName("Ries")

    AnonymousTalk(    #163
        "\x07\x00#1942FIf we walk through here, we can go home...\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(200, 320, -1, -1)
    SetChrName("Celeste")

    AnonymousTalk(    #164
        (
            "\x07\x0C#1616FI imagine you'll appear somewhere\x01",
            "near wherever it was you were when\x01",
            "you were first drawn in here.\x02\x03",

            "#1611FThose who were on airships will likely\x01",
            "reappear somewhere inside them.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(220, 320, -1, -1)
    SetChrName("Kevin")

    AnonymousTalk(    #165
        "\x07\x00#1840FOkay...\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(300)
    Fade(1000)
    OP_6D(1000, 0, 26200, 0)
    OP_67(0, 5560, -10000, 0)
    OP_6B(3140, 0)
    OP_6C(45000, 0)
    OP_6E(329, 0)
    OP_0D()
    Sleep(1000)

    ChrTalk(    #166
        0x1D,
        "#1025F#5PI guess this is it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #167
        0x16,
        "#1169F#11PIndeed...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #168
        0x11,
        "#065F#12PWh-What? Already?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #169
        0x1A,
        (
            "#813F#6PWe've been in here so long together,\x01",
            "my brain's having trouble processing\x01",
            "that it's actually about to end...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #170
        0x18,
        (
            "#1540F#6PI was hoping we would have time for one\x01",
            "final feast before we went our separate\x01",
            "ways...\x02\x03",

            "#1545F...but I suppose there are few partings in\x01",
            "this world that would allow us the good\x01",
            "fortune.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #171
        0x1B,
        "#1534F#5PHaha... You're probably right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #172
        0x1F,
        "#1307F#6P...\x02",
    )

    CloseMessageWindow()
    Sleep(150)

    def lambda_7406():
        OP_6D(3520, 0, 25400, 3000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_7406)

    def lambda_741E():
        OP_67(0, 5560, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_741E)

    def lambda_7436():
        OP_6B(3140, 3000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_7436)

    def lambda_7446():
        OP_6C(48000, 3000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_7446)

    def lambda_7456():
        OP_6E(329, 3000)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_7456)
    OP_62(0x19, 0x0, 2300, 0x18, 0x1B, 0xFA, 0x0)
    OP_62(0x1E, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(3000)
    OP_63(0x19)
    OP_63(0x1E)
    WaitChrThread(0x109, 0x0)
    Sleep(500)
    OP_20(0x7D0)

    def lambda_74A4():
        OP_8C(0xFE, 270, 300)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_74A4)
    Sleep(300)
    OP_8C(0x19, 270, 300)
    Sleep(500)

    ChrTalk(    #173
        0x19,
        "#070F#11PWell, then...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #174
        0x1E,
        "#119F#5P...allow us to be the first to take the plunge.\x02",
    )

    CloseMessageWindow()
    OP_62(0x21, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x20, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x15, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x11, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x13, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x14, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x12, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x1D, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x1F, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x1A, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x1B, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x16, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x18, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x1C, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_7672():

        label("loc_7672")

        TurnDirection(0xFE, 0x19, 400)
        OP_48()
        Jump("loc_7672")

    QueueWorkItem2(0x21, 3, lambda_7672)

    def lambda_7683():

        label("loc_7683")

        TurnDirection(0xFE, 0x1E, 400)
        OP_48()
        Jump("loc_7683")

    QueueWorkItem2(0x20, 3, lambda_7683)

    def lambda_7694():

        label("loc_7694")

        TurnDirection(0xFE, 0x1E, 400)
        OP_48()
        Jump("loc_7694")

    QueueWorkItem2(0x1D, 3, lambda_7694)

    def lambda_76A5():

        label("loc_76A5")

        TurnDirection(0xFE, 0x1E, 400)
        OP_48()
        Jump("loc_76A5")

    QueueWorkItem2(0x15, 3, lambda_76A5)

    def lambda_76B6():

        label("loc_76B6")

        TurnDirection(0xFE, 0x1E, 400)
        OP_48()
        Jump("loc_76B6")

    QueueWorkItem2(0x1F, 3, lambda_76B6)

    def lambda_76C7():

        label("loc_76C7")

        TurnDirection(0xFE, 0x1E, 400)
        OP_48()
        Jump("loc_76C7")

    QueueWorkItem2(0x11, 3, lambda_76C7)

    def lambda_76D8():

        label("loc_76D8")

        TurnDirection(0xFE, 0x1E, 400)
        OP_48()
        Jump("loc_76D8")

    QueueWorkItem2(0x12, 3, lambda_76D8)

    def lambda_76E9():

        label("loc_76E9")

        TurnDirection(0xFE, 0x19, 400)
        OP_48()
        Jump("loc_76E9")

    QueueWorkItem2(0x13, 3, lambda_76E9)

    def lambda_76FA():

        label("loc_76FA")

        TurnDirection(0xFE, 0x19, 400)
        OP_48()
        Jump("loc_76FA")

    QueueWorkItem2(0x14, 3, lambda_76FA)

    def lambda_770B():

        label("loc_770B")

        TurnDirection(0xFE, 0x1E, 400)
        OP_48()
        Jump("loc_770B")

    QueueWorkItem2(0x16, 3, lambda_770B)

    def lambda_771C():

        label("loc_771C")

        TurnDirection(0xFE, 0x19, 400)
        OP_48()
        Jump("loc_771C")

    QueueWorkItem2(0x18, 3, lambda_771C)

    def lambda_772D():

        label("loc_772D")

        TurnDirection(0xFE, 0x1E, 400)
        OP_48()
        Jump("loc_772D")

    QueueWorkItem2(0x1A, 3, lambda_772D)

    def lambda_773E():

        label("loc_773E")

        TurnDirection(0xFE, 0x1E, 400)
        OP_48()
        Jump("loc_773E")

    QueueWorkItem2(0x1B, 3, lambda_773E)

    def lambda_774F():

        label("loc_774F")

        TurnDirection(0xFE, 0x1E, 400)
        OP_48()
        Jump("loc_774F")

    QueueWorkItem2(0x1C, 3, lambda_774F)

    def lambda_7760():

        label("loc_7760")

        TurnDirection(0xFE, 0x19, 400)
        OP_48()
        Jump("loc_7760")

    QueueWorkItem2(0x22, 3, lambda_7760)
    Sleep(300)

    ChrTalk(    #175
        0x1D,
        "#1004F#5PWhy...?\x02",
    )

    CloseMessageWindow()
    OP_21()
    OP_1D(0xB3)
    Sleep(500)

    def lambda_7794():
        OP_6D(600, 0, 28300, 4000)
        ExitThread()

    QueueWorkItem(0x23, 0, lambda_7794)

    def lambda_77AC():
        OP_67(0, 4900, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x23, 1, lambda_77AC)

    def lambda_77C4():
        OP_6B(3180, 4000)
        ExitThread()

    QueueWorkItem(0x23, 2, lambda_77C4)

    def lambda_77D4():
        OP_6C(33000, 4000)
        ExitThread()

    QueueWorkItem(0x23, 3, lambda_77D4)

    def lambda_77E4():
        OP_6E(329, 4000)
        ExitThread()

    QueueWorkItem(0x22, 1, lambda_77E4)
    OP_43(0x1E, 0x0, 0x1, 0x25)
    OP_43(0x19, 0x0, 0x1, 0x26)
    WaitChrThread(0x1E, 0x0)
    WaitChrThread(0x19, 0x0)
    OP_44(0x21, 0x3)
    OP_44(0x20, 0x3)
    OP_44(0x1D, 0x3)
    OP_44(0x15, 0x3)
    OP_44(0x1F, 0x3)
    OP_44(0x11, 0x3)
    OP_44(0x12, 0x3)
    OP_44(0x13, 0x3)
    OP_44(0x14, 0x3)
    OP_44(0x16, 0x3)
    OP_44(0x18, 0x3)
    OP_44(0x1A, 0x3)
    OP_44(0x1B, 0x3)
    OP_44(0x1C, 0x3)
    OP_44(0x22, 0x3)
    OP_8C(0x1A, 0, 0)
    WaitChrThread(0x23, 0x0)
    Sleep(500)

    ChrTalk(    #176
        0x19,
        (
            "#573F#5PAt this rate, we're gonna be here forever 'cause\x01",
            "no one wants to be the first to say bye and leave\x01",
            "everyone behind.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #177
        0x1E,
        (
            "#111F#5PWhat Zin said. So as the eldest members of the \x01",
            "group, we thought we should be the ones to take\x01",
            "the initiative, so to speak.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #178
        0x1D,
        "#1026F#12POh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #179
        0x21,
        (
            "#1075F#12P...Thanks.\x02\x03",

            "#1840FYou guys're all right, you know.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #180
        0x1E,
        (
            "#110F#5PHaha. Think nothing of it.\x02\x03",

            "#119FThis is nothing compared to the kindness\x01",
            "you've showed by welcoming me into your\x01",
            "numbers despite my past transgressions.\x02\x03",

            "#111FBecause of you, I was able to achieve something \x01",
            "truly important. You have my deepest thanks.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #181
        0x1A,
        "#1314F#6PYou're very welcome.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #182
        0x15,
        (
            "#1513F#6PJust know that you have ours, too. I don't know\x01",
            "what we would've done without you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #183
        0x16,
        (
            "#1168F#4PWe may have to part for now, but I imagine your\x01",
            "work will bring us together again in the future.\x02\x03",

            "I can't wait to see you again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #184
        0x1E,
        (
            "#119F#5PI'm honored you would say so, Your Highness.\x02\x03",

            "#110FShould you ever require my services, please don't\x01",
            "hesitate to call on me. \x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #185
        0x19,
        (
            "#573F#5PAs for me...well, it was great getting to see you\x01",
            "all again.\x02\x03",

            "#070FDidn't ever picture us having a reunion like this,\x01",
            "but I'm sure glad it happened.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #186
        0x1B,
        "#1521F#6PHaha... You got that right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #187
        0x1C,
        (
            "#051F#12PI still wouldn't have turned down a few more\x01",
            "rounds of duking it out with you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #188
        0x19,
        (
            "#071F#5PSame here. Next time I get some free time,\x01",
            "I'll have to pop over to Liberl and rough you\x01",
            "up a bit.\x02\x03",

            "#070FOr, you know, you're all welcome to swing\x01",
            "by Calvard if you want.\x02\x03",

            "Kilika and I would welcome you with open\x01",
            "arms.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #189
        0x1D,
        "#1017F#12PYou bet! Count on it!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #190
        0x18,
        (
            "#1541F#6PReally? Then I'll start making preparations for\x01",
            "my visit as soon as I leave here!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #191
        0x13,
        (
            "#274F#5PYou're not doing anything until you've finished\x01",
            "the mountain of homework that's waiting for you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #192
        0x21,
        (
            "#1840F#12PHah. I'm sure me and Ries'll eventually make\x01",
            "our way there once the work comes knockin'\x01",
            "on our door.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #193
        0x20,
        "#1946F#6PI hope that day comes soon.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #194
        0x19,
        "#071F#5PHaha. Same here!\x02",
    )

    CloseMessageWindow()
    Sleep(150)
    OP_8C(0x19, 270, 400)
    Sleep(300)

    ChrTalk(    #195
        0x19,
        (
            "#070F#11PWell, I think that's about everything. \x01",
            "Let's get going, Colonel.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x1E, 90, 400)
    Sleep(300)

    ChrTalk(    #196
        0x1E,
        (
            "#495F#6PHonestly... Now even you've started calling\x01",
            "me that?\x02\x03",

            "#110FAlthough, I suppose being referred to in that\x01",
            "way by all of you may not be so bad.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    OP_D2(0x7056C, 0x7056D, 0x0)
    OP_D2(0x70071, 0x70079, 0x1)
    OP_8C(0x19, 0, 400)
    OP_8C(0x1E, 0, 400)

    def lambda_8153():
        OP_6D(0, 11800, 52460, 5000)
        ExitThread()

    QueueWorkItem(0x23, 0, lambda_8153)

    def lambda_816B():
        OP_67(0, 2950, -10000, 5000)
        ExitThread()

    QueueWorkItem(0x23, 1, lambda_816B)

    def lambda_8183():
        OP_6B(2950, 5000)
        ExitThread()

    QueueWorkItem(0x23, 2, lambda_8183)

    def lambda_8193():
        OP_6C(0, 5000)
        ExitThread()

    QueueWorkItem(0x23, 3, lambda_8193)

    def lambda_81A3():
        OP_6E(308, 5000)
        ExitThread()

    QueueWorkItem(0x22, 1, lambda_81A3)

    def lambda_81B3():

        label("loc_81B3")

        TurnDirection(0xFE, 0x19, 400)
        OP_48()
        Jump("loc_81B3")

    QueueWorkItem2(0x22, 3, lambda_81B3)
    OP_43(0x1E, 0x0, 0x1, 0x23)
    OP_43(0x19, 0x0, 0x1, 0x24)
    WaitChrThread(0x1E, 0x0)
    WaitChrThread(0x19, 0x0)
    WaitChrThread(0x23, 0x0)
    Sleep(2000)
    SetMessageWindowPos(150, 320, -1, -1)
    SetChrName("Olivier")

    AnonymousTalk(    #197
        (
            "\x07\x00#1545FHaha... Perhaps we should be the next to leave,\x01",
            "then.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(250, 320, -1, -1)
    SetChrName("Estelle")

    AnonymousTalk(    #198
        "\x07\x00#1004F...You?\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(300)
    Fade(1000)
    OP_6D(-2780, 0, 25520, 0)
    OP_67(0, 5300, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(300000, 0)
    OP_6E(325, 0)

    def lambda_82B2():
        OP_6D(-1750, 0, 29080, 4000)
        ExitThread()

    QueueWorkItem(0x23, 0, lambda_82B2)

    def lambda_82CA():
        OP_67(0, 4700, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x23, 1, lambda_82CA)

    def lambda_82E2():
        OP_6B(2950, 4000)
        ExitThread()

    QueueWorkItem(0x23, 2, lambda_82E2)

    def lambda_82F2():
        OP_6C(323000, 4000)
        ExitThread()

    QueueWorkItem(0x23, 3, lambda_82F2)

    def lambda_8302():
        OP_6E(336, 4000)
        ExitThread()

    QueueWorkItem(0x22, 1, lambda_8302)
    OP_43(0x18, 0x0, 0x1, 0x21)
    OP_43(0x13, 0x0, 0x1, 0x22)
    SetChrPos(0x20, -1870, 0, 22400, 0)
    SetChrPos(0x1A, -2500, 0, 23800, 0)
    SetChrPos(0x1B, -1900, 0, 24900, 0)
    SetChrPos(0x1C, 2470, 0, 23800, 0)
    SetChrPos(0x1F, -1150, 0, 23650, 0)

    def lambda_8375():

        label("loc_8375")

        TurnDirection(0xFE, 0x13, 400)
        OP_48()
        Jump("loc_8375")

    QueueWorkItem2(0x21, 3, lambda_8375)

    def lambda_8386():

        label("loc_8386")

        TurnDirection(0xFE, 0x13, 400)
        OP_48()
        Jump("loc_8386")

    QueueWorkItem2(0x20, 3, lambda_8386)

    def lambda_8397():

        label("loc_8397")

        TurnDirection(0xFE, 0x18, 400)
        OP_48()
        Jump("loc_8397")

    QueueWorkItem2(0x1D, 3, lambda_8397)

    def lambda_83A8():

        label("loc_83A8")

        TurnDirection(0xFE, 0x18, 400)
        OP_48()
        Jump("loc_83A8")

    QueueWorkItem2(0x15, 3, lambda_83A8)

    def lambda_83B9():

        label("loc_83B9")

        TurnDirection(0xFE, 0x13, 400)
        OP_48()
        Jump("loc_83B9")

    QueueWorkItem2(0x1F, 3, lambda_83B9)

    def lambda_83CA():

        label("loc_83CA")

        TurnDirection(0xFE, 0x18, 400)
        OP_48()
        Jump("loc_83CA")

    QueueWorkItem2(0x11, 3, lambda_83CA)

    def lambda_83DB():

        label("loc_83DB")

        TurnDirection(0xFE, 0x18, 400)
        OP_48()
        Jump("loc_83DB")

    QueueWorkItem2(0x12, 3, lambda_83DB)

    def lambda_83EC():

        label("loc_83EC")

        TurnDirection(0xFE, 0x18, 400)
        OP_48()
        Jump("loc_83EC")

    QueueWorkItem2(0x14, 3, lambda_83EC)

    def lambda_83FD():

        label("loc_83FD")

        TurnDirection(0xFE, 0x18, 400)
        OP_48()
        Jump("loc_83FD")

    QueueWorkItem2(0x16, 3, lambda_83FD)

    def lambda_840E():

        label("loc_840E")

        TurnDirection(0xFE, 0x13, 400)
        OP_48()
        Jump("loc_840E")

    QueueWorkItem2(0x1A, 3, lambda_840E)

    def lambda_841F():

        label("loc_841F")

        TurnDirection(0xFE, 0x13, 400)
        OP_48()
        Jump("loc_841F")

    QueueWorkItem2(0x1B, 3, lambda_841F)

    def lambda_8430():

        label("loc_8430")

        TurnDirection(0xFE, 0x18, 400)
        OP_48()
        Jump("loc_8430")

    QueueWorkItem2(0x1C, 3, lambda_8430)

    def lambda_8441():

        label("loc_8441")

        TurnDirection(0xFE, 0x18, 400)
        OP_48()
        Jump("loc_8441")

    QueueWorkItem2(0x22, 3, lambda_8441)
    WaitChrThread(0x18, 0x0)
    WaitChrThread(0x13, 0x0)
    OP_44(0x21, 0x3)
    OP_44(0x20, 0x3)
    OP_44(0x1D, 0x3)
    OP_44(0x15, 0x3)
    OP_44(0x1F, 0x3)
    OP_44(0x11, 0x3)
    OP_44(0x12, 0x3)
    OP_44(0x14, 0x3)
    OP_44(0x16, 0x3)
    OP_44(0x1A, 0x3)
    OP_44(0x1B, 0x3)
    OP_44(0x1C, 0x3)
    WaitChrThread(0x23, 0x0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #199
        0x18,
        (
            "#1545F#11PI feel as though the longer I stay, the less I'll\x01",
            "want to leave at all. It would be best for me to\x01",
            "get this done and over with.\x02\x03",

            "#1540FSo, this is farewell for now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #200
        0x21,
        "#1840F#6PHeh... Yeah. For now.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #201
        0x15,
        (
            "#1514F#6PI was honestly expecting you to hang on\x01",
            "longer. I'm surprised.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #202
        0x18,
        (
            "#1547F#11POh, Joshua! You twist my arm, but the pain\x01",
            "only leaves me weak with pleasure.\x02\x03",

            "#1541FHow I crave whisking you up as my prince\x01",
            "and taking you back with me!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #203
        0x1D,
        "#1019F#6POver my dead body, creep.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #204
        0x14,
        (
            "#413F#6P*sigh* I don't think I'll ever be able to believe\x01",
            "this guy is actually royalty...\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x13, 135, 400)
    Sleep(300)

    ChrTalk(    #205
        0x13,
        "#270F#5P...Olivier.\x02",
    )

    CloseMessageWindow()
    OP_62(0x18, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x18)
    Sleep(500)

    ChrTalk(    #206
        0x18,
        (
            "#1544F#11PHaha...\x02\x03",

            "#1540FTruth be told, I honestly never thought I'd be\x01",
            "blessed with an opportunity like this.\x02\x03",

            "#1545FThe thought of it coming to an end is making\x01",
            "me uncharacteristically emotional. \x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #207
        0x1D,
        "#1026F#6PAww...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #208
        0x1B,
        "#1534F#6P...Haha. It's certainty a new side to you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #209
        0x18,
        (
            "#1541F#11PBefore I go, however...I do want you to give\x01",
            "some serious thought to what I said, Schera.\x02\x03",

            "While I do realize it was brazen of me to ask...\x02\x03",

            "#1540F...you wouldn't deny me the joy of believing\x01",
            "you may one day say yes, would you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #210
        0x1B,
        (
            "#1525F#6PI swear...you are unbelievable.\x02\x03",

            "#1536FAll right. I will. You'll have an answer someday.\x02\x03",

            "In the meantime, you better work hard at what\x01",
            "you need to do!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #211
        0x18,
        "#1541F#11PHeh. But of course.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #212
        0x1A,
        "#814F#6PU-Umm... What's this all about?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #213
        0x1D,
        "#1013F#6PI think we're missing something pretty big...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #214
        0x21,
        (
            "#1840F#6PYeah. Something interesting happened right\x01",
            "under our noses, didn't it?\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    OP_8C(0x13, 180, 400)
    Sleep(300)

    ChrTalk(    #215
        0x13,
        (
            "#278F#5PFor my part, I would like to thank you for all you\x01",
            "have done for me and this one here.\x02\x03",

            "#277FI feel as though this experience has allowed me\x01",
            "to improve my swordsmanship all the more.\x02\x03",

            "I am truly grateful.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #216
        0x1C,
        (
            "#051F#6PHeh. I'll have to make sure I don't let you get\x01",
            "too far ahead of me, or I'm gonna have a hell\x01",
            "of a time catchin' up again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #217
        0x12,
        (
            "#179F#6PThe same goes for you as well, of course.\x02\x03",

            "#171FI do hope we will have the opportunity to\x01",
            "meet again one day.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x13, 135, 400)
    Sleep(300)

    ChrTalk(    #218
        0x13,
        (
            "#275F#5P...As do I.\x02\x03",

            "#272FOne last warning: I fear the Empire has some\x01",
            "truly stormy times ahead of it.\x02\x03",

            "#270FI would advise against all nonessential travel\x01",
            "there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #219
        0x12,
        "#178F#6PThat's concerning...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #220
        0x16,
        "#1382F#6PPlease be careful, then, Major.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #221
        0x13,
        (
            "#278F#5PAs long as this idiot pulls his weight, we should\x01",
            "be able to avoid the worst-case scenario.\x02\x03",

            "#277FIf you'd all pray Aidios doesn't give up on him,\x01",
            "I'd appreciate it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #222
        0x1D,
        "#1016F#6PAhaha...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #223
        0x11,
        "#067F#6PHeehee...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #224
        0x21,
        (
            "#1066F#6PSure thing. Praying is kinda what we church\x01",
            "folk do.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #225
        0x20,
        (
            "#1937F#6PI can't think of a simpler and more enjoyable\x01",
            "request.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x18, 0x0, 2000, 0xE, 0xF, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #226
        0x18,
        "#1544F#11PHow tragic it is that you all trust me so little.\x02",
    )

    CloseMessageWindow()
    OP_8C(0x18, 270, 400)
    Sleep(300)
    OP_62(0x18, 0x0, 2000, 0xA, 0xB, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #227
        0x18,
        (
            "#1547F#6PBut they do say that people bully those they\x01",
            "love the most.\x02\x03",

            "You're no exception to that, are you, love? ㈱\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #228
        0x13,
        (
            "#278F#5P...Am I to take that as confirmation that you\x01",
            "would like to be dragged out of here by the \x01",
            "scruff of your neck?\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x18, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #229
        0x18,
        "#1544F#6PI'd rather walk, please.\x02",
    )

    CloseMessageWindow()
    OP_8C(0x18, 180, 400)
    OP_8C(0x13, 180, 400)
    Sleep(300)

    ChrTalk(    #230
        0x18,
        "#1541F#11PWell, then, everyone. Until our next meeting!\x02",
    )

    CloseMessageWindow()
    Sleep(150)
    OP_D2(0x270045, 0x27004A, 0x0)
    OP_D2(0x270444, 0x270446, 0x1)
    OP_8C(0x18, 0, 400)
    OP_8C(0x13, 0, 400)

    def lambda_9156():
        OP_6D(0, 11800, 52460, 5000)
        ExitThread()

    QueueWorkItem(0x23, 0, lambda_9156)

    def lambda_916E():
        OP_67(0, 2950, -10000, 5000)
        ExitThread()

    QueueWorkItem(0x23, 1, lambda_916E)

    def lambda_9186():
        OP_6B(2950, 5000)
        ExitThread()

    QueueWorkItem(0x23, 2, lambda_9186)

    def lambda_9196():
        OP_6C(0, 5000)
        ExitThread()

    QueueWorkItem(0x23, 3, lambda_9196)

    def lambda_91A6():
        OP_6E(308, 5000)
        ExitThread()

    QueueWorkItem(0x22, 1, lambda_91A6)
    OP_43(0x18, 0x0, 0x1, 0x1F)
    OP_43(0x13, 0x0, 0x1, 0x20)
    WaitChrThread(0x18, 0x0)
    WaitChrThread(0x13, 0x0)
    WaitChrThread(0x23, 0x0)
    Sleep(2000)
    SetMessageWindowPos(150, 320, -1, -1)
    SetChrName("Scherazard")

    AnonymousTalk(    #231
        (
            "\x07\x00#1534FHaha... He managed to keep pretending he was\x01",
            "fine until the very end.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(300)
    Fade(1000)
    OP_6D(-2780, 0, 25520, 0)
    OP_67(0, 5080, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(300000, 0)
    OP_6E(325, 0)

    def lambda_9290():
        OP_6D(-1300, 0, 29080, 4000)
        ExitThread()

    QueueWorkItem(0x23, 0, lambda_9290)

    def lambda_92A8():
        OP_67(0, 4700, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x23, 1, lambda_92A8)

    def lambda_92C0():
        OP_6B(2950, 4000)
        ExitThread()

    QueueWorkItem(0x23, 2, lambda_92C0)

    def lambda_92D0():
        OP_6C(323000, 4000)
        ExitThread()

    QueueWorkItem(0x23, 3, lambda_92D0)

    def lambda_92E0():
        OP_6E(336, 4000)
        ExitThread()

    QueueWorkItem(0x22, 1, lambda_92E0)
    OP_43(0x1B, 0x0, 0x1, 0x1D)
    OP_43(0x1A, 0x0, 0x1, 0x1E)
    SetChrPos(0x21, -390, 0, 22460, 0)
    SetChrPos(0x20, -1870, 0, 22450, 0)
    SetChrPos(0x1F, -1150, 0, 23800, 0)

    def lambda_9331():

        label("loc_9331")

        TurnDirection(0xFE, 0x1B, 400)
        OP_48()
        Jump("loc_9331")

    QueueWorkItem2(0x21, 3, lambda_9331)

    def lambda_9342():

        label("loc_9342")

        TurnDirection(0xFE, 0x1A, 400)
        OP_48()
        Jump("loc_9342")

    QueueWorkItem2(0x20, 3, lambda_9342)

    def lambda_9353():

        label("loc_9353")

        TurnDirection(0xFE, 0x1B, 400)
        OP_48()
        Jump("loc_9353")

    QueueWorkItem2(0x1D, 3, lambda_9353)

    def lambda_9364():

        label("loc_9364")

        TurnDirection(0xFE, 0x1B, 400)
        OP_48()
        Jump("loc_9364")

    QueueWorkItem2(0x15, 3, lambda_9364)

    def lambda_9375():

        label("loc_9375")

        TurnDirection(0xFE, 0x1A, 400)
        OP_48()
        Jump("loc_9375")

    QueueWorkItem2(0x1F, 3, lambda_9375)

    def lambda_9386():

        label("loc_9386")

        TurnDirection(0xFE, 0x1B, 400)
        OP_48()
        Jump("loc_9386")

    QueueWorkItem2(0x11, 3, lambda_9386)

    def lambda_9397():

        label("loc_9397")

        TurnDirection(0xFE, 0x1B, 400)
        OP_48()
        Jump("loc_9397")

    QueueWorkItem2(0x12, 3, lambda_9397)

    def lambda_93A8():

        label("loc_93A8")

        TurnDirection(0xFE, 0x1B, 400)
        OP_48()
        Jump("loc_93A8")

    QueueWorkItem2(0x14, 3, lambda_93A8)

    def lambda_93B9():

        label("loc_93B9")

        TurnDirection(0xFE, 0x1B, 400)
        OP_48()
        Jump("loc_93B9")

    QueueWorkItem2(0x16, 3, lambda_93B9)

    def lambda_93CA():

        label("loc_93CA")

        TurnDirection(0xFE, 0x1B, 400)
        OP_48()
        Jump("loc_93CA")

    QueueWorkItem2(0x1C, 3, lambda_93CA)

    def lambda_93DB():

        label("loc_93DB")

        TurnDirection(0xFE, 0x1B, 400)
        OP_48()
        Jump("loc_93DB")

    QueueWorkItem2(0x22, 3, lambda_93DB)
    WaitChrThread(0x1B, 0x0)
    WaitChrThread(0x1A, 0x0)
    OP_44(0x21, 0x3)
    OP_44(0x20, 0x3)
    OP_44(0x1D, 0x3)
    OP_44(0x15, 0x3)
    OP_44(0x1F, 0x3)
    OP_44(0x11, 0x3)
    OP_44(0x12, 0x3)
    OP_44(0x14, 0x3)
    OP_44(0x16, 0x3)
    OP_44(0x1C, 0x3)
    WaitChrThread(0x23, 0x0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #232
        0x1D,
        "#1025F#6PYou two are next, then...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #233
        0x1A,
        "#1314F#5PYeah... This is it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #234
        0x1B,
        (
            "#1526F#11PMost of the people here I could go and see\x01",
            "if I set my mind to it...\x02\x03",

            "#1520F...but as for you two, Estelle and Joshua--\x01",
            "take care on that journey of yours, okay?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #235
        0x1D,
        "#1016F#6P...No problem.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #236
        0x15,
        (
            "#1501F#6PWe'll be sure to keep writing to you as often as\x01",
            "we can.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #237
        0x1B,
        (
            "#1521F#11PHaha. There's no need to send too many of them!\x01",
            "It won't be easy for my replies to reach you.\x02\x03",

            "#1536FPlus, there seems to be a lot of maintenance work\x01",
            "going on with the orbal communications network\x01",
            "lately.\x02\x03",

            "If you reeeally need me, just get in touch with the\x01",
            "Grancel branch.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #238
        0x1D,
        "#1017F#6POkay! We will!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #239
        0x15,
        (
            "#1514F#6PYou can always get in touch with us if you\x01",
            "need us in the same way.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #240
        0x1A,
        (
            "#1316F#5P*sigh* It's gonna suck not to be able to see\x01",
            "you again for a while though, Estelle.\x02\x03",

            "But it's gonna especially suck not to be able\x01",
            "to see Renne or Tita...\x02\x03",

            "#812FAnd YOU, Ries!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #241
        0x20,
        "#1934F#6PM-Me?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #242
        0x1A,
        (
            "#816F#5PDuh! I was really happy to get to know you,\x01",
            "you know.\x02\x03",

            "#811FSo if you ever come to Liberl again for work\x01",
            "or whatever, come see me, okay?\x02\x03",

            "#1310FI'll give you the scoop on all my favorite ice\x01",
            "cream spots!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #243
        0x20,
        (
            "#1932F#6P...I'd be happy to accept that invitation.\x02\x03",

            "#1937FComing to Liberl is now my top priority after\x01",
            "leaving here.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x21, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1200)

    ChrTalk(    #244
        0x21,
        "#1068F#6PLet's not forget about work, now...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #245
        0x1A,
        "#1314F#5PHeehee...\x02",
    )

    CloseMessageWindow()
    OP_8C(0x1A, 135, 400)
    Sleep(300)

    ChrTalk(    #246
        0x1A,
        (
            "#811F#5PAt least you'll be easy enough to see again, Tita.\x01",
            "I should be able to pop over and mess with you any\x01",
            "time your scaaary boy toy's not hovering over you.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x11, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(    #247
        0x11,
        "#067F#6PE-Erm...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #248
        0x1C,
        "#555F#6PDon't you even think about it, kiddo.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #249
        0x1A,
        (
            "#819F#5PHeh. How serious I am is for me to know.\x02\x03",

            "#816FOkay! Just one more thing before I go...\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x1A, 180, 400)
    Sleep(300)

    ChrTalk(    #250
        0x1A,
        (
            "#1310F#5PSay, Renne?\x02\x03",

            "#811FDo you like Estelle and Joshua? Or don't you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #251
        0x1F,
        "#1308F#6PWha...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #252
        0x1A,
        (
            "#1314F#5PThat's what matters the most.\x02\x03",

            "I want you to keep that question in mind as\x01",
            "a favor for your big sis Anelace.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #253
        0x1F,
        "#1307F#6PWh-What do you mean...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #254
        0x1D,
        "#1025F#6PAnelace...\x02",
    )

    CloseMessageWindow()
    OP_62(0x1A, 0x0, 2000, 0xA, 0xB, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #255
        0x1A,
        (
            "#811F#5POh, and expect a bajillion hugs next time I see\x01",
            "you. I'm not gonna let you get away! ♪\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #256
        0x1B,
        (
            "#1534F#11P*sigh* All right, I think we've hung around\x01",
            "long enough.\x02\x03",

            "#1535FSee you later.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #257
        0x21,
        "#1078F#6PTake care, Schera!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #258
        0x16,
        "#1168F#6PThank you both for sticking with us.\x02",
    )

    CloseMessageWindow()
    Sleep(150)
    OP_D2(0x270031, 0x270036, 0x0)
    OP_D2(0x270091, 0x270095, 0x1)
    OP_8C(0x1B, 0, 400)
    OP_8C(0x1A, 0, 400)

    def lambda_9DA2():
        OP_6D(0, 11800, 52460, 5000)
        ExitThread()

    QueueWorkItem(0x23, 0, lambda_9DA2)

    def lambda_9DBA():
        OP_67(0, 2950, -10000, 5000)
        ExitThread()

    QueueWorkItem(0x23, 1, lambda_9DBA)

    def lambda_9DD2():
        OP_6B(2950, 5000)
        ExitThread()

    QueueWorkItem(0x23, 2, lambda_9DD2)

    def lambda_9DE2():
        OP_6C(0, 5000)
        ExitThread()

    QueueWorkItem(0x23, 3, lambda_9DE2)

    def lambda_9DF2():
        OP_6E(308, 5000)
        ExitThread()

    QueueWorkItem(0x22, 1, lambda_9DF2)
    OP_43(0x1B, 0x0, 0x1, 0x1B)
    OP_43(0x1A, 0x0, 0x1, 0x1C)
    WaitChrThread(0x1B, 0x0)
    WaitChrThread(0x1A, 0x0)
    WaitChrThread(0x23, 0x0)
    Sleep(2000)
    SetMessageWindowPos(300, 320, -1, -1)
    SetChrName("Agate")

    AnonymousTalk(    #259
        (
            "\x07\x00#051FOkay. Guess we might as well be the next\x01",
            "ones to step up.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(200, 320, -1, -1)
    SetChrName("Tita")

    AnonymousTalk(    #260
        "\x07\x00#560FY-Yeah...\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(300)
    Fade(1000)
    OP_6D(1740, 0, 25710, 0)
    OP_67(0, 5320, -10000, 0)
    OP_6B(3050, 0)
    OP_6C(48000, 0)
    OP_6E(304, 0)

    def lambda_9EEF():
        OP_6D(700, 0, 28000, 4000)
        ExitThread()

    QueueWorkItem(0x23, 0, lambda_9EEF)

    def lambda_9F07():
        OP_67(0, 4750, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x23, 1, lambda_9F07)

    def lambda_9F1F():
        OP_6B(2980, 4000)
        ExitThread()

    QueueWorkItem(0x23, 2, lambda_9F1F)

    def lambda_9F2F():
        OP_6C(36000, 4000)
        ExitThread()

    QueueWorkItem(0x23, 3, lambda_9F2F)

    def lambda_9F3F():
        OP_6E(315, 4000)
        ExitThread()

    QueueWorkItem(0x22, 1, lambda_9F3F)
    OP_43(0x1C, 0x0, 0x1, 0x19)
    OP_43(0x11, 0x0, 0x1, 0x1A)
    SetChrPos(0x15, -100, 0, 24000, 0)
    SetChrPos(0x1F, -1330, 0, 23850, 0)
    SetChrPos(0x21, -300, 0, 22460, 0)
    SetChrPos(0x20, -1900, 0, 22210, 0)

    def lambda_9FA1():

        label("loc_9FA1")

        TurnDirection(0xFE, 0x1C, 400)
        OP_48()
        Jump("loc_9FA1")

    QueueWorkItem2(0x21, 3, lambda_9FA1)

    def lambda_9FB2():

        label("loc_9FB2")

        TurnDirection(0xFE, 0x11, 400)
        OP_48()
        Jump("loc_9FB2")

    QueueWorkItem2(0x20, 3, lambda_9FB2)

    def lambda_9FC3():

        label("loc_9FC3")

        TurnDirection(0xFE, 0x1C, 400)
        OP_48()
        Jump("loc_9FC3")

    QueueWorkItem2(0x1D, 3, lambda_9FC3)

    def lambda_9FD4():

        label("loc_9FD4")

        TurnDirection(0xFE, 0x1C, 400)
        OP_48()
        Jump("loc_9FD4")

    QueueWorkItem2(0x15, 3, lambda_9FD4)

    def lambda_9FE5():

        label("loc_9FE5")

        TurnDirection(0xFE, 0x11, 400)
        OP_48()
        Jump("loc_9FE5")

    QueueWorkItem2(0x1F, 3, lambda_9FE5)

    def lambda_9FF6():

        label("loc_9FF6")

        TurnDirection(0xFE, 0x1C, 400)
        OP_48()
        Jump("loc_9FF6")

    QueueWorkItem2(0x12, 3, lambda_9FF6)

    def lambda_A007():

        label("loc_A007")

        TurnDirection(0xFE, 0x1C, 400)
        OP_48()
        Jump("loc_A007")

    QueueWorkItem2(0x14, 3, lambda_A007)

    def lambda_A018():

        label("loc_A018")

        TurnDirection(0xFE, 0x1C, 400)
        OP_48()
        Jump("loc_A018")

    QueueWorkItem2(0x16, 3, lambda_A018)

    def lambda_A029():

        label("loc_A029")

        TurnDirection(0xFE, 0x11, 400)
        OP_48()
        Jump("loc_A029")

    QueueWorkItem2(0x22, 3, lambda_A029)
    WaitChrThread(0x1C, 0x0)
    WaitChrThread(0x11, 0x0)
    OP_44(0x21, 0x3)
    OP_44(0x20, 0x3)
    OP_44(0x1D, 0x3)
    OP_44(0x15, 0x3)
    OP_44(0x1F, 0x3)
    OP_44(0x12, 0x3)
    OP_44(0x14, 0x3)
    OP_44(0x16, 0x3)
    OP_8C(0x1D, 0, 0)
    WaitChrThread(0x23, 0x0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #261
        0x1D,
        "#1025F#6PThis is it, huh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #262
        0x15,
        "#1501F#6PTime to say farewell.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #263
        0x11,
        (
            "#067F#5PHeehee. I'll miss you both so much!\x02\x03",

            "#560FYou, too, Renne...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #264
        0x1F,
        "#1307F#6PYou mean it, Tita...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #265
        0x11,
        (
            "#563F#5PI can't say anything thought provoking like\x01",
            "Anelace...\x02\x03",

            "...and I don't have the power to chase after\x01",
            "you like Estelle and Joshua...\x02\x03",

            "#066F...but I'll always be waiting.\x02\x03",

            "I'll always be waiting for the day you three\x01",
            "come back to Liberl together.\x02\x03",

            "#067FIt's okay to hope for that, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #266
        0x1F,
        (
            "#1300F#6P...\x02\x03",

            "#266FHmph! P-Please. You can do what you like.\x02\x03",

            "#262FAs long as it's not getting sloppy with finishing\x01",
            "your Orbal Gear. You better finish that!\x02\x03",

            "#1301FPater-Mater welcomes all challengers!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #267
        0x11,
        "#061F#5POkay! I will!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #268
        0x1D,
        "#1017F#6PHeehee...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #269
        0x15,
        "#1514F#6PAhaha...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #270
        0x1C,
        (
            "#551F#5PI swear... Kids sure are violent these days.\x02\x03",

            "#556FLike Schera said, you guys take care, yeah?\x02\x03",

            "Especially you, Estelle. You ain't a rookie now,\x01",
            "so make sure you start lookin' before you leap.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #271
        0x1D,
        (
            "#1007F#6PI know, I know. \x02\x03",

            "#1028FYou just try not to fight with Tita's mom every\x01",
            "other second, okay?\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x1C, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(    #272
        0x1C,
        (
            "#055F#5PH-Hey, I'm not the one pickin' fights! She's the\x01",
            "one who's always trying to make my life hell!\x02\x03",

            "#552FI'm already dreading going back and getting\x01",
            "blamed for Tita ending up here...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #273
        0x11,
        "#067F#5PA-Ahaha...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #274
        0x21,
        (
            "#1066F#12PHaha. Yeeeah... I'm sure she'll find some way\x01",
            "to pin all this on you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #275
        0x1C,
        (
            "#551F#5PYou're only laughing because you ain't gonna\x01",
            "be on the receivin' end of it...\x02\x03",

            "#050FOh, and one last thing. I've got somethin' to say\x01",
            "to you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #276
        0x21,
        "#1079F#12P...Me?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #277
        0x1C,
        (
            "#053F#5PThe first time I met you, I thought you were\x01",
            "some sketchy weirdo, but you showed some\x01",
            "real guts this time.\x02\x03",

            "#051FGood on you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #278
        0x21,
        "#1064F#12P*gawk*\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #279
        0x1C,
        "#052F#5PHuh? I say somethin' funny?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #280
        0x21,
        (
            "#1066F#12PN-No... I just never thought the day would\x01",
            "come when you'd praise me. Like, at all.\x02\x03",

            "What brought that on?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #281
        0x1C,
        (
            "#053F#5PHeh... No real reason.\x02\x03",

            "#051FJust my way of sayin' let's keep on truckin',\x01",
            "I guess.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #282
        0x21,
        "#1840F#12PWell...thanks, then.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #283
        0x20,
        "#1946F#6PHeehee...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #284
        0x1D,
        (
            "#1016F#6P*sigh* Why do conversations like these between\x01",
            "two guys always end up so awkward?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #285
        0x1C,
        "#551F#5PAww, cram it.\x02",
    )

    CloseMessageWindow()
    Sleep(150)
    OP_8C(0x1C, 270, 400)
    Sleep(300)

    ChrTalk(    #286
        0x1C,
        "#051F#11PAnyway...you ready, Tita?\x02",
    )

    CloseMessageWindow()
    OP_8C(0x11, 90, 400)
    Sleep(300)

    ChrTalk(    #287
        0x11,
        "#061F#6PYup!\x02",
    )

    CloseMessageWindow()
    Sleep(150)
    OP_D2(0x600AA, 0x600AF, 0x0)
    OP_D2(0x70061, 0x70069, 0x1)
    OP_8C(0x1C, 0, 400)
    OP_8C(0x11, 0, 400)

    def lambda_A973():
        OP_6D(0, 11800, 52460, 5000)
        ExitThread()

    QueueWorkItem(0x23, 0, lambda_A973)

    def lambda_A98B():
        OP_67(0, 2950, -10000, 5000)
        ExitThread()

    QueueWorkItem(0x23, 1, lambda_A98B)

    def lambda_A9A3():
        OP_6B(2950, 5000)
        ExitThread()

    QueueWorkItem(0x23, 2, lambda_A9A3)

    def lambda_A9B3():
        OP_6C(0, 5000)
        ExitThread()

    QueueWorkItem(0x23, 3, lambda_A9B3)

    def lambda_A9C3():
        OP_6E(308, 5000)
        ExitThread()

    QueueWorkItem(0x22, 1, lambda_A9C3)
    OP_43(0x1C, 0x0, 0x1, 0x17)
    OP_43(0x11, 0x0, 0x1, 0x18)
    WaitChrThread(0x1C, 0x0)
    WaitChrThread(0x11, 0x0)
    WaitChrThread(0x23, 0x0)
    Sleep(2000)
    SetMessageWindowPos(200, 320, -1, -1)
    SetChrName("Kloe")

    AnonymousTalk(    #288
        "\x07\x00#1382FI think that marks our turn, Julia.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(300, 320, -1, -1)
    SetChrName("Julia")

    AnonymousTalk(    #289
        "\x07\x00#179F...As you wish.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(300)
    Fade(1000)
    OP_6D(-1330, 0, 25880, 0)
    OP_67(0, 5320, -10000, 0)
    OP_6B(3050, 0)
    OP_6C(306000, 0)
    OP_6E(288, 0)

    def lambda_AAB1():
        OP_6D(-1750, 0, 29080, 4000)
        ExitThread()

    QueueWorkItem(0x23, 0, lambda_AAB1)

    def lambda_AAC9():
        OP_67(0, 4700, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x23, 1, lambda_AAC9)

    def lambda_AAE1():
        OP_6B(2950, 4000)
        ExitThread()

    QueueWorkItem(0x23, 2, lambda_AAE1)

    def lambda_AAF1():
        OP_6C(323000, 4000)
        ExitThread()

    QueueWorkItem(0x23, 3, lambda_AAF1)

    def lambda_AB01():
        OP_6E(336, 4000)
        ExitThread()

    QueueWorkItem(0x22, 1, lambda_AB01)
    OP_43(0x16, 0x0, 0x1, 0x15)
    OP_43(0x12, 0x0, 0x1, 0x16)
    OP_43(0x17, 0x0, 0x1, 0x14)
    OP_43(0x14, 0x0, 0x1, 0x13)
    SetChrPos(0x1F, -1100, 0, 23850, 0)
    SetChrPos(0x21, 550, 0, 22660, 0)
    SetChrPos(0x20, -1000, 0, 22600, 0)

    def lambda_AB60():

        label("loc_AB60")

        TurnDirection(0xFE, 0x16, 400)
        OP_48()
        Jump("loc_AB60")

    QueueWorkItem2(0x21, 3, lambda_AB60)

    def lambda_AB71():

        label("loc_AB71")

        TurnDirection(0xFE, 0x16, 400)
        OP_48()
        Jump("loc_AB71")

    QueueWorkItem2(0x20, 3, lambda_AB71)

    def lambda_AB82():

        label("loc_AB82")

        TurnDirection(0xFE, 0x16, 400)
        OP_48()
        Jump("loc_AB82")

    QueueWorkItem2(0x1D, 3, lambda_AB82)

    def lambda_AB93():

        label("loc_AB93")

        TurnDirection(0xFE, 0x16, 400)
        OP_48()
        Jump("loc_AB93")

    QueueWorkItem2(0x15, 3, lambda_AB93)

    def lambda_ABA4():

        label("loc_ABA4")

        TurnDirection(0xFE, 0x16, 400)
        OP_48()
        Jump("loc_ABA4")

    QueueWorkItem2(0x1F, 3, lambda_ABA4)

    def lambda_ABB5():

        label("loc_ABB5")

        TurnDirection(0xFE, 0x16, 400)
        OP_48()
        Jump("loc_ABB5")

    QueueWorkItem2(0x22, 3, lambda_ABB5)
    WaitChrThread(0x16, 0x0)
    WaitChrThread(0x12, 0x0)
    WaitChrThread(0x17, 0x0)
    WaitChrThread(0x14, 0x0)
    OP_44(0x21, 0x3)
    OP_44(0x20, 0x3)
    OP_44(0x1D, 0x3)
    OP_44(0x15, 0x3)
    OP_44(0x1F, 0x3)
    OP_44(0x14, 0x3)
    WaitChrThread(0x23, 0x0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #290
        0x15,
        "#1501F#6PKloe...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #291
        0x1D,
        "#1025F#6PI guess this is goodbye for now.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #292
        0x16,
        (
            "#1165F#5PI'm afraid so.\x02\x03",

            "#1168FThis was an opportunity that I never expected\x01",
            "to be blessed with. \x02\x03",

            "I owe Aidios my deepest thanks for being able\x01",
            "to see you two again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #293
        0x15,
        "#1513F#6P...Us, too.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #294
        0x1D,
        (
            "#1016F#6PI'll keep writing to you, Kloe!\x01",
            "Count on it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #295
        0x16,
        (
            "#1161F#5PI won't get my hopes up the next\x01",
            "letter will be any time soon.\x02\x03",

            "#1382FOh... Josette?\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x14, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(    #296
        0x14,
        "#213F#6PErm... Wh-What's up?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #297
        0x16,
        (
            "#1168F#5PI really enjoyed spending time with you.\x02\x03",

            "I'd love to have the opportunity to hang\x01",
            "out again one day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #298
        0x14,
        (
            "#414F#6PU-Umm...\x02\x03",

            "#211FSure! We'll make it happen!\x02\x03",

            "We have a few hobbies in common, so I bet\x01",
            "we could talk for hours and hours.\x02\x03",

            "#210FWork'll mean I have to go to Grancel a lot,\x01",
            "anyway, so I'm sure we'll get the chance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #299
        0x16,
        "#1161F#5PHeehee. I'll be looking forward to it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #300
        0x1D,
        "#1019F#6PGah...\x02",
    )

    CloseMessageWindow()
    OP_8C(0x14, 315, 400)
    Sleep(300)

    ChrTalk(    #301
        0x14,
        (
            "#210F#6PIf you're feeling jealous you've got, like, nothing in\x01",
            "common with her, maybe you should try taking up\x01",
            "baking and handcrafts.\x02\x03",

            "#211FCan't wait to see the efforts of someone with all\x01",
            "the creativity and dexterity of a drunk pom.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x1D, 135, 400)
    Sleep(300)

    ChrTalk(    #302
        0x1D,
        "#1007F#5P...I wish I could disagree, but you totally got me.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #303
        0x16,
        "#1165F#5PIt's okay, Estelle. No one's good at everything.\x02",
    )

    CloseMessageWindow()
    Sleep(300)

    def lambda_B10D():
        OP_6D(200, 0, 30900, 1500)
        ExitThread()

    QueueWorkItem(0x23, 0, lambda_B10D)

    def lambda_B125():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_B125)
    Sleep(200)
    SetChrFlags(0x12, 0x20)
    OP_8C(0x12, 90, 400)
    OP_8C(0x14, 0, 400)
    OP_8C(0x1D, 0, 400)
    WaitChrThread(0x23, 0x0)
    Sleep(300)

    ChrTalk(    #304
        0x16,
        "#1163F#5PUmm...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #305
        0x22,
        (
            "\x07\x0C#1616F#11PPlease, don't feel obliged to say anything\x01",
            "to me.\x02\x03",

            "#1610FI'm not your ancestor, but merely a sentient\x01",
            "replica of her.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #306
        0x16,
        (
            "#1382F#5PEven so...I still wish you could have had the\x01",
            "opportunity to meet with my grandmother.\x02\x03",

            "#1169FI'm nowhere near as capable or intelligent\x01",
            "as she is...and after meeting only me, I can\x01",
            "only imagine you must be so disappointed...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #307
        0x22,
        (
            "\x07\x0C#1616F#11PHeehee...\x02\x03",

            "#1611FIt's almost eerie how much you remind me\x01",
            "of myself in that regard.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x16, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #308
        0x16,
        "#1164F#5P...I do? How?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #309
        0x22,
        (
            "\x07\x0C#1610F#11PI imagine your grandmother must feel the same way.\x02\x03",

            "#1616FThere's nothing to be ashamed of if you don't know\x01",
            "which way you should go sometimes. Just follow your\x01",
            "heart, and it will never betray you.\x02\x03",

            "#1611FOne day, you'll be able to spread your wings wide and\x01",
            "fly. I'm sure of it.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #310
        0x16,
        (
            "#1382F#5PI certainly hope so.\x02\x03",

            "#1161FThank you for your words of encouragement.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x12, 180, 400)
    Sleep(300)

    ChrTalk(    #311
        0x12,
        "#179F#11PHaha... Well, I suppose we should be going.\x02",
    )

    CloseMessageWindow()

    def lambda_B54F():
        OP_6D(-1200, 0, 27900, 1500)
        ExitThread()

    QueueWorkItem(0x23, 0, lambda_B54F)
    Sleep(150)
    OP_8C(0x16, 180, 400)
    WaitChrThread(0x23, 0x0)
    Sleep(300)

    ChrTalk(    #312
        0x12,
        (
            "#170F#11P...Oh, before we do.\x02\x03",

            "After we return, Kevin, I imagine things will be\x01",
            "more than a little chaotic.\x02\x03",

            "#179FSo should we require the church's help again,\x01",
            "I expect you to be there for us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #313
        0x21,
        (
            "#1075F#6PSure thing.\x02\x03",

            "#1060FI'll be getting in touch with the Congregation for\x01",
            "the Sacraments after I get out of here to decide\x01",
            "what to do next.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #314
        0x16,
        (
            "#1168F#5PHeehee. Well, then, everyone...\x02\x03",

            "...take care of yourselves!\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #315
        0x12,
        "Sieg",
        "#311F#5PScree!\x02",
    )

    CloseMessageWindow()
    Sleep(150)
    OP_D2(0x270399, 0x27039D, 0x0)
    OP_D2(0x270445, 0x270447, 0x1)
    OP_43(0x17, 0x0, 0x1, 0x12)
    Sleep(1500)
    OP_8C(0x16, 0, 400)
    OP_8C(0x12, 0, 400)

    def lambda_B770():
        OP_6D(0, 12500, 52460, 5000)
        ExitThread()

    QueueWorkItem(0x23, 0, lambda_B770)

    def lambda_B788():
        OP_67(0, 2800, -10000, 5000)
        ExitThread()

    QueueWorkItem(0x23, 1, lambda_B788)

    def lambda_B7A0():
        OP_6B(3100, 5000)
        ExitThread()

    QueueWorkItem(0x23, 2, lambda_B7A0)

    def lambda_B7B0():
        OP_6C(0, 5000)
        ExitThread()

    QueueWorkItem(0x23, 3, lambda_B7B0)

    def lambda_B7C0():
        OP_6E(310, 5000)
        ExitThread()

    QueueWorkItem(0x22, 1, lambda_B7C0)
    OP_43(0x16, 0x0, 0x1, 0x10)
    OP_43(0x12, 0x0, 0x1, 0x11)
    WaitChrThread(0x16, 0x0)
    WaitChrThread(0x12, 0x0)
    WaitChrThread(0x17, 0x0)
    WaitChrThread(0x23, 0x0)
    Sleep(2000)
    SetMessageWindowPos(250, 320, -1, -1)
    SetChrName("Josette")

    AnonymousTalk(    #316
        "\x07\x00#210FWell...I'm up.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(300)
    Fade(1000)
    OP_6D(1740, 0, 25710, 0)
    OP_67(0, 5050, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(48000, 0)
    OP_6E(308, 0)

    def lambda_B874():
        OP_6D(900, 0, 27400, 4000)
        ExitThread()

    QueueWorkItem(0x23, 0, lambda_B874)

    def lambda_B88C():
        OP_67(0, 4800, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x23, 1, lambda_B88C)

    def lambda_B8A4():
        OP_6B(2900, 4000)
        ExitThread()

    QueueWorkItem(0x23, 2, lambda_B8A4)

    def lambda_B8B4():
        OP_6C(40000, 4000)
        ExitThread()

    QueueWorkItem(0x23, 3, lambda_B8B4)

    def lambda_B8C4():
        OP_6E(315, 4000)
        ExitThread()

    QueueWorkItem(0x22, 1, lambda_B8C4)
    OP_43(0x14, 0x0, 0x1, 0xF)
    SetChrPos(0x21, -390, 0, 22360, 0)
    SetChrPos(0x20, -1800, 0, 22300, 0)
    SetChrPos(0x1F, -1400, 0, 23800, 0)

    def lambda_B90E():

        label("loc_B90E")

        TurnDirection(0xFE, 0x14, 400)
        OP_48()
        Jump("loc_B90E")

    QueueWorkItem2(0x21, 3, lambda_B90E)

    def lambda_B91F():

        label("loc_B91F")

        TurnDirection(0xFE, 0x14, 400)
        OP_48()
        Jump("loc_B91F")

    QueueWorkItem2(0x20, 3, lambda_B91F)

    def lambda_B930():

        label("loc_B930")

        TurnDirection(0xFE, 0x14, 400)
        OP_48()
        Jump("loc_B930")

    QueueWorkItem2(0x1D, 3, lambda_B930)

    def lambda_B941():

        label("loc_B941")

        TurnDirection(0xFE, 0x14, 400)
        OP_48()
        Jump("loc_B941")

    QueueWorkItem2(0x15, 3, lambda_B941)

    def lambda_B952():

        label("loc_B952")

        TurnDirection(0xFE, 0x14, 400)
        OP_48()
        Jump("loc_B952")

    QueueWorkItem2(0x1F, 3, lambda_B952)

    def lambda_B963():

        label("loc_B963")

        TurnDirection(0xFE, 0x14, 400)
        OP_48()
        Jump("loc_B963")

    QueueWorkItem2(0x22, 3, lambda_B963)
    WaitChrThread(0x14, 0x0)
    OP_44(0x21, 0x3)
    OP_44(0x20, 0x3)
    OP_44(0x1D, 0x3)
    OP_44(0x15, 0x3)
    OP_44(0x1F, 0x3)
    OP_8C(0x20, 0, 0)
    OP_8C(0x1F, 0, 0)
    WaitChrThread(0x23, 0x0)
    Sleep(500)

    ChrTalk(    #317
        0x15,
        "#1501F#12PI'm glad we had this time together, Josette.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #318
        0x1D,
        "#1013F#6PUmm... I...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #319
        0x14,
        (
            "#413F#5PIf you're gonna try and force yourself to say\x01",
            "something all emotional and crap, save it.\x02\x03",

            "#210FI don't wanna hear it from you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #320
        0x1D,
        "#1005F#6POh, that's REEEAL SWELL.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #321
        0x14,
        (
            "#416F#5PIf it looked like you and Joshua were finally\x01",
            "breaking up, then I was gonna use this chance\x01",
            "to take him from you. If only I was so lucky.\x02\x03",

            "#415FActuallyyy...you wanna come through the gate\x01",
            "the same time as me, Joshua?\x02\x03",

            "Maybe we'll reappear in the same place if we do!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #322
        0x1D,
        "#1019F#6PI'm on to you, missy. Hands off.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #323
        0x15,
        (
            "#1514F#12PUmm... Do you guys really have to fight\x01",
            "this way right to the very end...?\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x1D, 180, 600)
    Sleep(400)

    ChrTalk(    #324
        0x1D,
        "#1005F#6P#3SYou stay out of this!\x02",
    )


    ChrTalk(    #325
        0x14,
        "#214F#5P#3SYou stay out of this!\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    OP_56(0x1)
    OP_59()
    CloseMessageWindow()
    Sleep(300)

    ChrTalk(    #326
        0x15,
        "#1512F#12P...Sorry.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #327
        0x21,
        "#1068F#12P(Damn, man...)\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #328
        0x20,
        "#1936F#6P(This is such a pathetic spectacle.)\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #329
        0x14,
        (
            "#416F#5PHmph. But you know something?\x02\x03",

            "#210FIt was fun being here with you, Estelle.\x01",
            "In a way.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x1D, 0, 400)
    Sleep(300)

    ChrTalk(    #330
        0x1D,
        (
            "#1007F#6PYeah... I could say that, too. In a way.\x02\x03",

            "#1006FDon't overdo it with that business of yours,\x01",
            "you hear?\x02\x03",

            "Your line of work's like ours--you're out of luck\x01",
            "if you work yourself sick.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #331
        0x14,
        (
            "#210FHeh. Right back at you.\x02\x03",

            "#211FBut you can go causing trouble for yourself all\x01",
            "you like. Just don't go getting hurt and causing\x01",
            "any for Joshua!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #332
        0x15,
        (
            "#1513F#12P*sigh*\x02\x03",

            "#1514F(I don't think I've ever met two people who hate\x01",
            "each other this much who are so similar...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #333
        0x14,
        (
            "#210F#5PAnyway, guess I should actually get going now.\x02\x03",

            "#415FI'll be sure to write, Joshua! \x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #334
        0x15,
        "#1501F#12PThanks. Can't wait to hear from you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #335
        0x14,
        (
            "#416F#5PSounds like you two are gonna have\x01",
            "your work cut out for you...\x02\x03",

            "#210FTake care, all right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #336
        0x21,
        "#1840F#12PHaha. Thanks.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #337
        0x20,
        (
            "#1937F#6PMay the Goddess' light shine upon you\x01",
            "and your ship.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #338
        0x14,
        (
            "#211F#5PCan't ask for better from a sister. Thanks!\x02\x03",

            "#210FAll right. Later!\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    OP_D2(0x2700A1, 0x2700A5, 0x0)
    OP_8C(0x14, 0, 400)

    def lambda_C137():
        OP_6D(0, 11800, 52460, 5000)
        ExitThread()

    QueueWorkItem(0x23, 0, lambda_C137)

    def lambda_C14F():
        OP_67(0, 2950, -10000, 5000)
        ExitThread()

    QueueWorkItem(0x23, 1, lambda_C14F)

    def lambda_C167():
        OP_6B(2950, 5000)
        ExitThread()

    QueueWorkItem(0x23, 2, lambda_C167)

    def lambda_C177():
        OP_6C(0, 5000)
        ExitThread()

    QueueWorkItem(0x23, 3, lambda_C177)

    def lambda_C187():
        OP_6E(308, 5000)
        ExitThread()

    QueueWorkItem(0x22, 1, lambda_C187)
    OP_43(0x14, 0x0, 0x1, 0xE)
    WaitChrThread(0x14, 0x0)
    WaitChrThread(0x23, 0x0)
    Sleep(2000)
    SetMessageWindowPos(150, 320, -1, -1)
    SetChrName("Renne")

    AnonymousTalk(    #339
        "\x07\x00#1307F#40W...\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(300)
    Call(1, 3)
    Return()

    # Function_6_45E2 end

    SaveToFile()

Try(main)

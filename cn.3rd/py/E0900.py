from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'E0900   ._SN',
        MapName             = 'Event',
        Location            = 'E0900.x',
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
            '',
            '',
            '',
            ''
        ],
    )

    BuildStringList(
        '@FileName',                            # 8
        '艾莉卡博士',                           # 9
        '希德中校',                             # 10
        '尤莉亚上尉',                           # 11
        '格斯塔夫维修长',                       # 12
        '安东尼',                               # 13
        '男工作员',                             # 14
        '男工作员',                             # 15
        '男工作员',                             # 16
        '王国军士兵',                           # 17
        '王国军士兵',                           # 18
        '工房船',                               # 19
        '工房船的影子',                         # 20
        '军用艇',                               # 21
        '军用艇的影子',                         # 22
        '港口',                                 # 23
        '海鸥',                                 # 24
        '海鸥',                                 # 25
        '海鸥',                                 # 26
        '',                                     # 27
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
        'ED6_DT27/CH03970 ._CH',             # 00
        'ED6_DT27/CH03590 ._CH',             # 01
        'ED6_DT07/CH01450 ._CH',             # 02
        'ED6_DT07/CH01740 ._CH',             # 03
        'ED6_DT07/CH02440 ._CH',             # 04
        'ED6_DT07/CH01700 ._CH',             # 05
        'ED6_DT07/CH01300 ._CH',             # 06
    )

    AddCharChipPat(
        'ED6_DT27/CH03970P._CP',             # 00
        'ED6_DT27/CH03590P._CP',             # 01
        'ED6_DT07/CH01450P._CP',             # 02
        'ED6_DT07/CH01740P._CP',             # 03
        'ED6_DT07/CH02440P._CP',             # 04
        'ED6_DT07/CH01700P._CP',             # 05
        'ED6_DT07/CH01300P._CP',             # 06
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
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
        Unknown3            = 1,
        ChipIndex           = 0x1,
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
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x1C1,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x1C1,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x1C1,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
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
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
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
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x1C4,
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
        NpcIndex            = 0x1C4,
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
        NpcIndex            = 0x1C4,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    ScpFunction(
        "Function_0_322",          # 00, 0
        "Function_1_338",          # 01, 1
        "Function_2_347",          # 02, 2
        "Function_3_4C4",          # 03, 3
        "Function_4_26A3",         # 04, 4
        "Function_5_271F",         # 05, 5
        "Function_6_278B",         # 06, 6
        "Function_7_27F7",         # 07, 7
        "Function_8_2863",         # 08, 8
        "Function_9_289B",         # 09, 9
        "Function_10_28B7",        # 0A, 10
        "Function_11_28F5",        # 0B, 11
        "Function_12_2911",        # 0C, 12
        "Function_13_2942",        # 0D, 13
        "Function_14_29B2",        # 0E, 14
        "Function_15_29E3",        # 0F, 15
        "Function_16_2A14",        # 10, 16
        "Function_17_2A4B",        # 11, 17
    )


    def Function_0_322(): pass

    label("Function_0_322")

    OP_A3(0x2504)
    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 3)
    Return()

    # Function_0_322 end

    def Function_1_338(): pass

    label("Function_1_338")

    OP_B1("E0900_1")
    OP_22(0x1C5, 0x0, 0x64)
    Return()

    # Function_1_338 end

    def Function_2_347(): pass

    label("Function_2_347")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_36C")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_4AE")

    label("loc_36C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_385")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_4AE")

    label("loc_385")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_39E")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_4AE")

    label("loc_39E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3B7")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_4AE")

    label("loc_3B7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3D0")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_4AE")

    label("loc_3D0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3E9")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_4AE")

    label("loc_3E9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_402")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_4AE")

    label("loc_402")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_41B")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_4AE")

    label("loc_41B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_434")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_4AE")

    label("loc_434")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_44D")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_4AE")

    label("loc_44D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_466")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_4AE")

    label("loc_466")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_47F")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_4AE")

    label("loc_47F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_498")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_4AE")

    label("loc_498")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4AE")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_4AE")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4C3")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_4AE")

    label("loc_4C3")

    Return()

    # Function_2_347 end

    def Function_3_4C4(): pass

    label("Function_3_4C4")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrFlags(0x109, 0x80)
    SetChrPos(0x1A, 11090, -5000, -10000, 0)
    OP_A1(0x1A, 0x0)
    OP_72(0x400, 0x0)
    ExitThread()
    OP_72(0x2000, 0x0)
    ExitThread()
    OP_6F(0x0, 0)
    OP_70(0x0, 0x0)
    SetChrPos(0x1B, 10200, -2990, -10000, 0)
    OP_A1(0x1B, 0x2)
    OP_72(0x402, 0x0)
    ExitThread()
    SetChrPos(0x1E, -2520, -2990, -15300, 45)
    OP_A1(0x1E, 0x1)
    OP_72(0x401, 0x0)
    ExitThread()
    SetChrPos(0x1C, -12550, -6000, -2000, 60)
    OP_A1(0x1C, 0x3)
    OP_72(0x403, 0x0)
    ExitThread()
    OP_48()
    LoadEffect(0x0, "map\\mp013_02.eff")
    LoadEffect(0x2, "map\\mpsibuk.eff")
    SetChrPos(0x1F, -62870, -2990, 3220, 90)
    SetChrPos(0x20, -62090, -2990, 1230, 90)
    SetChrPos(0x21, -63820, -2990, -1520, 90)
    ClearChrFlags(0x1F, 0x80)
    ClearChrFlags(0x20, 0x80)
    ClearChrFlags(0x21, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    SetChrBattleFlags(0x15, 0x20)
    SetChrBattleFlags(0x16, 0x20)
    SetChrBattleFlags(0x17, 0x20)
    OP_89(0x15, -2490, -2570, -13050, 270)
    OP_89(0x16, -1760, -2570, -16700, 135)
    OP_89(0x17, -4980, -2570, -17540, 225)
    OP_43(0x15, 0x0, 0x0, 0x10)
    OP_43(0x16, 0x0, 0x0, 0x11)
    OP_43(0x17, 0x0, 0x0, 0xD)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x19, 0x80)
    SetChrBattleFlags(0x18, 0x20)
    SetChrBattleFlags(0x19, 0x20)
    OP_89(0x18, -10840, 1400, -3490, 135)
    OP_89(0x19, -14570, 1240, -6700, 180)
    OP_51(0x18, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x19, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_43(0x18, 0x0, 0x0, 0xF)
    OP_43(0x19, 0x0, 0x0, 0xE)
    ClearChrFlags(0x13, 0x80)
    SetChrBattleFlags(0x13, 0x20)
    OP_89(0x13, 7930, 2200, -14760, 270)
    OP_51(0x13, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x11, 0x80)
    SetChrBattleFlags(0x11, 0x20)
    OP_89(0x11, 8080, 2200, -13650, 270)
    OP_51(0x11, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x14, 0x80)
    SetChrBattleFlags(0x14, 0x20)
    OP_89(0x14, 11000, 2200, -14810, 270)
    OP_51(0x14, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    LoadEffect(0x1, "map\\mp074_00.eff")
    PlayEffect(0x1, 0xFF, 0xFF, -53250, -2000, -4290, 0, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0xFF, -49720, -2000, -3290, 0, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0xFF, -46550, -2000, -3750, 0, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0xFF, -46190, -2000, -7060, 0, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0xFF, -41570, -2000, -5990, 0, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)
    OP_6D(-45730, -2990, -2480, 0)
    OP_67(0, 6420, -10000, 0)
    OP_6B(4270, 0)
    OP_6C(60000, 0)
    OP_6E(262, 0)
    OP_C5(0x0, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x1, "C_VIS540._CH")
    OP_C6(0x0, 0x3, -1, 500, 0)
    Sleep(4000)
    OP_C6(0x0, 0x3, 16777215, 1000, 0)
    Sleep(1000)
    OP_43(0x1F, 0x0, 0x0, 0x5)
    OP_43(0x20, 0x0, 0x0, 0x6)
    OP_43(0x21, 0x0, 0x0, 0x7)

    def lambda_8F7():
        OP_6D(8460, -2990, -12750, 8000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_8F7)

    def lambda_90F():
        OP_67(0, 10190, -10000, 8000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_90F)

    def lambda_927():
        OP_6B(5740, 8000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_927)

    def lambda_937():
        OP_6C(45000, 8000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_937)

    def lambda_947():
        OP_6E(328, 8000)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_947)
    FadeToBright(2000, 0)
    Sleep(1000)
    OP_22(0x163, 0x0, 0x64)
    Sleep(1000)
    WaitChrThread(0x109, 0x0)
    OP_C5(0x1, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x6E, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x1, "C_VIS541._CH")
    OP_C6(0x1, 0x3, -1, 500, 0)
    Sleep(4000)
    OP_C6(0x1, 0x3, 16777215, 1000, 0)
    Sleep(1000)
    Sleep(500)

    def lambda_9CD():
        OP_6D(10460, -2990, -11750, 4000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_9CD)

    def lambda_9E5():
        OP_6B(5200, 4000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_9E5)
    Sleep(3500)
    OP_1D(0xD2)
    Fade(1000)
    OP_44(0x109, 0x1)
    OP_44(0x109, 0x2)
    OP_6D(9500, 2200, -15500, 0)
    OP_67(0, 5600, -10000, 0)
    OP_6B(3300, 0)
    OP_6C(134000, 0)
    OP_6E(285, 0)
    OP_0D()
    Sleep(500)
    OP_43(0x1F, 0x3, 0x0, 0xC)
    OP_44(0x15, 0x0)
    OP_44(0x16, 0x0)
    OP_44(0x17, 0x0)
    OP_44(0x18, 0x0)
    OP_44(0x19, 0x0)
    OP_63(0x15)
    OP_63(0x16)
    OP_63(0x17)

    ChrTalk(    #0
        0x13,
        (
            "#690F#5P唉～已经是傍晚了呢。\x02\x03",

            "如果还是什么都没有的话，\x01",
            "今天就到此为止吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x11, 180, 400)
    Sleep(300)

    ChrTalk(    #1
        0x11,
        (
            "#700F#6P但是，维修长……\x02\x03",

            "根据艾莉卡博士的测定，\x01",
            "应该是在这周围没错吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x13,
        (
            "#691F#5P啊，小艾莉卡都这么说，\x01",
            "应该是没有什么问题了吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x13, 0, 400)
    Sleep(300)

    ChrTalk(    #3
        0x13,
        (
            "#690F#2P只不过，\x01",
            "你也是知道的，\x01",
            "瓦雷利亚湖的水非常深。\x02\x03",

            "如果『那个东西』\x01",
            "是非常小的物体的话，\x01",
            "要打捞出来可是很困难的吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x11,
        (
            "#703F#6P嗯……\x02\x03",

            "#700F从接收到的导力反应来看\x01",
            "可以推测出目标\x01",
            "应该不是很大的物体……\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x10, 0x80)
    SetChrBattleFlags(0x10, 0x20)
    OP_89(0x10, 10850, 2300, -10990, 180)
    OP_9F(0x10, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_51(0x10, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_22(0x6, 0x0, 0x64)
    Sleep(500)

    NpcTalk(    #5
        0x10,
        "女性的声音",
        (
            "#2P……呵呵。\x01",
            "谁知道呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x11, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x13, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_D24():
        OP_6D(10000, 2200, -15000, 2000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_D24)

    def lambda_D3C():
        OP_67(0, 5350, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_D3C)

    def lambda_D54():
        OP_6B(3000, 2000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_D54)

    def lambda_D64():
        OP_6C(122000, 2000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_D64)
    SetChrFlags(0x10, 0x4)
    OP_43(0x10, 0x0, 0x0, 0x8)

    def lambda_D80():

        label("loc_D80")

        TurnDirection(0xFE, 0x10, 400)
        OP_48()
        Jump("loc_D80")

    QueueWorkItem2(0x11, 0, lambda_D80)
    Sleep(100)

    def lambda_D96():

        label("loc_D96")

        TurnDirection(0xFE, 0x10, 400)
        OP_48()
        Jump("loc_D96")

    QueueWorkItem2(0x13, 0, lambda_D96)
    Sleep(300)
    OP_22(0x7, 0x0, 0x64)
    WaitChrThread(0x10, 0x0)
    ClearChrFlags(0x10, 0x4)
    OP_44(0x11, 0x0)
    OP_44(0x13, 0x0)
    OP_8C(0x11, 90, 0)
    OP_8C(0x13, 90, 0)
    WaitChrThread(0x109, 0x0)
    Sleep(300)

    ChrTalk(    #6
        0x11,
        "#702F#6P博士……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x13,
        (
            "#691F小艾莉卡。\x01",
            "探测已经完毕了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x10,
        (
            "#1458F#5P嗯，总算结束了。\x02\x03",

            "#1452F对了，大叔。\x01",
            "不要再叫我『小艾莉卡』啦。\x02\x03",

            "我都早已经结婚生子了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x13,
        (
            "#693F啊哈哈，就算你这么说，\x01",
            "但我从你小时候开始不就是一直这么称呼的吗？\x02\x03",

            "现在要改过来也难了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x10,
        "#1833F#5P真是……算了。\x02",
    )

    CloseMessageWindow()
    Sleep(400)

    ChrTalk(    #11
        0x10,
        (
            "#1450F#5P希德中校。\x01",
            "让你部下的人\x01",
            "暂时撤退一下可以吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x11,
        (
            "#702F#6P你的意思是……\x02\x03",

            "已经查明\x01",
            "正确的沉没地点了吗？\x02",
        )
    )

    Jump("loc_FCB")

    label("loc_FCB")

    CloseMessageWindow()

    ChrTalk(    #13
        0x10,
        (
            "#1458F#5P嗯，误差在１亚矩以内。\x02\x03",

            "#1450F但是，\x01",
            "从声纳的探测的结果来看，\x01",
            "并不是很大的物体。\x02\x03",

            "虽然只是推测，\x01",
            "但它的尺寸最多不会超过５０里矩。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x13,
        (
            "#690F真小啊……\x02\x03",

            "５０里矩的话\x01",
            "只有安东尼那么大啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x14,
        "#5P喵喵～？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x11,
        (
            "#703F#6P嗯……\x02\x03",

            "#700F如果是『古代遗物』的话，\x01",
            "事情就变得很麻烦了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x10,
        (
            "#1457F#5P嗯，虽然有点不甘心，\x01",
            "但也只好惊动教会那些人了。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(400)

    ChrTalk(    #18
        0x10,
        (
            "#1832F#5P只要牵扯到『古代遗物』，\x01",
            "他们就摆出一付据为己有的模样……\x02\x03",

            "啊～～够啦！\x01",
            "真气人！\x02",
        )
    )

    Jump("loc_11E9")

    label("loc_11E9")

    CloseMessageWindow()
    OP_62(0x13, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(    #19
        0x13,
        "#692F哎呀呀，你冷静一点。\x02",
    )

    CloseMessageWindow()
    OP_8C(0x11, 180, 400)
    Sleep(300)

    ChrTalk(    #20
        0x11,
        (
            "#701F#6P那么，\x01",
            "我先让部下们撤退回去。\x02\x03",

            "维修长，那就拜托你了。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x13, 0, 400)
    Sleep(300)

    ChrTalk(    #21
        0x13,
        (
            "#691F#2P好的。\x02\x03",

            "好吧……\x01",
            "看看会出现什么鬼东西。\x02",
        )
    )

    Jump("loc_12DE")

    label("loc_12DE")

    CloseMessageWindow()
    Sleep(300)

    def lambda_12EA():
        OP_6B(3500, 3000)
        ExitThread()

    QueueWorkItem(0x13, 0, lambda_12EA)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_44(0x13, 0x0)
    Sleep(4000)
    OP_71(0x401, 0x0)
    ExitThread()
    OP_82(0x1, 0x0)
    OP_89(0x15, 7950, 2200, -11030, 270)
    OP_89(0x16, 8500, 2200, -12100, 270)
    OP_89(0x17, 7890, 2200, -9900, 270)
    SetChrSubChip(0x15, 0)
    SetChrSubChip(0x16, 0)
    SetChrSubChip(0x17, 0)
    OP_89(0x18, -10840, 1400, -3490, 135)
    OP_89(0x19, -12660, 1320, -5080, 180)
    SetChrSubChip(0x18, 0)
    SetChrSubChip(0x19, 0)
    OP_89(0x14, 12090, 2200, -12550, 270)
    OP_89(0x13, 13600, 2200, -17480, 270)
    OP_89(0x11, 9230, 2200, -13420, 225)
    OP_89(0x10, 9620, 2200, -14490, 225)
    OP_6D(10980, 2200, -15210, 0)
    OP_67(0, 5200, -10000, 0)
    OP_6B(2780, 0)
    OP_6C(101000, 0)
    OP_6E(346, 0)
    FadeToBright(1000, 0)
    OP_0D()

    def lambda_1410():
        OP_6D(7610, 2200, -16930, 3000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_1410)

    def lambda_1428():
        OP_67(0, 5260, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_1428)

    def lambda_1440():
        OP_6B(3010, 3000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_1440)

    def lambda_1450():
        OP_6C(101000, 3000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_1450)

    def lambda_1460():
        OP_6E(399, 3000)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_1460)
    OP_22(0x133, 0x0, 0x64)
    OP_B0(0x0, 0xA)
    OP_6F(0x0, 0)
    OP_70(0x0, 0x1E)
    OP_73(0x0)
    Sleep(1000)

    def lambda_148F():
        OP_6D(6860, 660, -18490, 3000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_148F)

    def lambda_14A7():
        OP_67(0, 5260, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_14A7)

    def lambda_14BF():
        OP_6B(3230, 3000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_14BF)

    def lambda_14CF():
        OP_6C(101000, 3000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_14CF)

    def lambda_14DF():
        OP_6E(413, 3000)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_14DF)
    OP_22(0x133, 0x0, 0x64)
    OP_B0(0x0, 0x19)
    OP_6F(0x0, 31)
    OP_70(0x0, 0x78)
    OP_73(0x0)
    WaitChrThread(0x109, 0x0)
    Sleep(500)

    ChrTalk(    #22
        0x10,
        (
            "#1452F#6P嗯……\x01",
            "这个位置应该没错了。\x02\x03",

            "#1455F大叔，开始吧！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x13,
        (
            "#690F#6P好！\x01",
            "打捞开始了。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1587():
        OP_6D(1860, 410, -18210, 3000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_1587)

    def lambda_159F():
        OP_67(0, 5400, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_159F)

    def lambda_15B7():
        OP_6B(2950, 3000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_15B7)

    def lambda_15C7():
        OP_6C(125000, 3000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_15C7)

    def lambda_15D7():
        OP_6E(399, 3000)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_15D7)
    OP_22(0x110, 0x1, 0x3C)
    OP_B0(0x0, 0x14)
    OP_6F(0x0, 121)
    OP_70(0x0, 0xE6)
    Sleep(300)
    OP_8C(0x10, 270, 400)
    Sleep(100)
    OP_8C(0x11, 270, 400)
    Sleep(1000)
    OP_22(0xE4, 0x0, 0x50)
    OP_22(0xDC, 0x0, 0x64)
    PlayEffect(0x2, 0x1, 0xFF, 2000, -2500, -19500, 0, 0, 0, 600, 600, 600, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0x0, 0xFF, 2120, -2990, -19430, 0, 0, 0, 1300, 1300, 900, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    OP_82(0x1, 0x2)
    OP_73(0x0)
    PlayEffect(0x0, 0x2, 0xFF, 2120, -2990, -19430, 0, 0, 0, 500, 500, 300, 0xFF, 0, 0, 0, 0)
    OP_82(0x0, 0x2)
    OP_71(0x2000, 0x0)
    ExitThread()
    OP_6F(0x0, 221)
    OP_70(0x0, 0xE6)
    Sleep(2000)
    Fade(500)
    OP_6D(10540, 2200, -15410, 0)
    OP_67(0, 5400, -10000, 0)
    OP_6B(2120, 0)
    OP_6C(125000, 0)
    OP_6E(399, 0)
    OP_0D()
    Sleep(500)
    OP_62(0x10, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_63(0x10)
    Sleep(500)

    ChrTalk(    #24
        0x10,
        "#1453F#5P……真是讨厌的声音呢。\x02",
    )

    CloseMessageWindow()
    OP_62(0x11, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)
    OP_8C(0x11, 180, 400)
    Sleep(300)

    ChrTalk(    #25
        0x11,
        (
            "#702F#6P怎么，\x01",
            "吊车的状况有异常吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x10,
        "#1833F#5P我不是这个意思。\x02",
    )

    CloseMessageWindow()
    Sleep(400)

    ChrTalk(    #27
        0x10,
        (
            "#1457F#5P『古代遗物』这东西，\x01",
            "我实在是没有好感啊。\x02\x03",

            "我们完全不能解释的，\x01",
            "拥有无法忽视的巨大力量的东西\x01",
            "确实存在于世上。\x02\x03",

            "这对研究者而言\x01",
            "真是最大的气愤与无奈。\x02\x03",

            "#1452F而且，就算知道没用，\x01",
            "也还是忍不住对它感兴趣。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x11,
        (
            "#703F#6P原来如此……\x01",
            "你的心情我多少还是了解的。\x02\x03",

            "#700F从那件事以来已经过了半年——\x02\x03",

            "虽然已经恢复了和平，\x01",
            "但是我们还远远没有\x01",
            "认清那个事件到底意味着什么。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x10,
        (
            "#1453F#5P……是啊。\x02\x03",

            "#1457F唉，毕竟当时\x01",
            "我并没有亲自到达现场。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    OP_72(0x2000, 0x0)
    ExitThread()
    OP_6F(0x0, 230)
    OP_70(0x0, 0xE6)
    PlayEffect(0x0, 0x0, 0xFF, 2120, -2990, -19430, 0, 0, 0, 1000, 1000, 600, 0xFF, 0, 0, 0, 0)
    OP_7C(0x0, 0x64, 0xBB8, 0x64)
    OP_23(0x110)
    OP_22(0xC8, 0x0, 0x50)
    Sleep(500)
    OP_82(0x0, 0x2)
    OP_62(0x10, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(100)
    OP_62(0x11, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_8C(0x11, 270, 400)
    Sleep(300)

    ChrTalk(    #30
        0x13,
        (
            "#690F吊车臂已经到达湖底。\x02\x03",

            "要开始捕捉了。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(500)
    OP_6D(4520, 1070, -15920, 0)
    OP_67(0, 5350, -10000, 0)
    OP_6B(2840, 0)
    OP_6C(125000, 0)
    OP_6E(434, 0)

    def lambda_1B31():
        OP_8E(0xFE, 0x1ED2, 0x898, 0xFFFFC6EE, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_1B31)
    Sleep(300)

    def lambda_1B51():
        OP_8E(0xFE, 0x1EFA, 0x898, 0xFFFFCB6C, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_1B51)
    Sleep(500)
    OP_0D()
    Sleep(500)
    OP_22(0x110, 0x1, 0x3C)
    OP_71(0x2000, 0x0)
    ExitThread()
    OP_6F(0x0, 221)
    OP_70(0x0, 0xE6)
    Sleep(1500)
    PlayEffect(0x0, 0x0, 0xFF, 2120, -2990, -19430, 0, 0, 0, 1000, 1000, 600, 0xFF, 0, 0, 0, 0)
    OP_7C(0x0, 0x64, 0xBB8, 0x64)
    OP_23(0x110)
    OP_22(0xC8, 0x0, 0x50)
    OP_6F(0x0, 230)
    OP_70(0x0, 0xE6)
    Sleep(500)
    OP_82(0x0, 0x2)
    Sleep(1000)

    ChrTalk(    #31
        0x13,
        (
            "#690F#6P没有对准。\x02\x03",

            "微微向右调整３０里矩。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    OP_82(0x2, 0x2)
    OP_22(0x133, 0x0, 0x64)
    OP_B0(0x0, 0xA)
    OP_72(0x2000, 0x0)
    ExitThread()
    OP_6F(0x0, 231)
    OP_70(0x0, 0x104)
    OP_73(0x0)
    PlayEffect(0x0, 0x2, 0xFF, 1970, -2990, -17900, 0, 0, 0, 500, 500, 300, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    OP_22(0x110, 0x1, 0x3C)
    OP_71(0x2000, 0x0)
    ExitThread()
    OP_6F(0x0, 261)
    OP_70(0x0, 0x10E)
    Sleep(1500)
    PlayEffect(0x0, 0x0, 0xFF, 1970, -2990, -17900, 0, 0, 0, 1000, 1000, 600, 0xFF, 0, 0, 0, 0)
    OP_7C(0x0, 0x64, 0xBB8, 0x64)
    OP_23(0x110)
    OP_22(0xC8, 0x0, 0x50)
    OP_6F(0x0, 270)
    OP_70(0x0, 0x10E)
    Sleep(1000)
    OP_82(0x0, 0x2)
    Sleep(500)
    OP_22(0x9C, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #32
        0x10,
        "#1458F#6P呵呵，正好对上。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x13,
        (
            "#691F#6P嗯，捕捉成功啦。\x02\x03",

            "要往上提升吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x10,
        "#1456F#6P是，拜托你了。\x02",
    )

    CloseMessageWindow()
    OP_20(0x1388)
    OP_22(0x110, 0x1, 0x3C)
    OP_71(0x2000, 0x0)
    ExitThread()
    OP_6F(0x0, 261)
    OP_70(0x0, 0x10E)

    ChrTalk(    #35
        0x11,
        "#701F#6P要露出真面目了吗……\x02",
    )

    CloseMessageWindow()

    def lambda_1DFC():
        OP_6B(2600, 8000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_1DFC)

    def lambda_1E0C():
        OP_6D(2520, 1070, -15920, 8000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_1E0C)
    Sleep(8000)

    ChrTalk(    #36
        0x13,
        "#690F#6P……出来了！\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(1000)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearMapFlags(0x10)
    OP_E5(0x0, 0x0, 0x1, 262144)
    OP_E5(0x2, 0x0, 0x1, 200)
    OP_6D(2300, -2590, -14920, 0)
    OP_67(0, 3250, -10000, 0)
    OP_6B(2170, 0)
    OP_6C(20000, 0)
    OP_6E(413, 0)
    OP_72(0x2000, 0x0)
    ExitThread()
    OP_B0(0x0, 0x19)
    OP_6F(0x0, 261)
    OP_70(0x0, 0x14D)

    def lambda_1EC7():
        OP_6D(7780, -4590, -16040, 6000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_1EC7)

    def lambda_1EDF():
        OP_67(0, 7230, -10000, 6000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_1EDF)

    def lambda_1EF7():
        OP_6B(2009, 6000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_1EF7)

    def lambda_1F07():
        OP_6E(414, 6000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_1F07)

    def lambda_1F17():
        OP_6C(71000, 6000)
        ExitThread()

    QueueWorkItem(0x10, 3, lambda_1F17)
    LoadEffect(0x4, "map\\mp256_01.eff")
    Play3DEffect(0x4, 0x4, 0x0, "FNul15_siten5_15", 0xFFFFFF9C, 0xFFFFFABA, 0xFFFFFF38, 0x0, 0x0, 0x0, 0x3E8, 0x3E8, 0x3E8, 0x0)
    OP_0D()
    OP_22(0xE3, 0x0, 0x64)
    OP_73(0x0)
    OP_22(0xDC, 0x0, 0x64)
    PlayEffect(0x2, 0x1, 0xFF, 2200, -2200, -18500, 0, 0, 0, 700, 700, 700, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0x0, 0xFF, 1970, -2990, -17900, 0, 0, 0, 1500, 1500, 900, 0xFF, 0, 0, 0, 0)
    OP_B0(0x0, 0x8)
    OP_6F(0x0, 333)
    OP_70(0x0, 0x168)
    OP_22(0x146, 0x1, 0x50)
    Sleep(1500)
    OP_82(0x1, 0x2)
    OP_82(0x0, 0x0)
    OP_82(0x2, 0x2)
    OP_73(0x0)
    OP_44(0x109, 0x3)
    WaitChrThread(0x109, 0x0)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_7C(0x0, 0x64, 0xBB8, 0x64)
    OP_23(0x110)
    OP_22(0xC8, 0x0, 0x50)
    Sleep(1500)

    ChrTalk(    #37
        0x10,
        "#1454F#4P什……！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x11,
        "#702F#3P这、这个是……\x02",
    )

    CloseMessageWindow()

    def lambda_2084():
        OP_6B(1700, 6000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_2084)
    Sleep(1000)
    FadeToDark(3000, 0, -1)
    OP_0D()
    OP_43(0x11, 0x0, 0x0, 0x4)
    WaitChrThread(0x11, 0x0)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapFlags(0x10)
    OP_A2(0x2507)
    NewScene("ED6_DT21/T4144   ._SN", 100, 0, 0)
    IdleLoop()
    WaitChrThread(0x109, 0x0)
    Sleep(1000)

    def lambda_20D4():
        OP_6D(8490, 2400, -17400, 4000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_20D4)

    def lambda_20EC():
        OP_67(0, 4380, -10000, 5000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_20EC)

    def lambda_2104():
        OP_6B(2190, 5000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_2104)

    def lambda_2114():
        OP_6C(129000, 5000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_2114)

    def lambda_2124():
        OP_6E(428, 5000)
        ExitThread()

    QueueWorkItem(0x10, 3, lambda_2124)
    OP_B0(0x0, 0x14)
    OP_6F(0x0, 104)
    OP_70(0x0, 0xA4)
    OP_22(0x133, 0x0, 0x64)
    Sleep(1000)
    OP_43(0x12, 0x0, 0x0, 0x9)
    Sleep(1000)
    OP_43(0x10, 0x0, 0x0, 0x8)
    ClearChrFlags(0x16, 0x1)
    WaitChrThread(0x16, 0x0)
    WaitChrThread(0x12, 0x0)
    WaitChrThread(0x10, 0x0)
    OP_73(0x0)
    Sleep(500)
    OP_22(0x133, 0x0, 0x64)
    OP_B0(0x0, 0x8)
    OP_6F(0x0, 165)
    OP_70(0x0, 0xC3)
    OP_73(0x0)
    Sleep(200)

    def lambda_219E():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x15, 0, lambda_219E)
    WaitChrThread(0x109, 0x0)
    WaitChrThread(0x109, 0x1)
    Sleep(300)

    ChrTalk(    #39
        0x12,
        "#170F#5P可以看到目标物体吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0x16,
        (
            "#4P是，是的，\x01",
            "在篮子里面有物体的影子……\x02\x03",

            "马、马上进行确认！\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_8E(0x16, 0x1EE6, 0x898, 0xFFFFBFAA, 0xBB8, 0x0)
    OP_8C(0x16, 270, 400)
    Sleep(300)

    ChrTalk(    #41
        0x10,
        (
            "#1450F#5P小心！\x02\x03",

            "在我没有同意之前\x01",
            "谁都不许直接碰那物体！\x02",
        )
    )

    CloseMessageWindow()
    LoadEffect(0x2, "monster\\ms31003a.eff")
    OP_43(0x109, 0x0, 0x0, 0xA)
    Sleep(200)
    OP_62(0x12, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x15, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x16, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(200)

    ChrTalk(    #42 op#A op#5
        0x16,
        "#5P#20A哇！？\x05\x02",
    )


    def lambda_2318():
        OP_8C(0xFE, 180, 600)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_2318)

    def lambda_2326():
        OP_8F(0xFE, 0x1F22, 0x898, 0xFFFFC23E, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 0, lambda_2326)
    WaitChrThread(0x16, 0x0)
    Sleep(1500)

    def lambda_234B():
        OP_6D(10920, 2000, -16720, 1500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_234B)
    WaitChrThread(0x109, 0x1)
    Sleep(300)

    ChrTalk(    #43
        0x12,
        "#170F#5P这、这是……！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0x10,
        (
            "#1450F#5P放心好了，用不着害怕。\x01",
            "只是储蓄起来的导力波放射出来而已。\x02\x03",

            "强力的『古代遗物』被发掘出来时\x01",
            "通常都有像这样的发光现象。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x12, 0, 400)

    ChrTalk(    #45
        0x12,
        "#170F#2P原、原来如此……\x02",
    )

    CloseMessageWindow()
    OP_62(0x12, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #46
        0x12,
        "#170F#2P！？　古代遗物！？\x02",
    )

    CloseMessageWindow()
    OP_8C(0x10, 180, 400)

    ChrTalk(    #47
        0x10,
        (
            "#1450F#6P哎呀，除此之外\x01",
            "你以为还会是其它的什么吗？\x02\x03",

            "那就麻烦你去联络一下――\x01",
            "我要开始进行调查的准备工作了。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(500)
    OP_6D(10980, 2200, -13080, 0)
    OP_67(0, 4540, -10000, 0)
    OP_6B(2410, 0)
    OP_6C(70000, 0)
    OP_6E(358, 0)
    OP_8C(0x16, 225, 0)
    SetChrPos(0x16, 7950, 2200, -16400, 225)
    SetChrPos(0x12, 9350, 2200, -14630, 45)
    SetChrPos(0x10, 9880, 2200, -13360, 225)
    Sleep(200)
    OP_43(0x10, 0x0, 0x0, 0xB)
    OP_0D()
    Sleep(500)

    ChrTalk(    #48
        0x12,
        "#170F#6P联络是指……？\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x10, 0x0)
    Sleep(300)
    OP_8C(0x10, 225, 400)

    ChrTalk(    #49
        0x10,
        (
            "#1450F#5P我们都弄出这种东西来了。\x01",
            "需要汇报的不是只有一个地方吗。\x02\x03",

            "『亚尔特利亚法典国』――\x02",
        )
    )

    CloseMessageWindow()
    OP_20(0x3E8)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_21()
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #50
        "\x07\x00◆如果有开场动画这里播放开场动画\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_A2(0x2505)
    NewScene("ED6_DT21/T4105   ._SN", 101, 0, 0)
    IdleLoop()
    Return()

    # Function_3_4C4 end

    def Function_4_26A3(): pass

    label("Function_4_26A3")

    OP_24(0x1C5, 0x5A)
    Sleep(200)
    OP_24(0x1C5, 0x50)
    Sleep(200)
    OP_24(0x1C5, 0x46)
    OP_24(0x146, 0x46)
    Sleep(200)
    OP_24(0x1C5, 0x3C)
    OP_24(0x146, 0x3C)
    Sleep(200)
    OP_24(0x1C5, 0x32)
    OP_24(0x146, 0x32)
    Sleep(200)
    OP_24(0x1C5, 0x28)
    OP_24(0x146, 0x28)
    Sleep(200)
    OP_24(0x1C5, 0x1E)
    OP_24(0x146, 0x1E)
    Sleep(200)
    OP_24(0x1C5, 0x14)
    OP_24(0x146, 0x14)
    Sleep(200)
    OP_24(0x1C5, 0xA)
    OP_24(0x146, 0xA)
    Sleep(200)
    OP_24(0x1C5, 0x0)
    OP_24(0x146, 0x0)
    OP_23(0x1C5)
    OP_23(0x146)
    Return()

    # Function_4_26A3 end

    def Function_5_271F(): pass

    label("Function_5_271F")

    SetChrFlags(0xFE, 0x20)
    OP_43(0xFE, 0x3, 0x0, 0x2)
    OP_22(0x155, 0x1, 0x3C)
    OP_8E(0xFE, 0xFFFFFF24, 0x157C, 0xFFFFB4BA, 0x2710, 0x0)
    OP_44(0xFE, 0x3)
    OP_23(0x155)
    SetChrSubChip(0xFE, 7)
    OP_97(0xFE, 0xFFFFFF24, 0xFFFFC842, 0xFFFAA8D0, 0x2EE0, 0x1)
    OP_43(0xFE, 0x3, 0x0, 0x2)
    OP_22(0x155, 0x1, 0x3C)
    OP_8E(0xFE, 0x9C72, 0x2134, 0xFFFFA4A2, 0x2710, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_5_271F end

    def Function_6_278B(): pass

    label("Function_6_278B")

    SetChrFlags(0xFE, 0x20)
    OP_43(0xFE, 0x3, 0x0, 0x2)
    OP_22(0x155, 0x1, 0x3C)
    OP_8E(0xFE, 0xFFFFFDA8, 0x1B58, 0xFFFFAA10, 0x2710, 0x0)
    OP_44(0xFE, 0x3)
    OP_23(0x155)
    SetChrSubChip(0xFE, 7)
    OP_97(0xFE, 0xFFFFFF24, 0xFFFFC842, 0xFFFA81C0, 0x32C8, 0x1)
    OP_43(0xFE, 0x3, 0x0, 0x2)
    OP_22(0x155, 0x1, 0x3C)
    OP_8E(0xFE, 0x9E98, 0x21FC, 0xFFFFA808, 0x2710, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_6_278B end

    def Function_7_27F7(): pass

    label("Function_7_27F7")

    SetChrFlags(0xFE, 0x20)
    OP_43(0xFE, 0x3, 0x0, 0x2)
    OP_22(0x155, 0x1, 0x3C)
    OP_8E(0xFE, 0xFFFFF880, 0x2134, 0xFFFFA04C, 0x2710, 0x0)
    OP_44(0xFE, 0x3)
    OP_23(0x155)
    SetChrSubChip(0xFE, 7)
    OP_97(0xFE, 0xFFFFFF24, 0xFFFFC842, 0xFFFAA8D0, 0x36B0, 0x1)
    OP_43(0xFE, 0x3, 0x0, 0x2)
    OP_22(0x155, 0x1, 0x3C)
    OP_8E(0xFE, 0x9420, 0x1F40, 0xFFFFAC04, 0x2710, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_7_27F7 end

    def Function_8_2863(): pass

    label("Function_8_2863")

    OP_89(0x10, 11230, 2300, -10170, 180)
    OP_9F(0x10, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_8E(0xFE, 0x27CE, 0x898, 0xFFFFCAAE, 0x7D0, 0x0)
    OP_8C(0xFE, 270, 400)
    Return()

    # Function_8_2863 end

    def Function_9_289B(): pass

    label("Function_9_289B")

    OP_8E(0xFE, 0x253A, 0x898, 0xFFFFC54A, 0x7D0, 0x0)
    OP_8C(0xFE, 270, 400)
    Return()

    # Function_9_289B end

    def Function_10_28B7(): pass

    label("Function_10_28B7")

    PlayEffect(0x2, 0x0, 0xFF, 6710, 3500, -16660, 50, -70, 0, 800, 800, 800, 0xFF, 0, 0, 0, 0)
    Sleep(2000)
    OP_82(0x0, 0x2)
    Return()

    # Function_10_28B7 end

    def Function_11_28F5(): pass

    label("Function_11_28F5")

    OP_8C(0xFE, 45, 400)
    OP_8F(0xFE, 0x2986, 0x8FC, 0xFFFFD1E8, 0x7D0, 0x0)
    Return()

    # Function_11_28F5 end

    def Function_12_2911(): pass

    label("Function_12_2911")

    OP_24(0x155, 0x32)
    Sleep(300)
    OP_24(0x155, 0x28)
    Sleep(300)
    OP_24(0x155, 0x1E)
    Sleep(300)
    OP_24(0x155, 0x14)
    Sleep(300)
    OP_24(0x155, 0xA)
    Sleep(300)
    OP_23(0x155)
    Return()

    # Function_12_2911 end

    def Function_13_2942(): pass

    label("Function_13_2942")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_29B1")
    OP_8C(0xFE, 135, 400)
    OP_8E(0xFE, 0xFFFFF434, 0xFFFFF5F6, 0xFFFFB1C2, 0x7D0, 0x0)
    OP_8C(0xFE, 225, 400)
    OP_62(0xFE, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(3000)
    OP_63(0xFE)
    OP_8C(0xFE, 315, 400)
    OP_8E(0xFE, 0xFFFFEC8C, 0xFFFFF5F6, 0xFFFFBB7C, 0x7D0, 0x0)
    OP_8C(0xFE, 225, 400)
    Sleep(2500)
    Jump("Function_13_2942")

    label("loc_29B1")

    Return()

    # Function_13_2942 end

    def Function_14_29B2(): pass

    label("Function_14_29B2")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_29E2")
    Sleep(2000)
    OP_8C(0xFE, 225, 400)
    Sleep(2200)
    OP_8C(0xFE, 180, 400)
    Sleep(2200)
    OP_8C(0xFE, 135, 400)
    Jump("Function_14_29B2")

    label("loc_29E2")

    Return()

    # Function_14_29B2 end

    def Function_15_29E3(): pass

    label("Function_15_29E3")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2A13")
    OP_8C(0xFE, 45, 400)
    Sleep(2200)
    OP_8C(0xFE, 135, 400)
    Sleep(2200)
    OP_8C(0xFE, 90, 400)
    Sleep(1500)
    Jump("Function_15_29E3")

    label("loc_2A13")

    Return()

    # Function_15_29E3 end

    def Function_16_2A14(): pass

    label("Function_16_2A14")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2A4A")
    Sleep(3000)
    OP_8C(0xFE, 225, 400)
    Sleep(2200)
    OP_62(0xFE, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_8C(0xFE, 270, 400)
    Jump("Function_16_2A14")

    label("loc_2A4A")

    Return()

    # Function_16_2A14 end

    def Function_17_2A4B(): pass

    label("Function_17_2A4B")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2B9B")
    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2A8E")
    Sleep(1000)
    OP_62(0xFE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_8C(0xFE, 135, 400)
    Jump("loc_2B98")

    label("loc_2A8E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2ABC")
    Sleep(1300)
    OP_62(0xFE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_8C(0xFE, 180, 400)
    Jump("loc_2B98")

    label("loc_2ABC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2AEA")
    Sleep(1600)
    OP_62(0xFE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_8C(0xFE, 90, 400)
    Jump("loc_2B98")

    label("loc_2AEA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2B18")
    Sleep(1900)
    OP_62(0xFE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_8C(0xFE, 135, 400)
    Jump("loc_2B98")

    label("loc_2B18")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2B46")
    Sleep(2200)
    OP_62(0xFE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_8C(0xFE, 180, 400)
    Jump("loc_2B98")

    label("loc_2B46")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2B6D")
    Sleep(2500)
    OP_62(0xFE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Jump("loc_2B98")

    label("loc_2B6D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2B98")
    Sleep(2800)
    OP_62(0xFE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_8C(0xFE, 135, 400)

    label("loc_2B98")

    Jump("Function_17_2A4B")

    label("loc_2B9B")

    Return()

    # Function_17_2A4B end

    SaveToFile()

Try(main)

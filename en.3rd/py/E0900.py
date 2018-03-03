from ED63RDScenarioHelper import *

def main():
    SetCodePage("ms932")

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
        'Erika Russell',                        # 9
        'Lt. Colonel Cid',                      # 10
        'Captain Schwarz',                      # 11
        'Maintenance Chief Gustav',             # 12
        'Antoine',                              # 13
        'Worker',                               # 14
        'Worker',                               # 15
        'Worker',                               # 16
        'Royal Army Soldier',                   # 17
        'Royal Army Soldier',                   # 18
        'Maintenance Ship',                     # 19
        'Maintenance Ship Shadow',              # 20
        'Military Ship',                        # 21
        'Military Ship Shadow',                 # 22
        'Port',                                 # 23
        'Seagull',                              # 24
        'Seagull',                              # 25
        'Seagull',                              # 26
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
        "Function_4_2ABE",         # 04, 4
        "Function_5_2B3A",         # 05, 5
        "Function_6_2BA6",         # 06, 6
        "Function_7_2C12",         # 07, 7
        "Function_8_2C7E",         # 08, 8
        "Function_9_2CB6",         # 09, 9
        "Function_10_2CD2",        # 0A, 10
        "Function_11_2D10",        # 0B, 11
        "Function_12_2D2C",        # 0C, 12
        "Function_13_2D5D",        # 0D, 13
        "Function_14_2DCD",        # 0E, 14
        "Function_15_2DFE",        # 0F, 15
        "Function_16_2E2F",        # 10, 16
        "Function_17_2E66",        # 11, 17
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
            "#690F#5PDamn. Sun goin' down already, huh?\x02\x03",

            "If this spot turns out to be a bust,\x01",
            "we're probably gonna have to call it\x01",
            "quits for today.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x11, 180, 400)
    Sleep(300)

    ChrTalk(    #1
        0x11,
        (
            "#700F#6PWe can only hope...\x02\x03",

            "Professor Russell is certain that this is\x01",
            "the area where we should be looking?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x13,
        "#691F#5PYep. And if she says it's here, it's here.\x02",
    )

    CloseMessageWindow()
    OP_8C(0x13, 0, 400)
    Sleep(300)

    ChrTalk(    #3
        0x13,
        (
            "#690F#2PUnfortunately, as you know, Valleria Lake's\x01",
            "about as deep as a lake can get.\x02\x03",

            "Depending on how small the thing we're\x01",
            "lookin' for is, actually finding it could\x01",
            "still be a real task and a half.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x11,
        (
            "#703F#6PHmm...\x02\x03",

            "#700FIs it likely to be small, though? The orbal readings\x01",
            "suggested we're dealing with quite a large object,\x01",
            "I believe...\x02",
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
        "Woman's Voice",
        (
            "#2POh, I wouldn't judge its size based\x01",
            "off of those.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x11, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x13, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_DE0():
        OP_6D(10000, 2200, -15000, 2000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_DE0)

    def lambda_DF8():
        OP_67(0, 5350, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_DF8)

    def lambda_E10():
        OP_6B(3000, 2000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_E10)

    def lambda_E20():
        OP_6C(122000, 2000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_E20)
    SetChrFlags(0x10, 0x4)
    OP_43(0x10, 0x0, 0x0, 0x8)

    def lambda_E3C():

        label("loc_E3C")

        TurnDirection(0xFE, 0x10, 400)
        OP_48()
        Jump("loc_E3C")

    QueueWorkItem2(0x11, 0, lambda_E3C)
    Sleep(100)

    def lambda_E52():

        label("loc_E52")

        TurnDirection(0xFE, 0x10, 400)
        OP_48()
        Jump("loc_E52")

    QueueWorkItem2(0x13, 0, lambda_E52)
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
        "#702F#6PAh, Professor.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x13,
        (
            "#691FHey there, kiddo. Finished getting us a new \x01",
            "estimated location?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x10,
        (
            "#1458F#5PJust about.\x02\x03",

            "#1452FIt'd be real swell if you knocked it off with the\x01",
            "'kiddo,' though.\x02\x03",

            "I'm not sure it's the most appropriate way to\x01",
            "address a married woman, much less one who's\x01",
            "already popped out a child.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x13,
        (
            "#693FHah! Sorry, but old habits die hard, y'know?\x02\x03",

            "Hard to make the switch when I've been callin'\x01",
            "you that since you were about knee-high.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x10,
        "#1833F#5P*sigh* Well, I'll let you off this time.\x02",
    )

    CloseMessageWindow()
    Sleep(400)

    ChrTalk(    #11
        0x10,
        (
            "#1450F#5PBack to work. Can you ask your subordinates\x01",
            "to stand down for the time being, Colonel?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x11,
        (
            "#702F#6PIs this the spot, then?\x02\x03",

            "Were you able to calculate exactly\x01",
            "where the object is?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x10,
        (
            "#1458F#5PGive or take an arge, yes.\x02\x03",

            "#1450FJudging by the readings, what we're trying\x01",
            "to pull up isn't all that big, either.\x02\x03",

            "Probably about 50 rege. Maybe even less.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x13,
        (
            "#690FYou serious?\x02\x03",

            "Thought we'd be dealing with a real monster,\x01",
            "not somethin' the size of Antoine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x14,
        "#5PNyaon?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x11,
        (
            "#703F#6PHmm...\x02\x03",

            "#700FStill, if it does turn out to be an artifact,\x01",
            "this could get problematic.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x10,
        (
            "#1457F#5PUnfortunately. The church isn't going to want\x01",
            "to let us keep it, that's for sure.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(400)

    ChrTalk(    #18
        0x10,
        (
            "#1832F#5PUgh! I really cannot stand them. No matter how \x01",
            "hard you work to get your hands on something, \x01",
            "the SECOND it turns out to be an artifact...\x02\x03",

            "...they swoop in like it's their Goddess-given right \x01",
            "to have it. It ticks me off.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x13, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(    #19
        0x13,
        (
            "#692FEasy, there. We don't know for sure that \x01",
            "this is even an artifact yet!\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x11, 180, 400)
    Sleep(300)

    ChrTalk(    #20
        0x11,
        (
            "#701F#6PRegardless, I'll pass on the message\x01",
            "to my subordinates right away.\x02\x03",

            "I'll leave the rest here to you, Gustav.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x13, 0, 400)
    Sleep(300)

    ChrTalk(    #21
        0x13,
        (
            "#691F#2PYou got it.\x02\x03",

            "Let's see what we're dealing with, yeah?\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)

    def lambda_1587():
        OP_6B(3500, 3000)
        ExitThread()

    QueueWorkItem(0x13, 0, lambda_1587)
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

    def lambda_16AD():
        OP_6D(7610, 2200, -16930, 3000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_16AD)

    def lambda_16C5():
        OP_67(0, 5260, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_16C5)

    def lambda_16DD():
        OP_6B(3010, 3000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_16DD)

    def lambda_16ED():
        OP_6C(101000, 3000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_16ED)

    def lambda_16FD():
        OP_6E(399, 3000)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_16FD)
    OP_22(0x133, 0x0, 0x64)
    OP_B0(0x0, 0xA)
    OP_6F(0x0, 0)
    OP_70(0x0, 0x1E)
    OP_73(0x0)
    Sleep(1000)

    def lambda_172C():
        OP_6D(6860, 660, -18490, 3000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_172C)

    def lambda_1744():
        OP_67(0, 5260, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_1744)

    def lambda_175C():
        OP_6B(3230, 3000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_175C)

    def lambda_176C():
        OP_6C(101000, 3000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_176C)

    def lambda_177C():
        OP_6E(413, 3000)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_177C)
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
            "#1452F#6POkay. That's the spot.\x02\x03",

            "#1455FGo on ahead!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x13,
        "#690F#6PYes, ma'am! Beginning the salvage operation!\x02",
    )

    CloseMessageWindow()

    def lambda_1823():
        OP_6D(1860, 410, -18210, 3000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_1823)

    def lambda_183B():
        OP_67(0, 5400, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_183B)

    def lambda_1853():
        OP_6B(2950, 3000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_1853)

    def lambda_1863():
        OP_6C(125000, 3000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_1863)

    def lambda_1873():
        OP_6E(399, 3000)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_1873)
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
        "#1453F#5PGah... That sound just fills me with dread.\x02",
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
            "#702F#6PDoes the salvage crane sound like it's in\x01",
            "poor condition to you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x10,
        "#1833F#5POh, that's not really what I meant.\x02",
    )

    CloseMessageWindow()
    Sleep(400)

    ChrTalk(    #27
        0x10,
        (
            "#1457F#5PI just can't bring myself to like artifacts, you see.\x02\x03",

            "We can't explain HOW they have the power they\x01",
            "do, but they have it, and it's not something we\x01",
            "can ignore, either.\x02\x03",

            "As a researcher, I can barely imagine anything\x01",
            "more frustrating.\x02\x03",

            "#1452FEven when we can't help but be captivated by\x01",
            "them, we're well aware that any attempt to solve\x01",
            "their mysteries is pointless.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x11,
        (
            "#703F#6PI see... When you put it that way, I can understand\x01",
            "to a degree how you must feel.\x02\x03",

            "#700FHalf a year has passed since all the chaos came to\x01",
            "an end, and on the surface, we're back to normal...\x02\x03",

            "...but even now, we still don't know what truly \x01",
            "happened here or what it signified.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x10,
        (
            "#1453F#5P...Yeah.\x02\x03",

            "#1457FNot that I was here to see it all happen,\x01",
            "of course.\x02",
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
            "#690FThe crane arm's reached the bottom of the lake.\x02\x03",

            "I'm gonna attempt to grip the object.\x02",
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

    def lambda_1F22():
        OP_8E(0xFE, 0x1ED2, 0x898, 0xFFFFC6EE, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_1F22)
    Sleep(300)

    def lambda_1F42():
        OP_8E(0xFE, 0x1EFA, 0x898, 0xFFFFCB6C, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_1F42)
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
            "#690F#6PSwing and a miss.\x02\x03",

            "Moving 30 rege to the right.\x02",
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
        "#1458F#6PHaha. There we go.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x13,
        (
            "#691F#6PYep! We've got it.\x02\x03",

            "Want me to pull it up?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x10,
        "#1456F#6PPlease do.\x02",
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
        "#701F#6PThe moment of truth, huh?\x02",
    )

    CloseMessageWindow()

    def lambda_21D6():
        OP_6B(2600, 8000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_21D6)

    def lambda_21E6():
        OP_6D(2520, 1070, -15920, 8000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_21E6)
    Sleep(8000)

    ChrTalk(    #36
        0x13,
        "#690F#6PHere we go!\x02",
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

    def lambda_2299():
        OP_6D(7780, -4590, -16040, 6000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_2299)

    def lambda_22B1():
        OP_67(0, 7230, -10000, 6000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_22B1)

    def lambda_22C9():
        OP_6B(2009, 6000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_22C9)

    def lambda_22D9():
        OP_6E(414, 6000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_22D9)

    def lambda_22E9():
        OP_6C(71000, 6000)
        ExitThread()

    QueueWorkItem(0x10, 3, lambda_22E9)
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
        "#1454F#4PWhat?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x11,
        "#702F#3PO-Oh, my...\x02",
    )

    CloseMessageWindow()

    def lambda_2441():
        OP_6B(1700, 6000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_2441)
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

    def lambda_2491():
        OP_6D(8490, 2400, -17400, 4000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_2491)

    def lambda_24A9():
        OP_67(0, 4380, -10000, 5000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_24A9)

    def lambda_24C1():
        OP_6B(2190, 5000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_24C1)

    def lambda_24D1():
        OP_6C(129000, 5000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_24D1)

    def lambda_24E1():
        OP_6E(428, 5000)
        ExitThread()

    QueueWorkItem(0x10, 3, lambda_24E1)
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

    def lambda_255B():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x15, 0, lambda_255B)
    WaitChrThread(0x109, 0x0)
    WaitChrThread(0x109, 0x1)
    Sleep(300)

    ChrTalk(    #39
        0x12,
        "#170F#5PCan you see the object?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0x16,
        (
            "#4PY-Yes... Or at least I think so.\x02\x03",

            "I-I'll go and get a closer look!\x02",
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
            "#1450F#5PBe careful!\x02\x03",

            "Don't attempt to touch it until I give the\x01",
            "go-ahead to do so!\x02",
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
        "#5P#20AW-Whoa!\x05\x02",
    )


    def lambda_26E2():
        OP_8C(0xFE, 180, 600)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_26E2)

    def lambda_26F0():
        OP_8F(0xFE, 0x1F22, 0x898, 0xFFFFC23E, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 0, lambda_26F0)
    WaitChrThread(0x16, 0x0)
    Sleep(1500)

    def lambda_2715():
        OP_6D(10920, 2000, -16720, 1500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_2715)
    WaitChrThread(0x109, 0x1)
    Sleep(300)

    ChrTalk(    #43
        0x12,
        "#170F#5PWh-What's happening?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0x10,
        (
            "#1450F#5PThere's no need to be afraid. It's just giving off\x01",
            "orbal waves that have built up over time.\x02\x03",

            "Powerful artifacts glowing brightly when excavated\x01",
            "isn't exactly a phenomenon without precedent.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x12, 0, 400)

    ChrTalk(    #45
        0x12,
        "#170F#2PI-I see...\x02",
    )

    CloseMessageWindow()
    OP_62(0x12, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #46
        0x12,
        "#170F#2PWait! So it is an artifact?!\x02",
    )

    CloseMessageWindow()
    OP_8C(0x10, 180, 400)

    ChrTalk(    #47
        0x10,
        (
            "#1450F#6PWhat else could it possibly be?\x02\x03",

            "Anyway, you know who to get in contact with.\x01",
            "I'll be preparing to investigate it as much as\x01",
            "possible.\x02",
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
        "#170F#6PI do...?\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x10, 0x0)
    Sleep(300)
    OP_8C(0x10, 225, 400)

    ChrTalk(    #49
        0x10,
        (
            "#1450F#5PWith what we're dealing with, who else could you\x01",
            "possibly need to let know? \x02\x03",

            "I'm referring to Arteria, of course.\x02",
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
        "\x07\x00◆If there's an OP movie, play it here.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_A2(0x2505)
    NewScene("ED6_DT21/T4105   ._SN", 101, 0, 0)
    IdleLoop()
    Return()

    # Function_3_4C4 end

    def Function_4_2ABE(): pass

    label("Function_4_2ABE")

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

    # Function_4_2ABE end

    def Function_5_2B3A(): pass

    label("Function_5_2B3A")

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

    # Function_5_2B3A end

    def Function_6_2BA6(): pass

    label("Function_6_2BA6")

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

    # Function_6_2BA6 end

    def Function_7_2C12(): pass

    label("Function_7_2C12")

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

    # Function_7_2C12 end

    def Function_8_2C7E(): pass

    label("Function_8_2C7E")

    OP_89(0x10, 11230, 2300, -10170, 180)
    OP_9F(0x10, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_8E(0xFE, 0x27CE, 0x898, 0xFFFFCAAE, 0x7D0, 0x0)
    OP_8C(0xFE, 270, 400)
    Return()

    # Function_8_2C7E end

    def Function_9_2CB6(): pass

    label("Function_9_2CB6")

    OP_8E(0xFE, 0x253A, 0x898, 0xFFFFC54A, 0x7D0, 0x0)
    OP_8C(0xFE, 270, 400)
    Return()

    # Function_9_2CB6 end

    def Function_10_2CD2(): pass

    label("Function_10_2CD2")

    PlayEffect(0x2, 0x0, 0xFF, 6710, 3500, -16660, 50, -70, 0, 800, 800, 800, 0xFF, 0, 0, 0, 0)
    Sleep(2000)
    OP_82(0x0, 0x2)
    Return()

    # Function_10_2CD2 end

    def Function_11_2D10(): pass

    label("Function_11_2D10")

    OP_8C(0xFE, 45, 400)
    OP_8F(0xFE, 0x2986, 0x8FC, 0xFFFFD1E8, 0x7D0, 0x0)
    Return()

    # Function_11_2D10 end

    def Function_12_2D2C(): pass

    label("Function_12_2D2C")

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

    # Function_12_2D2C end

    def Function_13_2D5D(): pass

    label("Function_13_2D5D")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2DCC")
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
    Jump("Function_13_2D5D")

    label("loc_2DCC")

    Return()

    # Function_13_2D5D end

    def Function_14_2DCD(): pass

    label("Function_14_2DCD")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2DFD")
    Sleep(2000)
    OP_8C(0xFE, 225, 400)
    Sleep(2200)
    OP_8C(0xFE, 180, 400)
    Sleep(2200)
    OP_8C(0xFE, 135, 400)
    Jump("Function_14_2DCD")

    label("loc_2DFD")

    Return()

    # Function_14_2DCD end

    def Function_15_2DFE(): pass

    label("Function_15_2DFE")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2E2E")
    OP_8C(0xFE, 45, 400)
    Sleep(2200)
    OP_8C(0xFE, 135, 400)
    Sleep(2200)
    OP_8C(0xFE, 90, 400)
    Sleep(1500)
    Jump("Function_15_2DFE")

    label("loc_2E2E")

    Return()

    # Function_15_2DFE end

    def Function_16_2E2F(): pass

    label("Function_16_2E2F")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2E65")
    Sleep(3000)
    OP_8C(0xFE, 225, 400)
    Sleep(2200)
    OP_62(0xFE, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_8C(0xFE, 270, 400)
    Jump("Function_16_2E2F")

    label("loc_2E65")

    Return()

    # Function_16_2E2F end

    def Function_17_2E66(): pass

    label("Function_17_2E66")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2FB6")
    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2EA9")
    Sleep(1000)
    OP_62(0xFE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_8C(0xFE, 135, 400)
    Jump("loc_2FB3")

    label("loc_2EA9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2ED7")
    Sleep(1300)
    OP_62(0xFE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_8C(0xFE, 180, 400)
    Jump("loc_2FB3")

    label("loc_2ED7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2F05")
    Sleep(1600)
    OP_62(0xFE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_8C(0xFE, 90, 400)
    Jump("loc_2FB3")

    label("loc_2F05")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2F33")
    Sleep(1900)
    OP_62(0xFE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_8C(0xFE, 135, 400)
    Jump("loc_2FB3")

    label("loc_2F33")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2F61")
    Sleep(2200)
    OP_62(0xFE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_8C(0xFE, 180, 400)
    Jump("loc_2FB3")

    label("loc_2F61")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2F88")
    Sleep(2500)
    OP_62(0xFE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Jump("loc_2FB3")

    label("loc_2F88")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2FB3")
    Sleep(2800)
    OP_62(0xFE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_8C(0xFE, 135, 400)

    label("loc_2FB3")

    Jump("Function_17_2E66")

    label("loc_2FB6")

    Return()

    # Function_17_2E66 end

    SaveToFile()

Try(main)

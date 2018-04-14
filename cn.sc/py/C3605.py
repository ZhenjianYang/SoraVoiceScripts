from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 蔡斯

    CreateScenaFile(
        FileName            = 'C3605   ._SN',
        MapName             = 'Zeiss',
        Location            = 'C3605.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60033",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            '',
            'ED6_DT21/C3605_1 ._SN',
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
        '瘦狼瓦鲁特',                           # 9
        '雾香',                                 # 10
        '剑齿虎',                               # 11
        '剑齿虎',                               # 12
        '剑齿虎',                               # 13
        '福音',                                 # 14
        '偃月轮',                               # 15
        '目标用照相机',                         # 16
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
        'ED6_DT27/CH03500 ._CH',             # 00
        'ED6_DT07/CH02610 ._CH',             # 01
        'ED6_DT26/CH20280 ._CH',             # 02
        'ED6_DT06/CH20021 ._CH',             # 03
        'ED6_DT26/CH20420 ._CH',             # 04
        'ED6_DT27/CH04500 ._CH',             # 05
        'ED6_DT27/CH04501 ._CH',             # 06
        'ED6_DT27/CH04502 ._CH',             # 07
        'ED6_DT27/CH04503 ._CH',             # 08
        'ED6_DT27/CH04508 ._CH',             # 09
        'ED6_DT27/CH04000 ._CH',             # 0A
        'ED6_DT27/CH04001 ._CH',             # 0B
        'ED6_DT27/CH04010 ._CH',             # 0C
        'ED6_DT27/CH04011 ._CH',             # 0D
        'ED6_DT07/CH00170 ._CH',             # 0E
        'ED6_DT07/CH00171 ._CH',             # 0F
        'ED6_DT07/CH00172 ._CH',             # 10
        'ED6_DT07/CH00173 ._CH',             # 11
    )

    AddCharChipPat(
        'ED6_DT27/CH03500P._CP',             # 00
        'ED6_DT07/CH02610P._CP',             # 01
        'ED6_DT26/CH20280P._CP',             # 02
        'ED6_DT06/CH20021P._CP',             # 03
        'ED6_DT26/CH20420P._CP',             # 04
        'ED6_DT27/CH04500P._CP',             # 05
        'ED6_DT27/CH04501P._CP',             # 06
        'ED6_DT27/CH04502P._CP',             # 07
        'ED6_DT27/CH04503P._CP',             # 08
        'ED6_DT27/CH04508P._CP',             # 09
        'ED6_DT27/CH04000P._CP',             # 0A
        'ED6_DT27/CH04001P._CP',             # 0B
        'ED6_DT27/CH04010P._CP',             # 0C
        'ED6_DT27/CH04011P._CP',             # 0D
        'ED6_DT07/CH00170P._CP',             # 0E
        'ED6_DT07/CH00171P._CP',             # 0F
        'ED6_DT07/CH00172P._CP',             # 10
        'ED6_DT07/CH00173P._CP',             # 11
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
        Y                   = 0,
        Direction           = 0,
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
        Direction           = 0,
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
        Direction           = 0,
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
        Direction           = 0,
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
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 458755,
        ChipIndex           = 0x3,
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
        Unknown3            = 393220,
        ChipIndex           = 0x4,
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
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x80,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    ScpFunction(
        "Function_0_23A",          # 00, 0
        "Function_1_297",          # 01, 1
        "Function_2_2BE",          # 02, 2
        "Function_3_43B",          # 03, 3
        "Function_4_5CB",          # 04, 4
        "Function_5_867",          # 05, 5
        "Function_6_8EE",          # 06, 6
    )


    def Function_0_23A(): pass

    label("Function_0_23A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C1, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_25B")
    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(1, 2)
    Jump("loc_296")

    label("loc_25B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_27A")
    OP_A3(0x10F0)
    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x21), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 3)
    Jump("loc_296")

    label("loc_27A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 1)), scpexpr(EXPR_END)), "loc_296")
    OP_A3(0x10F1)
    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x70), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 4)

    label("loc_296")

    Return()

    # Function_0_23A end

    def Function_1_297(): pass

    label("Function_1_297")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C0, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2A8")
    OP_22(0xEB, 0x1, 0x50)

    label("loc_2A8")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x29), scpexpr(EXPR_PUSH_LONG, 0x455), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2BD")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x6F), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2BD")

    Return()

    # Function_1_297 end

    def Function_2_2BE(): pass

    label("Function_2_2BE")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2E3")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_425")

    label("loc_2E3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2FC")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_425")

    label("loc_2FC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_315")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_425")

    label("loc_315")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_32E")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_425")

    label("loc_32E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_347")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_425")

    label("loc_347")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_360")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_425")

    label("loc_360")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_379")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_425")

    label("loc_379")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_392")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_425")

    label("loc_392")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3AB")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_425")

    label("loc_3AB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3C4")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_425")

    label("loc_3C4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3DD")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_425")

    label("loc_3DD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3F6")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_425")

    label("loc_3F6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_40F")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_425")

    label("loc_40F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_425")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_425")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_43A")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_425")

    label("loc_43A")

    Return()

    # Function_2_2BE end

    def Function_3_43B(): pass

    label("Function_3_43B")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    OP_82(0x80, 0x0)
    OP_71(0x0, 0x4)
    OP_71(0x1, 0x4)
    OP_71(0x2, 0x4)
    OP_71(0x3, 0x4)
    OP_71(0x4, 0x4)
    OP_79(0x0, 0x2)
    OP_79(0x1, 0x2)
    OP_79(0x2, 0x2)
    OP_79(0x3, 0x2)
    OP_79(0x4, 0x2)
    OP_7B()
    OP_6D(-20450, 250, 7600, 0)
    OP_67(0, 6500, -10000, 0)
    OP_6B(4230, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_22(0x1C3, 0x0, 0x64)
    SetChrPos(0x8, 430, 0, 8430, 0)
    ClearChrFlags(0x8, 0x80)
    SetChrChipByIndex(0x8, 2)
    SetChrSubChip(0x8, 0)
    Sleep(1000)

    def lambda_4F9():
        OP_6D(570, 250, 11510, 4000)
        ExitThread()

    QueueWorkItem(0xD, 0, lambda_4F9)
    OP_C8(0x200, 0x46, "C_PLAC20._CH", 0x0, 0x3E8)
    FadeToBright(1000, 0)
    WaitChrThread(0xD, 0x0)
    Sleep(1000)
    Fade(1000)
    OP_6D(570, 250, 11510, 0)
    OP_67(0, 5780, -10000, 0)
    OP_6B(2029, 0)
    OP_6C(36000, 0)
    OP_6E(455, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #0
        0x8,
        (
            "#252F这边是『瘦狼』，\x01",
            "也已经完成啦。\x02\x03",

            "赶快开始吧。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x10F0)
    NewScene("ED6_DT21/C2305   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_3_43B end

    def Function_4_5CB(): pass

    label("Function_4_5CB")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    OP_6D(1220, 950, 14960, 0)
    OP_67(0, 8600, -10000, 0)
    OP_6B(2830, 0)
    OP_6C(45000, 0)
    OP_6E(408, 0)
    SetChrPos(0x8, 430, 0, 8430, 0)
    ClearChrFlags(0x8, 0x80)
    SetChrChipByIndex(0x8, 2)
    SetChrSubChip(0x8, 0)
    OP_82(0x80, 0x0)
    OP_72(0x0, 0x8)
    OP_72(0x1, 0x8)
    OP_72(0x2, 0x8)
    OP_72(0x3, 0x8)
    OP_72(0x4, 0x8)
    OP_72(0x0, 0x20)
    OP_72(0x1, 0x20)
    OP_72(0x2, 0x20)
    OP_72(0x3, 0x20)
    OP_72(0x4, 0x20)
    OP_6F(0x0, 60)
    OP_6F(0x1, 60)
    OP_6F(0x2, 60)
    OP_6F(0x3, 60)
    OP_6F(0x4, 60)
    OP_70(0x0, 0x3C)
    OP_70(0x1, 0x3C)
    OP_70(0x2, 0x3C)
    OP_70(0x3, 0x3C)
    LoadEffect(0x0, "map\\\\mp061_00.eff")
    PlayEffect(0x0, 0xFF, 0xFF, 0, 1300, 13650, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(1000)
    OP_B0(0x0, 0x50)
    OP_B0(0x1, 0x50)
    OP_B0(0x2, 0x50)
    OP_B0(0x3, 0x50)
    OP_B0(0x4, 0x50)
    OP_22(0x99, 0x0, 0x64)
    OP_6F(0x1, 60)
    OP_70(0x1, 0x0)
    OP_73(0x1)
    OP_22(0x99, 0x0, 0x64)
    OP_6F(0x2, 60)
    OP_70(0x2, 0x0)
    OP_73(0x2)
    OP_22(0x99, 0x0, 0x64)
    OP_6F(0x3, 60)
    OP_70(0x3, 0x0)
    OP_73(0x3)
    OP_22(0x99, 0x0, 0x64)
    OP_6F(0x4, 60)
    OP_70(0x4, 0x0)
    OP_73(0x4)
    OP_22(0x99, 0x0, 0x64)
    OP_6F(0x0, 60)
    OP_70(0x0, 0x0)
    OP_73(0x0)
    Fade(1000)
    OP_11(0xA0, 0xB4, 0xFF, 0x17ED0, 0x38E28, 0x0)
    OP_6D(-32090, 30000, -26260, 0)
    OP_67(0, 6500, -10000, 0)
    OP_6B(3700, 0)
    OP_6C(45000, 0)
    OP_6E(300, 0)
    OP_0D()
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(1000)
    LoadEffect(0x0, "map\\mp049_03.eff")
    PlayEffect(0x0, 0x0, 0xFF, -32090, 30000, -26260, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x138, 0x0, 0x64)
    Sleep(3000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x10F1)
    NewScene("ED6_DT21/C2305   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_4_5CB end

    def Function_5_867(): pass

    label("Function_5_867")

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
            "【◇选择雪拉扎德为队友】\x01",      # 0
            "【◇选择阿加特为队友】\x01",        # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_8E1"),
        (1, "loc_8E7"),
        (SWITCH_DEFAULT, "loc_8ED"),
    )


    label("loc_8E1")

    OP_A2(0x1200)
    Jump("loc_8ED")

    label("loc_8E7")

    OP_A2(0x1201)
    Jump("loc_8ED")

    label("loc_8ED")

    Return()

    # Function_5_867 end

    def Function_6_8EE(): pass

    label("Function_6_8EE")

    FadeToDark(0, 0, -1)
    OP_6D(-66940, 250, 36210, 0)
    OP_67(0, 6500, -10000, 0)
    OP_6B(3700, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    Sleep(200)
    FadeToBright(0, 0)
    OP_0D()
    OP_C9(0x0, 0x4, 0x0, 0x1, 0x7, 0xFF, 0x5, 0x2, 0x6, 0x4, 0x8, 0xFFFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    FadeToDark(0, 0, -1)
    OP_69(0x0, 0x0)
    Return()

    # Function_6_8EE end

    SaveToFile()

Try(main)

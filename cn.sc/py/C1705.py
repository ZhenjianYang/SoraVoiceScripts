from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 柏斯

    CreateScenaFile(
        FileName            = 'C1705   ._SN',
        MapName             = 'Bose',
        Location            = 'C1705.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60033",
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
        '歼灭天使玲',                           # 9
        '哨兵改',                               # 10
        '哨兵改',                               # 11
        '哨兵改',                               # 12
        '哨兵改',                               # 13
        '哨兵改',                               # 14
        '哨兵改',                               # 15
        '福音',                                 # 16
        '帕蒂尔·玛蒂尔',                       # 17
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
        'ED6_DT27/CH03510 ._CH',             # 00
        'ED6_DT29/CH12910 ._CH',             # 01
        'ED6_DT06/CH20021 ._CH',             # 02
        'ED6_DT27/CH04510 ._CH',             # 03
        'ED6_DT26/CH20306 ._CH',             # 04
        'ED6_DT27/CH04000 ._CH',             # 05
        'ED6_DT27/CH04010 ._CH',             # 06
        'ED6_DT27/CH04012 ._CH',             # 07
    )

    AddCharChipPat(
        'ED6_DT27/CH03510P._CP',             # 00
        'ED6_DT29/CH12910P._CP',             # 01
        'ED6_DT06/CH20021P._CP',             # 02
        'ED6_DT27/CH04510P._CP',             # 03
        'ED6_DT26/CH20306P._CP',             # 04
        'ED6_DT27/CH04000P._CP',             # 05
        'ED6_DT27/CH04010P._CP',             # 06
        'ED6_DT27/CH04012P._CP',             # 07
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
        Unknown3            = 458754,
        ChipIndex           = 0x2,
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
        NpcIndex            = 0x1C5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    ScpFunction(
        "Function_0_20A",          # 00, 0
        "Function_1_267",          # 01, 1
        "Function_2_2BF",          # 02, 2
        "Function_3_2D5",          # 03, 3
        "Function_4_489",          # 04, 4
        "Function_5_904",          # 05, 5
        "Function_6_911",          # 06, 6
        "Function_7_25F6",         # 07, 7
        "Function_8_3902",         # 08, 8
        "Function_9_41F9",         # 09, 9
        "Function_10_4232",        # 0A, 10
        "Function_11_4261",        # 0B, 11
        "Function_12_4340",        # 0C, 12
        "Function_13_43C7",        # 0D, 13
    )


    def Function_0_20A(): pass

    label("Function_0_20A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C3, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_22B")
    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 5)
    Jump("loc_266")

    label("loc_22B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_24A")
    OP_A3(0x10F0)
    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x21), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 3)
    Jump("loc_266")

    label("loc_24A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 1)), scpexpr(EXPR_END)), "loc_266")
    OP_A3(0x10F1)
    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x70), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 4)

    label("loc_266")

    Return()

    # Function_0_20A end

    def Function_1_267(): pass

    label("Function_1_267")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C3, 5)), scpexpr(EXPR_END)), "loc_27A")
    OP_B1("C1705_y")
    Jump("loc_283")

    label("loc_27A")

    OP_B1("C1705_n")

    label("loc_283")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C0, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_294")
    OP_22(0xEB, 0x1, 0x50)

    label("loc_294")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x29), scpexpr(EXPR_PUSH_LONG, 0x3FD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2A9")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2A9")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x29), scpexpr(EXPR_PUSH_LONG, 0x453), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2BE")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x53), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2BE")

    Return()

    # Function_1_267 end

    def Function_2_2BF(): pass

    label("Function_2_2BF")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2D4")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_2BF")

    label("loc_2D4")

    Return()

    # Function_2_2BF end

    def Function_3_2D5(): pass

    label("Function_3_2D5")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    OP_6D(-210, 0, -3180, 0)
    OP_67(0, 6500, -10000, 0)
    OP_6B(3700, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_22(0x1C3, 0x0, 0x64)
    SetChrPos(0x8, 70, 0, 8530, 0)
    ClearChrFlags(0x8, 0x80)
    SetChrSubChip(0x8, 0)
    SetChrChipByIndex(0x8, 3)
    OP_82(0x80, 0x0)
    OP_71(0x0, 0x4)
    OP_71(0x3, 0x4)
    OP_71(0x4, 0x4)
    OP_71(0x5, 0x4)
    OP_71(0x6, 0x4)
    OP_71(0x7, 0x4)
    OP_79(0x0, 0x2)
    OP_79(0x1, 0x2)
    OP_79(0x2, 0x2)
    OP_79(0x3, 0x2)
    OP_79(0x4, 0x2)
    OP_7B()
    Sleep(1000)

    def lambda_398():
        OP_6D(240, 0, 10710, 4000)
        ExitThread()

    QueueWorkItem(0xF, 0, lambda_398)
    OP_C8(0x200, 0x46, "C_PLAC21._CH", 0x0, 0x3E8)
    FadeToBright(1000, 0)
    WaitChrThread(0xF, 0x0)
    Sleep(1000)
    Fade(1000)
    OP_6D(30, 0, 14990, 0)
    OP_67(0, 2470, -10000, 0)
    OP_6B(2750, 0)
    OP_6C(0, 0)
    OP_6E(465, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #0
        0x8,
        (
            "#263F#6P呵呵呵……这里是『歼灭天使』。\x02\x03",

            "#1305F玲的准备也完毕了，\x01",
            "随时都可以开始。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x10F8)
    NewScene("ED6_DT21/E0810   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_3_2D5 end

    def Function_4_489(): pass

    label("Function_4_489")

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
    SetChrPos(0x8, 70, 0, 8530, 0)
    ClearChrFlags(0x8, 0x80)
    SetChrSubChip(0x8, 0)
    SetChrChipByIndex(0x8, 3)
    OP_82(0x80, 0x0)
    OP_71(0x0, 0x4)
    OP_72(0x3, 0x8)
    OP_72(0x4, 0x8)
    OP_72(0x5, 0x8)
    OP_72(0x6, 0x8)
    OP_72(0x7, 0x8)
    OP_72(0x3, 0x20)
    OP_72(0x4, 0x20)
    OP_72(0x5, 0x20)
    OP_72(0x6, 0x20)
    OP_72(0x7, 0x20)
    OP_6F(0x3, 60)
    OP_6F(0x4, 60)
    OP_6F(0x5, 60)
    OP_6F(0x6, 60)
    OP_6F(0x7, 60)
    OP_70(0x3, 0x3C)
    OP_70(0x4, 0x3C)
    OP_70(0x5, 0x3C)
    OP_70(0x6, 0x3C)
    OP_70(0x7, 0x3C)
    SetChrPos(0xF, 0, 1100, 13760, 0)
    ClearChrFlags(0xF, 0x80)
    SetChrFlags(0xF, 0x2)
    SetChrChipByIndex(0xF, 2)
    SetChrSubChip(0xF, 14)
    LoadEffect(0x1, "map\\\\mp061_00.eff")
    PlayEffect(0x1, 0xFF, 0xFF, 0, 1300, 13650, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(1000)
    OP_B0(0x3, 0x50)
    OP_B0(0x4, 0x50)
    OP_B0(0x5, 0x50)
    OP_B0(0x6, 0x50)
    OP_B0(0x7, 0x50)
    OP_22(0x99, 0x0, 0x64)
    OP_6F(0x5, 60)
    OP_70(0x5, 0x0)
    OP_73(0x5)
    OP_22(0x99, 0x0, 0x64)
    OP_6F(0x4, 60)
    OP_70(0x4, 0x0)
    OP_73(0x4)
    OP_22(0x99, 0x0, 0x64)
    OP_6F(0x6, 60)
    OP_70(0x6, 0x0)
    OP_73(0x6)
    OP_22(0x99, 0x0, 0x64)
    OP_6F(0x7, 60)
    OP_70(0x7, 0x0)
    OP_73(0x7)
    OP_22(0x99, 0x0, 0x64)
    OP_6F(0x3, 60)
    OP_70(0x3, 0x0)
    OP_73(0x3)
    OP_79(0x0, 0x1)
    OP_79(0x1, 0x1)
    OP_79(0x2, 0x1)
    OP_79(0x3, 0x1)
    OP_79(0x4, 0x1)
    OP_7B()
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
    PlayEffect(0x0, 0xFF, 0xFF, -32090, 30000, -26260, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x138, 0x0, 0x64)
    Sleep(3000)
    SetMapFlags(0x2000000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_82(0x0, 0x0)
    Sleep(2000)
    Sleep(500)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("怀斯曼教授")

    AnonymousTalk(    #1
        (
            "\x07\x00#1155F好了！各位！\x01",
            "祝祭的准备已经就绪！\x02\x03",

            "让我们尽情享受这历史性的一刻吧！\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(80, 60, -1, -1)
    SetChrName("怪盗布卢布兰")

    AnonymousTalk(    #2
        "\x07\x00#231F──明白！\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(330, 60, -1, -1)
    SetChrName("幻惑之铃露茜奥拉")

    AnonymousTalk(    #3
        "\x07\x00#241F吾等『执行者』一起。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(80, 330, -1, -1)
    SetChrName("瘦狼瓦鲁特")

    AnonymousTalk(    #4
        (
            "\x07\x00#252F遵照伟大盟主的代理人\x01",
            "『蛇之使徒』的指示──\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(330, 330, -1, -1)
    SetChrName("歼灭天使玲")

    AnonymousTalk(    #5
        "\x07\x00#1306F现在开始『桩』的解锁！\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(500)
    OP_AD(0x2400AA, 0x0, 0x0, 0x64)
    Sleep(4000)
    OP_56(0x2)
    OP_AE(0xC8)
    Sleep(2000)
    ClearMapFlags(0x2000000)
    OP_A2(0x10F0)
    NewScene("ED6_DT21/T4201   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_4_489 end

    def Function_5_904(): pass

    label("Function_5_904")

    Call(0, 6)
    Call(0, 7)
    Call(0, 8)
    Return()

    # Function_5_904 end

    def Function_6_911(): pass

    label("Function_6_911")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_932")
    Call(0, 12)
    Call(0, 13)

    label("loc_932")

    OP_71(0x0, 0x4)
    OP_71(0x1, 0x4)
    OP_71(0x9, 0x4)
    Call(0, 11)
    OP_D2(0x270246, 0x270250, 0xA)
    OP_D2(0x270244, 0x27024E, 0xB)
    OP_D2(0x290391, 0x290395, 0xC)
    OP_6D(-150, 8440, -4110, 0)
    OP_67(0, 2640, -10000, 0)
    OP_6B(2810, 0)
    OP_6C(68000, 0)
    OP_6E(413, 0)
    SetChrPos(0x8, -450, 950, 12440, 180)
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x101, 740, -1750, -7480, 0)
    SetChrPos(0x102, -650, -1750, -7480, 0)
    SetChrPos(0xF8, 820, -1750, -7480, 0)
    SetChrPos(0xF9, -750, -1750, -7480, 0)
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x102, 0x80)
    SetChrFlags(0xF8, 0x80)
    SetChrFlags(0xF9, 0x80)
    OP_6F(0x3, 0)
    OP_6F(0x4, 0)
    OP_6F(0x5, 0)
    OP_6F(0x6, 0)
    OP_6F(0x7, 0)
    OP_70(0x3, 0x8)
    OP_70(0x4, 0x8)
    OP_70(0x5, 0x8)
    OP_70(0x6, 0x8)
    OP_70(0x7, 0x8)
    LoadEffect(0x0, "map\\\\mp061_00.eff")
    PlayEffect(0x0, 0xFF, 0xFF, 0, 1300, 13650, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_AA3():
        OP_6D(430, 0, -2500, 6000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_AA3)

    def lambda_ABB():
        OP_67(0, 8960, -10000, 6000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_ABB)

    def lambda_AD3():
        OP_6B(2300, 6000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_AD3)

    def lambda_AE3():
        OP_6C(45000, 6000)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_AE3)

    def lambda_AF3():
        OP_6E(315, 6000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_AF3)
    FadeToBright(1000, 0)
    Sleep(4000)
    ClearChrFlags(0x101, 0x80)

    def lambda_B16():
        OP_8E(0xFE, 0x2E4, 0x0, 0xFFFFF808, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_B16)
    Sleep(100)
    ClearChrFlags(0x102, 0x80)

    def lambda_B3B():
        OP_8E(0xFE, 0xFFFFFD76, 0x0, 0xFFFFF827, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_B3B)
    Sleep(600)
    ClearChrFlags(0xF8, 0x80)

    def lambda_B60():
        OP_8E(0xFE, 0x334, 0x0, 0xFFFFF240, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_B60)
    Sleep(100)
    ClearChrFlags(0xF9, 0x80)

    def lambda_B85():
        OP_8E(0xFE, 0xFFFFFD12, 0x0, 0xFFFFF1FA, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_B85)
    WaitChrThread(0xF9, 0x1)

    NpcTalk(    #6
        0x8,
        "少女的声音",
        (
            "真是的……\x01",
            "人家都等得不耐烦了。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C2E")
    OP_62(0xF8, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_C6C")

    label("loc_C2E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C55")
    OP_62(0xF8, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_C6C")

    label("loc_C55")

    OP_62(0xF8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_C6C")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C98")
    OP_62(0xF9, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_CD6")

    label("loc_C98")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CBF")
    OP_62(0xF9, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_CD6")

    label("loc_CBF")

    OP_62(0xF9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_CD6")

    Sleep(1000)
    OP_1D(0x6F)
    Sleep(500)

    def lambda_CE8():
        OP_6D(40, 950, 12620, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_CE8)

    def lambda_D00():
        OP_67(0, 5500, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_D00)

    def lambda_D18():
        OP_6E(310, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_D18)
    WaitChrThread(0x101, 0x3)
    Sleep(1000)
    Fade(500)
    OP_6D(0, 950, 9500, 0)
    OP_67(0, 3620, -10000, 0)
    OP_6B(4200, 0)
    OP_6C(0, 0)
    OP_6E(247, 0)
    SetChrPos(0x101, 150, -1750, -7480, 0)
    SetChrPos(0x102, -1000, -1750, -7480, 0)
    SetChrPos(0xF8, 900, -1750, -7480, 0)
    SetChrPos(0xF9, -200, -1750, -7480, 0)

    def lambda_DB8():
        OP_8E(0xFE, 0x96, 0x0, 0x157C, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_DB8)
    Sleep(300)

    def lambda_DD8():
        OP_8E(0xFE, 0xFFFFFC18, 0x0, 0x11BC, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_DD8)
    Sleep(300)

    def lambda_DF8():
        OP_8E(0xFE, 0x384, 0x0, 0x10CC, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_DF8)
    Sleep(300)

    def lambda_E18():
        OP_8E(0xFE, 0xFFFFFF38, 0x0, 0xC1C, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_E18)
    WaitChrThread(0xF9, 0x1)
    Sleep(500)

    ChrTalk(    #7
        0x101,
        "#1002F#6P玲……！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x8,
        (
            "#263F#5P哼哼。\x01",
            "艾丝蒂尔真是坏孩子。\x02\x03",

            "竟然趁玲不在的时候\x01",
            "从『方舟』逃掉了。\x02\x03",

            "#1305F不过也罢。\x01",
            "反正你现在也来陪我玩了。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_F7F")

    ChrTalk(    #9
        0x107,
        "#063F#6P玲、玲……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x8,
        (
            "#1306F#5P呵呵，提妲\x01",
            "也是特地来玩的吧？\x02\x03",

            "虽然不能请你吃冰淇淋，\x01",
            "不过可以在这里随便放松放松。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x107, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)

    ChrTalk(    #11
        0x107,
        "#065F#6P啊……呜……\x02",
    )

    CloseMessageWindow()
    Jump("loc_F9A")

    label("loc_F7F")


    ChrTalk(    #12
        0x101,
        "#1019F#6P来、来玩……\x02",
    )

    CloseMessageWindow()

    label("loc_F9A")


    ChrTalk(    #13
        0x8,
        (
            "#263F#5P还有……哈哈哈。\x01",
            "终于现身了呢。\x02\x03",

            "#260F我好想你哦，约修亚。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x102,
        (
            "#1035F#6P……没想到能在这种地方\x01",
            "与你再度相会啊。\x02\x03",

            "#1040F你长大了……玲。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x8,
        (
            "#261F#5P呵呵，当然了⊙\x01",
            "玲已经１１岁了嘛。\x02\x03",

            "#265F约修亚也是，一阵子不见\x01",
            "就变得好帅了呢。\x02\x03",

            "虽然眼神不再那样冰冷，\x01",
            "看起来有些怪怪的......\x02\x03",

            "#261F不过，现在的约修亚也不错。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x102,
        "#1053F#6P是吗……谢谢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x101,
        (
            "#1007F#6P真受不了……\x01",
            "你还是那么老气横秋。\x02\x03",

            "#1015F……那个，玲。\x02\x03",

            "我们，是为了阻止『结社』的计划\x01",
            "才来这里的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x8,
        (
            "#263F#5P呵呵，看样子好像确实是这样啊。\x02\x03",

            "#269F反正玲也很怕无聊，\x01",
            "陪你们玩玩也无妨哦。\x02",
        )
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x8, 10)
    SetChrSubChip(0x8, 14)

    def lambda_11D7():
        OP_99(0x8, 0xE, 0x8, 0x5DC)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_11D7)
    WaitChrThread(0x8, 0x1)
    Sleep(500)

    def lambda_11F1():
        OP_99(0x8, 0x8, 0x2, 0x7D0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_11F1)
    Sleep(200)
    Fade(500)

    def lambda_120B():
        OP_6B(4000, 0)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_120B)
    OP_22(0x1F9, 0x0, 0x64)
    WaitChrThread(0x8, 0x1)
    Sleep(500)

    def lambda_122A():
        OP_99(0x8, 0x2, 0x0, 0x5DC)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_122A)
    SetChrChipByIndex(0x8, 4)
    SetChrSubChip(0x8, 0)
    OP_0D()
    Sleep(500)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_12A3")
    OP_62(0xF8, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_12E1")

    label("loc_12A3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_12CA")
    OP_62(0xF8, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_12E1")

    label("loc_12CA")

    OP_62(0xF8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_12E1")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_130D")
    OP_62(0xF9, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_134B")

    label("loc_130D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1334")
    OP_62(0xF9, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_134B")

    label("loc_1334")

    OP_62(0xF9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_134B")

    Sleep(1000)

    ChrTalk(    #19
        0x8,
        (
            "#1306F#5P嘻嘻……\x01",
            "要让我开心一点哦！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x102,
        "#1042F#6P……玲……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x101,
        (
            "#1007F#6P抱歉，我并不是打算\x01",
            "来和玲战斗的。\x02\x03",

            "#1002F而是……有话要对你说。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x8,
        (
            "#264F#5P有话说？\x02\x03",

            "#261F哇，不会是\x01",
            "来讲故事给我听的吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x101,
        (
            "#1003F#6P不是……\x01",
            "是关于让我加入『结社』的事情。\x02\x03",

            "#1025F十分感谢你再一次的盛情邀请，\x01",
            "不过，我还是打算拒绝。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x8,
        (
            "#268F#5P算啦，毕竟你已经和约修亚重逢了，\x01",
            "这也是没办法的事吧。\x02\x03",

            "#269F不过，你最好还是能再重新考虑一下。\x02\x03",

            "就算你们再怎么努力，\x01",
            "也不可能阻止『噬身之蛇』的。\x02\x03",

            "这点，约修亚\x01",
            "应该最清楚不过了吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x102,
        "#1043F#6P……这……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x8,
        (
            "#265F#5P而且只要加入『结社』\x01",
            "艾丝蒂尔会变得更强。\x02\x03",

            "这样就能和玲一样\x01",
            "成为『执行者』哦。\x02\x03",

            "#261F呜呼呼，不觉得这很棒吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x101,
        (
            "#1015F#6P嗯～变得更强\x01",
            "确实很吸引人……\x02\x03",

            "#1007F不过……\x01",
            "我想这样的强并不是真正的强。\x02\x03",

            "至少对我来说是这样。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x8,
        "#264F#5P……咦……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x101,
        (
            "#1006F#6P我的确想变强。\x02\x03",

            "强到能够像妈妈一样，\x01",
            "守护自己珍视的人。\x02\x03",

            "强到可以保护好自己，\x01",
            "不再让约修亚担心。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x102,
        "#1044F#6P艾丝蒂尔……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x101,
        (
            "#1007F#6P但是，一旦加入了『结社』，\x01",
            "我就不再是自己了。\x02\x03",

            "我就不能作为真正的我，而逐渐变强。\x02\x03",

            "#1025F所以，我觉得这是毫无意义的。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x8)
    Sleep(500)

    ChrTalk(    #32
        0x8,
        (
            "#262F#5P……不明白。\x02\x03",

            "艾丝蒂尔所说的东西\x01",
            "玲一点儿也不明白。\x02\x03",

            "真正的我是什么？\x01",
            "那是怎样的东西？\x02",
        )
    )

    CloseMessageWindow()
    OP_8E(0x101, 0x0, 0x0, 0x17DE, 0x7D0, 0x0)
    Sleep(500)

    ChrTalk(    #33
        0x101,
        (
            "#1025F#6P我……\x01",
            "真的很喜欢玲。\x02\x03",

            "爱装成熟，喜欢恶作剧，\x01",
            "还意外地会关心别人……\x02\x03",

            "#1016F虽然被你骗得很惨，\x01",
            "但是我们一点都不恨你哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x8,
        "#264F#5P……艾丝蒂尔……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x101,
        (
            "#1003F#6P但是，正因为如此……\x02\x03",

            "#1007F正因为如此我才\x01",
            "不希望玲待在『结社』。\x02\x03",

            "#1002F如果你长大了，能够以自己的意志\x01",
            "来做出选择，那倒又是另外一回事了……\x02\x03",

            "而你还是孩子，待在\x01",
            "那种地方本身就是错误的。\x02\x03",

            "#1003F如果就这样长大的话，\x01",
            "一切就会变得无法挽回了……\x02\x03",

            "所以……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x8,
        (
            "#1300F#5P…………………………………\x02\x03",

            "#266F……我改变主意了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0x101,
        "#1004F#6P哎……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x102,
        "#1042F#6P……呜……！\x02",
    )

    CloseMessageWindow()
    LoadEffect(0x1, "map\\\\mp009_00.eff")
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    Fade(500)
    OP_6D(250, 0, 7960, 0)
    OP_67(0, 7630, -10000, 0)
    OP_6B(1230, 0)
    OP_6C(32000, 0)
    OP_6E(609, 0)
    OP_8C(0x101, 0, 0)
    OP_0D()
    SetChrFlags(0x8, 0x20)
    SetChrFlags(0x8, 0x4)
    OP_7D(0x0, 0x8, 0x32, 0x1F4)
    OP_22(0x23B, 0x0, 0x64)

    def lambda_1ABD():
        OP_6B(1100, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1ABD)

    def lambda_1ACD():
        OP_96(0xFE, 0xFFFFFE5C, 0x1F4, 0x1FCC, 0x4B0, 0x2EE0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1ACD)
    SetChrSubChip(0x8, 0)
    SetChrChipByIndex(0x8, 4)
    Sleep(100)
    OP_22(0x1F9, 0x0, 0x64)
    OP_8C(0x8, 225, 0)

    def lambda_1B06():
        OP_99(0xFE, 0x1, 0x7, 0xDAC)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_1B06)
    OP_7D(0x0, 0x102, 0x32, 0x1F4)
    SetChrSubChip(0x102, 2)
    SetChrChipByIndex(0x102, 7)

    def lambda_1B28():
        OP_96(0x102, 0xFFFFFEC0, 0x0, 0x19FA, 0x1F4, 0x2EE0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_1B28)
    Sleep(100)
    OP_22(0x1F5, 0x0, 0x64)

    def lambda_1B50():
        OP_99(0xFE, 0x5, 0x7, 0xBB8)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_1B50)
    WaitChrThread(0x8, 0x1)
    WaitChrThread(0x102, 0x0)
    WaitChrThread(0x102, 0x1)
    PlayEffect(0x1, 0xFF, 0x102, 0, 500, 500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0xD6, 0x0, 0x64)
    OP_22(0x9B, 0x0, 0x64)
    OP_7C(0x0, 0xC8, 0xBB8, 0x64)

    def lambda_1BBF():
        OP_9E(0xFE, 0x1E, 0x0, 0x3E8, 0x7D0)
        ExitThread()

    QueueWorkItem(0x8, 3, lambda_1BBF)

    def lambda_1BD9():
        OP_9E(0xFE, 0x1E, 0x0, 0x3E8, 0x7D0)
        ExitThread()

    QueueWorkItem(0x102, 3, lambda_1BD9)

    def lambda_1BF3():
        OP_96(0xFE, 0x258, 0x0, 0x26F2, 0x1F4, 0x2710)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1BF3)
    SetChrFlags(0x102, 0x20)
    SetChrFlags(0x102, 0x1000)

    def lambda_1C1B():
        OP_8F(0xFE, 0xFFFFFC7C, 0x0, 0x14E6, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1C1B)

    def lambda_1C36():
        OP_8F(0xFE, 0x96, 0x0, 0x170C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1C36)

    def lambda_1C51():
        OP_6B(1330, 1000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1C51)
    WaitChrThread(0x8, 0x1)
    ClearChrFlags(0x8, 0x20)
    ClearChrFlags(0x8, 0x4)
    WaitChrThread(0x102, 0x1)
    OP_7D(0x1, 0x8, 0x0, 0x0)
    OP_7D(0x1, 0x102, 0x0, 0x0)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    ChrTalk(    #39
        0x101,
        "#1020F#4P！！！\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x101, 0x2)
    Sleep(300)
    OP_22(0x23B, 0x0, 0x64)

    def lambda_1CB2():
        OP_96(0xFE, 0x3F2, 0x3B6, 0x2F94, 0x5DC, 0x2710)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1CB2)
    OP_8C(0x8, 180, 0)
    Fade(500)
    OP_6D(390, 950, 9200, 0)
    OP_67(0, 4570, -10000, 0)
    OP_6B(2700, 0)
    OP_6C(8000, 0)
    OP_6E(357, 0)
    WaitChrThread(0x8, 0x1)
    OP_22(0x1F9, 0x0, 0x64)
    OP_99(0x8, 0x7, 0xD, 0x5DC)
    SetChrSubChip(0x8, 0)
    SetChrChipByIndex(0x8, 4)
    Sleep(500)

    ChrTalk(    #40
        0x8,
        (
            "#1305F#5P呵呵……不愧是约修亚。\x02\x03",

            "反应速度相当快嘛。\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0xD5, 0x0, 0x64)
    OP_99(0x102, 0x8, 0xC, 0x7D0)
    Sleep(500)

    ChrTalk(    #41
        0x102,
        (
            "#1035F#6P彼此彼此……你也很强。\x02\x03",

            "#1042F看来『歼灭天使』的\x01",
            "别名真是名不虚传。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0x8,
        (
            "#263F#5P对，玲很强的。\x02\x03",

            "比只会藏匿在暗处行动的\x01",
            "『漆黑之牙』强得多哦。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    ChrTalk(    #43
        0x101,
        (
            "#1020F#6P等、等一下玲！\x01",
            "这么突然干什么啊！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0x8,
        (
            "#1306F#5P哼哼，我改变主意了。\x02\x03",

            "#261F既然不能做玲的同伴，\x01",
            "艾丝蒂尔就去死吧。\x02\x03",

            "约修亚，其他所有人都一起。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #45
        0x101,
        (
            "#1019F#6P……去死这种话\x01",
            "可不能随便说的啊！\x02\x03",

            "#1005F真是～气死我了！\x01",
            "我要打你的屁股一百下！\x02",
        )
    )

    CloseMessageWindow()
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrSubChip(0x101, 0)
    SetChrChipByIndex(0x101, 5)
    OP_0D()
    Sleep(500)

    ChrTalk(    #46
        0x102,
        (
            "#1042F#6P艾丝蒂尔，冷静点。\x01",
            "可不能小看她──\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x101,
        (
            "#1005F#6P约修亚你闭嘴！\x01",
            "我这是在教育小孩子！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0x8,
        (
            "#263F#5P嘻嘻，好天真。\x02\x03",

            "虽然我也曾经很喜欢\x01",
            "艾丝蒂尔这点……\x02\x03",

            "#1302F不过现在却很讨厌。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2029():
        OP_6D(470, 0, 7210, 1500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2029)

    def lambda_2041():
        OP_67(0, 5260, -10000, 1500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2041)

    def lambda_2059():
        OP_6B(3340, 1500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2059)

    def lambda_2069():
        OP_6C(25000, 1500)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_2069)

    def lambda_2079():
        OP_6E(301, 1500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_2079)
    SetChrFlags(0x8, 0x2)
    SetChrSubChip(0x8, 6)
    Sleep(1000)
    OP_43(0x9, 0x0, 0x0, 0x2)
    OP_43(0xA, 0x0, 0x0, 0x2)
    OP_43(0xB, 0x0, 0x0, 0x2)
    OP_43(0xC, 0x0, 0x0, 0x2)
    OP_43(0xD, 0x0, 0x0, 0x2)
    OP_43(0xE, 0x0, 0x0, 0x2)
    SetChrPos(0x9, -2140, 1250, 9460, 135)
    SetChrPos(0xA, 3240, 1250, 8880, 225)
    SetChrPos(0xB, 5080, 1250, 4410, 270)
    SetChrPos(0xC, 440, 1000, -330, 0)
    SetChrPos(0xD, -5680, 1250, 1470, 45)
    SetChrPos(0xE, -5200, 1250, 5190, 90)
    OP_9F(0x9, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0xA, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0xB, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0xC, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0xD, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0xE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrFlags(0x9, 0x4)
    SetChrFlags(0xA, 0x4)
    SetChrFlags(0xB, 0x4)
    SetChrFlags(0xC, 0x4)
    SetChrFlags(0xD, 0x4)
    SetChrFlags(0xE, 0x4)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    OP_22(0x211, 0x0, 0x64)
    OP_22(0x215, 0x0, 0x64)

    def lambda_21B0():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_21B0)

    def lambda_21C2():
        OP_8F(0xFE, 0xFFFFF7A4, 0xFA, 0x24F4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_21C2)
    Sleep(50)
    OP_22(0x211, 0x0, 0x64)
    OP_22(0x215, 0x0, 0x64)

    def lambda_21EC():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_21EC)

    def lambda_21FE():
        OP_8F(0xFE, 0xCA8, 0xFA, 0x22B0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_21FE)
    Sleep(50)
    OP_22(0x211, 0x0, 0x64)
    OP_22(0x215, 0x0, 0x64)

    def lambda_2228():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_2228)

    def lambda_223A():
        OP_8F(0xFE, 0x13D8, 0xFA, 0x113A, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_223A)
    Sleep(50)
    OP_22(0x211, 0x0, 0x64)
    OP_22(0x215, 0x0, 0x64)

    def lambda_2264():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_2264)

    def lambda_2276():
        OP_8F(0xFE, 0x1B8, 0x0, 0xFFFFFEB6, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_2276)
    Sleep(50)
    OP_22(0x211, 0x0, 0x64)
    OP_22(0x215, 0x0, 0x64)

    def lambda_22A0():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_22A0)

    def lambda_22B2():
        OP_8F(0xFE, 0xFFFFE9D0, 0xFA, 0x5BE, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 2, lambda_22B2)
    Sleep(50)
    OP_22(0x211, 0x0, 0x64)
    OP_22(0x215, 0x0, 0x64)

    def lambda_22DC():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_22DC)

    def lambda_22EE():
        OP_8F(0xFE, 0xFFFFEBB0, 0xFA, 0x1446, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_22EE)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(100)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_235D")
    OP_62(0xF8, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_239B")

    label("loc_235D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2384")
    OP_62(0xF8, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_239B")

    label("loc_2384")

    OP_62(0xF8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_239B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_23C2")
    OP_62(0xF9, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_2400")

    label("loc_23C2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_23E9")
    OP_62(0xF9, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_2400")

    label("loc_23E9")

    OP_62(0xF9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_2400")

    Sleep(1000)
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrSubChip(0xF8, 0)
    SetChrChipByIndex(0xF8, 8)
    SetChrSubChip(0xF9, 0)
    SetChrChipByIndex(0xF9, 9)
    OP_0D()

    def lambda_242A():
        OP_8C(0xFE, 270, 600)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_242A)

    def lambda_2438():
        OP_8C(0xFE, 180, 600)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_2438)
    OP_8C(0xF8, 90, 600)
    WaitChrThread(0x101, 0x0)
    Sleep(1000)

    ChrTalk(    #49
        0x8,
        (
            "#263F#6PＮｏ．ⅩⅤ──\x01",
            "『歼灭天使』玲。\x02\x03",

            "#1304F现在开始歼灭敌方集团。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_24A2():
        OP_6D(600, 0, 6760, 300)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_24A2)

    def lambda_24BA():
        OP_6B(2500, 300)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_24BA)
    OP_22(0xD5, 0x0, 0x64)
    ClearChrFlags(0x8, 0x2)
    SetChrSubChip(0x8, 2)

    def lambda_24D9():
        OP_96(0xFE, 0x28, 0x0, 0x19B4, 0x3E8, 0x1F40)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_24D9)
    Sleep(50)
    SetChrChipByIndex(0x9, 12)

    def lambda_2501():
        OP_8F(0xFE, 0xFFFFFC36, 0x0, 0x1AD6, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_2501)
    SetChrChipByIndex(0xA, 12)

    def lambda_2521():
        OP_8F(0xFE, 0x460, 0x0, 0x19DC, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_2521)
    SetChrChipByIndex(0xB, 12)

    def lambda_2541():
        OP_8F(0xFE, 0x712, 0x0, 0x11BC, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_2541)
    SetChrChipByIndex(0xC, 12)

    def lambda_2561():
        OP_8F(0xFE, 0x0, 0x0, 0x96A, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_2561)
    SetChrChipByIndex(0xD, 12)

    def lambda_2581():
        OP_8F(0xFE, 0xFFFFF8D0, 0x0, 0xD66, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_2581)
    SetChrChipByIndex(0xE, 12)

    def lambda_25A1():
        OP_8F(0xFE, 0xFFFFF876, 0x0, 0x13D8, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_25A1)
    WaitChrThread(0x101, 0x0)
    OP_44(0x8, 0x1)
    OP_44(0x9, 0x1)
    OP_44(0xA, 0x1)
    OP_44(0xB, 0x1)
    OP_44(0xC, 0x1)
    OP_44(0xD, 0x1)
    OP_44(0xE, 0x1)
    Battle(0x3FD, 0x0, 0x1, 0x0, 0xFF)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (1, "loc_25F0"),
        (SWITCH_DEFAULT, "loc_25F5"),
    )


    label("loc_25F0")

    OP_B4(0x0)
    Jump("loc_25F5")

    label("loc_25F5")

    Return()

    # Function_6_911 end

    def Function_7_25F6(): pass

    label("Function_7_25F6")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    Sleep(1000)
    OP_44(0x8, 0x1)
    OP_44(0x9, 0x1)
    OP_44(0xA, 0x1)
    OP_44(0xB, 0x1)
    OP_44(0xC, 0x1)
    OP_44(0xD, 0x1)
    OP_44(0xE, 0x1)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xE, 0x80)
    OP_71(0x0, 0x4)
    OP_71(0x1, 0x4)
    OP_71(0x9, 0x4)
    Call(0, 11)
    OP_D2(0x270246, 0x270250, 0xA)
    OP_D2(0x270244, 0x27024E, 0xB)
    OP_D2(0x27023F, 0x270249, 0xD)
    OP_6F(0x3, 0)
    OP_6F(0x4, 0)
    OP_6F(0x5, 0)
    OP_6F(0x6, 0)
    OP_6F(0x7, 0)
    OP_70(0x3, 0x8)
    OP_70(0x4, 0x8)
    OP_70(0x5, 0x8)
    OP_70(0x6, 0x8)
    OP_70(0x7, 0x8)
    LoadEffect(0x0, "map\\\\mp061_00.eff")
    PlayEffect(0x0, 0xFF, 0xFF, 0, 1300, 13650, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrPos(0x101, 600, 0, 4500, 0)
    SetChrPos(0x102, -600, 0, 3600, 0)
    SetChrPos(0xF8, 1300, 0, 3200, 0)
    SetChrPos(0xF9, 0, 0, 2200, 0)
    SetChrSubChip(0x101, 0)
    SetChrChipByIndex(0x101, 5)
    SetChrSubChip(0x102, 0)
    SetChrChipByIndex(0x102, 6)
    SetChrSubChip(0xF8, 1)
    SetChrChipByIndex(0xF8, 8)
    SetChrSubChip(0xF9, 1)
    SetChrChipByIndex(0xF9, 9)
    SetChrPos(0x8, 1220, 950, 12420, 180)
    ClearChrFlags(0x8, 0x80)
    SetChrSubChip(0x8, 0)
    SetChrChipByIndex(0x8, 4)
    OP_6D(400, 950, 9010, 0)
    OP_67(0, 3170, -10000, 0)
    OP_6B(4000, 0)
    OP_6C(4000, 0)
    OP_6E(262, 0)
    Sleep(500)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #50
        0x8,
        (
            "#264F#5P哎呀，带来的小家伙们\x01",
            "全部都被干掉了啊……\x02\x03",

            "#1305F嘻嘻，挺能撑的嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0x101,
        (
            "#1019F#6P你、你闹够了没有啊！\x02\x03",

            "#1005F做这种事\x01",
            "玲真的很开心吗！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0x8,
        (
            "#263F#5P哈哈哈，当然了。\x02\x03",

            "#1306F玲，最喜欢\x01",
            "看人痛苦的样子了。\x02\x03",

            "似乎只有这样才能\x01",
            "填补自己空虚的灵魂。\x02\x03",

            "#261F玲，也喜欢\x01",
            "听人痛苦的声音。\x02\x03",

            "他人的呻吟会令玲沉醉梦乡。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0x101,
        "#1020F#6P……呜……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0x102,
        "#1043F#6P是吗……你至今还……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0x8,
        "#1302F#5P……约修亚你闭嘴。\x02",
    )

    CloseMessageWindow()

    def lambda_2980():
        OP_6B(3800, 10000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2980)
    Sleep(500)
    OP_1D(0x53)
    Sleep(500)

    ChrTalk(    #56
        0x8,
        (
            "#1305F#5P唔，艾丝蒂尔。\x02\x03",

            "玲小的时候，\x01",
            "曾有过假的爸爸妈妈。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0x101,
        "#1026F#6P咦……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0x8,
        (
            "#263F#5P假的爸爸妈妈。\x02\x03",

            "#260F虽然我很喜欢他们，\x01",
            "但是他们在生意场上好像失败了。\x02\x03",

            "所以他们不得不把玲\x01",
            "交给了那些坏人。\x02\x03",

            "#261F他们一边哭着一边不断地说：\x01",
            "『我们一定会来接你的』…\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0x101,
        "#1026F#6P然、然后………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0x8,
        (
            "#268F#5P玲被交给那些人之后，\x01",
            "他们让玲做各式各样的事。\x02\x03",

            "玲很快就习惯了大部分的事情，\x01",
            "但只有疼痛，却一直都无法忍受…\x02\x03",

            "#1300F虽然也有同龄的孩子，\x01",
            "但往往很快就搞坏了身体，\x01",
            "很多就这样死了。\x02\x03",

            "#1305F这种生活持续了半年左右。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0x101,
        "#1022F#6P……呜……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2BDC")

    ChrTalk(    #62
        0x107,
        "#065F#6P……玲…………\x02",
    )

    CloseMessageWindow()

    label("loc_2BDC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2C11")

    ChrTalk(    #63
        0x109,
        "#1067F#6P………………………………\x02",
    )

    CloseMessageWindow()

    label("loc_2C11")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2C39")

    ChrTalk(    #64
        0x106,
        "#057F#6P混帐东西……\x02",
    )

    CloseMessageWindow()

    label("loc_2C39")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2C65")

    ChrTalk(    #65
        0x103,
        "#522F#6P……太过分了……\x02",
    )

    CloseMessageWindow()

    label("loc_2C65")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2C8F")

    ChrTalk(    #66
        0x105,
        "#049F#6P……女神啊……\x02",
    )

    CloseMessageWindow()

    label("loc_2C8F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2CBF")

    ChrTalk(    #67
        0x108,
        "#077F#6P……这些邪道…………\x02",
    )

    CloseMessageWindow()

    label("loc_2CBF")


    ChrTalk(    #68
        0x8,
        (
            "#265F#5P结果就是，\x01",
            "我的爸爸妈妈都是冒牌货。\x02\x03",

            "如果是真的，当玲觉得痛的时候\x01",
            "应该会马上来接我才对。\x02\x03",

            "#261F对吧，艾丝蒂尔？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0x101,
        "#1027F#6P………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0x8,
        (
            "#263F#5P哼哼，不过无所谓了。\x02\x03",

            "#1305F约修亚和莱维\x01",
            "代替他们来接玲了。\x02\x03",

            "他们把坏人们全部杀光了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0x101,
        "#1026F#6P咦……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0x102,
        (
            "#1043F#6P……『结社』偶尔\x01",
            "也会摧毁一些卑劣的犯罪组织。\x02\x03",

            "这当然不是为了正义，\x01",
            "而是为了将其纳入自己的秩序中。\x02\x03",

            "#1035F那次也是这类任务之一吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0x101,
        "#1026F#6P这样啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0x8,
        (
            "#263F#5P被带到『结社』之后\x01",
            "玲学会了各式各样的事情。\x02\x03",

            "#260F约修亚教了我隐形术，\x01",
            "莱维教了我武术。\x02\x03",

            "其他的人们，也各自\x01",
            "将擅长的本领教给我。\x02\x03",

            "#265F接着在『十三工房』\x01",
            "学会了和人偶做朋友的方法……\x02\x03",

            "#261F──然后玲\x01",
            "遇到了真正的爸爸和妈妈『帕蒂尔·玛蒂尔』。\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x101, 0x0)
    Sleep(500)
    Fade(250)
    SetChrChipByIndex(0x8, 11)
    OP_51(0x8, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_22(0xD5, 0x0, 0x64)
    OP_51(0x8, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(240)
    Sleep(500)

    def lambda_2FC9():

        label("loc_2FC9")

        OP_7C(0x0, 0x14, 0xBB8, 0x64)
        OP_48()
        Jump("loc_2FC9")

    QueueWorkItem2(0x10, 3, lambda_2FC9)
    LoadEffect(0x1, "map\\\\mp021_00.eff")
    LoadEffect(0x2, "map\\\\mp064_01.eff")
    LoadEffect(0x3, "map\\\\mp065_01.eff")
    OP_22(0x113, 0x0, 0x46)
    OP_A1(0x10, 0x0)
    SetChrPos(0x10, 10580, 14000, 9330, 225)
    OP_71(0x0, 0x20)
    OP_B0(0x0, 0x14)
    OP_6F(0x0, 201)
    OP_70(0x0, 0xDC)
    Sleep(500)
    OP_72(0x0, 0x4)
    Sleep(500)
    Fade(500)
    OP_6D(10320, 10980, 5440, 0)
    OP_67(0, -3080, -10000, 0)
    OP_6B(2320, 0)
    OP_6C(359000, 0)
    OP_6E(390, 0)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0x101, 1200, 0, 1600, 45)
    SetChrPos(0x102, 600, 0, 2100, 45)
    SetChrPos(0xF8, 800, 0, 300, 45)
    SetChrPos(0xF9, -750, 0, 1800, 45)
    SetChrSubChip(0x101, 0)
    SetChrChipByIndex(0x101, 5)
    SetChrSubChip(0x102, 0)
    SetChrChipByIndex(0x102, 6)
    SetChrSubChip(0xF8, 0)
    SetChrChipByIndex(0xF8, 8)
    SetChrSubChip(0xF9, 0)
    SetChrChipByIndex(0xF9, 9)
    SetChrSubChip(0x8, 0)
    SetChrChipByIndex(0x8, 3)
    ClearChrFlags(0x10, 0x80)
    SetChrFlags(0x10, 0x1)
    OP_51(0x10, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x1770), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10, 0x34, (scpexpr(EXPR_PUSH_LONG, 0xEA60), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearMapFlags(0x40)
    OP_24(0x113, 0x50)

    def lambda_3162():
        OP_8F(0xFE, 0x2954, 0x1F4, 0x2472, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_3162)
    Sleep(100)
    OP_24(0x113, 0x5A)

    def lambda_3186():
        OP_6D(10350, 5820, 6780, 5000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_3186)

    def lambda_319E():
        OP_67(0, 6200, -10000, 5000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_319E)

    def lambda_31B6():
        OP_6B(2320, 5000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_31B6)

    def lambda_31C6():
        OP_6E(390, 5000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_31C6)
    Play3DEffect(0x2, 0x0, 0x0, "Frame86__jet_0", 0x0, 0xFFFFFD44, 0x0, 0x3C, 0xFFA6, 0xB4, 0x3E8, 0x3E8, 0x3E8, 0x0)
    Play3DEffect(0x2, 0x1, 0x0, "Frame87__jet_1", 0x0, 0xFFFFFD44, 0x0, 0x1E, 0x46, 0xFF4C, 0x3E8, 0x3E8, 0x3E8, 0x0)

    def lambda_3240():
        OP_8F(0xFE, 0x2954, 0x3E8, 0x2472, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_3240)
    Sleep(100)
    OP_24(0x113, 0x64)

    def lambda_3264():
        OP_8F(0xFE, 0x2954, 0x1F4, 0x2472, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_3264)
    Sleep(100)

    def lambda_3284():
        OP_8F(0xFE, 0x2954, 0x1F4, 0x2472, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_3284)
    Sleep(4000)
    Fade(500)
    OP_6F(0x0, 1)
    OP_70(0x0, 0x28)
    PlayEffect(0x1, 0x2, 0x10, 0, -500, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0xCC, 0x0, 0x64)

    def lambda_32F1():
        OP_8F(0xFE, 0x2954, 0x1F4, 0x2472, 0x708, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_32F1)
    WaitChrThread(0x10, 0x1)
    OP_44(0x10, 0x3)
    OP_72(0x0, 0x20)
    OP_82(0x0, 0x2)
    OP_82(0x1, 0x2)
    OP_82(0x2, 0x2)
    OP_23(0x113)
    Fade(500)
    OP_6D(10600, 250, 14510, 0)
    OP_67(0, 4040, -10000, 0)
    OP_6B(5260, 0)
    OP_6C(35000, 0)
    OP_6E(227, 0)
    OP_6F(0x0, 221)
    OP_70(0x0, 0xF0)
    OP_7C(0x0, 0x12C, 0x1388, 0x3E8)
    OP_22(0x88, 0x0, 0x64)
    OP_22(0xF5, 0x0, 0x64)
    OP_73(0x0)
    OP_71(0x0, 0x20)
    OP_6F(0x0, 1)
    OP_70(0x0, 0x28)
    OP_D8(0x0, 0x1F4)
    WaitChrThread(0x101, 0x0)
    Sleep(500)
    Sleep(500)
    OP_22(0x3D4, 0x0, 0x64)
    Sleep(1500)
    Sleep(500)

    ChrTalk(    #75
        0x101,
        "#1020F#5P啊……！\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3410")

    ChrTalk(    #76
        0x109,
        "#1069F#5P那时的人形装甲吗……！\x02",
    )

    CloseMessageWindow()
    Jump("loc_34DF")

    label("loc_3410")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3445")

    ChrTalk(    #77
        0x106,
        "#054F#5P那时的人形装甲啊……！\x02",
    )

    CloseMessageWindow()
    Jump("loc_34DF")

    label("loc_3445")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_347C")

    ChrTalk(    #78
        0x107,
        "#065F#5P那、那时的人形兵器……！\x02",
    )

    CloseMessageWindow()
    Jump("loc_34DF")

    label("loc_347C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_34AF")

    ChrTalk(    #79
        0x103,
        "#024F#5P那时的人形兵器……！\x02",
    )

    CloseMessageWindow()
    Jump("loc_34DF")

    label("loc_34AF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_34DF")

    ChrTalk(    #80
        0x105,
        "#042F#5P那时的人形兵器……！\x02",
    )

    CloseMessageWindow()

    label("loc_34DF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3508")

    ChrTalk(    #81
        0x108,
        "#077F#5P好大……！\x02",
    )

    CloseMessageWindow()
    Jump("loc_35C5")

    label("loc_3508")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3537")

    ChrTalk(    #82
        0x105,
        "#042F#5P怎么这么大……！\x02",
    )

    CloseMessageWindow()
    Jump("loc_35C5")

    label("loc_3537")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3566")

    ChrTalk(    #83
        0x103,
        "#523F#5P怎么这么大……！\x02",
    )

    CloseMessageWindow()
    Jump("loc_35C5")

    label("loc_3566")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3597")

    ChrTalk(    #84
        0x107,
        "#065F#5P怎、怎么这么大……\x02",
    )

    CloseMessageWindow()
    Jump("loc_35C5")

    label("loc_3597")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_35C5")

    ChrTalk(    #85
        0x106,
        "#054F#5P怎么这么大啊……！\x02",
    )

    CloseMessageWindow()

    label("loc_35C5")


    ChrTalk(    #86
        0x102,
        (
            "#1046F#5P极限级战略人形兵器\x01",
            "『帕蒂尔·玛蒂尔』……！\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x8, 0)
    SetChrChipByIndex(0x8, 13)
    ClearChrFlags(0x8, 0x1)
    SetChrFlags(0x8, 0x4)
    OP_22(0xA3, 0x0, 0x64)

    def lambda_361E():
        OP_6D(10070, 250, 13790, 800)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_361E)
    OP_96(0x8, 0xFE6, 0xE10, 0x1BB2, 0xFA0, 0x1F40)
    SetChrSubChip(0x8, 0)
    SetChrChipByIndex(0x8, 4)
    OP_22(0xA4, 0x0, 0x64)
    Sleep(300)
    SetChrFlags(0x8, 0x10)
    OP_8C(0x8, 225, 400)
    ClearChrFlags(0x8, 0x10)
    Sleep(500)

    ChrTalk(    #87
        0x8,
        (
            "#1306F#5P让还是孩子的玲待在『结社』\x01",
            "本身就是一种错误……？\x02\x03",

            "如果就这样长大的话，\x01",
            "一切都会变得无法挽回……？\x02",
        )
    )

    CloseMessageWindow()
    OP_72(0x0, 0x20)
    OP_6F(0x0, 461)
    OP_70(0x0, 0x1E0)
    OP_22(0x115, 0x0, 0x64)
    OP_73(0x0)
    OP_71(0x0, 0x20)
    OP_D8(0x0, 0x1F4)
    OP_6F(0x0, 381)
    OP_70(0x0, 0x1A4)
    Sleep(500)

    def lambda_371F():
        OP_6D(12860, 250, 16720, 1000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_371F)

    def lambda_3737():
        OP_67(0, 3800, -10000, 1000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3737)

    def lambda_374F():
        OP_6B(5000, 1000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_374F)

    def lambda_375F():
        OP_6C(35000, 1000)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_375F)

    def lambda_376F():
        OP_6E(227, 1000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_376F)
    OP_22(0xA3, 0x0, 0x64)
    SetChrSubChip(0x8, 0)
    SetChrChipByIndex(0x8, 13)

    def lambda_378E():
        OP_99(0xFE, 0x0, 0x2, 0x9C4)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_378E)
    OP_96(0x8, 0x1C98, 0xC80, 0x2774, 0x9C4, 0x1F40)
    OP_CF(0x8, 0x0, "Frame85__ren")
    OP_51(0x8, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xA5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_22(0xA4, 0x0, 0x64)
    WaitChrThread(0x8, 0x2)
    SetChrFlags(0x8, 0x10)
    SetChrFlags(0x8, 0x2)
    SetChrSubChip(0x8, 6)
    SetChrChipByIndex(0x8, 3)
    WaitChrThread(0x101, 0x1)
    Sleep(500)

    ChrTalk(    #88
        0x8,
        (
            "#1301F#5P全都是骗人的！\x02\x03",

            "被『结社』收留之后，\x01",
            "玲才遇到真正的爸爸妈妈！\x02\x03",

            "才能成为这世上最幸福的女孩子！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0x101,
        "#1002F#5P……玲……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0x8,
        (
            "#263F#5P如果艾丝蒂尔你想要否定这点，\x01",
            "你就是玲的敌人……\x02\x03",

            "#1304F被爸爸妈妈捏碎，\x01",
            "在痛苦中死去吧！\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    Battle(0x453, 0x0, 0x0, 0x0, 0xFF)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (1, "loc_38FC"),
        (SWITCH_DEFAULT, "loc_3901"),
    )


    label("loc_38FC")

    OP_B4(0x0)
    Jump("loc_3901")

    label("loc_3901")

    Return()

    # Function_7_25F6 end

    def Function_8_3902(): pass

    label("Function_8_3902")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_71(0x0, 0x4)
    OP_71(0x1, 0x4)
    OP_71(0x9, 0x4)
    Call(0, 11)
    OP_D2(0x270246, 0x270250, 0xA)
    OP_D2(0x270244, 0x27024E, 0xB)
    OP_6F(0x3, 0)
    OP_6F(0x4, 0)
    OP_6F(0x5, 0)
    OP_6F(0x6, 0)
    OP_6F(0x7, 0)
    OP_70(0x3, 0x8)
    OP_70(0x4, 0x8)
    OP_70(0x5, 0x8)
    OP_70(0x6, 0x8)
    OP_70(0x7, 0x8)
    LoadEffect(0x0, "map\\\\mp061_00.eff")
    LoadEffect(0x1, "map\\\\mp021_00.eff")
    LoadEffect(0x2, "map\\\\mp064_01.eff")
    LoadEffect(0x3, "map\\\\mp065_01.eff")
    PlayEffect(0x0, 0x0, 0xFF, 0, 1300, 13650, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_72(0x0, 0x4)
    OP_A1(0x10, 0x0)
    SetChrPos(0x10, 10580, 500, 9330, 225)
    OP_71(0x0, 0x20)
    OP_B0(0x0, 0x14)
    OP_6F(0x0, 381)
    OP_70(0x0, 0x1A4)
    ClearChrFlags(0x10, 0x80)
    SetChrFlags(0x10, 0x1)
    OP_51(0x10, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x1770), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10, 0x34, (scpexpr(EXPR_PUSH_LONG, 0xEA60), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearMapFlags(0x40)
    SetChrPos(0x101, 1200, 0, 1200, 45)
    SetChrPos(0x102, 870, 0, 2560, 45)
    SetChrPos(0xF8, -50, 0, 110, 45)
    SetChrPos(0xF9, -450, 0, 1740, 45)
    SetChrSubChip(0x101, 0)
    SetChrChipByIndex(0x101, 5)
    SetChrSubChip(0x102, 0)
    SetChrChipByIndex(0x102, 6)
    SetChrSubChip(0xF8, 0)
    SetChrChipByIndex(0xF8, 8)
    SetChrSubChip(0xF9, 0)
    SetChrChipByIndex(0xF9, 9)
    SetChrPos(0x8, 1220, 950, 12420, 180)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x10)
    SetChrFlags(0x8, 0x2)
    SetChrSubChip(0x8, 7)
    SetChrChipByIndex(0x8, 3)
    ClearChrFlags(0x8, 0x1)
    OP_CF(0x8, 0x0, "Frame85__ren")
    OP_6D(4920, 2480, 5190, 0)
    OP_67(0, 3420, -10000, 0)
    OP_6B(4470, 0)
    OP_6C(15000, 0)
    OP_6E(243, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3B97")

    ChrTalk(    #91
        0x109,
        "#1070F呜……怎么这么坚固！\x02",
    )

    CloseMessageWindow()
    Jump("loc_3C5A")

    label("loc_3B97")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3BC9")

    ChrTalk(    #92
        0x106,
        "#057F可恶……怎么这么坚固！\x02",
    )

    CloseMessageWindow()
    Jump("loc_3C5A")

    label("loc_3BC9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3BFB")

    ChrTalk(    #93
        0x107,
        "#561F啊呜……太坚固了啦……\x02",
    )

    CloseMessageWindow()
    Jump("loc_3C5A")

    label("loc_3BFB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3C2B")

    ChrTalk(    #94
        0x103,
        "#523F呜，怎么这么坚固啊！\x02",
    )

    CloseMessageWindow()
    Jump("loc_3C5A")

    label("loc_3C2B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3C5A")

    ChrTalk(    #95
        0x105,
        "#043F……怎么这么坚固……！\x02",
    )

    CloseMessageWindow()

    label("loc_3C5A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3C9D")

    ChrTalk(    #96
        0x108,
        (
            "#077F力量和装甲\x01",
            "全都在『幻想乐曲』之上吗……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3DAA")

    label("loc_3C9D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3CE4")

    ChrTalk(    #97
        0x105,
        (
            "#043F无论力量还是装甲，\x01",
            "都在『幻想乐曲』之上……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3DAA")

    label("loc_3CE4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3D25")

    ChrTalk(    #98
        0x103,
        (
            "#523F力量和装甲\x01",
            "都在『幻想乐曲』之上啊……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3DAA")

    label("loc_3D25")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3D68")

    ChrTalk(    #99
        0x107,
        (
            "#065F力量和装甲\x01",
            "竟然都在『幻想乐曲』之上……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3DAA")

    label("loc_3D68")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3DAA")

    ChrTalk(    #100
        0x106,
        (
            "#057F力量和装甲\x01",
            "都凌驾在『幻想乐曲』之上啊……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3DAA")


    ChrTalk(    #101
        0x8,
        (
            "#1302F#6P……真难缠啊。\x02\x03",

            "#263F好吧，我玩腻了。\x02\x03",

            "#1304F『帕蒂尔·玛蒂尔』！\x01",
            "以最大能量将艾丝蒂尔他们一举歼灭——\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    OP_22(0x99, 0x0, 0x64)
    OP_23(0xEB)
    OP_1F(0x5A, 0x7D0)
    Fade(500)
    OP_6B(4270, 0)
    OP_82(0x0, 0x2)
    OP_82(0x81, 0x2)
    PlayEffect(0x82, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_82(0x83, 0x2)
    PlayEffect(0x84, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_79(0x0, 0x2)
    OP_79(0x1, 0x2)
    OP_79(0x2, 0x2)
    OP_79(0x3, 0x2)
    OP_79(0x4, 0x2)
    OP_7B()
    Sleep(1000)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3F10")
    OP_62(0xF8, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_3F4E")

    label("loc_3F10")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3F37")
    OP_62(0xF8, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_3F4E")

    label("loc_3F37")

    OP_62(0xF8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_3F4E")

    Sleep(50)
    OP_62(0x8, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3FB2")
    OP_62(0xF9, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_3FF0")

    label("loc_3FB2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3FD9")
    OP_62(0xF9, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_3FF0")

    label("loc_3FD9")

    OP_62(0xF9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_3FF0")

    Sleep(1000)

    def lambda_3FFB():
        OP_6D(2470, 950, 15540, 2000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_3FFB)

    def lambda_4013():
        OP_67(0, 3980, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4013)

    def lambda_402B():
        OP_6B(4400, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_402B)
    WaitChrThread(0x101, 0x0)
    OP_72(0x3, 0x20)
    OP_6F(0x3, 0)
    OP_70(0x3, 0x3C)
    Sleep(500)
    OP_72(0x4, 0x20)
    OP_6F(0x4, 0)
    OP_70(0x4, 0x3C)
    Sleep(100)
    OP_72(0x5, 0x20)
    OP_6F(0x5, 0)
    OP_70(0x5, 0x3C)
    Sleep(100)
    OP_72(0x6, 0x20)
    OP_6F(0x6, 0)
    OP_70(0x6, 0x3C)
    Sleep(100)
    OP_72(0x7, 0x20)
    OP_6F(0x7, 0)
    OP_70(0x7, 0x3C)
    SetChrChipByIndex(0x101, 65535)
    SetChrSubChip(0x101, 0)
    SetChrChipByIndex(0x102, 65535)
    SetChrSubChip(0x102, 0)

    def lambda_40C7():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_40C7)

    def lambda_40D5():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_40D5)
    Sleep(100)
    SetChrChipByIndex(0xF8, 65535)
    SetChrSubChip(0xF8, 0)
    SetChrChipByIndex(0xF9, 65535)
    SetChrSubChip(0xF9, 0)

    def lambda_40FC():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_40FC)
    OP_8C(0xF9, 0, 400)

    ChrTalk(    #102
        0x8,
        "#264F#8P啊……\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    OP_1F(0x64, 0x7D0)
    Fade(1000)
    OP_6D(5030, 3860, 11650, 0)
    OP_67(0, 1590, -10000, 0)
    OP_6B(4500, 0)
    OP_6C(45000, 0)
    OP_6E(363, 0)
    OP_0D()

    def lambda_4173():
        OP_6B(5500, 5000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_4173)
    Sleep(500)
    OP_22(0x139, 0x0, 0x64)
    LoadEffect(0x2, "map\\mp049_02.eff")
    PlayEffect(0x2, 0x2, 0xFF, 0, 0, 6720, 0, 0, 0, 550, 550, 550, 0xFF, 0, 0, 0, 0)
    Sleep(800)
    OP_82(0x80, 0x0)
    Sleep(1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetMapFlags(0x2000000)
    OP_A2(0x10F0)
    NewScene("ED6_DT21/C1707   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_8_3902 end

    def Function_9_41F9(): pass

    label("Function_9_41F9")

    OP_96(0xFE, 0x258, 0x0, 0x26F2, 0x1F4, 0x2710)
    OP_96(0xFE, 0x3F2, 0x3B6, 0x2F94, 0x5DC, 0x2710)
    ClearChrFlags(0x8, 0x20)
    ClearChrFlags(0x8, 0x4)
    Return()

    # Function_9_41F9 end

    def Function_10_4232(): pass

    label("Function_10_4232")

    OP_96(0xFE, 0x1CC, 0x0, 0x1BB2, 0x3E8, 0x2EE0)
    OP_96(0xFE, 0x2E4, 0x0, 0x198C, 0x3E8, 0x2EE0)
    Return()

    # Function_10_4232 end

    def Function_11_4261(): pass

    label("Function_11_4261")

    Switch(
        (scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_END)),
        (2, "loc_4282"),
        (5, "loc_428F"),
        (4, "loc_429C"),
        (6, "loc_42A9"),
        (7, "loc_42B6"),
        (8, "loc_42C3"),
        (SWITCH_DEFAULT, "loc_42D0"),
    )


    label("loc_4282")

    OP_D2(0x701D0, 0x701DC, 0x8)
    Jump("loc_42D0")

    label("loc_428F")

    OP_D2(0x70218, 0x70224, 0x8)
    Jump("loc_42D0")

    label("loc_429C")

    OP_D2(0x70200, 0x7020C, 0x8)
    Jump("loc_42D0")

    label("loc_42A9")

    OP_D2(0x70230, 0x7023C, 0x8)
    Jump("loc_42D0")

    label("loc_42B6")

    OP_D2(0x70248, 0x70254, 0x8)
    Jump("loc_42D0")

    label("loc_42C3")

    OP_D2(0x270176, 0x270183, 0x8)
    Jump("loc_42D0")

    label("loc_42D0")

    Switch(
        (scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_END)),
        (2, "loc_42F1"),
        (5, "loc_42FE"),
        (4, "loc_430B"),
        (6, "loc_4318"),
        (7, "loc_4325"),
        (8, "loc_4332"),
        (SWITCH_DEFAULT, "loc_433F"),
    )


    label("loc_42F1")

    OP_D2(0x701D0, 0x701DC, 0x9)
    Jump("loc_433F")

    label("loc_42FE")

    OP_D2(0x70218, 0x70224, 0x9)
    Jump("loc_433F")

    label("loc_430B")

    OP_D2(0x70200, 0x7020C, 0x9)
    Jump("loc_433F")

    label("loc_4318")

    OP_D2(0x70230, 0x7023C, 0x9)
    Jump("loc_433F")

    label("loc_4325")

    OP_D2(0x70248, 0x70254, 0x9)
    Jump("loc_433F")

    label("loc_4332")

    OP_D2(0x270176, 0x270183, 0x9)
    Jump("loc_433F")

    label("loc_433F")

    Return()

    # Function_11_4261 end

    def Function_12_4340(): pass

    label("Function_12_4340")

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
        (0, "loc_43BA"),
        (1, "loc_43C0"),
        (SWITCH_DEFAULT, "loc_43C6"),
    )


    label("loc_43BA")

    OP_A2(0x1200)
    Jump("loc_43C6")

    label("loc_43C0")

    OP_A2(0x1201)
    Jump("loc_43C6")

    label("loc_43C6")

    Return()

    # Function_12_4340 end

    def Function_13_43C7(): pass

    label("Function_13_43C7")

    FadeToDark(0, 0, -1)
    OP_6D(-66940, 250, 36210, 0)
    OP_67(0, 6500, -10000, 0)
    OP_6B(3700, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    Sleep(200)
    FadeToBright(0, 0)
    OP_0D()
    OP_C9(0x0, 0x4, 0x0, 0x1, 0xFF, 0xFF, 0x5, 0x2, 0x6, 0x4, 0x7, 0x8, 0xFFFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    FadeToDark(0, 0, -1)
    OP_69(0x0, 0x0)
    Return()

    # Function_13_43C7 end

    SaveToFile()

Try(main)

from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'R1402   ._SN',
        MapName             = 'Bose',
        Location            = 'R1402.x',
        MapIndex            = 58,
        MapDefaultBGM       = "ed60029",
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
        '安赛尔新道方向',                       # 9
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


    DeclNpc(
        X                   = 1070,
        Z                   = -600,
        Y                   = -32720,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0xFF,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclEvent(
        X                   = -3000,
        Y                   = -2000,
        Z                   = -22500,
        Range               = 5000,
        Unknown_10          = 0xBB8,
        Unknown_14          = 0xFFFFADF8,
        Unknown_18          = 0x0,
        Unknown_1C          = 6,
    )

    DeclEvent(
        X                   = -16000,
        Y                   = -3500,
        Z                   = 5000,
        Range               = 29380,
        Unknown_10          = 0xBB8,
        Unknown_14          = 0x251C,
        Unknown_18          = 0x0,
        Unknown_1C          = 7,
    )

    DeclEvent(
        X                   = -2200,
        Y                   = 3000,
        Z                   = 19000,
        Range               = 4200,
        Unknown_10          = 0x1388,
        Unknown_14          = 0x4E20,
        Unknown_18          = 0x0,
        Unknown_1C          = 10,
    )


    DeclActor(
        TriggerX            = -13360,
        TriggerZ            = 40,
        TriggerY            = -930,
        TriggerRange        = 1000,
        ActorX              = -14080,
        ActorZ              = 40,
        ActorY              = -960,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 2,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 26480,
        TriggerZ            = -20,
        TriggerY            = 8820,
        TriggerRange        = 1000,
        ActorX              = 27130,
        ActorZ              = -20,
        ActorY              = 8920,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 14820,
        TriggerZ            = 40,
        TriggerY            = -10480,
        TriggerRange        = 1000,
        ActorX              = 14240,
        ActorZ              = 40,
        ActorY              = -10750,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_196",          # 00, 0
        "Function_1_295",          # 01, 1
        "Function_2_380",          # 02, 2
        "Function_3_381",          # 03, 3
        "Function_4_498",          # 04, 4
        "Function_5_5AF",          # 05, 5
        "Function_6_83F",          # 06, 6
        "Function_7_90E",          # 07, 7
        "Function_8_C06",          # 08, 8
        "Function_9_C8D",          # 09, 9
        "Function_10_D1C",         # 0A, 10
        "Function_11_DFA",         # 0B, 11
        "Function_12_E7F",         # 0C, 12
        "Function_13_F04",         # 0D, 13
        "Function_14_F89",         # 0E, 14
        "Function_15_100E",        # 0F, 15
        "Function_16_119A",        # 10, 16
        "Function_17_11FB",        # 11, 17
        "Function_18_125C",        # 12, 18
        "Function_19_12BD",        # 13, 19
    )


    def Function_0_196(): pass

    label("Function_0_196")

    OP_A3(0x1BA0)
    OP_A3(0x1BA1)
    OP_A3(0x1BA2)
    OP_A3(0x1BA3)
    OP_A3(0x1BA4)
    OP_A3(0x1BA5)
    OP_A3(0x1BA6)
    OP_A3(0x1BA7)
    OP_A3(0x1BA8)
    OP_A3(0x1BA9)
    OP_A3(0x1BAA)
    OP_A3(0x1BAB)
    OP_A3(0x1BAC)
    OP_A3(0x1FDE)
    OP_A3(0x1FDF)
    OP_A3(0x1FE0)
    OP_A3(0x1FE1)
    OP_A3(0x1FE2)
    OP_A3(0x1FE3)
    OP_A3(0x1FE4)
    OP_A3(0x1FE5)
    OP_A3(0x1FE6)
    OP_A3(0x1FE7)
    OP_A3(0x1FE8)
    OP_A3(0x1FE9)
    OP_A3(0x1FEA)
    OP_A3(0x1FEB)
    OP_A3(0x1FEC)
    OP_A3(0x1FED)
    OP_A3(0x1FEE)
    OP_A3(0x1FEF)
    OP_A3(0x1FF0)
    OP_A3(0x1FF1)
    OP_A3(0x1FF2)
    OP_A3(0x1FF3)
    OP_A3(0x1FF4)
    OP_A3(0x1FF5)
    OP_A3(0x1FF6)
    OP_A3(0x1FF7)
    OP_A3(0x1FF8)
    OP_A3(0x1FF9)
    OP_A3(0x1FFA)
    OP_A3(0x1FFB)
    OP_A3(0x1FFC)
    OP_A3(0x1FFD)
    OP_A3(0x1FFE)
    OP_A3(0x1FFF)
    OP_A3(0x1E80)
    OP_A3(0x1E81)
    OP_A3(0x1E82)
    OP_A3(0x1E83)
    OP_A3(0x1E84)
    OP_A3(0x1E85)
    OP_A3(0x1E86)
    OP_A3(0x1E87)
    OP_A3(0x1E88)
    OP_A3(0x1E89)
    OP_A3(0x1E8A)
    OP_A3(0x1E8B)
    OP_A3(0x1E8C)
    OP_A3(0x1E8D)
    OP_A3(0x1E8E)
    OP_A3(0x1E8F)
    OP_A3(0x1E90)
    OP_A3(0x1E91)
    OP_A3(0x1E92)
    OP_A3(0x1E93)
    OP_A3(0x1E94)
    OP_A3(0x1E95)
    OP_A3(0x1E96)
    OP_A3(0x1E97)
    OP_A3(0x1E98)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_284")
    OP_A3(0x10F0)
    SetMapFlags(0x10000000)
    Event(0, 5)
    Jump("loc_294")

    label("loc_284")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_294")
    Event(0, 15)

    label("loc_294")

    Return()

    # Function_0_196 end

    def Function_1_295(): pass

    label("Function_1_295")

    OP_16(0x2, 0xFA0, 0xFFFE0C00, 0xFFFE0C00, 0x23001E)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x369, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2B9")
    OP_6F(0x1, 0)
    Jump("loc_2C0")

    label("loc_2B9")

    OP_6F(0x1, 60)

    label("loc_2C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x369, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2D2")
    OP_6F(0x2, 0)
    Jump("loc_2D9")

    label("loc_2D2")

    OP_6F(0x2, 60)

    label("loc_2D9")

    OP_64(0x0, 0x1)
    OP_71(0x0, 0x0)
    OP_71(0x0, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C0, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_301")
    SetMapFlags(0x2000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x21), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_301")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_310")
    Jump("loc_360")

    label("loc_310")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C2, 1)), scpexpr(EXPR_END)), "loc_360")
    LoadEffect(0x0, "map\\\\mp086_00.eff")
    PlayEffect(0x0, 0xFF, 0xFF, 1000, 6000, 19900, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    label("loc_360")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C2, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_379")
    OP_10(0x1, 0x0)
    OP_10(0x2, 0x1)
    Jump("loc_37F")

    label("loc_379")

    OP_10(0x1, 0x1)
    OP_10(0x2, 0x0)

    label("loc_37F")

    Return()

    # Function_1_295 end

    def Function_2_380(): pass

    label("Function_2_380")

    Return()

    # Function_2_380 end

    def Function_3_381(): pass

    label("Function_3_381")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x369, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_459")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x1, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FF, 1)"), scpexpr(EXPR_END)), "loc_3F0")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #0
        "\x07\x00得到了\x1F\xFF\x01\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1B48)
    Jump("loc_456")

    label("loc_3F0")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #1
        (
            "宝箱里装有\x1F\xFF\x01\x07\x00。   \x01",
            "所持物品已经满了，\x1F\xFF\x01\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x1, 60)
    OP_70(0x1, 0x0)

    label("loc_456")

    Jump("loc_48A")

    label("loc_459")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #2
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_48A")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_381 end

    def Function_4_498(): pass

    label("Function_4_498")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x369, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_570")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x2, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FD, 1)"), scpexpr(EXPR_END)), "loc_507")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #3
        "\x07\x00得到了\x1F\xFD\x01\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1B49)
    Jump("loc_56D")

    label("loc_507")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #4
        (
            "宝箱里装有\x1F\xFD\x01\x07\x00。   \x01",
            "所持物品已经满了，\x1F\xFD\x01\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x2, 60)
    OP_70(0x2, 0x0)

    label("loc_56D")

    Jump("loc_5A1")

    label("loc_570")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #5
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_5A1")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_498 end

    def Function_5_5AF(): pass

    label("Function_5_5AF")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5C6")
    Call(0, 8)
    Call(0, 9)

    label("loc_5C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C3, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7AD")
    OP_6D(1390, 400, 7280, 0)
    OP_67(0, 15420, -10000, 0)
    OP_6B(3020, 0)
    OP_6C(45000, 0)
    OP_6E(330, 0)
    StopSound(0x8CA0, 0x30D40, 0x0)
    SetChrPos(0x101, 2390, -280, -23110, 0)
    SetChrPos(0x102, 1220, -490, -23160, 0)
    SetChrPos(0xF8, 2400, -310, -24380, 0)
    SetChrPos(0xF9, 1020, -490, -24400, 0)

    def lambda_662():
        OP_6D(950, -20, -15430, 5000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_662)
    OP_C8(0x200, 0x46, "C_PLAC21._CH", 0x0, 0x3E8)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(2000)

    def lambda_69E():
        OP_8E(0xFE, 0x726, 0xA, 0xFFFFBFB4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_69E)

    def lambda_6B9():
        OP_8E(0xFE, 0x1F4, 0xFFFFFFEC, 0xFFFFBEE2, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_6B9)

    def lambda_6D4():
        OP_8E(0xFE, 0x7BC, 0x28, 0xFFFFBA82, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF8, 0, lambda_6D4)

    def lambda_6EF():
        OP_8E(0xFE, 0x1C2, 0xA, 0xFFFFB956, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF9, 0, lambda_6EF)
    WaitChrThread(0x101, 0x1)
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopSound(0x8CA0, 0x186A0, 0x0)
    OP_6D(1350, -40, -18500, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(3200, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    Sleep(500)
    SetChrPos(0x0, 1350, -40, -20010, 0)
    SetChrPos(0x1, 1350, -40, -20010, 0)
    SetChrPos(0x2, 1350, -40, -20010, 0)
    SetChrPos(0x3, 1350, -40, -20010, 0)
    OP_A2(0x1E1F)
    Jump("loc_82E")

    label("loc_7AD")

    OP_6D(1350, -40, -18500, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(3200, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0, 1350, -40, -20010, 0)
    SetChrPos(0x1, 1350, -40, -20010, 0)
    SetChrPos(0x2, 1350, -40, -20010, 0)
    SetChrPos(0x3, 1350, -40, -20010, 0)

    label("loc_82E")

    FadeToBright(1000, 0)
    EventEnd(0x0)
    SetMapFlags(0x2000000)
    Return()

    # Function_5_5AF end

    def Function_6_83F(): pass

    label("Function_6_83F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C3, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_851")
    Return()

    label("loc_851")

    EventBegin(0x1)
    SetChrName("")

    AnonymousTalk(    #6
        "\x07\x05要回『埃尔赛尤』吗？\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "【回船上】\x01",      # 0
            "【不回去】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8ED")
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x10F5)
    NewScene("ED6_DT21/E0301   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_90D")

    label("loc_8ED")

    OP_90(0x0, 0x0, 0x0, 0x5DC, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    SetMapFlags(0x2000000)

    label("loc_90D")

    Return()

    # Function_6_83F end

    def Function_7_90E(): pass

    label("Function_7_90E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_91E")
    Return()

    label("loc_91E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C4, 0)), scpexpr(EXPR_END)), "loc_926")
    Return()

    label("loc_926")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_94B")
    Call(0, 8)
    Call(0, 9)
    FadeToBright(0, 0)
    Sleep(100)

    label("loc_94B")

    Fade(1000)
    OP_6D(1350, 2800, 13070, 0)
    OP_67(0, 2270, -10000, 0)
    OP_6B(2850, 0)
    OP_6C(9000, 0)
    OP_6E(463, 0)
    SetChrPos(0x101, 1750, 400, 7850, 0)
    SetChrPos(0x102, 240, 400, 7460, 0)
    SetChrPos(0xF8, 2000, 50, 6000, 0)
    SetChrPos(0xF9, 590, 10, 6000, 0)
    OP_0D()

    ChrTalk(    #7
        0x101,
        (
            "#1015F#2P终于到最后的塔了吗……\x02\x03",

            "#1007F如果是和之前的塔一样\x01",
            "只有一条路的话，就不会迷路了，不过……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x102,
        (
            "#1035F#5P不过要是有强力的守卫\x01",
            "挡路也很麻烦呢。\x02\x03",

            "#1042F很快就要天黑了……\x01",
            "动作最好加快一点。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x101,
        (
            "#1003F#2P嗯，必须阻止玲才行。\x02\x03",

            "#1002F大家……\x01",
            "打起精神来，继续前进吧！\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B08")

    ChrTalk(    #10
        0x107,
        "#062F嗯……！\x02",
    )

    CloseMessageWindow()

    label("loc_B08")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B25")

    ChrTalk(    #11
        0x105,
        "#042F是！\x02",
    )

    CloseMessageWindow()

    label("loc_B25")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B44")

    ChrTalk(    #12
        0x103,
        "#022F嗯嗯！\x02",
    )

    CloseMessageWindow()

    label("loc_B44")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B62")

    ChrTalk(    #13
        0x109,
        "#1063F好！\x02",
    )

    CloseMessageWindow()

    label("loc_B62")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B81")

    ChrTalk(    #14
        0x106,
        "#057F哦哦！\x02",
    )

    CloseMessageWindow()

    label("loc_B81")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_BA0")

    ChrTalk(    #15
        0x108,
        "#072F啊啊！\x02",
    )

    CloseMessageWindow()

    label("loc_BA0")


    def lambda_BA6():
        OP_69(0x0, 0x7D0)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_BA6)

    def lambda_BB4():
        OP_67(0, 8000, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_BB4)

    def lambda_BCC():
        OP_6B(3200, 2000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_BCC)

    def lambda_BDC():
        OP_6C(45000, 2000)
        ExitThread()

    QueueWorkItem(0x0, 3, lambda_BDC)

    def lambda_BEC():
        OP_6E(262, 2000)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_BEC)
    OP_A2(0x1E20)
    WaitChrThread(0x0, 0x0)
    EventEnd(0x0)
    SetMapFlags(0x2000000)
    Return()

    # Function_7_90E end

    def Function_8_C06(): pass

    label("Function_8_C06")

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
        (0, "loc_C80"),
        (1, "loc_C86"),
        (SWITCH_DEFAULT, "loc_C8C"),
    )


    label("loc_C80")

    OP_A2(0x1200)
    Jump("loc_C8C")

    label("loc_C86")

    OP_A2(0x1201)
    Jump("loc_C8C")

    label("loc_C8C")

    Return()

    # Function_8_C06 end

    def Function_9_C8D(): pass

    label("Function_9_C8D")

    FadeToDark(0, 0, -1)
    OP_6D(-31870, 10, -30550, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(3200, 0)
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

    # Function_9_C8D end

    def Function_10_D1C(): pass

    label("Function_10_D1C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C3, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_DF9")
    EventBegin(0x0)
    Fade(500)
    OP_6D(610, 4000, 21090, 0)
    OP_67(0, 4950, -10000, 0)
    OP_6B(2200, 0)
    OP_6C(351000, 0)
    OP_6E(412, 0)
    SetChrPos(0x101, 500, 4000, 18000, 0)
    SetChrPos(0x102, 1500, 4000, 18000, 0)
    SetChrPos(0xF8, 500, 4000, 17000, 0)
    SetChrPos(0xF9, 1500, 4000, 17000, 0)
    OP_43(0x101, 0x0, 0x0, 0xB)
    Sleep(300)
    OP_43(0x102, 0x0, 0x0, 0xC)
    Sleep(300)
    OP_43(0xF8, 0x0, 0x0, 0xD)
    Sleep(300)
    OP_43(0xF9, 0x0, 0x0, 0xE)
    WaitChrThread(0xF9, 0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    ClearMapFlags(0x2000000)
    NewScene("ED6_DT21/C1700   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_DF9")

    Return()

    # Function_10_D1C end

    def Function_11_DFA(): pass

    label("Function_11_DFA")

    OP_91(0xFE, 0x0, 0x0, 0x9C4, 0x7D0, 0x0)
    ClearChrFlags(0xFE, 0x1)
    OP_7D(0x0, 0xFE, 0x32, 0x1F4)
    OP_22(0x99, 0x0, 0x64)
    SetChrFlags(0xFE, 0x4)
    OP_91(0xFE, 0x0, 0x1F4, 0x0, 0x0, 0x0)

    def lambda_E3F():
        OP_9E(0xFE, 0x0, 0x64, 0x3E8, 0x1388)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_E3F)

    def lambda_E59():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x5DC)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_E59)
    WaitChrThread(0xFE, 0x1)
    OP_91(0xFE, 0x0, 0x9C4, 0x0, 0x1388, 0x0)
    Return()

    # Function_11_DFA end

    def Function_12_E7F(): pass

    label("Function_12_E7F")

    OP_91(0xFE, 0x0, 0x0, 0x9C4, 0x7D0, 0x0)
    ClearChrFlags(0xFE, 0x1)
    OP_7D(0x0, 0xFE, 0x32, 0x1F4)
    OP_22(0x99, 0x0, 0x64)
    SetChrFlags(0xFE, 0x4)
    OP_91(0xFE, 0x0, 0x1F4, 0x0, 0x0, 0x0)

    def lambda_EC4():
        OP_9E(0xFE, 0x0, 0x64, 0x3E8, 0x1388)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_EC4)

    def lambda_EDE():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x5DC)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_EDE)
    WaitChrThread(0xFE, 0x1)
    OP_91(0xFE, 0x0, 0x9C4, 0x0, 0x1388, 0x0)
    Return()

    # Function_12_E7F end

    def Function_13_F04(): pass

    label("Function_13_F04")

    OP_91(0xFE, 0x0, 0x0, 0xDAC, 0x7D0, 0x0)
    ClearChrFlags(0xFE, 0x1)
    OP_7D(0x0, 0xFE, 0x32, 0x1F4)
    OP_22(0x99, 0x0, 0x64)
    SetChrFlags(0xFE, 0x4)
    OP_91(0xFE, 0x0, 0x1F4, 0x0, 0x0, 0x0)

    def lambda_F49():
        OP_9E(0xFE, 0x0, 0x64, 0x3E8, 0x1388)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_F49)

    def lambda_F63():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x5DC)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_F63)
    WaitChrThread(0xFE, 0x1)
    OP_91(0xFE, 0x0, 0x9C4, 0x0, 0x1388, 0x0)
    Return()

    # Function_13_F04 end

    def Function_14_F89(): pass

    label("Function_14_F89")

    OP_91(0xFE, 0x0, 0x0, 0xDAC, 0x7D0, 0x0)
    ClearChrFlags(0xFE, 0x1)
    OP_7D(0x0, 0xFE, 0x32, 0x1F4)
    OP_22(0x99, 0x0, 0x64)
    SetChrFlags(0xFE, 0x4)
    OP_91(0xFE, 0x0, 0x1F4, 0x0, 0x0, 0x0)

    def lambda_FCE():
        OP_9E(0xFE, 0x0, 0x64, 0x3E8, 0x1388)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_FCE)

    def lambda_FE8():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x5DC)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_FE8)
    WaitChrThread(0xFE, 0x1)
    OP_91(0xFE, 0x0, 0x9C4, 0x0, 0x1388, 0x0)
    Return()

    # Function_14_F89 end

    def Function_15_100E(): pass

    label("Function_15_100E")

    EventBegin(0x0)
    OP_6D(610, 4000, 21090, 0)
    OP_67(0, 4950, -10000, 0)
    OP_6B(2200, 0)
    OP_6C(351000, 0)
    OP_6E(412, 0)
    SetChrPos(0x101, 1500, 4400, 20500, 180)
    SetChrPos(0x102, 500, 4400, 20500, 180)
    SetChrPos(0xF8, 1500, 4400, 20500, 180)
    SetChrPos(0xF9, 500, 4400, 20500, 180)
    OP_9F(0x0, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x1, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x3, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x101, 0x1)
    ClearChrFlags(0x102, 0x1)
    ClearChrFlags(0xF8, 0x1)
    ClearChrFlags(0xF9, 0x1)
    FadeToBright(1000, 0)
    OP_0D()
    OP_43(0x101, 0x0, 0x0, 0x10)
    Sleep(800)
    OP_43(0x102, 0x0, 0x0, 0x11)
    Sleep(800)
    OP_43(0xF8, 0x0, 0x0, 0x12)
    Sleep(800)
    OP_43(0xF9, 0x0, 0x0, 0x13)
    WaitChrThread(0xF9, 0x0)
    Fade(500)
    OP_6D(1110, 4000, 17770, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(3200, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0, 1110, 4000, 17770, 180)
    SetChrPos(0x1, 1110, 4000, 17770, 180)
    SetChrPos(0x2, 1110, 4000, 17770, 180)
    SetChrPos(0x3, 1110, 4000, 17770, 180)
    OP_0D()
    EventEnd(0x0)
    SetMapFlags(0x2000000)
    Return()

    # Function_15_100E end

    def Function_16_119A(): pass

    label("Function_16_119A")

    OP_22(0x99, 0x0, 0x64)

    def lambda_11A5():
        OP_9E(0xFE, 0x0, 0x64, 0x3E8, 0x1388)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_11A5)

    def lambda_11BF():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_11BF)
    WaitChrThread(0xFE, 0x2)
    SetChrFlags(0xFE, 0x1)
    WaitChrThread(0xFE, 0x1)

    def lambda_11E0():
        OP_8F(0xFE, 0x5DC, 0xE10, 0x4268, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_11E0)
    WaitChrThread(0xFE, 0x2)
    Return()

    # Function_16_119A end

    def Function_17_11FB(): pass

    label("Function_17_11FB")

    OP_22(0x99, 0x0, 0x64)

    def lambda_1206():
        OP_9E(0xFE, 0x0, 0x64, 0x3E8, 0x1388)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1206)

    def lambda_1220():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1220)
    WaitChrThread(0xFE, 0x2)
    SetChrFlags(0xFE, 0x1)
    WaitChrThread(0xFE, 0x1)

    def lambda_1241():
        OP_8F(0xFE, 0x1F4, 0xE10, 0x4268, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1241)
    WaitChrThread(0xFE, 0x2)
    Return()

    # Function_17_11FB end

    def Function_18_125C(): pass

    label("Function_18_125C")

    OP_22(0x99, 0x0, 0x64)

    def lambda_1267():
        OP_9E(0xFE, 0x0, 0x64, 0x3E8, 0x1388)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1267)

    def lambda_1281():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1281)
    WaitChrThread(0xFE, 0x2)
    SetChrFlags(0xFE, 0x1)
    WaitChrThread(0xFE, 0x1)

    def lambda_12A2():
        OP_8F(0xFE, 0x5DC, 0xE10, 0x4650, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_12A2)
    WaitChrThread(0xFE, 0x2)
    Return()

    # Function_18_125C end

    def Function_19_12BD(): pass

    label("Function_19_12BD")

    OP_22(0x99, 0x0, 0x64)

    def lambda_12C8():
        OP_9E(0xFE, 0x0, 0x64, 0x3E8, 0x1388)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_12C8)

    def lambda_12E2():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_12E2)
    WaitChrThread(0xFE, 0x2)
    SetChrFlags(0xFE, 0x1)
    WaitChrThread(0xFE, 0x1)

    def lambda_1303():
        OP_8F(0xFE, 0x1F4, 0xE10, 0x4650, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1303)
    WaitChrThread(0xFE, 0x2)
    Return()

    # Function_19_12BD end

    SaveToFile()

Try(main)

from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'C5508   ._SN',
        MapName             = 'Other',
        Location            = 'C5508.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60034",
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


    DeclEvent(
        X                   = -8100,
        Y                   = -200,
        Z                   = -42000,
        Range               = 5600,
        Unknown_10          = 0x1C20,
        Unknown_14          = 0xFFFF7874,
        Unknown_18          = 0x0,
        Unknown_1C          = 2,
    )


    ScpFunction(
        "Function_0_CA",           # 00, 0
        "Function_1_DC",           # 01, 1
        "Function_2_F2",           # 02, 2
        "Function_3_5EB",          # 03, 3
    )


    def Function_0_CA(): pass

    label("Function_0_CA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x204, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DB")
    SetMapFlags(0x10000000)
    Event(0, 3)

    label("loc_DB")

    Return()

    # Function_0_CA end

    def Function_1_DC(): pass

    label("Function_1_DC")

    OP_10(0x1, 0x0)
    OP_16(0x2, 0xFA0, 0xFFFE0818, 0xFFFDCD80, 0x230070)
    Return()

    # Function_1_DC end

    def Function_2_F2(): pass

    label("Function_2_F2")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x204, 2)), scpexpr(EXPR_END)), "loc_110")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_121")

    label("loc_110")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x202, 2)), scpexpr(EXPR_END)), "loc_121")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_121")

    SetMapFlags(0x80)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_C5(0x0, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS137._CH")
    OP_C6(0x0, 0x4, 0, 0, 0)
    OP_C6(0x0, 0x3, -1, 500, 0)
    OP_C7(0x0, 0x0, 0x3)
    OP_77(0x0, 0x0, 0x0, 0x0, 0x0)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_192")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4AF")
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_END)),
        (0, "loc_1BD"),
        (1, "loc_1E9"),
        (2, "loc_226"),
        (SWITCH_DEFAULT, "loc_278"),
    )


    label("loc_1BD")


    Menu(
        0,
        30,
        80,
        0,
        (
            "【训练场宿舍】\x01",        # 0
            "【巴斯塔尔水道】\x01",      # 1
        )
    )

    Jump("loc_278")

    label("loc_1E9")


    Menu(
        0,
        30,
        80,
        0,
        (
            "【训练场宿舍】\x01",        # 0
            "【巴斯塔尔水道】\x01",      # 1
            "【圣科洛瓦森林】\x01",      # 2
        )
    )

    Jump("loc_278")

    label("loc_226")


    Menu(
        0,
        30,
        80,
        0,
        (
            "【训练场宿舍】\x01",            # 0
            "【巴斯塔尔水道】\x01",          # 1
            "【圣科洛瓦森林】\x01",          # 2
            "【格林姆瑟尔小要塞】\x01",      # 3
        )
    )

    Jump("loc_278")

    label("loc_278")

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2A2"),
        (1, "loc_322"),
        (2, "loc_3A4"),
        (3, "loc_426"),
        (SWITCH_DEFAULT, "loc_4AC"),
    )


    label("loc_2A2")

    SetChrName("")
    SetMessageWindowPos(-1, 120, -1, -1)

    AnonymousTalk(    #0
        "\x07\x05要移动至【训练场宿舍】吗？\x02",
    )

    CloseMessageWindow()
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        1,
        10,
        -1,
        0,
        (
            "【是】\x01",      # 0
            "【否】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x1)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_30F"),
        (1, "loc_31C"),
        (SWITCH_DEFAULT, "loc_31F"),
    )


    label("loc_30F")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_31F")

    label("loc_31C")

    Jump("loc_31F")

    label("loc_31F")

    Jump("loc_4AC")

    label("loc_322")

    SetChrName("")
    SetMessageWindowPos(-1, 120, -1, -1)

    AnonymousTalk(    #1
        "\x07\x05要移动至【巴斯塔尔水道】吗？\x02",
    )

    CloseMessageWindow()
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        1,
        10,
        -1,
        0,
        (
            "【是】\x01",      # 0
            "【否】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x1)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_391"),
        (1, "loc_39E"),
        (SWITCH_DEFAULT, "loc_3A1"),
    )


    label("loc_391")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3A1")

    label("loc_39E")

    Jump("loc_3A1")

    label("loc_3A1")

    Jump("loc_4AC")

    label("loc_3A4")

    SetChrName("")
    SetMessageWindowPos(-1, 120, -1, -1)

    AnonymousTalk(    #2
        "\x07\x05要移动至【圣科洛瓦森林】吗？\x02",
    )

    CloseMessageWindow()
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        1,
        10,
        -1,
        0,
        (
            "【是】\x01",      # 0
            "【否】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x1)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_413"),
        (1, "loc_420"),
        (SWITCH_DEFAULT, "loc_423"),
    )


    label("loc_413")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_423")

    label("loc_420")

    Jump("loc_423")

    label("loc_423")

    Jump("loc_4AC")

    label("loc_426")

    SetChrName("")
    SetMessageWindowPos(-1, 120, -1, -1)

    AnonymousTalk(    #3
        "\x07\x05要移动至【格林姆瑟尔小要塞】吗？\x02",
    )

    CloseMessageWindow()
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        1,
        10,
        -1,
        0,
        (
            "【是】\x01",      # 0
            "【否】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x1)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_499"),
        (1, "loc_4A6"),
        (SWITCH_DEFAULT, "loc_4A9"),
    )


    label("loc_499")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4A9")

    label("loc_4A6")

    Jump("loc_4A9")

    label("loc_4A9")

    Jump("loc_4AC")

    label("loc_4AC")

    Jump("loc_192")

    label("loc_4AF")

    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_4C8"),
        (1, "loc_4FC"),
        (2, "loc_530"),
        (3, "loc_564"),
        (SWITCH_DEFAULT, "loc_598"),
    )


    label("loc_4C8")

    OP_C6(0x0, 0x0, -640000, 0, 2000)
    OP_C6(0x0, 0x1, 2000, 2000, 2000)
    OP_C6(0x0, 0x3, 16777215, 2000, 0)
    OP_C7(0x0, 0x0, 0x3)
    Jump("loc_598")

    label("loc_4FC")

    OP_C6(0x0, 0x0, -358000, -37000, 2000)
    OP_C6(0x0, 0x1, 2000, 2000, 2000)
    OP_C6(0x0, 0x3, 16777215, 2000, 0)
    OP_C7(0x0, 0x0, 0x3)
    Jump("loc_598")

    label("loc_530")

    OP_C6(0x0, 0x0, -362000, -266000, 2000)
    OP_C6(0x0, 0x1, 2000, 2000, 2000)
    OP_C6(0x0, 0x3, 16777215, 2000, 0)
    OP_C7(0x0, 0x0, 0x3)
    Jump("loc_598")

    label("loc_564")

    OP_C6(0x0, 0x0, -64000, -340000, 2000)
    OP_C6(0x0, 0x1, 2000, 2000, 2000)
    OP_C6(0x0, 0x3, 16777215, 2000, 0)
    OP_C7(0x0, 0x0, 0x3)
    Jump("loc_598")

    label("loc_598")

    OP_77(0xFF, 0xFF, 0xFF, 0x0, 0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_5BA"),
        (1, "loc_5C6"),
        (2, "loc_5D2"),
        (3, "loc_5DE"),
        (SWITCH_DEFAULT, "loc_5EA"),
    )


    label("loc_5BA")

    NewScene("ED6_DT21/T5100   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_5EA")

    label("loc_5C6")

    NewScene("ED6_DT21/C5503   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_5EA")

    label("loc_5D2")

    NewScene("ED6_DT21/C5507   ._SN", 101, 0, 0)
    IdleLoop()
    Jump("loc_5EA")

    label("loc_5DE")

    NewScene("ED6_DT21/C5508   ._SN", 101, 0, 0)
    IdleLoop()
    Jump("loc_5EA")

    label("loc_5EA")

    Return()

    # Function_2_F2 end

    def Function_3_5EB(): pass

    label("Function_3_5EB")

    EventBegin(0x0)
    OP_6D(-770, 500, -3680, 0)
    OP_67(0, 12230, -10000, 0)
    OP_6B(5220, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, -2000, 0, -31300, 13)
    SetChrPos(0x10A, -200, 0, -31500, 360)
    OP_C8(0x200, 0x46, "C_PLAC03._CH", 0x0, 0x7D0)
    FadeToBright(2000, 0)

    def lambda_670():
        OP_6D(-770, 0, -21740, 6000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_670)
    Sleep(1500)

    def lambda_68D():
        OP_8E(0xFE, 0xFFFFF830, 0x0, 0xFFFFAD76, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_68D)
    Sleep(400)

    def lambda_6AD():
        OP_8E(0xFE, 0xFFFFFF38, 0x0, 0xFFFFAD76, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x10A, 0, lambda_6AD)
    OP_0D()
    WaitChrThread(0x101, 0x0)
    Fade(1000)
    OP_6D(-590, 0, -18490, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3080, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_0D()
    WaitChrThread(0x101, 0x1)
    WaitChrThread(0x10A, 0x0)

    ChrTalk(    #4
        0x101,
        "#1004F#6P这就是『格林姆瑟尔小要塞』……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x10A,
        (
            "#5P#812F好厉害……\x01",
            "是相当正统的训练设施哦。\x02\x03",

            "总之从外面看起来\x01",
            "几乎感觉不到有人的气息……\x02",
        )
    )

    CloseMessageWindow()
    OP_8E(0x101, 0xFFFFFCE0, 0x0, 0xFFFFB3F2, 0x7D0, 0x0)

    def lambda_7BA():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x10A, 0, lambda_7BA)
    OP_8C(0x101, 90, 500)
    Sleep(200)
    OP_8C(0x101, 0, 500)
    OP_8C(0x101, 270, 500)
    Sleep(400)
    OP_8C(0x101, 0, 500)
    OP_8C(0x101, 180, 500)
    Sleep(500)

    ChrTalk(    #6
        0x101,
        (
            "#1002F#5P嗯，没有错……\x02\x03",

            "地面上还留有一些人\x01",
            "最近走过的痕迹。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x10A,
        (
            "#811F呵呵，看来追踪训练\x01",
            "的成果发挥作用了呢。\x02\x03",

            "#810F照这个情况，敌人的数量\x01",
            "应该不会太多。\x02\x03",

            "约三四人的样子吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x101,
        (
            "#1006F#5P虽然说敌人似乎相当厉害……\x01",
            "但我们毕竟也是正游击士。\x02\x03",

            "还不至于无法对抗吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x10A,
        "#816F嗯，尽全力吧！\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1023)
    OP_28(0x80, 0x1, 0x400)
    EventEnd(0x0)
    Return()

    # Function_3_5EB end

    SaveToFile()

Try(main)

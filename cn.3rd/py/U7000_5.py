from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'U7000_5 ._SN',
        MapName             = 'Gaiden2',
        Location            = 'U7000.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60210",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            'ED6_DT21/U7000   ._SN',
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
        '',                                     # 8
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


    ScpFunction(
        "Function_0_AA",           # 00, 0
        "Function_1_AB",           # 01, 1
        "Function_2_AC",           # 02, 2
        "Function_3_476",          # 03, 3
        "Function_4_536",          # 04, 4
        "Function_5_609",          # 05, 5
        "Function_6_6FC",          # 06, 6
        "Function_7_19F6",         # 07, 7
        "Function_8_2DF1",         # 08, 8
        "Function_9_308E",         # 09, 9
        "Function_10_3113",        # 0A, 10
        "Function_11_45EC",        # 0B, 11
        "Function_12_4855",        # 0C, 12
        "Function_13_4A7E",        # 0D, 13
        "Function_14_4BC7",        # 0E, 14
        "Function_15_4E7C",        # 0F, 15
        "Function_16_4E7D",        # 10, 16
        "Function_17_4E7E",        # 11, 17
        "Function_18_50E0",        # 12, 18
        "Function_19_51DC",        # 13, 19
        "Function_20_71F6",        # 14, 20
        "Function_21_7219",        # 15, 21
        "Function_22_725F",        # 16, 22
        "Function_23_981B",        # 17, 23
        "Function_24_9837",        # 18, 24
        "Function_25_988F",        # 19, 25
    )


    def Function_0_AA(): pass

    label("Function_0_AA")

    Return()

    # Function_0_AA end

    def Function_1_AB(): pass

    label("Function_1_AB")

    Return()

    # Function_1_AB end

    def Function_2_AC(): pass

    label("Function_2_AC")

    EventBegin(0x0)
    Fade(500)
    OP_6D(-900, 4000, 4220, 0)
    OP_67(0, 5290, -10000, 0)
    OP_6B(2040, 0)
    OP_6C(0, 0)
    OP_6E(435, 0)
    SetChrPos(0x0, -1040, 4000, 1270, 315)
    SetChrPos(0x1, -40, 4000, 2200, 315)
    SetChrPos(0x2, -110, 4000, -250, 315)
    SetChrPos(0x3, 870, 4000, 1110, 315)
    SetChrChipByIndex(0x0, 65535)
    SetChrChipByIndex(0x1, 65535)
    SetChrChipByIndex(0x2, 65535)
    SetChrChipByIndex(0x3, 65535)
    SetChrSubChip(0x0, 0)
    SetChrSubChip(0x1, 0)
    SetChrSubChip(0x2, 0)
    SetChrSubChip(0x3, 0)
    OP_8C(0x22, 135, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #0
        0x22,
        (
            "#1615F#5P#12C对了……\x01",
            "有件事要告诉你们。\x02\x03",

            "#1613F我发现在『第七星层』中，\x01",
            "除了凯文神父坠落的地方以外，\x01",
            "还有大规模的领域。\x02\x03",

            "那里大概是被称为『恶魔』的敌人\x01",
            "所徘徊的危险领域……\x02\x03",

            "#1612F以防万一……\x01",
            "我已经在那里建立了『石碑』，\x01",
            "请用『方石』前去确认一下。\x02\x03",

            "目前能传送的场所\x01",
            "应该已经增加了一个。#0C\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #1
        "\x07\x02前往『深渊』的道路\x07\x05已经打开了。\x02",
    )

    CloseMessageWindow()

    AnonymousTalk(    #2
        (
            "\x07\x05在传送画面的『第七星层』\x01",
            "增加了传送点，\x01",
            "可以直接从那里开始攻略。\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #3
        (
            "\x07\x05在『深渊』里有恶魔级别的敌人徘徊，\x01",
            "比起其它场所来\x01",
            "更能有效地锻炼队伍成员。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_A2(0x2C21)
    OP_AA(7936)
    OP_28(0x3E, 0x1, 0x20)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6D(-540, 4000, 1460, 0)
    OP_67(0, 7900, -10000, 0)
    OP_6B(2530, 0)
    OP_6C(0, 0)
    OP_6E(450, 0)
    SetChrPos(0x0, -540, 4000, 1460, 315)
    SetChrPos(0x1, -540, 4000, 1460, 315)
    SetChrPos(0x2, -540, 4000, 1460, 315)
    SetChrPos(0x3, -540, 4000, 1460, 315)
    SetChrChipByIndex(0x0, 65535)
    SetChrChipByIndex(0x1, 65535)
    SetChrChipByIndex(0x2, 65535)
    SetChrChipByIndex(0x3, 65535)
    SetChrSubChip(0x0, 0)
    SetChrSubChip(0x1, 0)
    SetChrSubChip(0x2, 0)
    SetChrSubChip(0x3, 0)
    OP_69(0x0, 0x0)
    Sleep(500)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    SetMapFlags(0x2000000)
    Return()

    # Function_2_AC end

    def Function_3_476(): pass

    label("Function_3_476")

    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_493")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_535")

    Menu(
        1,
        -1,
        150,
        1,
        (
            "对话\x01",                  # 0
            "乘埃尔赛尤号出发\x01",      # 1
            "离开\x01",                  # 2
        )
    )

    Jump("loc_4D0")

    label("loc_4D0")

    MenuEnd(0x3)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x1)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_END)),
        (0, "loc_4FA"),
        (1, "loc_514"),
        (SWITCH_DEFAULT, "loc_525"),
    )


    label("loc_4FA")

    Call(5, 10)
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_532")

    label("loc_514")

    Call(5, 11)
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_532")

    label("loc_525")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_532")

    label("loc_532")

    Jump("loc_493")

    label("loc_535")

    Return()

    # Function_3_476 end

    def Function_4_536(): pass

    label("Function_4_536")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_540")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_608")
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        1,
        -1,
        150,
        1,
        (
            "对话\x01",                      # 0
            "用塞姆里亚石制作武器\x01",      # 1
            "离开\x01",                      # 2
        )
    )

    Jump("loc_594")

    label("loc_594")

    MenuEnd(0x3)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x1)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_END)),
        (0, "loc_5BE"),
        (1, "loc_5D8"),
        (SWITCH_DEFAULT, "loc_5F8"),
    )


    label("loc_5BE")

    Call(5, 10)
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_605")

    label("loc_5D8")

    Call(5, 7)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x33B, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_5F5")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5F5")

    Jump("loc_605")

    label("loc_5F8")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_605")

    label("loc_605")

    Jump("loc_540")

    label("loc_608")

    Return()

    # Function_4_536 end

    def Function_5_609(): pass

    label("Function_5_609")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_613")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6FB")
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        1,
        -1,
        150,
        1,
        (
            "对话\x01",                      # 0
            "乘埃尔赛尤号出发\x01",          # 1
            "用塞姆里亚石制作武器\x01",      # 2
            "离开\x01",                      # 3
        )
    )

    Jump("loc_678")

    label("loc_678")

    MenuEnd(0x3)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x1)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_END)),
        (0, "loc_6A6"),
        (1, "loc_6C0"),
        (2, "loc_6D1"),
        (SWITCH_DEFAULT, "loc_6EB"),
    )


    label("loc_6A6")

    Call(5, 10)
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_6F8")

    label("loc_6C0")

    Call(5, 11)
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_6F8")

    label("loc_6D1")

    Call(5, 7)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x33B, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_6E8")
    Call(5, 3)

    label("loc_6E8")

    Jump("loc_6F8")

    label("loc_6EB")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_6F8")

    label("loc_6F8")

    Jump("loc_613")

    label("loc_6FB")

    Return()

    # Function_5_609 end

    def Function_6_6FC(): pass

    label("Function_6_6FC")

    EventBegin(0x0)
    Fade(500)
    OP_6D(-900, 4000, 4220, 0)
    OP_67(0, 5290, -10000, 0)
    OP_6B(2040, 0)
    OP_6C(0, 0)
    OP_6E(435, 0)
    SetChrPos(0x0, -1040, 4000, 1270, 315)
    SetChrPos(0x1, -40, 4000, 2200, 315)
    SetChrPos(0x2, -110, 4000, -250, 315)
    SetChrPos(0x3, 870, 4000, 1110, 315)
    SetChrChipByIndex(0x0, 65535)
    SetChrChipByIndex(0x1, 65535)
    SetChrChipByIndex(0x2, 65535)
    SetChrChipByIndex(0x3, 65535)
    SetChrSubChip(0x0, 0)
    SetChrSubChip(0x1, 0)
    SetChrSubChip(0x2, 0)
    SetChrSubChip(0x3, 0)
    OP_8C(0x22, 135, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #4
        0x22,
        (
            "#1614F#12C#5P哎呀……\x01",
            "从你们那里感到的波动是……#0C\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x22, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #5
        0x22,
        (
            "#1612F#12C#5P这、这是……\x01",
            "难道是塞姆里亚石！？\x02\x03",

            "#1613F怎么会这样……\x01",
            "连这种物质都在\x01",
            "『影之国』再现了……\x02\x03",

            "在什么时候呢……？\x01",
            "不……应该是一开始就……#0C\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x22, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x22)
    Sleep(500)

    ChrTalk(    #6
        0x22,
        (
            "#1615F#12C#5P……就算是在你们的时代\x01",
            "我想应该也一样……\x02\x03",

            "这种素材的组成\x01",
            "无论用什么方法\x01",
            "都不可能解析出来。\x02\x03",

            "#1610F不过，在一次奇迹般的偶然下\x01",
            "倒是发现了加工方法。\x02\x03",

            "要是你们希望的话，\x01",
            "我可以使用『庭院』的力量\x01",
            "把这石头制作成武器。#0C\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, 100, -1, -1)

    AnonymousTalk(    #7
        "\x06\x18\x07\x05要用塞姆里亚石制作武器吗？\x02",
    )

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        1,
        -1,
        200,
        1,
        (
            "好的\x01",      # 0
            "不用\x01",      # 1
        )
    )

    Jump("loc_A55")

    label("loc_A55")

    MenuEnd(0x3)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x1)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_END)),
        (0, "loc_A71"),
        (SWITCH_DEFAULT, "loc_188A"),
    )


    label("loc_A71")

    SetMessageWindowPos(-1, 30, -1, -1)

    AnonymousTalk(    #8
        "\x06\x18\x07\x05制作成哪种武器呢？\x02",
    )

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        2,
        -1,
        120,
        1,
        (
            "自动弓「七七无穷射」\x01",          # 0
            "法剑  「光铬剑」\x01",              # 1
            "棒具  「星球之光」\x01",            # 2
            "双剑  「行云流水」\x01",            # 3
            "鞭    「虹」\x01",                  # 4
            "导力枪「假面之眼」\x01",            # 5
            "单手剑「神圣新星」\x01",            # 6
            "大剑  「动力化石剑」\x01",          # 7
            "导力炮「溶化破坏者」\x01",          # 8
            "护手甲「四圣兽」\x01",              # 9
            "刀    「彗星」\x01",                # 10
            "巨镰  「复仇女神之诅咒」\x01",      # 11
            "退出\x01",                          # 12
        )
    )

    Jump("loc_B9E")

    label("loc_B9E")

    MenuEnd(0x4)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x2)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_END)),
        (0, "loc_BE8"),
        (1, "loc_CE9"),
        (2, "loc_DEA"),
        (3, "loc_EEB"),
        (4, "loc_FEC"),
        (5, "loc_10EA"),
        (6, "loc_11EB"),
        (7, "loc_12EC"),
        (8, "loc_13ED"),
        (9, "loc_14EE"),
        (10, "loc_15EF"),
        (11, "loc_16F0"),
        (SWITCH_DEFAULT, "loc_17F1"),
    )


    label("loc_BE8")

    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_22(0x138, 0x0, 0x64)
    OP_22(0x146, 0x1, 0x46)
    Sleep(2500)
    OP_23(0x146)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #9
        "\x07\x00得到了\x1F\x61\x05\x07\x00。\x02",
    )

    Jump("loc_C2C")

    label("loc_C2C")

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x561, 1)
    OP_3F(0x33B, 1)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(    #10
        0x22,
        (
            "#1616F#12C#5P呵呵……\x01",
            "总算做成了。\x02\x03",

            "#1611F要是再发现这样的石头\x01",
            "就请拿过来给我。\x02\x03",

            "我可以把它制作成\x01",
            "对你们有所帮助的武器。#0C\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2C37)
    Jump("loc_1887")

    label("loc_CE9")

    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_22(0x138, 0x0, 0x64)
    OP_22(0x146, 0x1, 0x46)
    Sleep(2500)
    OP_23(0x146)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #11
        "\x07\x00得到了\x1F\xBB\x05\x07\x00。\x02",
    )

    Jump("loc_D2D")

    label("loc_D2D")

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x5BB, 1)
    OP_3F(0x33B, 1)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(    #12
        0x22,
        (
            "#1616F#12C#5P呵呵……\x01",
            "总算做成了。\x02\x03",

            "#1611F要是再发现这样的石头\x01",
            "就请拿过来给我。\x02\x03",

            "我可以把它制作成\x01",
            "对你们有所帮助的武器。#0C\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2C37)
    Jump("loc_1887")

    label("loc_DEA")

    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_22(0x138, 0x0, 0x64)
    OP_22(0x146, 0x1, 0x46)
    Sleep(2500)
    OP_23(0x146)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #13
        "\x07\x00得到了\x1F\xF4\x03\x07\x00。\x02",
    )

    Jump("loc_E2E")

    label("loc_E2E")

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x3F4, 1)
    OP_3F(0x33B, 1)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(    #14
        0x22,
        (
            "#1616F#12C#5P呵呵……\x01",
            "总算做成了。\x02\x03",

            "#1611F要是再发现这样的石头\x01",
            "就请拿过来给我。\x02\x03",

            "我可以把它制作成\x01",
            "对你们有所帮助的武器。#0C\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2C37)
    Jump("loc_1887")

    label("loc_EEB")

    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_22(0x138, 0x0, 0x64)
    OP_22(0x146, 0x1, 0x46)
    Sleep(2500)
    OP_23(0x146)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #15
        "\x07\x00得到了\x1F\x24\x04\x07\x00。\x02",
    )

    Jump("loc_F2F")

    label("loc_F2F")

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x424, 1)
    OP_3F(0x33B, 1)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(    #16
        0x22,
        (
            "#1616F#12C#5P呵呵……\x01",
            "总算做成了。\x02\x03",

            "#1611F要是再发现这样的石头\x01",
            "就请拿过来给我。\x02\x03",

            "我可以把它制作成\x01",
            "对你们有所帮助的武器。#0C\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2C37)
    Jump("loc_1887")

    label("loc_FEC")

    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_22(0x138, 0x0, 0x64)
    OP_22(0x146, 0x1, 0x46)
    Sleep(2500)
    OP_23(0x146)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #17
        "\x07\x00得到了\x1F\x4F\x04\x07\x00。\x02",
    )

    Jump("loc_1030")

    label("loc_1030")

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x44F, 1)
    OP_3F(0x33B, 1)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(    #18
        0x22,
        (
            "#1616F#12C#5P呵呵……\x01",
            "总算做成了。\x02\x03",

            "#1611F要是再发现这样的石头\x01",
            "就请拿过来给我。\x02\x03",

            "我可以把它制作成\x01",
            "对你们有所帮助的武器。#0C\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1887")

    label("loc_10EA")

    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_22(0x138, 0x0, 0x64)
    OP_22(0x146, 0x1, 0x46)
    Sleep(2500)
    OP_23(0x146)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #19
        "\x07\x00得到了\x1F\x7F\x04\x07\x00。\x02",
    )

    Jump("loc_112E")

    label("loc_112E")

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x47F, 1)
    OP_3F(0x33B, 1)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(    #20
        0x22,
        (
            "#1616F#12C#5P呵呵……\x01",
            "总算做成了。\x02\x03",

            "#1611F要是再发现这样的石头\x01",
            "就请拿过来给我。\x02\x03",

            "我可以把它制作成\x01",
            "对你们有所帮助的武器。#0C\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2C37)
    Jump("loc_1887")

    label("loc_11EB")

    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_22(0x138, 0x0, 0x64)
    OP_22(0x146, 0x1, 0x46)
    Sleep(2500)
    OP_23(0x146)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #21
        "\x07\x00得到了\x1F\xAD\x04\x07\x00。\x02",
    )

    Jump("loc_122F")

    label("loc_122F")

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x4AD, 1)
    OP_3F(0x33B, 1)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(    #22
        0x22,
        (
            "#1616F#12C#5P呵呵……\x01",
            "总算做成了。\x02\x03",

            "#1611F要是再发现这样的石头\x01",
            "就请拿过来给我。\x02\x03",

            "我可以把它制作成\x01",
            "对你们有所帮助的武器。#0C\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2C37)
    Jump("loc_1887")

    label("loc_12EC")

    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_22(0x138, 0x0, 0x64)
    OP_22(0x146, 0x1, 0x46)
    Sleep(2500)
    OP_23(0x146)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #23
        "\x07\x00得到了\x1F\xD9\x04\x07\x00。\x02",
    )

    Jump("loc_1330")

    label("loc_1330")

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x4D9, 1)
    OP_3F(0x33B, 1)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(    #24
        0x22,
        (
            "#1616F#12C#5P呵呵……\x01",
            "总算做成了。\x02\x03",

            "#1611F要是再发现这样的石头\x01",
            "就请拿过来给我。\x02\x03",

            "我可以把它制作成\x01",
            "对你们有所帮助的武器。#0C\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2C37)
    Jump("loc_1887")

    label("loc_13ED")

    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_22(0x138, 0x0, 0x64)
    OP_22(0x146, 0x1, 0x46)
    Sleep(2500)
    OP_23(0x146)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #25
        "\x07\x00得到了\x1F\x07\x05\x07\x00。\x02",
    )

    Jump("loc_1431")

    label("loc_1431")

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x507, 1)
    OP_3F(0x33B, 1)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(    #26
        0x22,
        (
            "#1616F#12C#5P呵呵……\x01",
            "总算做成了。\x02\x03",

            "#1611F要是再发现这样的石头\x01",
            "就请拿过来给我。\x02\x03",

            "我可以把它制作成\x01",
            "对你们有所帮助的武器。#0C\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2C37)
    Jump("loc_1887")

    label("loc_14EE")

    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_22(0x138, 0x0, 0x64)
    OP_22(0x146, 0x1, 0x46)
    Sleep(2500)
    OP_23(0x146)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #27
        "\x07\x00得到了\x1F\x30\x05\x07\x00。\x02",
    )

    Jump("loc_1532")

    label("loc_1532")

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x530, 1)
    OP_3F(0x33B, 1)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(    #28
        0x22,
        (
            "#1616F#12C#5P呵呵……\x01",
            "总算做成了。\x02\x03",

            "#1611F要是再发现这样的石头\x01",
            "就请拿过来给我。\x02\x03",

            "我可以把它制作成\x01",
            "对你们有所帮助的武器。#0C\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2C37)
    Jump("loc_1887")

    label("loc_15EF")

    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_22(0x138, 0x0, 0x64)
    OP_22(0x146, 0x1, 0x46)
    Sleep(2500)
    OP_23(0x146)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #29
        "\x07\x00得到了\x1F\x89\x05\x07\x00。\x02",
    )

    Jump("loc_1633")

    label("loc_1633")

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x589, 1)
    OP_3F(0x33B, 1)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(    #30
        0x22,
        (
            "#1616F#12C#5P呵呵……\x01",
            "总算做成了。\x02\x03",

            "#1611F要是再发现这样的石头\x01",
            "就请拿过来给我。\x02\x03",

            "我可以把它制作成\x01",
            "对你们有所帮助的武器。#0C\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2C37)
    Jump("loc_1887")

    label("loc_16F0")

    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_22(0x138, 0x0, 0x64)
    OP_22(0x146, 0x1, 0x46)
    Sleep(2500)
    OP_23(0x146)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #31
        "\x07\x00得到了\x1F\xE0\x05\x07\x00。\x02",
    )

    Jump("loc_1734")

    label("loc_1734")

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x5E0, 1)
    OP_3F(0x33B, 1)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(    #32
        0x22,
        (
            "#1616F#12C#5P呵呵……\x01",
            "总算做成了。\x02\x03",

            "#1611F要是再发现这样的石头\x01",
            "就请拿过来给我。\x02\x03",

            "我可以把它制作成\x01",
            "对你们有所帮助的武器。#0C\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2C37)
    Jump("loc_1887")

    label("loc_17F1")

    FadeToBright(300, 0)
    OP_0D()

    ChrTalk(    #33
        0x22,
        (
            "#1615F#12C#5P是吗……\x02\x03",

            "#1610F如果改变主意的话，\x01",
            "就把石头交给我吧。\x02\x03",

            "我可以把它制作成\x01",
            "对你们有所帮助的武器。#0C\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1887")

    label("loc_1887")

    Jump("loc_1922")

    label("loc_188A")

    OP_56(0x0)
    FadeToBright(300, 0)
    OP_0D()

    ChrTalk(    #34
        0x22,
        (
            "#1615F#12C#5P是吗……\x02\x03",

            "#1610F如果改变主意的话，\x01",
            "就把石头交给我吧。\x02\x03",

            "我可以把它制作成\x01",
            "对你们有所帮助的武器。#0C\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1922")

    label("loc_1922")

    OP_A2(0x2C36)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6D(-540, 4000, 1460, 0)
    OP_67(0, 7900, -10000, 0)
    OP_6B(2530, 0)
    OP_6C(0, 0)
    OP_6E(450, 0)
    SetChrPos(0x0, -540, 4000, 1460, 315)
    SetChrPos(0x1, -540, 4000, 1460, 315)
    SetChrPos(0x2, -540, 4000, 1460, 315)
    SetChrPos(0x3, -540, 4000, 1460, 315)
    SetChrChipByIndex(0x0, 65535)
    SetChrChipByIndex(0x1, 65535)
    SetChrChipByIndex(0x2, 65535)
    SetChrChipByIndex(0x3, 65535)
    SetChrSubChip(0x0, 0)
    SetChrSubChip(0x1, 0)
    SetChrSubChip(0x2, 0)
    SetChrSubChip(0x3, 0)
    OP_69(0x0, 0x0)
    Sleep(500)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    SetMapFlags(0x2000000)
    Return()

    # Function_6_6FC end

    def Function_7_19F6(): pass

    label("Function_7_19F6")


    ChrTalk(    #35
        0x22,
        (
            "#1610F#12C要用塞姆里亚石\x01",
            "制作武器吗？\x02\x03",

            "我明白了。\x01",
            "请选择要制作的种类。#0C\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, 30, -1, -1)

    AnonymousTalk(    #36
        "\x06\x18\x07\x05制作成哪种武器呢？\x02",
    )

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        2,
        -1,
        120,
        1,
        (
            "自动弓「七七无穷射」\x01",          # 0
            "法剑  「光铬剑」\x01",              # 1
            "棒具  「星球之光」\x01",            # 2
            "双剑  「行云流水」\x01",            # 3
            "鞭    「虹」\x01",                  # 4
            "导力枪「假面之眼」\x01",            # 5
            "单手剑「神圣新星」\x01",            # 6
            "大剑  「动力化石剑」\x01",          # 7
            "导力炮「溶化破坏者」\x01",          # 8
            "护手甲「四圣兽」\x01",              # 9
            "刀    「彗星」\x01",                # 10
            "巨镰  「复仇女神之诅咒」\x01",      # 11
            "退出\x01",                          # 12
        )
    )

    Jump("loc_1B8A")

    label("loc_1B8A")

    MenuEnd(0x4)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x2)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_END)),
        (0, "loc_1BD4"),
        (1, "loc_1D4C"),
        (2, "loc_1EC4"),
        (3, "loc_203C"),
        (4, "loc_21B4"),
        (5, "loc_232C"),
        (6, "loc_24A4"),
        (7, "loc_261C"),
        (8, "loc_2794"),
        (9, "loc_290C"),
        (10, "loc_2A84"),
        (11, "loc_2BFC"),
        (SWITCH_DEFAULT, "loc_2D74"),
    )


    label("loc_1BD4")

    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_22(0x138, 0x0, 0x64)
    OP_22(0x146, 0x1, 0x46)
    Sleep(2500)
    OP_23(0x146)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #37
        "\x07\x00得到了\x1F\x61\x05\x07\x00。\x02",
    )

    Jump("loc_1C18")

    label("loc_1C18")

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x561, 1)
    OP_3F(0x33B, 1)
    FadeToBright(1000, 0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x586, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1CDA")

    ChrTalk(    #38
        0x22,
        (
            "#1616F#12C呵呵……\x01",
            "总算做成了。\x02\x03",

            "#1611F要是再发现这样的石头\x01",
            "就请拿过来给我。\x02\x03",

            "我可以把它制作成\x01",
            "对你们有所帮助的武器。#0C\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2C37)
    Jump("loc_1D49")

    label("loc_1CDA")


    ChrTalk(    #39
        0x22,
        (
            "#1610F#12C要是再发现这样的石头\x01",
            "就请拿过来给我。\x02\x03",

            "我可以把它制作成\x01",
            "对你们有所帮助的武器。#0C\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D49")

    Jump("loc_2DF0")

    label("loc_1D4C")

    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_22(0x138, 0x0, 0x64)
    OP_22(0x146, 0x1, 0x46)
    Sleep(2500)
    OP_23(0x146)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #40
        "\x07\x00得到了\x1F\xBB\x05\x07\x00。\x02",
    )

    Jump("loc_1D90")

    label("loc_1D90")

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x5BB, 1)
    OP_3F(0x33B, 1)
    FadeToBright(1000, 0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x586, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E52")

    ChrTalk(    #41
        0x22,
        (
            "#1616F#12C呵呵……\x01",
            "总算做成了。\x02\x03",

            "#1611F要是再发现这样的石头\x01",
            "就请拿过来给我。\x02\x03",

            "我可以把它制作成\x01",
            "对你们有所帮助的武器。#0C\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2C37)
    Jump("loc_1EC1")

    label("loc_1E52")


    ChrTalk(    #42
        0x22,
        (
            "#1610F#12C要是再发现这样的石头\x01",
            "就请拿过来给我。\x02\x03",

            "我可以把它制作成\x01",
            "对你们有所帮助的武器。#0C\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1EC1")

    Jump("loc_2DF0")

    label("loc_1EC4")

    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_22(0x138, 0x0, 0x64)
    OP_22(0x146, 0x1, 0x46)
    Sleep(2500)
    OP_23(0x146)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #43
        "\x07\x00得到了\x1F\xF4\x03\x07\x00。\x02",
    )

    Jump("loc_1F08")

    label("loc_1F08")

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x3F4, 1)
    OP_3F(0x33B, 1)
    FadeToBright(1000, 0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x586, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1FCA")

    ChrTalk(    #44
        0x22,
        (
            "#1616F#12C呵呵……\x01",
            "总算做成了。\x02\x03",

            "#1611F要是再发现这样的石头\x01",
            "就请拿过来给我。\x02\x03",

            "我可以把它制作成\x01",
            "对你们有所帮助的武器。#0C\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2C37)
    Jump("loc_2039")

    label("loc_1FCA")


    ChrTalk(    #45
        0x22,
        (
            "#1610F#12C要是再发现这样的石头\x01",
            "就请拿过来给我。\x02\x03",

            "我可以把它制作成\x01",
            "对你们有所帮助的武器。#0C\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2039")

    Jump("loc_2DF0")

    label("loc_203C")

    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_22(0x138, 0x0, 0x64)
    OP_22(0x146, 0x1, 0x46)
    Sleep(2500)
    OP_23(0x146)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #46
        "\x07\x00得到了\x1F\x24\x04\x07\x00。\x02",
    )

    Jump("loc_2080")

    label("loc_2080")

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x424, 1)
    OP_3F(0x33B, 1)
    FadeToBright(1000, 0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x586, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2142")

    ChrTalk(    #47
        0x22,
        (
            "#1616F#12C呵呵……\x01",
            "总算做成了。\x02\x03",

            "#1611F要是再发现这样的石头\x01",
            "就请拿过来给我。\x02\x03",

            "我可以把它制作成\x01",
            "对你们有所帮助的武器。#0C\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2C37)
    Jump("loc_21B1")

    label("loc_2142")


    ChrTalk(    #48
        0x22,
        (
            "#1610F#12C要是再发现这样的石头\x01",
            "就请拿过来给我。\x02\x03",

            "我可以把它制作成\x01",
            "对你们有所帮助的武器。#0C\x02",
        )
    )

    CloseMessageWindow()

    label("loc_21B1")

    Jump("loc_2DF0")

    label("loc_21B4")

    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_22(0x138, 0x0, 0x64)
    OP_22(0x146, 0x1, 0x46)
    Sleep(2500)
    OP_23(0x146)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #49
        "\x07\x00得到了\x1F\x4F\x04\x07\x00。\x02",
    )

    Jump("loc_21F8")

    label("loc_21F8")

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x44F, 1)
    OP_3F(0x33B, 1)
    FadeToBright(1000, 0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x586, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_22BA")

    ChrTalk(    #50
        0x22,
        (
            "#1616F#12C呵呵……\x01",
            "总算做成了。\x02\x03",

            "#1611F要是再发现这样的石头\x01",
            "就请拿过来给我。\x02\x03",

            "我可以把它制作成\x01",
            "对你们有所帮助的武器。#0C\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2C37)
    Jump("loc_2329")

    label("loc_22BA")


    ChrTalk(    #51
        0x22,
        (
            "#1610F#12C要是再发现这样的石头\x01",
            "就请拿过来给我。\x02\x03",

            "我可以把它制作成\x01",
            "对你们有所帮助的武器。#0C\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2329")

    Jump("loc_2DF0")

    label("loc_232C")

    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_22(0x138, 0x0, 0x64)
    OP_22(0x146, 0x1, 0x46)
    Sleep(2500)
    OP_23(0x146)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #52
        "\x07\x00得到了\x1F\x7F\x04\x07\x00。\x02",
    )

    Jump("loc_2370")

    label("loc_2370")

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x47F, 1)
    OP_3F(0x33B, 1)
    FadeToBright(1000, 0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x586, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2432")

    ChrTalk(    #53
        0x22,
        (
            "#1616F#12C呵呵……\x01",
            "总算做成了。\x02\x03",

            "#1611F要是再发现这样的石头\x01",
            "就请拿过来给我。\x02\x03",

            "我可以把它制作成\x01",
            "对你们有所帮助的武器。#0C\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2C37)
    Jump("loc_24A1")

    label("loc_2432")


    ChrTalk(    #54
        0x22,
        (
            "#1610F#12C要是再发现这样的石头\x01",
            "就请拿过来给我。\x02\x03",

            "我可以把它制作成\x01",
            "对你们有所帮助的武器。#0C\x02",
        )
    )

    CloseMessageWindow()

    label("loc_24A1")

    Jump("loc_2DF0")

    label("loc_24A4")

    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_22(0x138, 0x0, 0x64)
    OP_22(0x146, 0x1, 0x46)
    Sleep(2500)
    OP_23(0x146)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #55
        "\x07\x00得到了\x1F\xAD\x04\x07\x00。\x02",
    )

    Jump("loc_24E8")

    label("loc_24E8")

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x4AD, 1)
    OP_3F(0x33B, 1)
    FadeToBright(1000, 0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x586, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_25AA")

    ChrTalk(    #56
        0x22,
        (
            "#1616F#12C呵呵……\x01",
            "总算做成了。\x02\x03",

            "#1611F要是再发现这样的石头\x01",
            "就请拿过来给我。\x02\x03",

            "我可以把它制作成\x01",
            "对你们有所帮助的武器。#0C\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2C37)
    Jump("loc_2619")

    label("loc_25AA")


    ChrTalk(    #57
        0x22,
        (
            "#1610F#12C要是再发现这样的石头\x01",
            "就请拿过来给我。\x02\x03",

            "我可以把它制作成\x01",
            "对你们有所帮助的武器。#0C\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2619")

    Jump("loc_2DF0")

    label("loc_261C")

    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_22(0x138, 0x0, 0x64)
    OP_22(0x146, 0x1, 0x46)
    Sleep(2500)
    OP_23(0x146)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #58
        "\x07\x00得到了\x1F\xD9\x04\x07\x00。\x02",
    )

    Jump("loc_2660")

    label("loc_2660")

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x4D9, 1)
    OP_3F(0x33B, 1)
    FadeToBright(1000, 0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x586, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2722")

    ChrTalk(    #59
        0x22,
        (
            "#1616F#12C呵呵……\x01",
            "总算做成了。\x02\x03",

            "#1611F要是再发现这样的石头\x01",
            "就请拿过来给我。\x02\x03",

            "我可以把它制作成\x01",
            "对你们有所帮助的武器。#0C\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2C37)
    Jump("loc_2791")

    label("loc_2722")


    ChrTalk(    #60
        0x22,
        (
            "#1610F#12C要是再发现这样的石头\x01",
            "就请拿过来给我。\x02\x03",

            "我可以把它制作成\x01",
            "对你们有所帮助的武器。#0C\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2791")

    Jump("loc_2DF0")

    label("loc_2794")

    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_22(0x138, 0x0, 0x64)
    OP_22(0x146, 0x1, 0x46)
    Sleep(2500)
    OP_23(0x146)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #61
        "\x07\x00得到了\x1F\x07\x05\x07\x00。\x02",
    )

    Jump("loc_27D8")

    label("loc_27D8")

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x507, 1)
    OP_3F(0x33B, 1)
    FadeToBright(1000, 0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x586, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_289A")

    ChrTalk(    #62
        0x22,
        (
            "#1616F#12C呵呵……\x01",
            "总算做成了。\x02\x03",

            "#1611F要是再发现这样的石头\x01",
            "就请拿过来给我。\x02\x03",

            "我可以把它制作成\x01",
            "对你们有所帮助的武器。#0C\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2C37)
    Jump("loc_2909")

    label("loc_289A")


    ChrTalk(    #63
        0x22,
        (
            "#1610F#12C要是再发现这样的石头\x01",
            "就请拿过来给我。\x02\x03",

            "我可以把它制作成\x01",
            "对你们有所帮助的武器。#0C\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2909")

    Jump("loc_2DF0")

    label("loc_290C")

    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_22(0x138, 0x0, 0x64)
    OP_22(0x146, 0x1, 0x46)
    Sleep(2500)
    OP_23(0x146)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #64
        "\x07\x00得到了\x1F\x30\x05\x07\x00。\x02",
    )

    Jump("loc_2950")

    label("loc_2950")

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x530, 1)
    OP_3F(0x33B, 1)
    FadeToBright(1000, 0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x586, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2A12")

    ChrTalk(    #65
        0x22,
        (
            "#1616F#12C呵呵……\x01",
            "总算做成了。\x02\x03",

            "#1611F要是再发现这样的石头\x01",
            "就请拿过来给我。\x02\x03",

            "我可以把它制作成\x01",
            "对你们有所帮助的武器。#0C\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2C37)
    Jump("loc_2A81")

    label("loc_2A12")


    ChrTalk(    #66
        0x22,
        (
            "#1610F#12C要是再发现这样的石头\x01",
            "就请拿过来给我。\x02\x03",

            "我可以把它制作成\x01",
            "对你们有所帮助的武器。#0C\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A81")

    Jump("loc_2DF0")

    label("loc_2A84")

    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_22(0x138, 0x0, 0x64)
    OP_22(0x146, 0x1, 0x46)
    Sleep(2500)
    OP_23(0x146)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #67
        "\x07\x00得到了\x1F\x89\x05\x07\x00。\x02",
    )

    Jump("loc_2AC8")

    label("loc_2AC8")

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x589, 1)
    OP_3F(0x33B, 1)
    FadeToBright(1000, 0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x586, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2B8A")

    ChrTalk(    #68
        0x22,
        (
            "#1616F#12C呵呵……\x01",
            "总算做成了。\x02\x03",

            "#1611F要是再发现这样的石头\x01",
            "就请拿过来给我。\x02\x03",

            "我可以把它制作成\x01",
            "对你们有所帮助的武器。#0C\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2C37)
    Jump("loc_2BF9")

    label("loc_2B8A")


    ChrTalk(    #69
        0x22,
        (
            "#1610F#12C要是再发现这样的石头\x01",
            "就请拿过来给我。\x02\x03",

            "我可以把它制作成\x01",
            "对你们有所帮助的武器。#0C\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2BF9")

    Jump("loc_2DF0")

    label("loc_2BFC")

    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_22(0x138, 0x0, 0x64)
    OP_22(0x146, 0x1, 0x46)
    Sleep(2500)
    OP_23(0x146)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #70
        "\x07\x00得到了\x1F\xE0\x05\x07\x00。\x02",
    )

    Jump("loc_2C40")

    label("loc_2C40")

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x5E0, 1)
    OP_3F(0x33B, 1)
    FadeToBright(1000, 0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x586, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2D02")

    ChrTalk(    #71
        0x22,
        (
            "#1616F#12C呵呵……\x01",
            "总算做成了。\x02\x03",

            "#1611F要是再发现这样的石头\x01",
            "就请拿过来给我。\x02\x03",

            "我可以把它制作成\x01",
            "对你们有所帮助的武器。#0C\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2C37)
    Jump("loc_2D71")

    label("loc_2D02")


    ChrTalk(    #72
        0x22,
        (
            "#1610F#12C要是再发现这样的石头\x01",
            "就请拿过来给我。\x02\x03",

            "我可以把它制作成\x01",
            "对你们有所帮助的武器。#0C\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2D71")

    Jump("loc_2DF0")

    label("loc_2D74")

    FadeToBright(300, 0)
    OP_0D()

    ChrTalk(    #73
        0x22,
        (
            "#1610F#12C如果改变主意的话，\x01",
            "就把石头交给我吧。\x02\x03",

            "我可以把它制作成\x01",
            "对你们有所帮助的武器。#0C\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2DF0")

    label("loc_2DF0")

    Return()

    # Function_7_19F6 end

    def Function_8_2DF1(): pass

    label("Function_8_2DF1")


    ChrTalk(    #74
        0x22,
        (
            "#1611F#12C呵呵，\x01",
            "玲的行动真是让人吃惊呢。\x02\x03",

            "#1610F不过在这个世界里，\x01",
            "不正规的行为\x01",
            "是会消耗巨大精神力的。\x02\x03",

            "#1616F过度使用力量的话，\x01",
            "身心都会过度消耗，\x01",
            "请务必注意控制。#0C\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_308A")

    ChrTalk(    #75
        0x110,
        (
            "#268F呼，真没办法。\x02\x03",

            "#267F反正帕蒂尔·玛蒂尔也来了，\x01",
            "玲已经很满足了……\x02\x03",

            "#260F这点小事我就照办吧，\x01",
            "姐姐。\x02",
        )
    )

    Jump("loc_2F4E")

    label("loc_2F4E")

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2FA7")

    ChrTalk(    #76
        0x105,
        (
            "#1165F（呵呵，\x01",
            "  玲把千年以前的始祖大人\x01",
            "  也当作姐姐……）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_305A")

    label("loc_2FA7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3005")

    ChrTalk(    #77
        0x101,
        (
            "#1016F（哈哈，\x01",
            "  玲把千年以前的赛雷斯托始祖\x01",
            "  也当作姐姐了……）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_305A")

    label("loc_3005")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_305A")

    ChrTalk(    #78
        0x109,
        (
            "#1077F（哈哈……\x01",
            "  千年以前的始祖\x01",
            "  对她来说也是姐姐吗。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_305A")


    ChrTalk(    #79
        0x22,
        "#1611F#12C呵呵，那就请多关照了。#0C\x02",
    )

    CloseMessageWindow()

    label("loc_308A")

    OP_A2(0x2657)
    Return()

    # Function_8_2DF1 end

    def Function_9_308E(): pass

    label("Function_9_308E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x586, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4CA, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_30A4")
    Call(5, 8)
    Jump("loc_310F")

    label("loc_30A4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x584, 0)), scpexpr(EXPR_END)), "loc_30E6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x584, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_30BA")
    Call(5, 2)
    Jump("loc_30E3")

    label("loc_30BA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x33B, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_30DF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x586, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_30D8")
    Call(5, 6)
    Jump("loc_30DC")

    label("loc_30D8")

    Call(5, 5)

    label("loc_30DC")

    Jump("loc_30E3")

    label("loc_30DF")

    Call(5, 3)

    label("loc_30E3")

    Jump("loc_310F")

    label("loc_30E6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x33B, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_310B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x586, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3104")
    Call(5, 6)
    Jump("loc_3108")

    label("loc_3104")

    Call(5, 4)

    label("loc_3108")

    Jump("loc_310F")

    label("loc_310B")

    Call(5, 10)

    label("loc_310F")

    TalkEnd(0xFE)
    Return()

    # Function_9_308E end

    def Function_10_3113(): pass

    label("Function_10_3113")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x584, 0)), scpexpr(EXPR_END)), "loc_327E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_31FB")
    OP_A2(0x3)

    ChrTalk(    #80
        0x22,
        (
            "#1616F#12C……呵呵，这个地方\x01",
            "已经很久没这么热闹了。\x02\x03",

            "……再次有16个人\x01",
            "聚集在这里吗…………\x02\x03",

            "#1611F说起来，『封印机构』的\x01",
            "核心队员也是16个人……\x02\x03",

            "这难道也是\x01",
            "空之女神的引导吗。#0C\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_327B")

    label("loc_31FB")


    ChrTalk(    #81
        0x22,
        (
            "#1616F#12C出发准备完成了的话，\x01",
            "就请告诉我一声。\x02\x03",

            "#1611F我会试着使用\x01",
            "『庭院』的力量\x01",
            "帮忙让『白翼』苏醒的。#0C\x02",
        )
    )

    CloseMessageWindow()

    label("loc_327B")

    Jump("loc_45EB")

    label("loc_327E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x565, 3)), scpexpr(EXPR_END)), "loc_353B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_33F5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x580, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_33B5")

    ChrTalk(    #82
        0x22,
        (
            "#1615F#12C………最后的障壁\x01",
            "好像也解除了。\x02\x03",

            "#1613F不过…………\x01",
            "无法确认前方的领域。\x02\x03",

            "………好奇怪啊…………#0C\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x565, 4)), scpexpr(EXPR_END)), "loc_33B2")

    ChrTalk(    #83
        0x109,
        (
            "#1060F……我想莉丝\x01",
            "应该就是那个『钥匙』。\x02\x03",

            "#1075F首先去试一试吧。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_33B2")

    ChrTalk(    #84
        0x10F,
        "#1802F………………………………\x02",
    )

    CloseMessageWindow()

    label("loc_33B2")

    Jump("loc_33EF")

    label("loc_33B5")


    ChrTalk(    #85
        0x22,
        "#1613F#12C…………………………………………#0C\x02",
    )

    CloseMessageWindow()

    label("loc_33EF")

    OP_A2(0x3)
    Jump("loc_3538")

    label("loc_33F5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x580, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_34FE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x565, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3497")

    ChrTalk(    #86
        0x22,
        (
            "#1615F#12C无法确认前方的领域……\x02\x03",

            "#1613F这个领域似乎也需要\x01",
            "特定的『钥匙』……#0C\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0x109,
        "#1067F………………………………\x02",
    )

    CloseMessageWindow()
    Jump("loc_34FB")

    label("loc_3497")


    ChrTalk(    #88
        0x22,
        (
            "#1615F#12C无法确认前方的领域……\x02\x03",

            "#1613F这个领域似乎也需要\x01",
            "特定的『钥匙』……#0C\x02",
        )
    )

    CloseMessageWindow()

    label("loc_34FB")

    Jump("loc_3538")

    label("loc_34FE")


    ChrTalk(    #89
        0x22,
        "#1613F#12C…………………………………………#0C\x02",
    )

    CloseMessageWindow()

    label("loc_3538")

    Jump("loc_45EB")

    label("loc_353B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x564, 0)), scpexpr(EXPR_END)), "loc_38B4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3767")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x564, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_35D0")

    ChrTalk(    #90
        0x22,
        (
            "#1615F#12C最后的领域…………\x02\x03",

            "在『门』的那边，\x01",
            "我感到了一种不寻常的气息。\x02\x03",

            "#1612F请务必小心。#0C\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3761")

    label("loc_35D0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3650")
    TurnDirection(0x22, 0x102, 0)

    ChrTalk(    #91
        0x22,
        (
            "#1613F#12C…………………………\x02\x03",

            "#1610F……请务必注意。#0C\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0x102,
        "#1500F……是。\x02",
    )

    CloseMessageWindow()
    Jump("loc_3761")

    label("loc_3650")


    ChrTalk(    #93
        0x22,
        "#1613F#12C『灭亡故里的遗孤』―――#0C\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0x109,
        "#1063F最后是约修亚吗……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_36E4")

    ChrTalk(    #95
        0x101,
        "#1002F……………………………………\x02",
    )

    CloseMessageWindow()

    label("loc_36E4")


    ChrTalk(    #96
        0x22,
        (
            "#1615F#12C黑曜之门的钥匙…………\x01",
            "就在那边的泉水旁边。\x02\x03",

            "#1612F他好像已经做好准备了。\x01",
            "请去和他说一声吧。#0C\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3761")

    OP_A2(0x3)
    Jump("loc_38B1")

    label("loc_3767")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x564, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3809")

    ChrTalk(    #97
        0x22,
        (
            "#1612F#12C『第六星层』的试炼\x01",
            "终于要到最后了。\x02\x03",

            "#1613F可是，这种气氛……#0C\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3806")

    ChrTalk(    #98
        0x102,
        "#1503F………………………………\x02",
    )

    CloseMessageWindow()

    label("loc_3806")

    Jump("loc_38B1")

    label("loc_3809")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3844")

    ChrTalk(    #99
        0x22,
        "#1610F#12C……请务必小心。#0C\x02",
    )

    CloseMessageWindow()
    Jump("loc_38B1")

    label("loc_3844")


    ChrTalk(    #100
        0x22,
        (
            "#1615F#12C黑曜之门的钥匙…………\x01",
            "就在那边的泉水旁边。\x02\x03",

            "#1613F他好像已经\x01",
            "做好准备了……#0C\x02",
        )
    )

    CloseMessageWindow()

    label("loc_38B1")

    Jump("loc_45EB")

    label("loc_38B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x562, 5)), scpexpr(EXPR_END)), "loc_3C7D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3AF5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x562, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3951")

    ChrTalk(    #101
        0x22,
        (
            "#1613F#12C………………………………\x02\x03",

            "虽然很缓慢，\x01",
            "但『王』的力量仍在不断增强。\x02\x03",

            "#1612F请各位尽快前进。#0C\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3AEF")

    label("loc_3951")


    ChrTalk(    #102
        0x22,
        (
            "#1610F#12C为了通过红耀之门，\x01",
            "必须要有『剑圣的继承者』。#0C\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xB)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3A60")

    ChrTalk(    #103
        0x10C,
        "#115F……是指我吗…………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0x22,
        (
            "#1615F#12C……恐怕是。\x02\x03",

            "#1610F『影之王』利用\x01",
            "大家的思念和记忆\x01",
            "来设置试炼。\x02\x03",

            "……虽然伴随着困难，\x01",
            "但请各位继续前进。#0C\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3AEF")

    label("loc_3A60")


    ChrTalk(    #105
        0x109,
        "#1060F……是说理查德先生吗。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #106
        0x22,
        (
            "#1616F#12C……这寂静的波纹…………\x01",
            "他应该在高台那里。\x02\x03",

            "#1610F请去和他说一声吧。#0C\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3AEF")

    OP_A2(0x3)
    Jump("loc_3C7A")

    label("loc_3AF5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x562, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3B7B")

    ChrTalk(    #107
        0x22,
        (
            "#1615F#12C……我大半的力量\x01",
            "都在维持这个庭院。\x02\x03",

            "不过，这样下去的话……\x02\x03",

            "#1610F请各位尽快前进。#0C\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3C7A")

    label("loc_3B7B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xB)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3BEC")

    ChrTalk(    #108
        0x22,
        (
            "#1613F#12C红耀之门……\x01",
            "虽然伴随着巨大的困难……\x02\x03",

            "#1610F但请各位继续前进。#0C\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3C7A")

    label("loc_3BEC")


    ChrTalk(    #109
        0x22,
        (
            "#1610F#12C为了通过红耀之门，\x01",
            "必须要有『剑圣的继承者』。\x02\x03",

            "#1616F……他应该是\x01",
            "去了那边的高台。\x02\x03",

            "请去和他说一声吧。#0C\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3C7A")

    Jump("loc_45EB")

    label("loc_3C7D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x561, 0)), scpexpr(EXPR_END)), "loc_40ED")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3F56")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x561, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3D9B")

    ChrTalk(    #110
        0x22,
        (
            "#1610F#12C现在已经确认的『门』有四个……\x02\x03",

            "它们都连接到\x01",
            "『王』所创造的领域。\x02\x03",

            "#1613F……………………………………\x02\x03",

            "在它们前方，\x01",
            "还有无论如何都无法搜寻到的领域。\x02\x03",

            "#1615F……不靠大家的力量\x01",
            "果然还是无法解除\x01",
            "这个障壁吗……#0C\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3F50")

    label("loc_3D9B")


    ChrTalk(    #111
        0x22,
        (
            "#1610F#12C为了通过琥耀之门，\x01",
            "必须要有『剑道之少女』。#0C\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3EAC")

    ChrTalk(    #112
        0x10A,
        "#814F那个，好像是说我。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0x22,
        (
            "#1610F#12C……对。\x02\x03",

            "#1615F前面的领域\x01",
            "是『王』所创造出来的……\x02\x03",

            "很可能利用了\x01",
            "你们记忆里的空间。\x02\x03",

            "#1610F请务必小心。#0C\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3F50")

    label("loc_3EAC")


    ChrTalk(    #114
        0x109,
        "#1060F……是说亚妮拉丝吗。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0x22,
        (
            "#1610F#12C……嗯，应该是的。\x02\x03",

            "#1616F她现在……\x01",
            "……好像在大树之丘那里。\x02\x03",

            "#1610F去和她说一声吧。#0C\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3F50")

    OP_A2(0x3)
    Jump("loc_40EA")

    label("loc_3F56")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x561, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3FFB")

    ChrTalk(    #116
        0x22,
        (
            "#1610F#12C现在已经确认的『门』有四个……\x02\x03",

            "各自都需要特定的人物\x01",
            "作为前进的钥匙。\x02\x03",

            "#1615F……为了继续前进，\x01",
            "需要大家的力量……#0C\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_40EA")

    label("loc_3FFB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_405E")

    ChrTalk(    #117
        0x22,
        (
            "#1612F#12C前面的领域\x01",
            "是『王』所创造出来的……\x02\x03",

            "请务必小心。#0C\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_40EA")

    label("loc_405E")


    ChrTalk(    #118
        0x22,
        (
            "#1610F#12C为了通过琥耀之门，\x01",
            "必须要有『剑道之少女』。\x02\x03",

            "#1616F……现在她应该\x01",
            "在大树之丘那里。\x02\x03",

            "去和她说一声吧。#0C\x02",
        )
    )

    CloseMessageWindow()

    label("loc_40EA")

    Jump("loc_45EB")

    label("loc_40ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x560, 0)), scpexpr(EXPR_END)), "loc_45EB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_43EA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x560, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_41BB")

    ChrTalk(    #119
        0x22,
        (
            "#1615F#12C我自身也是『影』，\x01",
            "并且是基于这个『影之国』的法则\x01",
            "才能成立的存在。\x02\x03",

            "因此我不能做出\x01",
            "超出此范围的事……\x02\x03",

            "#1610F但我仍然会尽可能的\x01",
            "来支持大家。#0C\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_43E4")

    label("loc_41BB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_42FB")

    ChrTalk(    #120
        0x22,
        (
            "#1615F#12C要通过『影之王』\x01",
            "设置的『门』，必须要带上\x01",
            "特定的人物同行才行。\x02\x03",

            "#1612F要进入苍耀之门\x01",
            "必须要有『白翼』……#0C\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #121
        0x105,
        "#1167F……好像是说我吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #122
        0x22,
        (
            "#1613F#12C……嗯。\x02\x03",

            "#1612F在『影之国』中，\x01",
            "『王』的规则是绝对的……\x02\x03",

            "想要继续前进的话\x01",
            "就只能遵从。#0C\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_43E4")

    label("loc_42FB")


    ChrTalk(    #123
        0x22,
        (
            "#1615F#12C要通过『影之王』\x01",
            "设置的『门』，必须要带上\x01",
            "特定的人物同行才行。\x02\x03",

            "要进苍耀之门\x01",
            "必须要有『白翼』……#5200W \x01",
            "#20W#1612F那应该是在说我的后裔吧。\x02\x03",

            "#1610F……她现在好像\x01",
            "正在书架那里，\x01",
            "去和她说一声吧。#0C\x02",
        )
    )

    CloseMessageWindow()

    label("loc_43E4")

    OP_A2(0x3)
    Jump("loc_45EB")

    label("loc_43EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x560, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4499")

    ChrTalk(    #124
        0x22,
        (
            "#1610F#12C作为『影』存在的我，\x01",
            "是不能做出超出这个『影之国』法则的事的……\x02\x03",

            "但我仍然会尽可能的\x01",
            "来支持大家。\x02\x03",

            "#1611F遇到困难就来找我吧。#0C\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_45EB")

    label("loc_4499")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_453D")

    ChrTalk(    #125
        0x22,
        (
            "#1615F#12C为了通过苍耀之门，\x01",
            "必须要有『白翼』……\x01",
            "也就是我的后裔。\x02\x03",

            "#1612F……里面一定会有\x01",
            "相应的机关。\x02\x03",

            "请各位小心。#0C\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_45EB")

    label("loc_453D")


    ChrTalk(    #126
        0x22,
        (
            "#1615F#12C为了要通过苍耀之门，\x01",
            "必须要有『白翼』……\x01",
            "也就是我的后裔。\x02\x03",

            "#1610F……她现在好像\x01",
            "正在书架那里。\x02\x03",

            "我已经向她说明过了。\x01",
            "去和她说一声吧。#0C\x02",
        )
    )

    CloseMessageWindow()

    label("loc_45EB")

    Return()

    # Function_10_3113 end

    def Function_11_45EC(): pass

    label("Function_11_45EC")


    ChrTalk(    #127
        0x22,
        (
            "#1613F#12C如果乘坐『白翼』\x01",
            "出发前往『影之王』\x01",
            "那里的话……\x02\x03",

            "就不能再回到\x01",
            "这个『庭院』来了。\x02\x03",

            "#1612F做好准备了吗？#0C\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4698")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4854")

    Menu(
        2,
        -1,
        150,
        1,
        (
            "做好准备了\x01",        # 0
            "还要继续准备\x01",      # 1
        )
    )

    MenuEnd(0x4)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x2)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_END)),
        (0, "loc_46EC"),
        (SWITCH_DEFAULT, "loc_4844"),
    )


    label("loc_46EC")

    EventBegin(0x0)
    EventBegin(0x0)
    Fade(500)
    OP_6D(-900, 4000, 4220, 0)
    OP_67(0, 5450, -10000, 0)
    OP_6B(2120, 0)
    OP_6C(0, 0)
    OP_6E(410, 0)
    SetChrPos(0x0, -1040, 4000, 1270, 315)
    SetChrPos(0x1, -40, 4000, 2200, 315)
    SetChrPos(0x2, -110, 4000, -250, 315)
    SetChrPos(0x3, 870, 4000, 1110, 315)
    SetChrChipByIndex(0x0, 65535)
    SetChrChipByIndex(0x1, 65535)
    SetChrChipByIndex(0x2, 65535)
    SetChrChipByIndex(0x3, 65535)
    SetChrSubChip(0x0, 0)
    SetChrSubChip(0x1, 0)
    SetChrSubChip(0x2, 0)
    SetChrSubChip(0x3, 0)
    OP_8C(0x22, 135, 0)
    OP_0D()
    Sleep(300)

    ChrTalk(    #128
        0x22,
        (
            "#1616F#5P#12C……明白了。\x02\x03",

            "#1610F那么就叫上大家，\x01",
            "前往『白翼』吧。#0C\x02",
        )
    )

    CloseMessageWindow()

    def lambda_480A():
        OP_6B(2500, 3000)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_480A)
    FadeToDark(2000, 0, -1)
    OP_0D()
    WaitChrThread(0xEE, 0x0)
    SetMapFlags(0x2000000)
    OP_A2(0x2506)
    NewScene("ED6_DT21/M7002   ._SN", 100, 0, 0)
    IdleLoop()
    EventEnd(0x0)
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4851")

    label("loc_4844")

    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4851")

    label("loc_4851")

    Jump("loc_4698")

    label("loc_4854")

    Return()

    # Function_11_45EC end

    def Function_12_4855(): pass

    label("Function_12_4855")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4CB, 0)), scpexpr(EXPR_END)), "loc_4904")

    ChrTalk(    #129
        0x21,
        (
            "#1065F……埃尔赛尤号出击\x01",
            "只有一次机会。\x02\x03",

            "#1063F为了脱离这个世界，\x01",
            "迎向新的明天……\x02\x03",

            "#1062F……为了不留下遗憾，\x01",
            "趁现在把事情都处理完吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4A7A")

    label("loc_4904")

    SetChrSubChip(0xFE, 0)

    ChrTalk(    #130
        0x21,
        (
            "#1065F…………其实，\x01",
            "我本来有句话想对大家说。\x02\x03",

            "#1067F对被卷入这次事件\x01",
            "也毫无怨言地陪着我……\x02\x03",

            "#1063F不仅认真听我的胡言乱语，\x01",
            "而且还不遗余力地\x01",
            "给予我帮助的大家……\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xFE, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x1)
    Sleep(1300)

    ChrTalk(    #131
        0x21,
        (
            "#1062F不过，还是等到\x01",
            "大家平安离开之后再说吧。\x02\x03",

            "#1061F……在那之前请允许我暂时保留。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4A77")

    ChrTalk(    #132
        0x10F,
        "#1952F……嗯……………！\x02",
    )

    CloseMessageWindow()

    label("loc_4A77")

    OP_A2(0x2658)

    label("loc_4A7A")

    TalkEnd(0xFE)
    Return()

    # Function_12_4855 end

    def Function_13_4A7E(): pass

    label("Function_13_4A7E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x584, 0)), scpexpr(EXPR_END)), "loc_4BC6")
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4B49")

    ChrTalk(    #133
        0x16,
        (
            "#1164F……啊，各位。\x02\x03",

            "#1160F关于埃尔赛尤号的启动\x01",
            "已经有头绪了。\x02\x03",

            "#1382F不过在到达目的地之前\x01",
            "将会没有补给机会……\x02\x03",

            "请各位最好\x01",
            "趁现在好好休息一下。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x7)
    Jump("loc_4BC3")

    label("loc_4B49")


    ChrTalk(    #134
        0x16,
        (
            "#1160F在到达目的地之前\x01",
            "将会没有补给机会。\x02\x03",

            "#1382F途中也不知道会发生什么事，\x01",
            "请尽量趁现在好好休息一下。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4BC3")

    TalkEnd(0xFE)

    label("loc_4BC6")

    Return()

    # Function_13_4A7E end

    def Function_14_4BC7(): pass

    label("Function_14_4BC7")

    TalkBegin(0x1A)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4E78")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x561, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x561, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4E5B")
    EventBegin(0x0)
    Fade(500)
    OP_6D(5480, 4000, -8340, 0)
    OP_67(0, 6420, -10000, 0)
    OP_6B(2180, 0)
    OP_6C(315000, 0)
    OP_6E(400, 0)
    SetChrPos(0x109, 6530, 4000, -9150, 180)
    SetChrPos(0xEF, 7370, 4000, -7880, 180)
    SetChrPos(0xF0, 5500, 4000, -7630, 180)
    SetChrPos(0xF1, 6290, 4000, -6550, 180)
    OP_8C(0x1A, 0, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #135
        0x1A,
        (
            "#814F啊，大家。\x01",
            "有什么事吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #136
        0x109,
        "#1060F啊，是这么回事……\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(72, 320, 56, 3)

    AnonymousTalk(    #137
        (
            "\x07\x05凯文把琥耀石石碑上\x01",
            "记述的语句向亚妮拉丝作了说明。\x01",
            "　\x02",
        )
    )

    Jump("loc_4D18")

    label("loc_4D18")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    ChrTalk(    #138
        0x1A,
        (
            "#1317F『剑道之少女』……是说我吗！？\x02\x03",

            "#819F唔，那个……\x01",
            "我倒是觉得自己\x01",
            "并没有那么了不起啦……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #139
        0x109,
        (
            "#1077F没关系，不试试看怎么知道呢。\x02\x03",

            "#1078F能陪我们去看看吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #140
        0x1A,
        (
            "#810F嗯，当然了。\x01",
            "这点小事倒不要紧……\x02\x03",

            "#1310F只要做好准备，\x01",
            "我随时都可以加入队伍哦。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2B0B)
    Sleep(300)
    EventEnd(0x0)
    Jump("loc_4E78")

    label("loc_4E5B")


    ChrTalk(    #141
        0x1A,
        "#810F◆一般信息表示。\x02",
    )

    CloseMessageWindow()

    label("loc_4E78")

    TalkEnd(0x1A)
    Return()

    # Function_14_4BC7 end

    def Function_15_4E7C(): pass

    label("Function_15_4E7C")

    Return()

    # Function_15_4E7C end

    def Function_16_4E7D(): pass

    label("Function_16_4E7D")

    Return()

    # Function_16_4E7D end

    def Function_17_4E7E(): pass

    label("Function_17_4E7E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x584, 0)), scpexpr(EXPR_END)), "loc_50DF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5035")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4F5E")
    TalkBegin(0xFE)

    ChrTalk(    #142
        0x12,
        (
            "#170F我在这里\x01",
            "确认一下埃尔赛尤号\x01",
            "出发前的程序。\x02\x03",

            "#176F虽然应该没有大问题，\x01",
            "但这次我们没有正规船员。\x02\x03",

            "#178F作为舰长的我\x01",
            "更要好好的指挥了。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Jump("loc_502F")

    label("loc_4F5E")

    SetChrFlags(0xFE, 0x10)
    TalkBegin(0xFE)

    ChrTalk(    #143
        0x12,
        (
            "#176F……对了，\x01",
            "也有可能会遇到\x01",
            "外敌入侵的情况……\x02\x03",

            "#178F到达埃尔赛尤号后，\x01",
            "我和少校首先确认船内的情况。\x02\x03",

            "还要检查重要机关\x01",
            "和启动的设置等。\x02\x03",

            "#179F舰桥要员吗……\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    ClearChrFlags(0xFE, 0x10)

    label("loc_502F")

    OP_A2(0x4)
    Jump("loc_50DF")

    label("loc_5035")

    TalkBegin(0xFE)

    ChrTalk(    #144
        0x12,
        (
            "#170F要埃尔赛尤号启动的话\x01",
            "应该没有什么大问题。\x02\x03",

            "#176F不过在『星层』的外侧……\x01",
            "不知道到底会有什么等着我们呢。\x02\x03",

            "#178F还是做好万全的准备吧。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)

    label("loc_50DF")

    Return()

    # Function_17_4E7E end

    def Function_18_50E0(): pass

    label("Function_18_50E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x584, 0)), scpexpr(EXPR_END)), "loc_51DB")
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_51A3")

    ChrTalk(    #145
        0x13,
        (
            "#272F『影之王』……\x01",
            "露菲娜·亚尔珍特。\x02\x03",

            "她生前被称作『千之腕』，\x01",
            "用她那高超的交涉手段\x01",
            "解决了很多事件……\x02\x03",

            "#276F……这样的敌人\x01",
            "也许是最难对付的。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x5)
    Jump("loc_51D8")

    label("loc_51A3")


    ChrTalk(    #146
        0x13,
        (
            "#278F……我也要重新\x01",
            "彻底地锻炼一下才行。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_51D8")

    TalkEnd(0xFE)

    label("loc_51DB")

    Return()

    # Function_18_50E0 end

    def Function_19_51DC(): pass

    label("Function_19_51DC")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_D2(0x27023E, 0x270248, 0x13)
    OP_D2(0x270244, 0x27024E, 0x14)
    OP_D2(0x270022, 0x270025, 0x15)
    LoadEffect(0x0, "map\\mp252_04.eff")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_526E")
    SetChrPos(0xF1, 1660, 4000, 480, 180)
    SetChrPos(0xF0, -10, 4000, 730, 180)
    SetChrPos(0xEF, 1450, 4000, 2260, 180)
    SetChrPos(0xEE, -70, 4000, 2280, 180)
    Jump("loc_536A")

    label("loc_526E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_52C3")
    SetChrPos(0xF1, 1660, 4000, 480, 180)
    SetChrPos(0xF0, -10, 4000, 730, 180)
    SetChrPos(0xEE, 1450, 4000, 2260, 180)
    SetChrPos(0xEF, -70, 4000, 2280, 180)
    Jump("loc_536A")

    label("loc_52C3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5318")
    SetChrPos(0xF1, 1660, 4000, 480, 180)
    SetChrPos(0xEF, -10, 4000, 730, 180)
    SetChrPos(0xEE, 1450, 4000, 2260, 180)
    SetChrPos(0xF0, -70, 4000, 2280, 180)
    Jump("loc_536A")

    label("loc_5318")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_536A")
    SetChrPos(0xF0, 1660, 4000, 480, 180)
    SetChrPos(0xEF, -10, 4000, 730, 180)
    SetChrPos(0xEE, 1450, 4000, 2260, 180)
    SetChrPos(0xF1, -70, 4000, 2280, 180)

    label("loc_536A")

    OP_9F(0x0, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x1, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x3, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_6D(-1200, 4000, 3500, 0)
    OP_67(0, 6250, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(315000, 0)
    OP_6E(432, 0)

    def lambda_53D9():
        OP_6B(2100, 6000)
        ExitThread()

    QueueWorkItem(0x22, 0, lambda_53D9)
    FadeToBright(1000, 0)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5433")
    OP_22(0x162, 0x0, 0x64)
    OP_43(0xF1, 0x0, 0x5, 0x15)
    Sleep(500)
    OP_43(0xF0, 0x0, 0x5, 0x15)
    Sleep(500)
    OP_43(0xEF, 0x0, 0x5, 0x15)
    Sleep(4000)
    OP_22(0x162, 0x0, 0x64)
    OP_43(0xEE, 0x0, 0x5, 0x15)
    Jump("loc_5502")

    label("loc_5433")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5479")
    OP_22(0x162, 0x0, 0x64)
    OP_43(0xF1, 0x0, 0x5, 0x15)
    Sleep(500)
    OP_43(0xF0, 0x0, 0x5, 0x15)
    Sleep(500)
    OP_43(0xEE, 0x0, 0x5, 0x15)
    Sleep(4000)
    OP_22(0x162, 0x0, 0x64)
    OP_43(0xEF, 0x0, 0x5, 0x15)
    Jump("loc_5502")

    label("loc_5479")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_54BF")
    OP_22(0x162, 0x0, 0x64)
    OP_43(0xF1, 0x0, 0x5, 0x15)
    Sleep(500)
    OP_43(0xEF, 0x0, 0x5, 0x15)
    Sleep(500)
    OP_43(0xEE, 0x0, 0x5, 0x15)
    Sleep(4000)
    OP_22(0x162, 0x0, 0x64)
    OP_43(0xF0, 0x0, 0x5, 0x15)
    Jump("loc_5502")

    label("loc_54BF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5502")
    OP_22(0x162, 0x0, 0x64)
    OP_43(0xF0, 0x0, 0x5, 0x15)
    Sleep(500)
    OP_43(0xEF, 0x0, 0x5, 0x15)
    Sleep(500)
    OP_43(0xEE, 0x0, 0x5, 0x15)
    Sleep(2000)
    OP_22(0x162, 0x0, 0x64)
    OP_43(0xF1, 0x0, 0x5, 0x15)

    label("loc_5502")

    WaitChrThread(0xEE, 0x0)
    WaitChrThread(0xEF, 0x0)
    WaitChrThread(0xF0, 0x0)
    WaitChrThread(0xF1, 0x0)
    Sleep(1000)
    WaitChrThread(0x22, 0x0)

    ChrTalk(    #147
        0x22,
        "\x07\x0C#1610F#5P各位，辛苦你们了。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_62(0x110, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x1)
    Sleep(1300)

    ChrTalk(    #148
        0x110,
        "#268F#2P呼…………\x02",
    )

    CloseMessageWindow()
    OP_62(0x110, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5766")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_55CF")
    OP_62(0xEF, 0x0, 2300, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_5636")

    label("loc_55CF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_55F7")
    OP_62(0xEF, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_5636")

    label("loc_55F7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_561F")
    OP_62(0xEF, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_5636")

    label("loc_561F")

    OP_62(0xEF, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)

    label("loc_5636")

    Sleep(100)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5663")
    OP_62(0xF0, 0x0, 2300, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_56CA")

    label("loc_5663")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_568B")
    OP_62(0xF0, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_56CA")

    label("loc_568B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_56B3")
    OP_62(0xF0, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_56CA")

    label("loc_56B3")

    OP_62(0xF0, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)

    label("loc_56CA")

    Sleep(100)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_56F7")
    OP_62(0xF1, 0x0, 2300, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_575E")

    label("loc_56F7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_571F")
    OP_62(0xF1, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_575E")

    label("loc_571F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5747")
    OP_62(0xF1, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_575E")

    label("loc_5747")

    OP_62(0xF1, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)

    label("loc_575E")

    Sleep(1000)
    Jump("loc_5CCA")

    label("loc_5766")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5933")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_579C")
    OP_62(0xEE, 0x0, 2300, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_5803")

    label("loc_579C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_57C4")
    OP_62(0xEE, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_5803")

    label("loc_57C4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_57EC")
    OP_62(0xEE, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_5803")

    label("loc_57EC")

    OP_62(0xEE, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)

    label("loc_5803")

    Sleep(100)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5830")
    OP_62(0xF0, 0x0, 2300, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_5897")

    label("loc_5830")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5858")
    OP_62(0xF0, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_5897")

    label("loc_5858")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5880")
    OP_62(0xF0, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_5897")

    label("loc_5880")

    OP_62(0xF0, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)

    label("loc_5897")

    Sleep(100)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_58C4")
    OP_62(0xF1, 0x0, 2300, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_592B")

    label("loc_58C4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_58EC")
    OP_62(0xF1, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_592B")

    label("loc_58EC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5914")
    OP_62(0xF1, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_592B")

    label("loc_5914")

    OP_62(0xF1, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)

    label("loc_592B")

    Sleep(1000)
    Jump("loc_5CCA")

    label("loc_5933")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5B00")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5969")
    OP_62(0xEE, 0x0, 2300, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_59D0")

    label("loc_5969")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5991")
    OP_62(0xEE, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_59D0")

    label("loc_5991")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_59B9")
    OP_62(0xEE, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_59D0")

    label("loc_59B9")

    OP_62(0xEE, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)

    label("loc_59D0")

    Sleep(100)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_59FD")
    OP_62(0xEF, 0x0, 2300, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_5A64")

    label("loc_59FD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5A25")
    OP_62(0xEF, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_5A64")

    label("loc_5A25")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5A4D")
    OP_62(0xEF, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_5A64")

    label("loc_5A4D")

    OP_62(0xEF, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)

    label("loc_5A64")

    Sleep(100)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5A91")
    OP_62(0xF1, 0x0, 2300, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_5AF8")

    label("loc_5A91")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5AB9")
    OP_62(0xF1, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_5AF8")

    label("loc_5AB9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5AE1")
    OP_62(0xF1, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_5AF8")

    label("loc_5AE1")

    OP_62(0xF1, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)

    label("loc_5AF8")

    Sleep(1000)
    Jump("loc_5CCA")

    label("loc_5B00")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5CCA")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5B36")
    OP_62(0xEE, 0x0, 2300, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_5B9D")

    label("loc_5B36")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5B5E")
    OP_62(0xEE, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_5B9D")

    label("loc_5B5E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5B86")
    OP_62(0xEE, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_5B9D")

    label("loc_5B86")

    OP_62(0xEE, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)

    label("loc_5B9D")

    Sleep(100)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5BCA")
    OP_62(0xEF, 0x0, 2300, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_5C31")

    label("loc_5BCA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5BF2")
    OP_62(0xEF, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_5C31")

    label("loc_5BF2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5C1A")
    OP_62(0xEF, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_5C31")

    label("loc_5C1A")

    OP_62(0xEF, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)

    label("loc_5C31")

    Sleep(100)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5C5E")
    OP_62(0xF0, 0x0, 2300, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_5CC5")

    label("loc_5C5E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5C86")
    OP_62(0xF0, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_5CC5")

    label("loc_5C86")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5CAE")
    OP_62(0xF0, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_5CC5")

    label("loc_5CAE")

    OP_62(0xF0, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)

    label("loc_5CC5")

    Sleep(1000)

    label("loc_5CCA")


    def lambda_5CD0():
        OP_6D(-600, 4000, 2600, 1500)
        ExitThread()

    QueueWorkItem(0x22, 0, lambda_5CD0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5D20")

    def lambda_5CF6():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_5CF6)
    Sleep(100)

    def lambda_5D09():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0xF0, 1, lambda_5D09)
    Sleep(100)
    OP_8C(0xF1, 315, 400)
    Jump("loc_5DD7")

    label("loc_5D20")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5D5E")

    def lambda_5D34():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_5D34)
    Sleep(100)

    def lambda_5D47():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0xF0, 1, lambda_5D47)
    Sleep(100)
    OP_8C(0xF1, 315, 400)
    Jump("loc_5DD7")

    label("loc_5D5E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5D9C")

    def lambda_5D72():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_5D72)
    Sleep(100)

    def lambda_5D85():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_5D85)
    Sleep(100)
    OP_8C(0xF1, 315, 400)
    Jump("loc_5DD7")

    label("loc_5D9C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5DD7")

    def lambda_5DB0():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_5DB0)
    Sleep(100)

    def lambda_5DC3():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_5DC3)
    Sleep(100)
    OP_8C(0xF0, 315, 400)

    label("loc_5DD7")

    WaitChrThread(0x22, 0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5E58")

    ChrTalk(    #149
        0x109,
        (
            "#1064F咦……\x01",
            "玲，你累了吗？\x02\x03",

            "#1066F稍微休息一下怎么样。\x02\x03",

            "大家也正好\x01",
            "放松一下……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_63E9")

    label("loc_5E58")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5EC6")

    ChrTalk(    #150
        0x101,
        (
            "#1004F……玲，累了吗？\x02\x03",

            "#1015F唔，还是放松一下吧。\x01",
            "那里正好有个休息处……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_63E9")

    label("loc_5EC6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5F52")

    ChrTalk(    #151
        0x107,
        (
            "#064F那个……\x01",
            "玲，你累了吗？\x02\x03",

            "#062F还是休息一下比较好吧？\x02\x03",

            "累的时候\x01",
            "就要好好休息……\x02",
        )
    )

    Jump("loc_5F4E")

    label("loc_5F4E")

    CloseMessageWindow()
    Jump("loc_63E9")

    label("loc_5F52")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5FC2")

    ChrTalk(    #152
        0x102,
        (
            "#1504F玲……你累了吗？\x02\x03",

            "#1503F还是放松一下吧。\x01",
            "泉水的前面正好有个休息处……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_63E9")

    label("loc_5FC2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_608D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x584, 0)), scpexpr(EXPR_END)), "loc_6032")

    ChrTalk(    #153
        0x10F,
        (
            "#1938F……感到累的话\x01",
            "就该休息一下。\x02\x03",

            "#1937F总是勉强自己\x01",
            "可不太好哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_608A")

    label("loc_6032")


    ChrTalk(    #154
        0x10F,
        (
            "#1440F……感到累的话\x01",
            "就该休息一下。\x02\x03",

            "#1446F总是勉强自己\x01",
            "可不太好哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_608A")

    Jump("loc_63E9")

    label("loc_608D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_60FC")

    ChrTalk(    #155
        0x105,
        (
            "#1382F那个，累了的话\x01",
            "就请休息一会儿吧。\x02\x03",

            "#1165F我来泡茶，\x01",
            "请大家也一起……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_63E9")

    label("loc_60FC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6163")

    ChrTalk(    #156
        0x10A,
        (
            "#814F咦……\x01",
            "小玲，你累了吗？\x02\x03",

            "#819F呵呵，\x01",
            "让姐姐陪你休息一会儿吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_63E9")

    label("loc_6163")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_61C7")

    ChrTalk(    #157
        0x10B,
        (
            "#213F哎……你累了吗？\x02\x03",

            "#210F啊，那么……\x01",
            "在那边休息一下怎么样？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_63E9")

    label("loc_61C7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_622B")

    ChrTalk(    #158
        0x106,
        (
            "#052F……怎么，累了吗？\x02\x03",

            "#053F小孩还是别勉强了。\x01",
            "去那边休息吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_63E9")

    label("loc_622B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xB)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_62AA")

    ChrTalk(    #159
        0x10C,
        (
            "#115F……玲，\x01",
            "你可是重要的战斗成员啊。\x02\x03",

            "#110F要是感到劳累的话\x01",
            "还是别勉强自己，休息一下吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_63E9")

    label("loc_62AA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6318")

    ChrTalk(    #160
        0x103,
        (
            "#1523F咦，你累了吗？\x02\x03",

            "#1520F还是放松一下比较好吧。\x01",
            "那边正好有个休息处……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_63E9")

    label("loc_6318")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6382")

    ChrTalk(    #161
        0x10D,
        (
            "#272F……累了的话\x01",
            "就应该休息一下。\x02\x03",

            "否则在关键时刻\x01",
            "判断能力会下降的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_63E9")

    label("loc_6382")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_63E9")

    ChrTalk(    #162
        0x10E,
        (
            "#176F……累了吗………………\x02\x03",

            "#170F那里有个休息处。\x01",
            "放松一下比较好吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_63E9")

    OP_63(0x110)
    Sleep(150)
    OP_8C(0x110, 135, 400)

    ChrTalk(    #163
        0x110,
        (
            "#266F#5P……真是的，\x01",
            "玲才没有累呢。\x02\x03",

            "#267F只不过\x01",
            "有些在意的事罢了。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6489")

    ChrTalk(    #164
        0x101,
        "#1011F咦，在意的事是什么呢？\x02",
    )

    CloseMessageWindow()
    Jump("loc_673D")

    label("loc_6489")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_64F2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x584, 0)), scpexpr(EXPR_END)), "loc_64C8")

    ChrTalk(    #165
        0x10F,
        "#1930F………………………？\x02",
    )

    CloseMessageWindow()
    Jump("loc_64EF")

    label("loc_64C8")


    ChrTalk(    #166
        0x10F,
        "#1440F………………………？\x02",
    )

    CloseMessageWindow()

    label("loc_64EF")

    Jump("loc_673D")

    label("loc_64F2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6526")

    ChrTalk(    #167
        0x104,
        "#1543F哦……是什么呢？\x02",
    )

    CloseMessageWindow()
    Jump("loc_673D")

    label("loc_6526")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_655D")

    ChrTalk(    #168
        0x108,
        "#072F唔，在意什么呢……？\x02",
    )

    CloseMessageWindow()
    Jump("loc_673D")

    label("loc_655D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_65AA")

    ChrTalk(    #169
        0x109,
        (
            "#1064F我说，小玲？\x02\x03",

            "有什么在意的呢……？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_673D")

    label("loc_65AA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_65DB")

    ChrTalk(    #170
        0x10E,
        "#172F在意的事……？\x02",
    )

    CloseMessageWindow()
    Jump("loc_673D")

    label("loc_65DB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_660E")

    ChrTalk(    #171
        0x10D,
        "#270F唔………………？\x02",
    )

    CloseMessageWindow()
    Jump("loc_673D")

    label("loc_660E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6648")

    ChrTalk(    #172
        0x103,
        "#1522F哎，你在意什么呢……？\x02",
    )

    CloseMessageWindow()
    Jump("loc_673D")

    label("loc_6648")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6679")

    ChrTalk(    #173
        0x10B,
        "#213F哎……………？\x02",
    )

    CloseMessageWindow()
    Jump("loc_673D")

    label("loc_6679")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_66AA")

    ChrTalk(    #174
        0x10A,
        "#814F那是…………？\x02",
    )

    CloseMessageWindow()
    Jump("loc_673D")

    label("loc_66AA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_66DE")

    ChrTalk(    #175
        0x105,
        "#1164F咦………………？\x02",
    )

    CloseMessageWindow()
    Jump("loc_673D")

    label("loc_66DE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6711")

    ChrTalk(    #176
        0x106,
        "#555F嗯………………？\x02",
    )

    CloseMessageWindow()
    Jump("loc_673D")

    label("loc_6711")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_673D")

    ChrTalk(    #177
        0x107,
        "#564F咦，玲……？\x02",
    )

    CloseMessageWindow()

    label("loc_673D")

    OP_62(0x110, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x110)
    Sleep(150)

    ChrTalk(    #178
        0x110,
        (
            "#263F#5P对了………………\x02\x03",

            "#269F嘻嘻，\x01",
            "就让我稍微试一下吧。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)

    def lambda_67B5():
        OP_6D(-3580, 4000, 3190, 2000)
        ExitThread()

    QueueWorkItem(0xEE, 2, lambda_67B5)

    def lambda_67CD():
        OP_67(0, 6380, -10000, 2000)
        ExitThread()

    QueueWorkItem(0xEE, 3, lambda_67CD)

    def lambda_67E5():
        OP_6B(2270, 2000)
        ExitThread()

    QueueWorkItem(0xEF, 3, lambda_67E5)

    def lambda_67F5():
        OP_6C(326000, 2000)
        ExitThread()

    QueueWorkItem(0xF0, 3, lambda_67F5)

    def lambda_6805():
        OP_6E(419, 2000)
        ExitThread()

    QueueWorkItem(0xF1, 3, lambda_6805)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_686B")
    OP_43(0xEE, 0x0, 0x5, 0x14)

    def lambda_682A():

        label("loc_682A")

        TurnDirection(0xFE, 0x110, 400)
        OP_48()
        Jump("loc_682A")

    QueueWorkItem2(0x22, 0, lambda_682A)

    def lambda_683B():

        label("loc_683B")

        TurnDirection(0xFE, 0x110, 400)
        OP_48()
        Jump("loc_683B")

    QueueWorkItem2(0xEF, 0, lambda_683B)

    def lambda_684C():

        label("loc_684C")

        TurnDirection(0xFE, 0x110, 400)
        OP_48()
        Jump("loc_684C")

    QueueWorkItem2(0xF0, 0, lambda_684C)

    def lambda_685D():

        label("loc_685D")

        TurnDirection(0xFE, 0x110, 400)
        OP_48()
        Jump("loc_685D")

    QueueWorkItem2(0xF1, 0, lambda_685D)
    Jump("loc_697C")

    label("loc_686B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_68C7")
    OP_43(0xEF, 0x0, 0x5, 0x14)

    def lambda_6886():

        label("loc_6886")

        TurnDirection(0xFE, 0x110, 400)
        OP_48()
        Jump("loc_6886")

    QueueWorkItem2(0x22, 0, lambda_6886)

    def lambda_6897():

        label("loc_6897")

        TurnDirection(0xFE, 0x110, 400)
        OP_48()
        Jump("loc_6897")

    QueueWorkItem2(0xEE, 0, lambda_6897)

    def lambda_68A8():

        label("loc_68A8")

        TurnDirection(0xFE, 0x110, 400)
        OP_48()
        Jump("loc_68A8")

    QueueWorkItem2(0xF0, 0, lambda_68A8)

    def lambda_68B9():

        label("loc_68B9")

        TurnDirection(0xFE, 0x110, 400)
        OP_48()
        Jump("loc_68B9")

    QueueWorkItem2(0xF1, 0, lambda_68B9)
    Jump("loc_697C")

    label("loc_68C7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6923")
    OP_43(0xF0, 0x0, 0x5, 0x14)

    def lambda_68E2():

        label("loc_68E2")

        TurnDirection(0xFE, 0x110, 400)
        OP_48()
        Jump("loc_68E2")

    QueueWorkItem2(0x22, 0, lambda_68E2)

    def lambda_68F3():

        label("loc_68F3")

        TurnDirection(0xFE, 0x110, 400)
        OP_48()
        Jump("loc_68F3")

    QueueWorkItem2(0xEE, 0, lambda_68F3)

    def lambda_6904():

        label("loc_6904")

        TurnDirection(0xFE, 0x110, 400)
        OP_48()
        Jump("loc_6904")

    QueueWorkItem2(0xEF, 0, lambda_6904)

    def lambda_6915():

        label("loc_6915")

        TurnDirection(0xFE, 0x110, 400)
        OP_48()
        Jump("loc_6915")

    QueueWorkItem2(0xF1, 0, lambda_6915)
    Jump("loc_697C")

    label("loc_6923")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_697C")
    OP_43(0xF1, 0x0, 0x5, 0x14)

    def lambda_693E():

        label("loc_693E")

        TurnDirection(0xFE, 0x110, 400)
        OP_48()
        Jump("loc_693E")

    QueueWorkItem2(0x22, 0, lambda_693E)

    def lambda_694F():

        label("loc_694F")

        TurnDirection(0xFE, 0x110, 400)
        OP_48()
        Jump("loc_694F")

    QueueWorkItem2(0xEE, 0, lambda_694F)

    def lambda_6960():

        label("loc_6960")

        TurnDirection(0xFE, 0x110, 400)
        OP_48()
        Jump("loc_6960")

    QueueWorkItem2(0xEF, 0, lambda_6960)

    def lambda_6971():

        label("loc_6971")

        TurnDirection(0xFE, 0x110, 400)
        OP_48()
        Jump("loc_6971")

    QueueWorkItem2(0xF0, 0, lambda_6971)

    label("loc_697C")

    WaitChrThread(0xEE, 0x2)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6B6A")
    OP_62(0x22, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(100)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_69D3")
    OP_62(0xEF, 0x0, 2300, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_6A3A")

    label("loc_69D3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_69FB")
    OP_62(0xEF, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_6A3A")

    label("loc_69FB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6A23")
    OP_62(0xEF, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_6A3A")

    label("loc_6A23")

    OP_62(0xEF, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)

    label("loc_6A3A")

    Sleep(100)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6A67")
    OP_62(0xF0, 0x0, 2300, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_6ACE")

    label("loc_6A67")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6A8F")
    OP_62(0xF0, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_6ACE")

    label("loc_6A8F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6AB7")
    OP_62(0xF0, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_6ACE")

    label("loc_6AB7")

    OP_62(0xF0, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)

    label("loc_6ACE")

    Sleep(100)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6AFB")
    OP_62(0xF1, 0x0, 2300, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_6B62")

    label("loc_6AFB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6B23")
    OP_62(0xF1, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_6B62")

    label("loc_6B23")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6B4B")
    OP_62(0xF1, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_6B62")

    label("loc_6B4B")

    OP_62(0xF1, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)

    label("loc_6B62")

    Sleep(1000)
    Jump("loc_7122")

    label("loc_6B6A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6D53")
    OP_62(0x22, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(100)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6BBC")
    OP_62(0xEE, 0x0, 2300, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_6C23")

    label("loc_6BBC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6BE4")
    OP_62(0xEE, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_6C23")

    label("loc_6BE4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6C0C")
    OP_62(0xEE, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_6C23")

    label("loc_6C0C")

    OP_62(0xEE, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)

    label("loc_6C23")

    Sleep(100)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6C50")
    OP_62(0xF0, 0x0, 2300, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_6CB7")

    label("loc_6C50")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6C78")
    OP_62(0xF0, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_6CB7")

    label("loc_6C78")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6CA0")
    OP_62(0xF0, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_6CB7")

    label("loc_6CA0")

    OP_62(0xF0, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)

    label("loc_6CB7")

    Sleep(100)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6CE4")
    OP_62(0xF1, 0x0, 2300, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_6D4B")

    label("loc_6CE4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6D0C")
    OP_62(0xF1, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_6D4B")

    label("loc_6D0C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6D34")
    OP_62(0xF1, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_6D4B")

    label("loc_6D34")

    OP_62(0xF1, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)

    label("loc_6D4B")

    Sleep(1000)
    Jump("loc_7122")

    label("loc_6D53")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6F3C")
    OP_62(0x22, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(100)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6DA5")
    OP_62(0xEE, 0x0, 2300, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_6E0C")

    label("loc_6DA5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6DCD")
    OP_62(0xEE, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_6E0C")

    label("loc_6DCD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6DF5")
    OP_62(0xEE, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_6E0C")

    label("loc_6DF5")

    OP_62(0xEE, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)

    label("loc_6E0C")

    Sleep(100)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6E39")
    OP_62(0xEF, 0x0, 2300, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_6EA0")

    label("loc_6E39")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6E61")
    OP_62(0xEF, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_6EA0")

    label("loc_6E61")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6E89")
    OP_62(0xEF, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_6EA0")

    label("loc_6E89")

    OP_62(0xEF, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)

    label("loc_6EA0")

    Sleep(100)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6ECD")
    OP_62(0xF1, 0x0, 2300, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_6F34")

    label("loc_6ECD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6EF5")
    OP_62(0xF1, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_6F34")

    label("loc_6EF5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6F1D")
    OP_62(0xF1, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_6F34")

    label("loc_6F1D")

    OP_62(0xF1, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)

    label("loc_6F34")

    Sleep(1000)
    Jump("loc_7122")

    label("loc_6F3C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7122")
    OP_62(0x22, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(100)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6F8E")
    OP_62(0xEE, 0x0, 2300, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_6FF5")

    label("loc_6F8E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6FB6")
    OP_62(0xEE, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_6FF5")

    label("loc_6FB6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6FDE")
    OP_62(0xEE, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_6FF5")

    label("loc_6FDE")

    OP_62(0xEE, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)

    label("loc_6FF5")

    Sleep(100)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7022")
    OP_62(0xEF, 0x0, 2300, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_7089")

    label("loc_7022")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_704A")
    OP_62(0xEF, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_7089")

    label("loc_704A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7072")
    OP_62(0xEF, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_7089")

    label("loc_7072")

    OP_62(0xEF, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)

    label("loc_7089")

    Sleep(100)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_70B6")
    OP_62(0xF0, 0x0, 2300, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_711D")

    label("loc_70B6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_70DE")
    OP_62(0xF0, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_711D")

    label("loc_70DE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7106")
    OP_62(0xF0, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_711D")

    label("loc_7106")

    OP_62(0xF0, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)

    label("loc_711D")

    Sleep(1000)

    label("loc_7122")

    OP_44(0x22, 0x0)
    OP_44(0xEE, 0x0)
    OP_44(0xEF, 0x0)
    OP_44(0xF0, 0x0)
    OP_44(0xF1, 0x0)

    ChrTalk(    #179
        0x22,
        "\x07\x0C#1614F那是……………？\x07\x00\x02",
    )

    CloseMessageWindow()
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x110, 19)
    SetChrSubChip(0x110, 0)
    OP_0D()
    Sleep(500)
    Fade(500)
    OP_22(0xD8, 0x0, 0x64)
    SetChrChipByIndex(0x110, 20)
    SetChrSubChip(0x110, 1)

    def lambda_7191():
        OP_6D(-4000, 4000, 3300, 500)
        ExitThread()

    QueueWorkItem(0x22, 0, lambda_7191)

    def lambda_71A9():
        OP_6B(2100, 500)
        ExitThread()

    QueueWorkItem(0x22, 1, lambda_71A9)
    OP_0D()
    Sleep(500)

    ChrTalk(    #180
        0x110,
        "#263F#5P……帕蒂尔……玛蒂尔…………！\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    Call(5, 25)
    Return()

    # Function_19_51DC end

    def Function_20_71F6(): pass

    label("Function_20_71F6")

    OP_8C(0x110, 270, 400)
    OP_8E(0xFE, 0xFFFFF330, 0xFA0, 0x6EA, 0x7D0, 0x0)
    OP_8C(0xFE, 270, 400)
    Return()

    # Function_20_71F6 end

    def Function_21_7219(): pass

    label("Function_21_7219")

    PlayEffect(0x0, 0xFF, 0xFE, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1500)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
    Return()

    # Function_21_7219 end

    def Function_22_725F(): pass

    label("Function_22_725F")

    OP_DE(0x0, 0x3, 0x1)
    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_D2(0x27023E, 0x270248, 0x13)
    OP_D2(0x270244, 0x27024E, 0x14)
    OP_D2(0x270022, 0x270025, 0x15)
    LoadEffect(0x0, "map\\mp204_02.eff")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_72F5")
    SetChrPos(0xF1, -640, 11920, 40680, 180)
    SetChrPos(0xF0, 1290, 11920, 40570, 180)
    SetChrPos(0xEF, 370, 11920, 39610, 180)
    SetChrPos(0xEE, 220, 11920, 41870, 180)
    Jump("loc_73F1")

    label("loc_72F5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_734A")
    SetChrPos(0xF1, -640, 11920, 40680, 180)
    SetChrPos(0xF0, 1290, 11920, 40570, 180)
    SetChrPos(0xEE, 370, 11920, 39610, 180)
    SetChrPos(0xEF, 220, 11920, 41870, 180)
    Jump("loc_73F1")

    label("loc_734A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_739F")
    SetChrPos(0xF1, -640, 11920, 40680, 180)
    SetChrPos(0xEF, 1290, 11920, 40570, 180)
    SetChrPos(0xEE, 370, 11920, 39610, 180)
    SetChrPos(0xF0, 220, 11920, 41870, 180)
    Jump("loc_73F1")

    label("loc_739F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_73F1")
    SetChrPos(0xF0, -640, 11920, 40680, 180)
    SetChrPos(0xEF, 1290, 11920, 40570, 180)
    SetChrPos(0xEE, 370, 11920, 39610, 180)
    SetChrPos(0xF1, 220, 11920, 41870, 180)

    label("loc_73F1")

    OP_9F(0x0, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x1, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x3, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_6D(-500, 11920, 41690, 0)
    OP_67(0, 7590, -10000, 0)
    OP_6B(2300, 0)
    OP_6C(315000, 0)
    OP_6E(419, 0)

    def lambda_7460():
        OP_6B(1880, 6000)
        ExitThread()

    QueueWorkItem(0x22, 0, lambda_7460)
    FadeToBright(1000, 0)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_75CE")
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    PlayEffect(0x0, 0xFF, 0xFF, 370, 11920, 39610, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)

    def lambda_74C7():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_74C7)
    Sleep(500)
    PlayEffect(0x0, 0xFF, 0xFF, 1290, 11920, 40570, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)

    def lambda_7513():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0xF0, 1, lambda_7513)
    Sleep(500)
    PlayEffect(0x0, 0xFF, 0xFF, -640, 11920, 40680, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)

    def lambda_755F():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0xF1, 1, lambda_755F)
    Sleep(1500)
    PlayEffect(0x0, 0xFF, 0xFF, 220, 11920, 41870, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)

    def lambda_75B5():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_75B5)
    WaitChrThread(0xEE, 0x1)
    Sleep(1000)
    Jump("loc_79D9")

    label("loc_75CE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7728")
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    PlayEffect(0x0, 0xFF, 0xFF, 370, 11920, 39610, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)

    def lambda_7621():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_7621)
    Sleep(500)
    PlayEffect(0x0, 0xFF, 0xFF, 1290, 11920, 40570, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)

    def lambda_766D():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0xF0, 1, lambda_766D)
    Sleep(500)
    PlayEffect(0x0, 0xFF, 0xFF, -640, 11920, 40680, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)

    def lambda_76B9():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0xF1, 1, lambda_76B9)
    Sleep(1500)
    PlayEffect(0x0, 0xFF, 0xFF, 220, 11920, 41870, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)

    def lambda_770F():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_770F)
    WaitChrThread(0xEF, 0x1)
    Sleep(1000)
    Jump("loc_79D9")

    label("loc_7728")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7882")
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    PlayEffect(0x0, 0xFF, 0xFF, 370, 11920, 39610, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)

    def lambda_777B():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_777B)
    Sleep(500)
    PlayEffect(0x0, 0xFF, 0xFF, 1290, 11920, 40570, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)

    def lambda_77C7():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_77C7)
    Sleep(500)
    PlayEffect(0x0, 0xFF, 0xFF, -640, 11920, 40680, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)

    def lambda_7813():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0xF1, 1, lambda_7813)
    Sleep(1500)
    PlayEffect(0x0, 0xFF, 0xFF, 220, 11920, 41870, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)

    def lambda_7869():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0xF0, 1, lambda_7869)
    WaitChrThread(0xF0, 0x1)
    Sleep(1000)
    Jump("loc_79D9")

    label("loc_7882")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_79D9")
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    PlayEffect(0x0, 0xFF, 0xFF, 370, 11920, 39610, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)

    def lambda_78D5():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_78D5)
    Sleep(500)
    PlayEffect(0x0, 0xFF, 0xFF, 1290, 11920, 40570, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)

    def lambda_7921():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_7921)
    Sleep(500)
    PlayEffect(0x0, 0xFF, 0xFF, -640, 11920, 40680, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)

    def lambda_796D():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0xF0, 1, lambda_796D)
    Sleep(1500)
    PlayEffect(0x0, 0xFF, 0xFF, 220, 11920, 41870, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)

    def lambda_79C3():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0xF1, 1, lambda_79C3)
    WaitChrThread(0xF1, 0x1)
    Sleep(1000)

    label("loc_79D9")

    OP_62(0x110, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x1)
    Sleep(1300)

    ChrTalk(    #181
        0x110,
        "#268F#2P呼…………\x02",
    )

    CloseMessageWindow()
    OP_62(0x110, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    WaitChrThread(0xEE, 0x0)
    WaitChrThread(0xEF, 0x0)
    WaitChrThread(0xF0, 0x0)
    WaitChrThread(0xF1, 0x0)
    WaitChrThread(0x22, 0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7C0C")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7A75")
    OP_62(0xEF, 0x0, 2300, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_7ADC")

    label("loc_7A75")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7A9D")
    OP_62(0xEF, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_7ADC")

    label("loc_7A9D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7AC5")
    OP_62(0xEF, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_7ADC")

    label("loc_7AC5")

    OP_62(0xEF, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)

    label("loc_7ADC")

    Sleep(100)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7B09")
    OP_62(0xF0, 0x0, 2300, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_7B70")

    label("loc_7B09")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7B31")
    OP_62(0xF0, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_7B70")

    label("loc_7B31")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7B59")
    OP_62(0xF0, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_7B70")

    label("loc_7B59")

    OP_62(0xF0, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)

    label("loc_7B70")

    Sleep(100)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7B9D")
    OP_62(0xF1, 0x0, 2300, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_7C04")

    label("loc_7B9D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7BC5")
    OP_62(0xF1, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_7C04")

    label("loc_7BC5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7BED")
    OP_62(0xF1, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_7C04")

    label("loc_7BED")

    OP_62(0xF1, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)

    label("loc_7C04")

    Sleep(1000)
    Jump("loc_8170")

    label("loc_7C0C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7DD9")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7C42")
    OP_62(0xEE, 0x0, 2300, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_7CA9")

    label("loc_7C42")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7C6A")
    OP_62(0xEE, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_7CA9")

    label("loc_7C6A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7C92")
    OP_62(0xEE, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_7CA9")

    label("loc_7C92")

    OP_62(0xEE, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)

    label("loc_7CA9")

    Sleep(100)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7CD6")
    OP_62(0xF0, 0x0, 2300, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_7D3D")

    label("loc_7CD6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7CFE")
    OP_62(0xF0, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_7D3D")

    label("loc_7CFE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7D26")
    OP_62(0xF0, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_7D3D")

    label("loc_7D26")

    OP_62(0xF0, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)

    label("loc_7D3D")

    Sleep(100)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7D6A")
    OP_62(0xF1, 0x0, 2300, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_7DD1")

    label("loc_7D6A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7D92")
    OP_62(0xF1, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_7DD1")

    label("loc_7D92")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7DBA")
    OP_62(0xF1, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_7DD1")

    label("loc_7DBA")

    OP_62(0xF1, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)

    label("loc_7DD1")

    Sleep(1000)
    Jump("loc_8170")

    label("loc_7DD9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7FA6")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7E0F")
    OP_62(0xEE, 0x0, 2300, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_7E76")

    label("loc_7E0F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7E37")
    OP_62(0xEE, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_7E76")

    label("loc_7E37")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7E5F")
    OP_62(0xEE, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_7E76")

    label("loc_7E5F")

    OP_62(0xEE, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)

    label("loc_7E76")

    Sleep(100)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7EA3")
    OP_62(0xEF, 0x0, 2300, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_7F0A")

    label("loc_7EA3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7ECB")
    OP_62(0xEF, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_7F0A")

    label("loc_7ECB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7EF3")
    OP_62(0xEF, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_7F0A")

    label("loc_7EF3")

    OP_62(0xEF, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)

    label("loc_7F0A")

    Sleep(100)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7F37")
    OP_62(0xF1, 0x0, 2300, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_7F9E")

    label("loc_7F37")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7F5F")
    OP_62(0xF1, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_7F9E")

    label("loc_7F5F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7F87")
    OP_62(0xF1, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_7F9E")

    label("loc_7F87")

    OP_62(0xF1, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)

    label("loc_7F9E")

    Sleep(1000)
    Jump("loc_8170")

    label("loc_7FA6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8170")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7FDC")
    OP_62(0xEE, 0x0, 2300, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_8043")

    label("loc_7FDC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8004")
    OP_62(0xEE, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_8043")

    label("loc_8004")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_802C")
    OP_62(0xEE, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_8043")

    label("loc_802C")

    OP_62(0xEE, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)

    label("loc_8043")

    Sleep(100)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8070")
    OP_62(0xEF, 0x0, 2300, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_80D7")

    label("loc_8070")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8098")
    OP_62(0xEF, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_80D7")

    label("loc_8098")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_80C0")
    OP_62(0xEF, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_80D7")

    label("loc_80C0")

    OP_62(0xEF, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)

    label("loc_80D7")

    Sleep(100)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8104")
    OP_62(0xF0, 0x0, 2300, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_816B")

    label("loc_8104")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_812C")
    OP_62(0xF0, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_816B")

    label("loc_812C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8154")
    OP_62(0xF0, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_816B")

    label("loc_8154")

    OP_62(0xF0, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)

    label("loc_816B")

    Sleep(1000)

    label("loc_8170")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_81AE")

    def lambda_8184():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_8184)
    Sleep(100)

    def lambda_8197():
        OP_8C(0xFE, 315, 400)
        ExitThread()

    QueueWorkItem(0xF0, 1, lambda_8197)
    Sleep(100)
    OP_8C(0xF1, 0, 0)
    Jump("loc_8265")

    label("loc_81AE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_81EC")

    def lambda_81C2():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_81C2)
    Sleep(100)

    def lambda_81D5():
        OP_8C(0xFE, 315, 400)
        ExitThread()

    QueueWorkItem(0xF0, 1, lambda_81D5)
    Sleep(100)
    OP_8C(0xF1, 0, 400)
    Jump("loc_8265")

    label("loc_81EC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_822A")

    def lambda_8200():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_8200)
    Sleep(100)

    def lambda_8213():
        OP_8C(0xFE, 315, 400)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_8213)
    Sleep(100)
    OP_8C(0xF1, 0, 400)
    Jump("loc_8265")

    label("loc_822A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8265")

    def lambda_823E():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_823E)
    Sleep(100)

    def lambda_8251():
        OP_8C(0xFE, 315, 400)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_8251)
    Sleep(100)
    OP_8C(0xF0, 0, 400)

    label("loc_8265")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_82E1")

    ChrTalk(    #182
        0x109,
        (
            "#1064F咦……\x01",
            "玲，你累了吗？\x02\x03",

            "#1066F稍微休息一下怎么样。\x02\x03",

            "大家也正好\x01",
            "放松一下……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8872")

    label("loc_82E1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_834F")

    ChrTalk(    #183
        0x101,
        (
            "#1004F……玲，累了吗？\x02\x03",

            "#1015F唔，还是放松一下吧。\x01",
            "那里正好有个休息处……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8872")

    label("loc_834F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_83DB")

    ChrTalk(    #184
        0x107,
        (
            "#064F那个……\x01",
            "玲，你累了吗？\x02\x03",

            "#062F还是休息一下比较好吧？\x02\x03",

            "累的时候\x01",
            "就要好好休息……\x02",
        )
    )

    Jump("loc_83D7")

    label("loc_83D7")

    CloseMessageWindow()
    Jump("loc_8872")

    label("loc_83DB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_844B")

    ChrTalk(    #185
        0x102,
        (
            "#1504F玲……你累了吗？\x02\x03",

            "#1503F还是放松一下吧。\x01",
            "泉水的前面正好有个休息处……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8872")

    label("loc_844B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8516")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x584, 0)), scpexpr(EXPR_END)), "loc_84BB")

    ChrTalk(    #186
        0x10F,
        (
            "#1938F……感到累的话\x01",
            "就该休息一下。\x02\x03",

            "#1937F总是勉强自己\x01",
            "可不太好哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8513")

    label("loc_84BB")


    ChrTalk(    #187
        0x10F,
        (
            "#1440F……感到累的话\x01",
            "就该休息一下。\x02\x03",

            "#1446F总是勉强自己\x01",
            "可不太好哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8513")

    Jump("loc_8872")

    label("loc_8516")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8585")

    ChrTalk(    #188
        0x105,
        (
            "#1382F那个，累了的话\x01",
            "就请休息一会儿吧。\x02\x03",

            "#1165F我来泡茶，\x01",
            "请大家也一起……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8872")

    label("loc_8585")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_85EC")

    ChrTalk(    #189
        0x10A,
        (
            "#814F咦……\x01",
            "小玲，你累了吗？\x02\x03",

            "#819F呵呵，\x01",
            "让姐姐陪你休息一会儿吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8872")

    label("loc_85EC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8650")

    ChrTalk(    #190
        0x10B,
        (
            "#213F哎……你累了吗？\x02\x03",

            "#210F啊，那么……\x01",
            "在那边休息一下怎么样？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8872")

    label("loc_8650")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_86B4")

    ChrTalk(    #191
        0x106,
        (
            "#052F……怎么，累了吗？\x02\x03",

            "#053F小孩还是别勉强了。\x01",
            "去那边休息吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8872")

    label("loc_86B4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xB)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8733")

    ChrTalk(    #192
        0x10C,
        (
            "#115F……玲，\x01",
            "你可是重要的战斗成员啊。\x02\x03",

            "#110F要是感到劳累的话\x01",
            "还是别勉强自己，休息一下吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8872")

    label("loc_8733")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_87A1")

    ChrTalk(    #193
        0x103,
        (
            "#1523F咦，你累了吗？\x02\x03",

            "#1520F还是放松一下比较好吧。\x01",
            "那边正好有个休息处……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8872")

    label("loc_87A1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_880B")

    ChrTalk(    #194
        0x10D,
        (
            "#272F……累了的话\x01",
            "就应该休息一下。\x02\x03",

            "否则在关键时刻\x01",
            "判断能力会下降的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8872")

    label("loc_880B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8872")

    ChrTalk(    #195
        0x10E,
        (
            "#176F……累了吗………………\x02\x03",

            "#170F那里有个休息处。\x01",
            "放松一下比较好吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8872")

    OP_63(0x110)
    Sleep(300)

    ChrTalk(    #196
        0x110,
        (
            "#266F#11P……真是的，\x01",
            "玲才没有累呢。\x02\x03",

            "#267F只不过\x01",
            "有些在意的事罢了。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_890C")

    ChrTalk(    #197
        0x101,
        "#1011F咦，在意的事是什么呢？\x02",
    )

    CloseMessageWindow()
    Jump("loc_8BC0")

    label("loc_890C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8975")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x584, 0)), scpexpr(EXPR_END)), "loc_894B")

    ChrTalk(    #198
        0x10F,
        "#1930F………………………？\x02",
    )

    CloseMessageWindow()
    Jump("loc_8972")

    label("loc_894B")


    ChrTalk(    #199
        0x10F,
        "#1440F………………………？\x02",
    )

    CloseMessageWindow()

    label("loc_8972")

    Jump("loc_8BC0")

    label("loc_8975")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_89A9")

    ChrTalk(    #200
        0x104,
        "#1543F哦……是什么呢？\x02",
    )

    CloseMessageWindow()
    Jump("loc_8BC0")

    label("loc_89A9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_89E0")

    ChrTalk(    #201
        0x108,
        "#072F唔，在意什么呢……？\x02",
    )

    CloseMessageWindow()
    Jump("loc_8BC0")

    label("loc_89E0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8A2D")

    ChrTalk(    #202
        0x109,
        (
            "#1064F我说，小玲？\x02\x03",

            "有什么在意的呢……？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8BC0")

    label("loc_8A2D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8A5E")

    ChrTalk(    #203
        0x10E,
        "#172F在意的事……？\x02",
    )

    CloseMessageWindow()
    Jump("loc_8BC0")

    label("loc_8A5E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8A91")

    ChrTalk(    #204
        0x10D,
        "#270F唔………………？\x02",
    )

    CloseMessageWindow()
    Jump("loc_8BC0")

    label("loc_8A91")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8ACB")

    ChrTalk(    #205
        0x103,
        "#1522F哎，你在意什么呢……？\x02",
    )

    CloseMessageWindow()
    Jump("loc_8BC0")

    label("loc_8ACB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8AFC")

    ChrTalk(    #206
        0x10B,
        "#213F哎……………？\x02",
    )

    CloseMessageWindow()
    Jump("loc_8BC0")

    label("loc_8AFC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8B2D")

    ChrTalk(    #207
        0x10A,
        "#814F那是…………？\x02",
    )

    CloseMessageWindow()
    Jump("loc_8BC0")

    label("loc_8B2D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8B61")

    ChrTalk(    #208
        0x105,
        "#1164F咦………………？\x02",
    )

    CloseMessageWindow()
    Jump("loc_8BC0")

    label("loc_8B61")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8B94")

    ChrTalk(    #209
        0x106,
        "#555F嗯………………？\x02",
    )

    CloseMessageWindow()
    Jump("loc_8BC0")

    label("loc_8B94")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8BC0")

    ChrTalk(    #210
        0x107,
        "#564F咦，玲……？\x02",
    )

    CloseMessageWindow()

    label("loc_8BC0")

    OP_62(0x110, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x110)
    Sleep(150)

    ChrTalk(    #211
        0x110,
        (
            "#263F#11P对了………………\x02\x03",

            "#269F嘻嘻，\x01",
            "就让我稍微试一下吧。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8DFB")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8C64")
    OP_62(0xEF, 0x0, 2300, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_8CCB")

    label("loc_8C64")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8C8C")
    OP_62(0xEF, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_8CCB")

    label("loc_8C8C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8CB4")
    OP_62(0xEF, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_8CCB")

    label("loc_8CB4")

    OP_62(0xEF, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)

    label("loc_8CCB")

    Sleep(100)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8CF8")
    OP_62(0xF0, 0x0, 2300, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_8D5F")

    label("loc_8CF8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8D20")
    OP_62(0xF0, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_8D5F")

    label("loc_8D20")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8D48")
    OP_62(0xF0, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_8D5F")

    label("loc_8D48")

    OP_62(0xF0, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)

    label("loc_8D5F")

    Sleep(100)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8D8C")
    OP_62(0xF1, 0x0, 2300, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_8DF3")

    label("loc_8D8C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8DB4")
    OP_62(0xF1, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_8DF3")

    label("loc_8DB4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8DDC")
    OP_62(0xF1, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_8DF3")

    label("loc_8DDC")

    OP_62(0xF1, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)

    label("loc_8DF3")

    Sleep(1000)
    Jump("loc_935F")

    label("loc_8DFB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8FC8")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8E31")
    OP_62(0xEE, 0x0, 2300, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_8E98")

    label("loc_8E31")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8E59")
    OP_62(0xEE, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_8E98")

    label("loc_8E59")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8E81")
    OP_62(0xEE, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_8E98")

    label("loc_8E81")

    OP_62(0xEE, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)

    label("loc_8E98")

    Sleep(100)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8EC5")
    OP_62(0xF0, 0x0, 2300, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_8F2C")

    label("loc_8EC5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8EED")
    OP_62(0xF0, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_8F2C")

    label("loc_8EED")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8F15")
    OP_62(0xF0, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_8F2C")

    label("loc_8F15")

    OP_62(0xF0, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)

    label("loc_8F2C")

    Sleep(100)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8F59")
    OP_62(0xF1, 0x0, 2300, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_8FC0")

    label("loc_8F59")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8F81")
    OP_62(0xF1, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_8FC0")

    label("loc_8F81")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8FA9")
    OP_62(0xF1, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_8FC0")

    label("loc_8FA9")

    OP_62(0xF1, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)

    label("loc_8FC0")

    Sleep(1000)
    Jump("loc_935F")

    label("loc_8FC8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9195")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8FFE")
    OP_62(0xEE, 0x0, 2300, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_9065")

    label("loc_8FFE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9026")
    OP_62(0xEE, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_9065")

    label("loc_9026")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_904E")
    OP_62(0xEE, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_9065")

    label("loc_904E")

    OP_62(0xEE, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)

    label("loc_9065")

    Sleep(100)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9092")
    OP_62(0xEF, 0x0, 2300, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_90F9")

    label("loc_9092")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_90BA")
    OP_62(0xEF, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_90F9")

    label("loc_90BA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_90E2")
    OP_62(0xEF, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_90F9")

    label("loc_90E2")

    OP_62(0xEF, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)

    label("loc_90F9")

    Sleep(100)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9126")
    OP_62(0xF1, 0x0, 2300, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_918D")

    label("loc_9126")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_914E")
    OP_62(0xF1, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_918D")

    label("loc_914E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9176")
    OP_62(0xF1, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_918D")

    label("loc_9176")

    OP_62(0xF1, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)

    label("loc_918D")

    Sleep(1000)
    Jump("loc_935F")

    label("loc_9195")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_935F")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_91CB")
    OP_62(0xEE, 0x0, 2300, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_9232")

    label("loc_91CB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_91F3")
    OP_62(0xEE, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_9232")

    label("loc_91F3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_921B")
    OP_62(0xEE, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_9232")

    label("loc_921B")

    OP_62(0xEE, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)

    label("loc_9232")

    Sleep(100)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_925F")
    OP_62(0xEF, 0x0, 2300, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_92C6")

    label("loc_925F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9287")
    OP_62(0xEF, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_92C6")

    label("loc_9287")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_92AF")
    OP_62(0xEF, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_92C6")

    label("loc_92AF")

    OP_62(0xEF, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)

    label("loc_92C6")

    Sleep(100)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_92F3")
    OP_62(0xF0, 0x0, 2300, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_935A")

    label("loc_92F3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_931B")
    OP_62(0xF0, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_935A")

    label("loc_931B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9343")
    OP_62(0xF0, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_935A")

    label("loc_9343")

    OP_62(0xF0, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)

    label("loc_935A")

    Sleep(1000)

    label("loc_935F")


    ChrTalk(    #212
        0x110,
        (
            "#1305F#11P嘻嘻，来这边。\x02\x03",

            "这里实在太狭小了。\x02",
        )
    )

    CloseMessageWindow()
    OP_43(0x110, 0x0, 0x5, 0x18)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_93EA")

    def lambda_93BA():

        label("loc_93BA")

        TurnDirection(0xFE, 0x110, 400)
        OP_48()
        Jump("loc_93BA")

    QueueWorkItem2(0xEF, 0, lambda_93BA)

    def lambda_93CB():

        label("loc_93CB")

        TurnDirection(0xFE, 0x110, 400)
        OP_48()
        Jump("loc_93CB")

    QueueWorkItem2(0xF0, 0, lambda_93CB)

    def lambda_93DC():

        label("loc_93DC")

        TurnDirection(0xFE, 0x110, 400)
        OP_48()
        Jump("loc_93DC")

    QueueWorkItem2(0xF1, 0, lambda_93DC)
    Jump("loc_94B3")

    label("loc_93EA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_942E")

    def lambda_93FE():

        label("loc_93FE")

        TurnDirection(0xFE, 0x110, 400)
        OP_48()
        Jump("loc_93FE")

    QueueWorkItem2(0xEE, 0, lambda_93FE)

    def lambda_940F():

        label("loc_940F")

        TurnDirection(0xFE, 0x110, 400)
        OP_48()
        Jump("loc_940F")

    QueueWorkItem2(0xF0, 0, lambda_940F)

    def lambda_9420():

        label("loc_9420")

        TurnDirection(0xFE, 0x110, 400)
        OP_48()
        Jump("loc_9420")

    QueueWorkItem2(0xF1, 0, lambda_9420)
    Jump("loc_94B3")

    label("loc_942E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9472")

    def lambda_9442():

        label("loc_9442")

        TurnDirection(0xFE, 0x110, 400)
        OP_48()
        Jump("loc_9442")

    QueueWorkItem2(0xEE, 0, lambda_9442)

    def lambda_9453():

        label("loc_9453")

        TurnDirection(0xFE, 0x110, 400)
        OP_48()
        Jump("loc_9453")

    QueueWorkItem2(0xEF, 0, lambda_9453)

    def lambda_9464():

        label("loc_9464")

        TurnDirection(0xFE, 0x110, 400)
        OP_48()
        Jump("loc_9464")

    QueueWorkItem2(0xF1, 0, lambda_9464)
    Jump("loc_94B3")

    label("loc_9472")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_94B3")

    def lambda_9486():

        label("loc_9486")

        TurnDirection(0xFE, 0x110, 400)
        OP_48()
        Jump("loc_9486")

    QueueWorkItem2(0xEE, 0, lambda_9486)

    def lambda_9497():

        label("loc_9497")

        TurnDirection(0xFE, 0x110, 400)
        OP_48()
        Jump("loc_9497")

    QueueWorkItem2(0xEF, 0, lambda_9497)

    def lambda_94A8():

        label("loc_94A8")

        TurnDirection(0xFE, 0x110, 400)
        OP_48()
        Jump("loc_94A8")

    QueueWorkItem2(0xF0, 0, lambda_94A8)

    label("loc_94B3")

    Sleep(2500)

    def lambda_94BE():
        OP_6D(-500, 11000, 36690, 6000)
        ExitThread()

    QueueWorkItem(0x22, 0, lambda_94BE)
    Sleep(1000)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9505")
    OP_43(0xEF, 0x0, 0x5, 0x17)
    Sleep(300)
    OP_43(0xF0, 0x0, 0x5, 0x17)
    Sleep(300)
    OP_43(0xF1, 0x0, 0x5, 0x17)
    Jump("loc_9592")

    label("loc_9505")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9535")
    OP_43(0xEE, 0x0, 0x5, 0x17)
    Sleep(300)
    OP_43(0xF0, 0x0, 0x5, 0x17)
    Sleep(300)
    OP_43(0xF1, 0x0, 0x5, 0x17)
    Jump("loc_9592")

    label("loc_9535")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9565")
    OP_43(0xEE, 0x0, 0x5, 0x17)
    Sleep(300)
    OP_43(0xEF, 0x0, 0x5, 0x17)
    Sleep(300)
    OP_43(0xF1, 0x0, 0x5, 0x17)
    Jump("loc_9592")

    label("loc_9565")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9592")
    OP_43(0xEE, 0x0, 0x5, 0x17)
    Sleep(300)
    OP_43(0xEF, 0x0, 0x5, 0x17)
    Sleep(300)
    OP_43(0xF0, 0x0, 0x5, 0x17)

    label("loc_9592")

    Sleep(2000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_44(0x22, 0x0)
    OP_44(0xEE, 0x0)
    OP_44(0xEF, 0x0)
    OP_44(0xF0, 0x0)
    OP_44(0xF1, 0x0)
    SetChrChipByIndex(0x0, 65535)
    SetChrChipByIndex(0x1, 65535)
    SetChrChipByIndex(0x2, 65535)
    SetChrChipByIndex(0x3, 65535)
    SetChrSubChip(0x0, 0)
    SetChrSubChip(0x1, 0)
    SetChrSubChip(0x2, 0)
    SetChrSubChip(0x3, 0)
    Sleep(2000)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9638")
    SetChrPos(0xF1, 1660, 4000, 480, 270)
    SetChrPos(0xF0, -10, 4000, 730, 270)
    SetChrPos(0xEF, 1450, 4000, 2260, 270)
    SetChrPos(0xEE, -3280, 4000, 1770, 270)
    Jump("loc_9734")

    label("loc_9638")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_968D")
    SetChrPos(0xF1, 1660, 4000, 480, 270)
    SetChrPos(0xF0, -10, 4000, 730, 270)
    SetChrPos(0xEE, 1450, 4000, 2260, 270)
    SetChrPos(0xEF, -3280, 4000, 1770, 270)
    Jump("loc_9734")

    label("loc_968D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_96E2")
    SetChrPos(0xF1, 1660, 4000, 480, 270)
    SetChrPos(0xEF, -10, 4000, 730, 270)
    SetChrPos(0xEE, 1450, 4000, 2260, 270)
    SetChrPos(0xF0, -3280, 4000, 1770, 270)
    Jump("loc_9734")

    label("loc_96E2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9734")
    SetChrPos(0xF0, 1660, 4000, 480, 270)
    SetChrPos(0xEF, -10, 4000, 730, 270)
    SetChrPos(0xEE, 1450, 4000, 2260, 270)
    SetChrPos(0xF1, -3280, 4000, 1770, 270)

    label("loc_9734")

    OP_8C(0x22, 180, 0)
    OP_6D(-3580, 4000, 3190, 0)
    OP_67(0, 6380, -10000, 0)
    OP_6B(2270, 0)
    OP_6C(326000, 0)
    OP_6E(419, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x110, 19)
    SetChrSubChip(0x110, 0)
    OP_0D()
    Sleep(500)
    Fade(500)
    OP_22(0xD8, 0x0, 0x64)
    SetChrChipByIndex(0x110, 20)
    SetChrSubChip(0x110, 1)

    def lambda_97B6():
        OP_6D(-4000, 4000, 3300, 500)
        ExitThread()

    QueueWorkItem(0x22, 0, lambda_97B6)

    def lambda_97CE():
        OP_6B(2100, 500)
        ExitThread()

    QueueWorkItem(0x22, 1, lambda_97CE)
    OP_0D()
    Sleep(500)

    ChrTalk(    #213
        0x110,
        "#263F#5P……帕蒂尔……玛蒂尔…………！\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    Call(5, 25)
    Return()

    # Function_22_725F end

    def Function_23_981B(): pass

    label("Function_23_981B")

    OP_8C(0xFE, 180, 0)
    OP_91(0xFE, 0x0, 0x0, 0xFFFFD8F0, 0x7D0, 0x0)
    Return()

    # Function_23_981B end

    def Function_24_9837(): pass

    label("Function_24_9837")

    OP_8C(0xFE, 90, 400)
    OP_8E(0xFE, 0x9F6, 0x2E90, 0xA12C, 0xBB8, 0x0)
    OP_8E(0xFE, 0x8E8, 0x2E90, 0x966E, 0xBB8, 0x0)
    OP_8E(0xFE, 0x122, 0x2E90, 0x8CC8, 0xBB8, 0x0)
    OP_8E(0xFE, 0x1E0, 0xFA0, 0x4196, 0xBB8, 0x0)
    Return()

    # Function_24_9837 end

    def Function_25_988F(): pass

    label("Function_25_988F")

    EventBegin(0x0)
    SetChrSubChip(0x110, 1)

    def lambda_989C():

        label("loc_989C")

        OP_7C(0xA, 0xA, 0xBB8, 0x64)
        OP_48()
        Jump("loc_989C")

    QueueWorkItem2(0x10, 3, lambda_989C)
    OP_22(0x113, 0x1, 0x46)
    Sleep(1000)

    def lambda_98C1():

        label("loc_98C1")

        OP_7C(0x1E, 0x1E, 0xBB8, 0x64)
        OP_48()
        Jump("loc_98C1")

    QueueWorkItem2(0x10, 3, lambda_98C1)
    OP_22(0x113, 0x1, 0x50)
    Sleep(1000)

    def lambda_98E6():

        label("loc_98E6")

        OP_7C(0x32, 0x32, 0xBB8, 0x64)
        OP_48()
        Jump("loc_98E6")

    QueueWorkItem2(0x10, 3, lambda_98E6)
    OP_22(0x113, 0x1, 0x5A)
    Sleep(1000)

    def lambda_990B():

        label("loc_990B")

        OP_7C(0x50, 0x50, 0xBB8, 0x64)
        OP_48()
        Jump("loc_990B")

    QueueWorkItem2(0x10, 3, lambda_990B)
    OP_22(0x113, 0x1, 0x64)
    Sleep(1000)
    Fade(1000)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_6D(-6890, 12700, 3150, 0)
    OP_67(0, 9030, -10000, 0)
    OP_6B(2210, 0)
    OP_6C(335000, 0)
    OP_6E(567, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_99CA")
    SetChrPos(0xF1, 990, 4000, -870, 315)
    SetChrPos(0xF0, -970, 4000, -580, 315)
    SetChrPos(0xEF, 890, 4000, 750, 315)
    SetChrPos(0xEE, -4400, 4000, 2420, 315)
    Jump("loc_9AC6")

    label("loc_99CA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9A1F")
    SetChrPos(0xF1, 990, 4000, -870, 315)
    SetChrPos(0xF0, -970, 4000, -580, 315)
    SetChrPos(0xEE, 890, 4000, 750, 315)
    SetChrPos(0xEF, -4400, 4000, 2420, 315)
    Jump("loc_9AC6")

    label("loc_9A1F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9A74")
    SetChrPos(0xF1, 990, 4000, -870, 315)
    SetChrPos(0xEF, -970, 4000, -580, 315)
    SetChrPos(0xEE, 890, 4000, 750, 315)
    SetChrPos(0xF0, -4400, 4000, 2420, 315)
    Jump("loc_9AC6")

    label("loc_9A74")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9AC6")
    SetChrPos(0xF0, 990, 4000, -870, 315)
    SetChrPos(0xEF, -970, 4000, -580, 315)
    SetChrPos(0xEE, 890, 4000, 750, 315)
    SetChrPos(0xF1, -4400, 4000, 2420, 315)

    label("loc_9AC6")

    OP_8C(0x22, 270, 0)

    def lambda_9AD3():
        OP_6B(1600, 1000)
        ExitThread()

    QueueWorkItem(0x22, 0, lambda_9AD3)
    SetChrFlags(0x10, 0x4)
    SetChrPos(0x10, -8000, 22000, 5590, 135)
    OP_A1(0x10, 0x17)
    OP_72(0x417, 0x0)
    ExitThread()
    OP_B0(0x17, 0xF)
    OP_6F(0x17, 260)
    OP_70(0x17, 0xF1)

    def lambda_9B16():
        OP_8F(0xFE, 0xFFFFE0C0, 0xFA0, 0x1612, 0x4268, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_9B16)
    Sleep(1000)
    OP_72(0x2017, 0x0)
    ExitThread()
    OP_6F(0x17, 221)
    OP_70(0x17, 0xF0)
    OP_44(0x22, 0x0)
    OP_6D(-10490, 5100, 8140, 0)
    OP_67(0, 6030, -10000, 0)
    OP_6B(2530, 0)
    OP_6C(315000, 0)
    OP_6E(442, 0)

    def lambda_9B8B():
        OP_6B(2300, 3000)
        ExitThread()

    QueueWorkItem(0x22, 0, lambda_9B8B)
    OP_44(0x10, 0x3)
    OP_23(0x113)
    OP_22(0x88, 0x0, 0x64)
    OP_22(0xF5, 0x0, 0x64)
    OP_7C(0x0, 0x1F4, 0x1388, 0x5DC)
    WaitChrThread(0x10, 0x1)
    OP_73(0x17)
    OP_71(0x2017, 0x0)
    ExitThread()
    OP_D8(0x17, 0x3E8)
    OP_6F(0x17, 1)
    OP_70(0x17, 0x28)
    Sleep(1000)
    OP_22(0x3D4, 0x0, 0x64)
    Sleep(1000)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_9BF5():
        OP_6D(-9100, 4500, 7000, 3000)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_9BF5)

    def lambda_9C0D():
        OP_67(0, 3500, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_9C0D)

    def lambda_9C25():
        OP_6B(3400, 3000)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_9C25)

    def lambda_9C35():
        OP_6E(348, 3000)
        ExitThread()

    QueueWorkItem(0x10, 3, lambda_9C35)
    WaitChrThread(0x10, 0x0)

    ChrTalk(    #214
        0x110,
        "#261F#5P嘻嘻，果然过来了。\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x110, 19)
    SetChrSubChip(0x110, 0)
    OP_0D()
    Sleep(300)

    ChrTalk(    #215
        0x110,
        (
            "#263F#5P『帕蒂尔·玛蒂尔』，进入待机模式……\x02\x03",

            "#260F……………就是这样。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_9CEB():
        OP_6D(-8970, 4000, 6760, 5000)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_9CEB)

    def lambda_9D03():
        OP_67(0, 3300, -10000, 5000)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_9D03)

    def lambda_9D1B():
        OP_6B(3000, 5000)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_9D1B)

    def lambda_9D2B():
        OP_6E(330, 5000)
        ExitThread()

    QueueWorkItem(0x10, 3, lambda_9D2B)
    OP_8C(0x110, 135, 400)
    Sleep(300)
    SetChrFlags(0x110, 0x2)
    SetChrChipByIndex(0x110, 21)
    SetChrSubChip(0x110, 0)
    OP_99(0x110, 0x0, 0x4, 0x5DC)
    OP_22(0x1F6, 0x0, 0x64)
    OP_99(0x110, 0x5, 0x16, 0x708)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_44(0x10, 0x0)
    OP_44(0x10, 0x1)
    OP_44(0x10, 0x2)
    OP_44(0x10, 0x3)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #216
        (
            "\x07\x05玲学会了新的Ｓ战技\x01",
            "\x07\x02『帕蒂尔·玛蒂尔』\x07\x05。\x02",
        )
    )

    Jump("loc_9DC2")

    label("loc_9DC2")

    CloseMessageWindow()
    OP_56(0x0)
    OP_22(0x21E, 0x0, 0x64)
    OP_35(0xF, 0x11D)
    SetMessageWindowPos(-1, 80, -1, -1)

    AnonymousTalk(    #217
        "\x07\x05将『帕蒂尔·玛蒂尔』设定为Ｓ爆发技吗？\x18\x02",
    )

    CloseMessageWindow()
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_9E19")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_9E91")

    Menu(
        1,
        -1,
        200,
        0,
        (
            "【是】\x01",      # 0
            "【否】\x01",      # 1
        )
    )

    Jump("loc_9E4F")

    label("loc_9E4F")

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_56(0x0)
    OP_5F(0x1)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_9E6D"),
        (SWITCH_DEFAULT, "loc_9E81"),
    )


    label("loc_9E6D")

    OP_BB(0xF, 0x6, 0x11D)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_9E8E")

    label("loc_9E81")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_9E8E")

    label("loc_9E8E")

    Jump("loc_9E19")

    label("loc_9E91")

    SetMessageWindowPos(72, 320, 56, 3)
    ClearChrFlags(0x110, 0x2)
    SetChrChipByIndex(0x110, 65535)
    SetChrSubChip(0x110, 0)
    SetChrPos(0x110, -3280, 4000, 1770, 90)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9EFE")
    SetChrPos(0xF1, 800, 4000, -650, 270)
    SetChrPos(0xF0, -810, 4000, -380, 270)
    SetChrPos(0xEF, 520, 4000, 1410, 270)
    Jump("loc_9FC7")

    label("loc_9EFE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9F42")
    SetChrPos(0xF1, 800, 4000, -650, 270)
    SetChrPos(0xF0, -810, 4000, -380, 270)
    SetChrPos(0xEE, 520, 4000, 1410, 270)
    Jump("loc_9FC7")

    label("loc_9F42")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9F86")
    SetChrPos(0xF1, 800, 4000, -650, 270)
    SetChrPos(0xEF, -810, 4000, -380, 270)
    SetChrPos(0xEE, 520, 4000, 1410, 270)
    Jump("loc_9FC7")

    label("loc_9F86")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9FC7")
    SetChrPos(0xF0, 800, 4000, -650, 270)
    SetChrPos(0xEF, -810, 4000, -380, 270)
    SetChrPos(0xEE, 520, 4000, 1410, 270)

    label("loc_9FC7")

    OP_8C(0x22, 180, 0)
    OP_6D(-2400, 5080, 2800, 0)
    OP_67(0, 4320, -10000, 0)
    OP_6B(2630, 0)
    OP_6C(336000, 0)
    OP_6E(419, 0)
    Sleep(500)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A08D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x584, 0)), scpexpr(EXPR_END)), "loc_A062")

    ChrTalk(    #218
        0x10F,
        "#1934F………………………………\x02",
    )

    CloseMessageWindow()
    Jump("loc_A08D")

    label("loc_A062")


    ChrTalk(    #219
        0x10F,
        "#1444F………………………………\x02",
    )

    CloseMessageWindow()

    label("loc_A08D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A0C4")

    ChrTalk(    #220
        0x107,
        "#065F#12P那、那个…………\x02",
    )

    CloseMessageWindow()
    Jump("loc_A1D6")

    label("loc_A0C4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A107")

    ChrTalk(    #221
        0x101,
        (
            "#1016F#12P哎…………\x01",
            "……哎呀…………\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A1D6")

    label("loc_A107")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A141")

    ChrTalk(    #222
        0x109,
        "#1066F#12P啊……我说，小玲？\x02",
    )

    CloseMessageWindow()
    Jump("loc_A1D6")

    label("loc_A141")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A176")

    ChrTalk(    #223
        0x10A,
        "#812F#12P哎、哎…………\x02",
    )

    CloseMessageWindow()
    Jump("loc_A1D6")

    label("loc_A176")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A1AF")

    ChrTalk(    #224
        0x10B,
        "#215F#12P啊……这个…………\x02",
    )

    CloseMessageWindow()
    Jump("loc_A1D6")

    label("loc_A1AF")


    ChrTalk(    #225
        0x22,
        "\x07\x0C#1614F#11P哎呀…………\x07\x00\x02",
    )

    CloseMessageWindow()

    label("loc_A1D6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A367")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A207")
    OP_62(0xEF, 0x0, 2300, 0x28, 0x2B, 0x64, 0x3)
    Jump("loc_A25F")

    label("loc_A207")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A22A")
    OP_62(0xEF, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Jump("loc_A25F")

    label("loc_A22A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A24D")
    OP_62(0xEF, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Jump("loc_A25F")

    label("loc_A24D")

    OP_62(0xEF, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    label("loc_A25F")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A287")
    OP_62(0xF0, 0x0, 2300, 0x28, 0x2B, 0x64, 0x3)
    Jump("loc_A2DF")

    label("loc_A287")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A2AA")
    OP_62(0xF0, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Jump("loc_A2DF")

    label("loc_A2AA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A2CD")
    OP_62(0xF0, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Jump("loc_A2DF")

    label("loc_A2CD")

    OP_62(0xF0, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    label("loc_A2DF")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A307")
    OP_62(0xF1, 0x0, 2300, 0x28, 0x2B, 0x64, 0x3)
    Jump("loc_A35F")

    label("loc_A307")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A32A")
    OP_62(0xF1, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Jump("loc_A35F")

    label("loc_A32A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A34D")
    OP_62(0xF1, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Jump("loc_A35F")

    label("loc_A34D")

    OP_62(0xF1, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    label("loc_A35F")

    Sleep(1000)
    Jump("loc_A817")

    label("loc_A367")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A4F8")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A398")
    OP_62(0xEE, 0x0, 2300, 0x28, 0x2B, 0x64, 0x3)
    Jump("loc_A3F0")

    label("loc_A398")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A3BB")
    OP_62(0xEE, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Jump("loc_A3F0")

    label("loc_A3BB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A3DE")
    OP_62(0xEE, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Jump("loc_A3F0")

    label("loc_A3DE")

    OP_62(0xEE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    label("loc_A3F0")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A418")
    OP_62(0xF0, 0x0, 2300, 0x28, 0x2B, 0x64, 0x3)
    Jump("loc_A470")

    label("loc_A418")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A43B")
    OP_62(0xF0, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Jump("loc_A470")

    label("loc_A43B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A45E")
    OP_62(0xF0, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Jump("loc_A470")

    label("loc_A45E")

    OP_62(0xF0, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    label("loc_A470")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A498")
    OP_62(0xF1, 0x0, 2300, 0x28, 0x2B, 0x64, 0x3)
    Jump("loc_A4F0")

    label("loc_A498")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A4BB")
    OP_62(0xF1, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Jump("loc_A4F0")

    label("loc_A4BB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A4DE")
    OP_62(0xF1, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Jump("loc_A4F0")

    label("loc_A4DE")

    OP_62(0xF1, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    label("loc_A4F0")

    Sleep(1000)
    Jump("loc_A817")

    label("loc_A4F8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A689")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A529")
    OP_62(0xEE, 0x0, 2300, 0x28, 0x2B, 0x64, 0x3)
    Jump("loc_A581")

    label("loc_A529")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A54C")
    OP_62(0xEE, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Jump("loc_A581")

    label("loc_A54C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A56F")
    OP_62(0xEE, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Jump("loc_A581")

    label("loc_A56F")

    OP_62(0xEE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    label("loc_A581")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A5A9")
    OP_62(0xEF, 0x0, 2300, 0x28, 0x2B, 0x64, 0x3)
    Jump("loc_A601")

    label("loc_A5A9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A5CC")
    OP_62(0xEF, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Jump("loc_A601")

    label("loc_A5CC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A5EF")
    OP_62(0xEF, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Jump("loc_A601")

    label("loc_A5EF")

    OP_62(0xEF, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    label("loc_A601")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A629")
    OP_62(0xF1, 0x0, 2300, 0x28, 0x2B, 0x64, 0x3)
    Jump("loc_A681")

    label("loc_A629")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A64C")
    OP_62(0xF1, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Jump("loc_A681")

    label("loc_A64C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A66F")
    OP_62(0xF1, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Jump("loc_A681")

    label("loc_A66F")

    OP_62(0xF1, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    label("loc_A681")

    Sleep(1000)
    Jump("loc_A817")

    label("loc_A689")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A817")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A6BA")
    OP_62(0xEE, 0x0, 2300, 0x28, 0x2B, 0x64, 0x3)
    Jump("loc_A712")

    label("loc_A6BA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A6DD")
    OP_62(0xEE, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Jump("loc_A712")

    label("loc_A6DD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A700")
    OP_62(0xEE, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Jump("loc_A712")

    label("loc_A700")

    OP_62(0xEE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    label("loc_A712")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A73A")
    OP_62(0xEF, 0x0, 2300, 0x28, 0x2B, 0x64, 0x3)
    Jump("loc_A792")

    label("loc_A73A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A75D")
    OP_62(0xEF, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Jump("loc_A792")

    label("loc_A75D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A780")
    OP_62(0xEF, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Jump("loc_A792")

    label("loc_A780")

    OP_62(0xEF, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    label("loc_A792")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A7BA")
    OP_62(0xF0, 0x0, 2300, 0x28, 0x2B, 0x64, 0x3)
    Jump("loc_A812")

    label("loc_A7BA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A7DD")
    OP_62(0xF0, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Jump("loc_A812")

    label("loc_A7DD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A800")
    OP_62(0xF0, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Jump("loc_A812")

    label("loc_A800")

    OP_62(0xF0, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    label("loc_A812")

    Sleep(1000)

    label("loc_A817")

    SetMessageWindowPos(300, 330, -1, -1)
    SetChrName("全体")

    AnonymousTalk(    #226
        "\x07\x00#4S哎——————！！？\x02",
    )

    Jump("loc_A84F")

    label("loc_A84F")

    OP_7C(0x0, 0x12C, 0xBB8, 0x1F4)
    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(500)

    ChrTalk(    #227
        0x110,
        (
            "#269F#5P嘻嘻……\x01",
            "有什么好吃惊的？\x02\x03",

            "#263F这里是反映意念\x01",
            "而产生的影子世界……\x02\x03",

            "#265F嘻嘻，能叫来帕蒂尔·玛蒂尔\x01",
            "不是当然的事情吗？\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)

    def lambda_A916():
        OP_6B(3400, 5000)
        ExitThread()

    QueueWorkItem(0x22, 0, lambda_A916)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_44(0x22, 0x0)
    OP_71(0x417, 0x0)
    ExitThread()
    OP_28(0x17, 0x4, 0x20)
    OP_A2(0x2C35)
    OP_6D(390, 4000, -1290, 0)
    OP_67(0, 7900, -10000, 0)
    OP_6B(2530, 0)
    OP_6C(315000, 0)
    OP_6E(450, 0)
    SetChrPos(0x0, 510, 4000, -1300, 180)
    SetChrPos(0x1, 510, 4000, -1300, 180)
    SetChrPos(0x2, 510, 4000, -1300, 180)
    SetChrPos(0x3, 510, 4000, -1300, 180)
    SetChrChipByIndex(0x0, 65535)
    SetChrChipByIndex(0x1, 65535)
    SetChrChipByIndex(0x2, 65535)
    SetChrChipByIndex(0x3, 65535)
    SetChrSubChip(0x0, 0)
    SetChrSubChip(0x1, 0)
    SetChrSubChip(0x2, 0)
    SetChrSubChip(0x3, 0)
    OP_69(0x0, 0x0)
    OP_8C(0x22, 135, 0)
    Sleep(1000)
    Call(0, 9)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x584, 0)), scpexpr(EXPR_END)), "loc_AA14")
    SetMapFlags(0x2000000)

    label("loc_AA14")

    Return()

    # Function_25_988F end

    SaveToFile()

Try(main)

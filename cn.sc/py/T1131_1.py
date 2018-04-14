from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 柏斯

    CreateScenaFile(
        FileName            = 'T1131_1 ._SN',
        MapName             = 'Bose',
        Location            = 'T1131.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60011",
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
        '',                                     # 9
        '',                                     # 10
        '',                                     # 11
        '',                                     # 12
        '',                                     # 13
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


    ScpFunction(
        "Function_0_AA",           # 00, 0
        "Function_1_1CE",          # 01, 1
        "Function_2_275",          # 02, 2
        "Function_3_366",          # 03, 3
        "Function_4_734",          # 04, 4
        "Function_5_986",          # 05, 5
        "Function_6_3035",         # 06, 6
        "Function_7_3AC7",         # 07, 7
        "Function_8_41C6",         # 08, 8
        "Function_9_43F1",         # 09, 9
        "Function_10_5754",        # 0A, 10
        "Function_11_63A8",        # 0B, 11
        "Function_12_6403",        # 0C, 12
        "Function_13_642B",        # 0D, 13
    )


    def Function_0_AA(): pass

    label("Function_0_AA")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x13), scpexpr(EXPR_PUSH_LONG, 0x381), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B7")
    Return()

    label("loc_B7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x79, 0x0, 0x10)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x79, 0x0, 0x40)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_C9")
    Return()

    label("loc_C9")

    SetMapFlags(0x80)
    OP_C0(0x1, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    Sleep(30)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CD(0x20)"), scpexpr(EXPR_END)), "loc_104")
    Call(0, 35)
    Jump("loc_1C7")

    label("loc_104")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CD(0x1B)"), scpexpr(EXPR_END)), "loc_113")
    Call(1, 1)
    Jump("loc_1C7")

    label("loc_113")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CD(0x3E8)"), scpexpr(EXPR_END)), "loc_122")
    Call(1, 1)
    Jump("loc_1C7")

    label("loc_122")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CD(0x8)"), scpexpr(EXPR_END)), "loc_131")
    Call(1, 2)
    Jump("loc_1C7")

    label("loc_131")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CD(0xFF)"), scpexpr(EXPR_END)), "loc_189")
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #0
        (
            "\x07\x05试着出示了照片，\x01",
            "但似乎没有见过的印象。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    Jump("loc_1C7")

    label("loc_189")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #1
        "\x07\x05附近没有人可以确认照片。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    label("loc_1C7")

    OP_0D()
    ClearMapFlags(0x80)
    Return()

    # Function_0_AA end

    def Function_1_1CE(): pass

    label("Function_1_1CE")

    TalkBegin(0x1B)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3, 2)), scpexpr(EXPR_END)), "loc_20B")

    ChrTalk(    #2
        0x1B,
        "不好意思，我没印象呢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x1B,
        "问问其他人吧。\x02",
    )

    CloseMessageWindow()
    Jump("loc_271")

    label("loc_20B")


    ChrTalk(    #4
        0x1B,
        "啊啊，找人吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x1B,
        "好可爱的女孩啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x1B,
        (
            "这孩子的父母因为战争去世了啊。\x01",
            "战争果然是场错误啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1A)

    label("loc_271")

    TalkEnd(0x1B)
    Return()

    # Function_1_1CE end

    def Function_2_275(): pass

    label("Function_2_275")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_2D6")

    ChrTalk(    #7
        0x8,
        (
            "那照片中少女的眼睛……\x01",
            "感觉似乎在哪里见过。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x8,
        (
            "本店的客人中\x01",
            "有这样的人吗……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_362")

    label("loc_2D6")


    ChrTalk(    #9
        0x8,
        "唔，寻找失踪的人吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x8,
        (
            "真不巧，我似乎\x01",
            "没有见过的印象……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x8,
        (
            "……这绿色的眼睛\x01",
            "含着某种牵挂。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x8,
        (
            "本店的客人中\x01",
            "有这样的人吗……\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_362")

    TalkEnd(0x8)
    Return()

    # Function_2_275 end

    def Function_3_366(): pass

    label("Function_3_366")

    EventBegin(0x0)
    Fade(1000)
    OP_8C(0x20, 270, 0)
    SetChrPos(0x101, 1120, 0, 1500, 90)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF7)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3C8")
    SetChrPos(0xF8, 1000, 0, 110, 32)
    SetChrPos(0xF7, 10, 0, 1520, 90)
    SetChrPos(0xF9, -120, 0, 490, 90)
    Jump("loc_481")

    label("loc_3C8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_40B")
    SetChrPos(0xF7, 1000, 0, 110, 32)
    SetChrPos(0xF8, 10, 0, 1520, 90)
    SetChrPos(0xF9, -120, 0, 490, 90)
    Jump("loc_481")

    label("loc_40B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_44E")
    SetChrPos(0xF7, 1000, 0, 110, 32)
    SetChrPos(0xF9, 10, 0, 1520, 90)
    SetChrPos(0xF8, -120, 0, 490, 90)
    Jump("loc_481")

    label("loc_44E")

    SetChrPos(0xF7, 1000, 0, 110, 32)
    SetChrPos(0xF8, -120, 0, 490, 90)
    SetChrPos(0xF9, 10, 0, 1520, 90)

    label("loc_481")

    OP_6D(780, 0, 1170, 0)
    OP_67(0, 6150, -10000, 0)
    OP_6B(2750, 0)
    OP_6C(315000, 0)
    OP_6E(280, 0)
    OP_0D()

    ChrTalk(    #13
        0x101,
        "#1011F请问～打扰一下行吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0xFE,
        "好，什么事。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x101,
        (
            "#1000F您是科尔娜女士吧？\x02\x03",

            "我们是\x01",
            "游击士协会的人……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0xFE,
        "呀，你们可来了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0xFE,
        (
            "正等着你们呢。\x01",
            "我就是提出委托的科尔娜。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x101,
        (
            "#1011F啊，幸会。\x01",
            "我是游击士艾丝蒂尔·布莱特。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0xFE,
        (
            "突然叫你们来\x01",
            "真是不好意思……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0xFE,
        (
            "但是靠我一个人的力量\x01",
            "已经毫无办法了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0xFE,
        (
            "总之拜托你们先\x01",
            "听听我的苦衷好吗？\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "【是】\x01",      # 0
            "【否】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_685")

    ChrTalk(    #22
        0x101,
        "#1006F嗯，没问题。\x02",
    )

    CloseMessageWindow()
    Call(1, 5)
    Jump("loc_731")

    label("loc_685")


    ChrTalk(    #23
        0x101,
        (
            "#1007F唔～实在对不起。\x02\x03",

            "现在有点不方便。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0xFE,
        "呀，这样吗……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0xFE,
        (
            "嗯，那么\x01",
            "就请你们方便的时候，\x01",
            "再过来找我吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0xFE,
        "我会在这里等你们的。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x101,
        "#1000F嗯，知道了。\x02",
    )

    CloseMessageWindow()
    OP_28(0x79, 0x1, 0x8000)

    label("loc_731")

    EventEnd(0x0)
    Return()

    # Function_3_366 end

    def Function_4_734(): pass

    label("Function_4_734")

    EventBegin(0x0)
    Fade(1000)
    OP_8C(0x20, 270, 0)
    SetChrPos(0x101, 1120, 0, 1500, 90)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF7)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_796")
    SetChrPos(0xF8, 1000, 0, 110, 32)
    SetChrPos(0xF7, 10, 0, 1520, 90)
    SetChrPos(0xF9, -120, 0, 490, 90)
    Jump("loc_84F")

    label("loc_796")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7D9")
    SetChrPos(0xF7, 1000, 0, 110, 32)
    SetChrPos(0xF8, 10, 0, 1520, 90)
    SetChrPos(0xF9, -120, 0, 490, 90)
    Jump("loc_84F")

    label("loc_7D9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_81C")
    SetChrPos(0xF7, 1000, 0, 110, 32)
    SetChrPos(0xF9, 10, 0, 1520, 90)
    SetChrPos(0xF8, -120, 0, 490, 90)
    Jump("loc_84F")

    label("loc_81C")

    SetChrPos(0xF7, 1000, 0, 110, 32)
    SetChrPos(0xF8, -120, 0, 490, 90)
    SetChrPos(0xF9, 10, 0, 1520, 90)

    label("loc_84F")

    OP_6D(780, 0, 1170, 0)
    OP_67(0, 6150, -10000, 0)
    OP_6B(2750, 0)
    OP_6C(315000, 0)
    OP_6E(280, 0)
    OP_0D()

    ChrTalk(    #28
        0xFE,
        "哎呀，各位游击士。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0xFE,
        "这下方便了吗？\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "【是】\x01",      # 0
            "【否】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_92B")

    ChrTalk(    #30
        0x101,
        "#1006F嗯，没问题了。\x02",
    )

    CloseMessageWindow()
    Call(1, 5)
    Jump("loc_983")

    label("loc_92B")


    ChrTalk(    #31
        0x101,
        (
            "#1007F唔～抱歉哦。\x01",
            "还没什么空闲。\x02\x03",

            "方便的时候\x01",
            "再来找你吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0xFE,
        "嗯，那就拜托了……\x02",
    )

    CloseMessageWindow()

    label("loc_983")

    EventEnd(0x0)
    Return()

    # Function_4_734 end

    def Function_5_986(): pass

    label("Function_5_986")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_9CD")

    ChrTalk(    #33
        0x103,
        (
            "#020F这么多人别站着说话吧。\x02\x03",

            "先坐下来吧。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 400)
    Jump("loc_B25")

    label("loc_9CD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A18")

    ChrTalk(    #34
        0x106,
        (
            "#050F这么多人别站着说话。\x02\x03",

            "先找地方坐下来吧。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x106, 400)
    Jump("loc_B25")

    label("loc_A18")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A6E")

    ChrTalk(    #35
        0x108,
        (
            "#070F这么一堆人别站着说话。\x02\x03",

            "先坐下来，\x01",
            "然后再慢慢说吧。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x108, 400)
    Jump("loc_B25")

    label("loc_A6E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_AD5")

    ChrTalk(    #36
        0x105,
        (
            "#040F站着说话不太好吧，\x01",
            "不先找地方坐下吗？\x02\x03",

            "这么多人\x01",
            "会给店里添麻烦的……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x105, 400)
    Jump("loc_B25")

    label("loc_AD5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B25")

    ChrTalk(    #37
        0x104,
        (
            "#030F唔，不过站着说话不太好吧。\x02\x03",

            "不先找地方坐下来吗？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x104, 400)

    label("loc_B25")


    ChrTalk(    #38
        0x101,
        (
            "#1000F啊，是呢。\x02\x03",

            "那就找个地方\x01",
            "先坐下来吧。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrFlags(0x38, 0x80)
    OP_4A(0x20, 255)
    SetChrChipByIndex(0x20, 6)
    SetChrFlags(0x20, 0x4)
    SetChrPos(0x20, 3800, 120, -3550, 0)
    OP_D2(0x270003, 0x270007, 0x24)
    Switch(
        (scpexpr(EXPR_EXEC_OP, "OP_CB(0xF7)"), scpexpr(EXPR_END)),
        (2, "loc_BB4"),
        (3, "loc_BC1"),
        (4, "loc_BCE"),
        (5, "loc_BDB"),
        (6, "loc_BE8"),
        (7, "loc_BF5"),
        (8, "loc_C02"),
        (SWITCH_DEFAULT, "loc_C0F"),
    )


    label("loc_BB4")

    OP_D2(0x70023, 0x7002B, 0x25)
    Jump("loc_C0F")

    label("loc_BC1")

    OP_D2(0x70033, 0x7003B, 0x25)
    Jump("loc_C0F")

    label("loc_BCE")

    OP_D2(0x70043, 0x7004B, 0x25)
    Jump("loc_C0F")

    label("loc_BDB")

    OP_D2(0x70053, 0x7005B, 0x25)
    Jump("loc_C0F")

    label("loc_BE8")

    OP_D2(0x70063, 0x7006B, 0x25)
    Jump("loc_C0F")

    label("loc_BF5")

    OP_D2(0x70073, 0x7007B, 0x25)
    Jump("loc_C0F")

    label("loc_C02")

    OP_D2(0x270083, 0x270087, 0x25)
    Jump("loc_C0F")

    label("loc_C0F")

    Switch(
        (scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_END)),
        (2, "loc_C34"),
        (3, "loc_C41"),
        (4, "loc_C4E"),
        (5, "loc_C5B"),
        (6, "loc_C68"),
        (7, "loc_C75"),
        (8, "loc_C82"),
        (SWITCH_DEFAULT, "loc_C8F"),
    )


    label("loc_C34")

    OP_D2(0x70023, 0x7002B, 0x26)
    Jump("loc_C8F")

    label("loc_C41")

    OP_D2(0x70033, 0x7003B, 0x26)
    Jump("loc_C8F")

    label("loc_C4E")

    OP_D2(0x70043, 0x7004B, 0x26)
    Jump("loc_C8F")

    label("loc_C5B")

    OP_D2(0x70053, 0x7005B, 0x26)
    Jump("loc_C8F")

    label("loc_C68")

    OP_D2(0x70063, 0x7006B, 0x26)
    Jump("loc_C8F")

    label("loc_C75")

    OP_D2(0x70073, 0x7007B, 0x26)
    Jump("loc_C8F")

    label("loc_C82")

    OP_D2(0x270083, 0x270087, 0x26)
    Jump("loc_C8F")

    label("loc_C8F")

    Switch(
        (scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_END)),
        (2, "loc_CB4"),
        (3, "loc_CC1"),
        (4, "loc_CCE"),
        (5, "loc_CDB"),
        (6, "loc_CE8"),
        (7, "loc_CF5"),
        (8, "loc_D02"),
        (SWITCH_DEFAULT, "loc_D0F"),
    )


    label("loc_CB4")

    OP_D2(0x70023, 0x7002B, 0x27)
    Jump("loc_D0F")

    label("loc_CC1")

    OP_D2(0x70033, 0x7003B, 0x27)
    Jump("loc_D0F")

    label("loc_CCE")

    OP_D2(0x70043, 0x7004B, 0x27)
    Jump("loc_D0F")

    label("loc_CDB")

    OP_D2(0x70053, 0x7005B, 0x27)
    Jump("loc_D0F")

    label("loc_CE8")

    OP_D2(0x70063, 0x7006B, 0x27)
    Jump("loc_D0F")

    label("loc_CF5")

    OP_D2(0x70073, 0x7007B, 0x27)
    Jump("loc_D0F")

    label("loc_D02")

    OP_D2(0x270083, 0x270087, 0x27)
    Jump("loc_D0F")

    label("loc_D0F")

    SetChrChipByIndex(0x101, 36)
    SetChrChipByIndex(0xF7, 37)
    SetChrChipByIndex(0xF8, 38)
    SetChrChipByIndex(0xF9, 39)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0xF7, 0x4)
    SetChrFlags(0xF8, 0x4)
    SetChrFlags(0xF9, 0x4)
    SetChrPos(0x101, 2760, 200, -2500, 90)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF7)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D73")
    SetChrPos(0xF7, 5100, 100, -950, 270)
    RunExpression(0x7, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_E1D")

    label("loc_D73")

    SetChrPos(0xF7, 5100, 200, -950, 270)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF7)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D9E")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_E1D")

    label("loc_D9E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF7)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DB8")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_E1D")

    label("loc_DB8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF7)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DD2")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_E1D")

    label("loc_DD2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF7)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DEC")
    RunExpression(0x5, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_E1D")

    label("loc_DEC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF7)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E06")
    RunExpression(0x6, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_E1D")

    label("loc_E06")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF7)"), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E1D")
    RunExpression(0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_E1D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E48")
    SetChrPos(0xF8, 5100, 100, -2550, 270)
    RunExpression(0x7, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_EF2")

    label("loc_E48")

    SetChrPos(0xF8, 5100, 200, -2550, 270)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E73")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_EF2")

    label("loc_E73")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E8D")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_EF2")

    label("loc_E8D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_EA7")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_EF2")

    label("loc_EA7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_EC1")
    RunExpression(0x5, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_EF2")

    label("loc_EC1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_EDB")
    RunExpression(0x6, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_EF2")

    label("loc_EDB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_EF2")
    RunExpression(0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_EF2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F1D")
    SetChrPos(0xF9, 2900, 100, -900, 90)
    RunExpression(0x7, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_FC7")

    label("loc_F1D")

    SetChrPos(0xF9, 2900, 200, -900, 90)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F48")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_FC7")

    label("loc_F48")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F62")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_FC7")

    label("loc_F62")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F7C")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_FC7")

    label("loc_F7C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F96")
    RunExpression(0x5, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_FC7")

    label("loc_F96")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FB0")
    RunExpression(0x6, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_FC7")

    label("loc_FB0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FC7")
    RunExpression(0x8, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_FC7")

    OP_6D(3330, 0, -1410, 0)
    SetChrSubChip(0x101, 2)
    SetChrSubChip(0xF9, 2)
    SetChrSubChip(0xF7, 1)
    SetChrSubChip(0xF8, 1)
    FadeToBright(1000, 0)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1050")

    ChrTalk(    #39
        0x106,
        (
            "#050F看了公告板，\x01",
            "您好像要找人啊。\x02\x03",

            "说是１０年前\x01",
            "就失踪了什么的……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_11C8")

    label("loc_1050")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_10AA")

    ChrTalk(    #40
        0x103,
        (
            "#022F看了公告板，\x01",
            "您好像要找人吧。\x02\x03",

            "说是１０年前\x01",
            "就失踪了什么的……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_11C8")

    label("loc_10AA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1104")

    ChrTalk(    #41
        0x108,
        (
            "#070F看了公告板，\x01",
            "您好像要找人啊。\x02\x03",

            "说是１０年前\x01",
            "就失踪了什么的……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_11C8")

    label("loc_1104")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1162")

    ChrTalk(    #42
        0x105,
        (
            "#043F看了公告板，\x01",
            "您好像要找什么人吧。\x02\x03",

            "说是１０年前\x01",
            "就失踪了什么的……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_11C8")

    label("loc_1162")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_11C8")

    ChrTalk(    #43
        0x109,
        (
            "#1063F那么，就开门见山的说吧……\x01",
            "您好像要找人吧。\x02\x03",

            "说是１０年前\x01",
            "就失踪了什么的……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_11C8")


    ChrTalk(    #44
        0xFE,
        (
            "是，其实……\x01",
            "我在寻找我侄女。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0xFE,
        "她名叫蕾妮……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0xFE,
        (
            "如果平安无事，\x01",
            "现在应该２０岁了。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)
    OP_63(0x101)

    ChrTalk(    #47
        0x101,
        "#1015F如果平安无事……？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_12AF")

    ChrTalk(    #48
        0x106,
        (
            "#053F原来如此啊……\x02\x03",

            "#552F总算明白\x01",
            "１０年前的意思了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_13D5")

    label("loc_12AF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_12F9")

    ChrTalk(    #49
        0x103,
        (
            "#026F原来如此……\x02\x03",

            "#522F总算明白\x01",
            "１０年前的意思了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_13D5")

    label("loc_12F9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1347")

    ChrTalk(    #50
        0x108,
        (
            "#074F呼，原来如此啊……\x02\x03",

            "#072F总算明白\x01",
            "10年前的意思了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_13D5")

    label("loc_1347")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1394")

    ChrTalk(    #51
        0x104,
        (
            "#032F唔，原来如此……\x02\x03",

            "总算明白了。\x01",
            "１０年前的意义了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_13D5")

    label("loc_1394")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_13D5")

    ChrTalk(    #52
        0x107,
        (
            "#065F难，难不成……\x02\x03",

            "从现在算起１０年前是……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_13D5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1432")

    ChrTalk(    #53
        0x109,
        (
            "#1065F……………………………\x02\x03",

            "听爷爷说那时发生一场『百日战役』……吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_14F3")

    label("loc_1432")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1464")

    ChrTalk(    #54
        0x105,
        "#042F『百日战役』……对吧。\x02",
    )

    CloseMessageWindow()
    Jump("loc_14F3")

    label("loc_1464")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1496")

    ChrTalk(    #55
        0x107,
        "#063F『百日战役』……对吧。\x02",
    )

    CloseMessageWindow()
    Jump("loc_14F3")

    label("loc_1496")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_14C6")

    ChrTalk(    #56
        0x104,
        "#032F『百日战役』……吧。\x02",
    )

    CloseMessageWindow()
    Jump("loc_14F3")

    label("loc_14C6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_14F3")

    ChrTalk(    #57
        0x108,
        "#072F『百日战役』……啊。\x02",
    )

    CloseMessageWindow()

    label("loc_14F3")


    ChrTalk(    #58
        0x101,
        "#1026F……啊……………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0xFE,
        "……是，正如你们所说。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0xFE,
        (
            "当时，我姐姐一家\x01",
            "还住在这个城市……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0xFE,
        (
            "不幸卷入了\x01",
            "那场突如其来的战火。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0xFE,
        (
            "不久我便通过熟人的关系\x01",
            "得知了姐姐夫妇的死讯……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0xFE,
        (
            "而１０岁的蕾妮\x01",
            "至今仍去向不明。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0xFE,
        "从那以来过了１０年……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0xFE,
        (
            "我们也完全\x01",
            "死心了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0xFE,
        (
            "然而，最近\x01",
            "却有了新的消息。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0xFE,
        (
            "有人说当时\x01",
            "『蕾妮被寄养在当地人家里』。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #68
        0x101,
        (
            "#1004F这、这么说，\x01",
            "蕾妮还活着吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0xFE,
        "这就……不清楚了……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0xFE,
        (
            "因为连寄养的人家\x01",
            "的名字也都不知道。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0x101,
        (
            "#1007F啊……\x01",
            "这，这样啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0xFE,
        (
            "但是，我相信。\x01",
            "那女孩一定还活着。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0xFE,
        (
            "正因为这样相信\x01",
            "才会请求各位协助。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_17E0")

    ChrTalk(    #74
        0x106,
        (
            "#050F……事情我们明白了。\x02\x03",

            "确实有调查的价值啊。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_17AF")
    SetChrSubChip(0x101, 1)
    SetChrSubChip(0xF8, 2)
    SetChrSubChip(0xF9, 0)
    Jump("loc_17DD")

    label("loc_17AF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_17CE")
    SetChrSubChip(0x101, 0)
    SetChrSubChip(0xF7, 1)
    SetChrSubChip(0xF9, 2)
    Jump("loc_17DD")

    label("loc_17CE")

    SetChrSubChip(0x101, 1)
    SetChrSubChip(0xF7, 0)
    SetChrSubChip(0xF8, 2)

    label("loc_17DD")

    Jump("loc_1A2D")

    label("loc_17E0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1873")

    ChrTalk(    #75
        0x103,
        (
            "#022F……事情我们明白了。\x02\x03",

            "确实有调查的价值呢。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1842")
    SetChrSubChip(0x101, 1)
    SetChrSubChip(0xF8, 2)
    SetChrSubChip(0xF9, 0)
    Jump("loc_1870")

    label("loc_1842")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1861")
    SetChrSubChip(0x101, 0)
    SetChrSubChip(0xF7, 1)
    SetChrSubChip(0xF9, 2)
    Jump("loc_1870")

    label("loc_1861")

    SetChrSubChip(0x101, 1)
    SetChrSubChip(0xF7, 0)
    SetChrSubChip(0xF8, 2)

    label("loc_1870")

    Jump("loc_1A2D")

    label("loc_1873")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1902")

    ChrTalk(    #76
        0x108,
        (
            "#070F……事情明白了。\x02\x03",

            "确实有调查的价值啊。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_GET_RESULT, 0x7), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_18D1")
    SetChrSubChip(0x101, 1)
    SetChrSubChip(0xF8, 2)
    SetChrSubChip(0xF9, 0)
    Jump("loc_18FF")

    label("loc_18D1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x7), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_18F0")
    SetChrSubChip(0x101, 0)
    SetChrSubChip(0xF7, 1)
    SetChrSubChip(0xF9, 2)
    Jump("loc_18FF")

    label("loc_18F0")

    SetChrSubChip(0x101, 1)
    SetChrSubChip(0xF7, 0)
    SetChrSubChip(0xF8, 2)

    label("loc_18FF")

    Jump("loc_1A2D")

    label("loc_1902")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1991")

    ChrTalk(    #77
        0x104,
        (
            "#032F……事情明白啦。\x02\x03",

            "确实有调查的价值呢。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1960")
    SetChrSubChip(0x101, 1)
    SetChrSubChip(0xF8, 2)
    SetChrSubChip(0xF9, 0)
    Jump("loc_198E")

    label("loc_1960")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_197F")
    SetChrSubChip(0x101, 0)
    SetChrSubChip(0xF7, 1)
    SetChrSubChip(0xF9, 2)
    Jump("loc_198E")

    label("loc_197F")

    SetChrSubChip(0x101, 1)
    SetChrSubChip(0xF7, 0)
    SetChrSubChip(0xF8, 2)

    label("loc_198E")

    Jump("loc_1A2D")

    label("loc_1991")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1A2D")

    ChrTalk(    #78
        0x109,
        (
            "#1060F……好啦，事情搞清楚了。\x02\x03",

            "看来这确实\x01",
            "有调查的价值呀。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_GET_RESULT, 0x8), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_19FF")
    SetChrSubChip(0x101, 1)
    SetChrSubChip(0xF8, 2)
    SetChrSubChip(0xF9, 0)
    Jump("loc_1A2D")

    label("loc_19FF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x8), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1A1E")
    SetChrSubChip(0x101, 0)
    SetChrSubChip(0xF7, 1)
    SetChrSubChip(0xF9, 2)
    Jump("loc_1A2D")

    label("loc_1A1E")

    SetChrSubChip(0x101, 1)
    SetChrSubChip(0xF7, 0)
    SetChrSubChip(0xF8, 2)

    label("loc_1A2D")


    ChrTalk(    #79
        0x101,
        (
            "#1015F不过，\x01",
            "线索实在少了点呢……\x02\x03",

            "现在所知道的\x01",
            "只有她的姓名和年龄哦？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0xFE,
        (
            "那……这样的话\x01",
            "请收下这张照片。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 2)
    Sleep(50)
    SetChrSubChip(0xF7, 1)
    Sleep(50)
    SetChrSubChip(0xF9, 2)
    SetChrSubChip(0xF8, 1)

    ChrTalk(    #81
        0x101,
        "#1011F照片里……是蕾妮？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0xFE,
        "嗯，就是她……\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_AD(0x240092, 0x0, 0x0, 0x1F4)
    Sleep(1000)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1B4B")
    SetMessageWindowPos(50, 50, -1, -1)
    SetChrName("提妲")

    AnonymousTalk(    #83
        "#560F哇，真可爱的女孩子……\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    Jump("loc_1CC9")

    label("loc_1B4B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1B90")
    SetMessageWindowPos(50, 50, -1, -1)
    SetChrName("科洛丝")

    AnonymousTalk(    #84
        "#048F呵呵，是个可爱的女孩子。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    Jump("loc_1CC9")

    label("loc_1B90")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1BD3")
    SetMessageWindowPos(50, 50, -1, -1)
    SetChrName("雪拉扎德")

    AnonymousTalk(    #85
        "#526F啊，不是可爱的女孩。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    Jump("loc_1CC9")

    label("loc_1BD3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1C96")
    SetMessageWindowPos(50, 50, -1, -1)
    SetChrName("奥利维尔")

    AnonymousTalk(    #86
        (
            "#033F嗯，相当有潜力啊。\x02\x03",

            "#037F呼呼呼……\x01",
            "现在的样子真值得期待。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(50, 340, -1, -1)
    SetChrName("艾丝蒂尔")

    AnonymousTalk(    #87
        (
            "#1019F你，你的感想\x01",
            "怎么就这么直白啊。\x02\x03",

            "#1000F不过，真的很可爱呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Jump("loc_1CC9")

    label("loc_1C96")

    SetMessageWindowPos(50, 50, -1, -1)
    SetChrName("艾丝蒂尔")

    AnonymousTalk(    #88
        "#1018F真是个可爱的女孩子㈱\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_1CC9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1D23")
    SetMessageWindowPos(360, 340, -1, -1)
    SetChrName("凯文神父")

    AnonymousTalk(    #89
        (
            "#1062F啊哈哈，真的吗。\x02\x03",

            "大概１０岁左右的样子吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Jump("loc_1E6A")

    label("loc_1D23")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1D70")
    SetMessageWindowPos(360, 340, -1, -1)
    SetChrName("金")

    AnonymousTalk(    #90
        (
            "#070F哈哈，没有错。\x02\x03",

            "１０岁左右的样子吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Jump("loc_1E6A")

    label("loc_1D70")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1DC1")
    SetMessageWindowPos(360, 340, -1, -1)
    SetChrName("阿加特")

    AnonymousTalk(    #91
        (
            "#051F啊啊，看来没错。\x02\x03",

            "大概１０岁左右吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Jump("loc_1E6A")

    label("loc_1DC1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1E1C")
    SetMessageWindowPos(360, 340, -1, -1)
    SetChrName("奥利维尔")

    AnonymousTalk(    #92
        (
            "#037F是呀，我也有同感。\x02\x03",

            "唔，１０岁左右的样子吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Jump("loc_1E6A")

    label("loc_1E1C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1E6A")
    SetMessageWindowPos(360, 50, -1, -1)
    SetChrName("雪拉扎德")

    ChrTalk(    #93
        0x103,
        (
            "#021F呵呵，真的是……\x02\x03",

            "１０岁左右吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_1E6A")

    SetMessageWindowPos(50, 340, -1, -1)
    SetChrName("科尔娜")

    AnonymousTalk(    #94
        "正好１０岁呀。\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(50, 340, -1, -1)
    SetChrName("科尔娜")

    AnonymousTalk(    #95
        (
            "过生日的时候\x01",
            "拍摄的。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_AE(0x1F4)
    FadeToBright(300, 0)

    ChrTalk(    #96
        0x101,
        "#1026F…………………………\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1F51")
    Jc((scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1F13")
    SetChrSubChip(0x107, 1)
    Jump("loc_1F2D")

    label("loc_1F13")

    Jc((scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1F28")
    SetChrSubChip(0x107, 0)
    Jump("loc_1F2D")

    label("loc_1F28")

    SetChrSubChip(0x107, 2)

    label("loc_1F2D")


    ChrTalk(    #97
        0x107,
        (
            "#064F？？？\x02\x03",

            "姐姐，怎么了？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_20EC")

    label("loc_1F51")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1FB3")
    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1F74")
    SetChrSubChip(0x105, 1)
    Jump("loc_1F8E")

    label("loc_1F74")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1F89")
    SetChrSubChip(0x105, 0)
    Jump("loc_1F8E")

    label("loc_1F89")

    SetChrSubChip(0x105, 2)

    label("loc_1F8E")


    ChrTalk(    #98
        0x105,
        (
            "#043F艾丝蒂尔，\x01",
            "有什么事吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_20EC")

    label("loc_1FB3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_201E")
    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1FD6")
    SetChrSubChip(0x104, 1)
    Jump("loc_1FF0")

    label("loc_1FD6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1FEB")
    SetChrSubChip(0x104, 0)
    Jump("loc_1FF0")

    label("loc_1FEB")

    SetChrSubChip(0x104, 2)

    label("loc_1FF0")


    ChrTalk(    #99
        0x104,
        (
            "#033F哎呀，艾丝蒂尔。\x02\x03",

            "出什么事了吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_20EC")

    label("loc_201E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2085")
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2041")
    SetChrSubChip(0x103, 1)
    Jump("loc_205B")

    label("loc_2041")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2056")
    SetChrSubChip(0x103, 0)
    Jump("loc_205B")

    label("loc_2056")

    SetChrSubChip(0x103, 2)

    label("loc_205B")


    ChrTalk(    #100
        0x103,
        (
            "#023F嗯……？\x02\x03",

            "艾丝蒂尔，怎么了？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_20EC")

    label("loc_2085")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_20EC")
    Jc((scpexpr(EXPR_GET_RESULT, 0x8), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_20A8")
    SetChrSubChip(0x109, 1)
    Jump("loc_20C2")

    label("loc_20A8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x8), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_20BD")
    SetChrSubChip(0x109, 0)
    Jump("loc_20C2")

    label("loc_20BD")

    SetChrSubChip(0x109, 2)

    label("loc_20C2")


    ChrTalk(    #101
        0x109,
        (
            "#1063F…………？\x02\x03",

            "艾丝蒂尔，怎么了？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_20EC")

    SetChrSubChip(0xF7, 1)
    SetChrSubChip(0xF8, 0)
    SetChrSubChip(0xF9, 2)
    SetChrSubChip(0x101, 0)

    ChrTalk(    #102
        0x101,
        (
            "#1025F唔，嗯……\x01",
            "稍微有点难过。\x02\x03",

            "一想到这孩子\x01",
            "在那场战争中遭遇那么痛苦的事。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_228C")
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2175")
    SetChrSubChip(0x106, 1)
    Jump("loc_218F")

    label("loc_2175")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_218A")
    SetChrSubChip(0x106, 0)
    Jump("loc_218F")

    label("loc_218A")

    SetChrSubChip(0x106, 2)

    label("loc_218F")


    ChrTalk(    #103
        0x106,
        (
            "#552F啊啊，真不知该说些什么。\x02\x03",

            "#053F……想办法\x01",
            "让她与家人重逢吧。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_21EB")
    SetChrSubChip(0x101, 1)
    Jump("loc_2205")

    label("loc_21EB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2200")
    SetChrSubChip(0x101, 0)
    Jump("loc_2205")

    label("loc_2200")

    SetChrSubChip(0x101, 1)

    label("loc_2205")


    ChrTalk(    #104
        0x101,
        (
            "#1025F啊……\x02\x03",

            "#1006F嗯、嗯！\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 2)
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2241")
    SetChrSubChip(0x106, 1)
    Jump("loc_225B")

    label("loc_2241")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2256")
    SetChrSubChip(0x106, 1)
    Jump("loc_225B")

    label("loc_2256")

    SetChrSubChip(0x106, 2)

    label("loc_225B")


    ChrTalk(    #105
        0x106,
        (
            "#051F那么，这张照片，\x01",
            "就暂借我们一下吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_27E2")

    label("loc_228C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_23CA")
    Jc((scpexpr(EXPR_GET_RESULT, 0x7), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_22AF")
    SetChrSubChip(0x108, 1)
    Jump("loc_22C9")

    label("loc_22AF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x7), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_22C4")
    SetChrSubChip(0x108, 0)
    Jump("loc_22C9")

    label("loc_22C4")

    SetChrSubChip(0x108, 2)

    label("loc_22C9")


    ChrTalk(    #106
        0x108,
        (
            "#074F啊啊，真不知该说什么了。\x02\x03",

            "#070F……努力想办法\x01",
            "让她与家人重逢吧。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_GET_RESULT, 0x7), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2329")
    SetChrSubChip(0x101, 1)
    Jump("loc_2343")

    label("loc_2329")

    Jc((scpexpr(EXPR_GET_RESULT, 0x7), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_233E")
    SetChrSubChip(0x101, 0)
    Jump("loc_2343")

    label("loc_233E")

    SetChrSubChip(0x101, 1)

    label("loc_2343")


    ChrTalk(    #107
        0x101,
        (
            "#1011F啊……\x02\x03",

            "#1006F嗯、嗯！\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 2)
    Jc((scpexpr(EXPR_GET_RESULT, 0x7), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_237F")
    SetChrSubChip(0x108, 1)
    Jump("loc_2399")

    label("loc_237F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x7), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2394")
    SetChrSubChip(0x108, 1)
    Jump("loc_2399")

    label("loc_2394")

    SetChrSubChip(0x108, 2)

    label("loc_2399")


    ChrTalk(    #108
        0x108,
        (
            "#070F那么，这张照片，\x01",
            "就暂借我们一下吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_27E2")

    label("loc_23CA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_250E")
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_23ED")
    SetChrSubChip(0x103, 1)
    Jump("loc_2407")

    label("loc_23ED")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2402")
    SetChrSubChip(0x103, 0)
    Jump("loc_2407")

    label("loc_2402")

    SetChrSubChip(0x103, 2)

    label("loc_2407")


    ChrTalk(    #109
        0x103,
        (
            "#522F嗯，真不知该说什么好。\x02\x03",

            "#020F……想办法用我们的力量\x01",
            "让她与家人重逢吧。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_246D")
    SetChrSubChip(0x101, 1)
    Jump("loc_2487")

    label("loc_246D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2482")
    SetChrSubChip(0x101, 0)
    Jump("loc_2487")

    label("loc_2482")

    SetChrSubChip(0x101, 1)

    label("loc_2487")


    ChrTalk(    #110
        0x101,
        (
            "#1011F啊……\x02\x03",

            "#1006F嗯、嗯！\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 2)
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_24C3")
    SetChrSubChip(0x103, 1)
    Jump("loc_24DD")

    label("loc_24C3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_24D8")
    SetChrSubChip(0x103, 1)
    Jump("loc_24DD")

    label("loc_24D8")

    SetChrSubChip(0x103, 2)

    label("loc_24DD")


    ChrTalk(    #111
        0x103,
        (
            "#020F那么，这张照片，\x01",
            "就暂时借给我们吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_27E2")

    label("loc_250E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_266F")
    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2531")
    SetChrSubChip(0x104, 1)
    Jump("loc_254B")

    label("loc_2531")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2546")
    SetChrSubChip(0x104, 0)
    Jump("loc_254B")

    label("loc_2546")

    SetChrSubChip(0x104, 2)

    label("loc_254B")


    ChrTalk(    #112
        0x104,
        (
            "#035F唔，真不知该说什么。\x02\x03",

            "虽然身为帝国人的我\x01",
            "也没资格说什么……\x02\x03",

            "#030F……还是想办法\x01",
            "让她与家人重逢吧。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_25CE")
    SetChrSubChip(0x101, 1)
    Jump("loc_25E8")

    label("loc_25CE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_25E3")
    SetChrSubChip(0x101, 0)
    Jump("loc_25E8")

    label("loc_25E3")

    SetChrSubChip(0x101, 1)

    label("loc_25E8")


    ChrTalk(    #113
        0x101,
        (
            "#1011F啊……\x02\x03",

            "#1006F嗯、嗯！\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 2)
    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2624")
    SetChrSubChip(0x104, 1)
    Jump("loc_263E")

    label("loc_2624")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2639")
    SetChrSubChip(0x104, 1)
    Jump("loc_263E")

    label("loc_2639")

    SetChrSubChip(0x104, 2)

    label("loc_263E")


    ChrTalk(    #114
        0x104,
        (
            "#030F那么，这张照片，\x01",
            "就暂时借给我们啦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_27E2")

    label("loc_266F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_27E2")
    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2692")
    SetChrSubChip(0x105, 1)
    Jump("loc_26AC")

    label("loc_2692")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_26A7")
    SetChrSubChip(0x105, 0)
    Jump("loc_26AC")

    label("loc_26A7")

    SetChrSubChip(0x105, 2)

    label("loc_26AC")


    ChrTalk(    #115
        0x105,
        (
            "#049F嗯，真不知该说什么好。\x02\x03",

            "#047F但是，接到这样的委托\x01",
            "一定也是女神的指引……\x02\x03",

            "#040F……想办法尽我们的力量\x01",
            "让她与家人重逢吧。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2744")
    SetChrSubChip(0x101, 1)
    Jump("loc_275E")

    label("loc_2744")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2759")
    SetChrSubChip(0x101, 0)
    Jump("loc_275E")

    label("loc_2759")

    SetChrSubChip(0x101, 1)

    label("loc_275E")


    ChrTalk(    #116
        0x101,
        (
            "#1011F啊……\x02\x03",

            "#1006F嗯、嗯！\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 2)
    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_279A")
    SetChrSubChip(0x105, 1)
    Jump("loc_27B4")

    label("loc_279A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_27AF")
    SetChrSubChip(0x105, 1)
    Jump("loc_27B4")

    label("loc_27AF")

    SetChrSubChip(0x105, 2)

    label("loc_27B4")


    ChrTalk(    #117
        0x105,
        (
            "#040F那么，就暂时\x01",
            "把这张照片借给我们吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_27E2")


    ChrTalk(    #118
        0xFE,
        "好的，请带上。\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #119
        "\x07\x00得到了\x1F\x81\x03\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x381, 1)
    SetChrSubChip(0x101, 0)

    ChrTalk(    #120
        0x101,
        (
            "#1015F好了，这样\x01",
            "总算是把事情弄清楚了……\x02\x03",

            "不过该怎样\x01",
            "开始调查呢。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_294A")
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_28AC")
    SetChrSubChip(0x103, 1)
    Jump("loc_28C6")

    label("loc_28AC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_28C1")
    SetChrSubChip(0x103, 0)
    Jump("loc_28C6")

    label("loc_28C1")

    SetChrSubChip(0x103, 2)

    label("loc_28C6")


    ChrTalk(    #121
        0x103,
        (
            "#020F也是，难得借来的，\x01",
            "就从照片这线索开始吧。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2919")
    SetChrSubChip(0x101, 1)
    SetChrSubChip(0xF8, 2)
    SetChrSubChip(0xF9, 0)
    Jump("loc_2947")

    label("loc_2919")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2938")
    SetChrSubChip(0x101, 0)
    SetChrSubChip(0xF7, 1)
    SetChrSubChip(0xF9, 2)
    Jump("loc_2947")

    label("loc_2938")

    SetChrSubChip(0x101, 1)
    SetChrSubChip(0xF7, 0)
    SetChrSubChip(0xF8, 2)

    label("loc_2947")

    Jump("loc_2C6A")

    label("loc_294A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2A0D")
    Jc((scpexpr(EXPR_GET_RESULT, 0x7), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_296D")
    SetChrSubChip(0x108, 1)
    Jump("loc_2987")

    label("loc_296D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x7), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2982")
    SetChrSubChip(0x108, 0)
    Jump("loc_2987")

    label("loc_2982")

    SetChrSubChip(0x108, 2)

    label("loc_2987")


    ChrTalk(    #122
        0x108,
        (
            "#070F呼，难得借来的。\x02\x03",

            "就有效地使用\x01",
            "那张照片吧。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_GET_RESULT, 0x7), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_29DC")
    SetChrSubChip(0x101, 1)
    SetChrSubChip(0xF8, 2)
    SetChrSubChip(0xF9, 0)
    Jump("loc_2A0A")

    label("loc_29DC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x7), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_29FB")
    SetChrSubChip(0x101, 0)
    SetChrSubChip(0xF7, 1)
    SetChrSubChip(0xF9, 2)
    Jump("loc_2A0A")

    label("loc_29FB")

    SetChrSubChip(0x101, 1)
    SetChrSubChip(0xF7, 0)
    SetChrSubChip(0xF8, 2)

    label("loc_2A0A")

    Jump("loc_2C6A")

    label("loc_2A0D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2AC6")
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2A30")
    SetChrSubChip(0x106, 1)
    Jump("loc_2A4A")

    label("loc_2A30")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2A45")
    SetChrSubChip(0x106, 0)
    Jump("loc_2A4A")

    label("loc_2A45")

    SetChrSubChip(0x106, 2)

    label("loc_2A4A")


    ChrTalk(    #123
        0x106,
        (
            "#050F说得也是，\x01",
            "就从照片这线索开始吧。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2A95")
    SetChrSubChip(0x101, 1)
    SetChrSubChip(0xF8, 2)
    SetChrSubChip(0xF9, 0)
    Jump("loc_2AC3")

    label("loc_2A95")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2AB4")
    SetChrSubChip(0x101, 0)
    SetChrSubChip(0xF7, 1)
    SetChrSubChip(0xF9, 2)
    Jump("loc_2AC3")

    label("loc_2AB4")

    SetChrSubChip(0x101, 1)
    SetChrSubChip(0xF7, 0)
    SetChrSubChip(0xF8, 2)

    label("loc_2AC3")

    Jump("loc_2C6A")

    label("loc_2AC6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2B93")
    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2AE9")
    SetChrSubChip(0x104, 1)
    Jump("loc_2B03")

    label("loc_2AE9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2AFE")
    SetChrSubChip(0x104, 0)
    Jump("loc_2B03")

    label("loc_2AFE")

    SetChrSubChip(0x104, 2)

    label("loc_2B03")


    ChrTalk(    #124
        0x104,
        (
            "#030F呼呼，说得也是。\x02\x03",

            "难得借来的，\x01",
            "就从照片这线索开始吧。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2B62")
    SetChrSubChip(0x101, 1)
    SetChrSubChip(0xF8, 2)
    SetChrSubChip(0xF9, 0)
    Jump("loc_2B90")

    label("loc_2B62")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2B81")
    SetChrSubChip(0x101, 0)
    SetChrSubChip(0xF7, 1)
    SetChrSubChip(0xF9, 2)
    Jump("loc_2B90")

    label("loc_2B81")

    SetChrSubChip(0x101, 1)
    SetChrSubChip(0xF7, 0)
    SetChrSubChip(0xF8, 2)

    label("loc_2B90")

    Jump("loc_2C6A")

    label("loc_2B93")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2C6A")
    Jc((scpexpr(EXPR_GET_RESULT, 0x8), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2BB6")
    SetChrSubChip(0x109, 1)
    Jump("loc_2BD0")

    label("loc_2BB6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x8), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2BCB")
    SetChrSubChip(0x109, 0)
    Jump("loc_2BD0")

    label("loc_2BCB")

    SetChrSubChip(0x109, 2)

    label("loc_2BD0")


    ChrTalk(    #125
        0x109,
        (
            "#1067F呼……也是呀……\x02\x03",

            "#1062F难得借来了，\x01",
            "就从照片这线索开始吧，怎样。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_GET_RESULT, 0x8), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2C3C")
    SetChrSubChip(0x101, 1)
    SetChrSubChip(0xF8, 2)
    SetChrSubChip(0xF9, 0)
    Jump("loc_2C6A")

    label("loc_2C3C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x8), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2C5B")
    SetChrSubChip(0x101, 0)
    SetChrSubChip(0xF7, 1)
    SetChrSubChip(0xF9, 2)
    Jump("loc_2C6A")

    label("loc_2C5B")

    SetChrSubChip(0x101, 1)
    SetChrSubChip(0xF7, 0)
    SetChrSubChip(0xF8, 2)

    label("loc_2C6A")


    ChrTalk(    #126
        0x101,
        "#1004F啊，用照片？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2CE6")

    ChrTalk(    #127
        0x103,
        (
            "#020F嗯，总之先\x01",
            "拿那个给城里的人看看。\x02\x03",

            "看到照片上的人\x01",
            "说不定会有人想起什么。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E86")

    label("loc_2CE6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2D4C")

    ChrTalk(    #128
        0x108,
        (
            "#070F啊啊，总之先拿那个\x01",
            "给城里的人看看吧。\x02\x03",

            "看到女孩的脸\x01",
            "或许有人能想起什么吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E86")

    label("loc_2D4C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2DB6")

    ChrTalk(    #129
        0x106,
        (
            "#050F啊啊，总之先拿这个\x01",
            "给城里的人看看吧。\x02\x03",

            "看到那女孩的脸，\x01",
            "应该会有人想起什么的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E86")

    label("loc_2DB6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2E1E")

    ChrTalk(    #130
        0x104,
        (
            "#030F啊啊，总之拿照片\x01",
            "给城里的人看看吧。\x02\x03",

            "看到那女孩的脸，\x01",
            "应该会有人想起什么的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E86")

    label("loc_2E1E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2E86")

    ChrTalk(    #131
        0x109,
        (
            "#1060F对对，总之拿照片\x01",
            "给城里的人看看吧。\x02\x03",

            "看到那小姑娘的脸，\x01",
            "我想会有人能想起点啥。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2E86")


    ChrTalk(    #132
        0x101,
        (
            "#1006F是吗，虽说是快\x01",
            "１０年前的事了。\x02\x03",

            "那么，就先用这个方法\x01",
            "试着开始调查吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #133
        0xFE,
        "那就麻烦你们了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #134
        0xFE,
        (
            "如果发现了什么，\x01",
            "请再来找我吧。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 2)
    SetChrSubChip(0xF7, 1)
    Sleep(40)
    SetChrSubChip(0xF9, 2)
    SetChrSubChip(0xF8, 1)

    ChrTalk(    #135
        0x101,
        "#1000F嗯，知道了。\x02",
    )

    CloseMessageWindow()
    OP_28(0x79, 0x4, 0x8)
    OP_28(0x79, 0x4, 0x4)
    OP_28(0x79, 0x1, 0x1)
    OP_28(0x79, 0x1, 0x2)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrChipByIndex(0x20, 20)
    SetChrChipByIndex(0x101, 65535)
    SetChrChipByIndex(0xF7, 65535)
    SetChrChipByIndex(0xF8, 65535)
    SetChrChipByIndex(0xF9, 65535)
    ClearChrFlags(0x20, 0x4)
    ClearChrFlags(0x101, 0x4)
    ClearChrFlags(0xF7, 0x4)
    ClearChrFlags(0xF8, 0x4)
    ClearChrFlags(0xF9, 0x4)
    SetChrPos(0x20, 2400, 0, 1370, 0)
    OP_4B(0x20, 255)
    SetChrPos(0x101, 360, 0, -2430, 180)
    SetChrPos(0xF7, 360, 0, -2430, 180)
    SetChrPos(0xF8, 360, 0, -2430, 180)
    SetChrPos(0xF9, 360, 0, -2430, 180)
    OP_69(0x101, 0x0)
    OP_30(0x0)
    OP_8C(0x101, 180, 0)
    OP_8C(0xF7, 180, 0)
    OP_8C(0xF8, 180, 0)
    OP_8C(0xF9, 180, 0)
    OP_4A(0x0, 255)
    OP_4A(0x1, 255)
    OP_4A(0x2, 255)
    OP_4A(0x3, 255)
    ClearChrFlags(0x38, 0x80)
    FadeToBright(1000, 0)
    OP_0D()
    Return()

    # Function_5_986 end

    def Function_6_3035(): pass

    label("Function_6_3035")

    EventBegin(0x0)
    ClearChrFlags(0x27, 0x80)
    ClearChrFlags(0x26, 0x80)
    SetChrPos(0x20, -230, 0, -650, 180)
    SetChrPos(0x27, -230, 0, -1730, 0)
    SetChrPos(0x26, -1280, 0, -2300, 0)
    OP_4A(0x20, 255)
    SetChrPos(0x101, 1710, 0, 0, 270)
    SetChrPos(0xF7, 2009, 0, -1460, 270)
    SetChrPos(0xF8, 2210, 0, -3180, 315)
    SetChrPos(0xF9, 2600, 0, -230, 270)
    SetChrFlags(0x1C, 0x80)
    SetChrFlags(0x38, 0x80)
    OP_4A(0x1B, 255)
    OP_6D(-1220, 0, -240, 0)
    OP_67(0, 4240, -10000, 0)
    OP_6B(2680, 0)
    OP_6C(315000, 0)
    OP_6E(280, 0)
    OP_0D()

    ChrTalk(    #136
        0x20,
        "#2P──是这样吗。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #137
        0x20,
        (
            "#2P没想到，竟然\x01",
            "会发生这种事……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #138
        0x20,
        (
            "#2P蕾妮……\x01",
            "以前真是对不起了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #139
        0x20,
        (
            "#2P真该早点……\x01",
            "找到你才对的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #140
        0x27,
        (
            "#621F#1P哪里的话，婶婶……\x01",
            "请别向我道歉。\x02\x03",

            "一切都是时代的错……\x01",
            "不是任何人的罪过。\x02\x03",

            "而且，这１０年间……\x02\x03",

            "我真的很幸福。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x20, 0x26, 400)

    ChrTalk(    #141
        0x20,
        (
            "#2P梅贝尔小姐……\x01",
            "请让我再次道谢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #142
        0x20,
        (
            "#2P您和令尊\x01",
            "真的是我们的恩人。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x26, 0x20, 400)

    ChrTalk(    #143
        0x26,
        (
            "#1P#610F哪里，别这么说……\x02\x03",

            "必须说谢谢的\x01",
            "其实是我们才对。\x02\x03",

            "莉拉的存在对我来说\x01",
            "是多大的鼓励啊……\x02\x03",

            "#615F#1P咳咳……\x01",
            "抱歉，应该称呼为蕾妮小姐吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #144
        0x20,
        (
            "#2P不用，还是和平常一样\x01",
            "称呼她为莉拉就可以了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #145
        0x20,
        (
            "#2P因为那是你一直\x01",
            "称呼她的名字。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x20, 0x27, 400)

    ChrTalk(    #146
        0x20,
        (
            "#2P不过，真是太好了……\x01",
            "这孩子能够一直这么幸福地生活着，太好了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #147
        0x20,
        "#2P梅贝尔小姐……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #148
        0x20,
        (
            "#2P从今以后，\x01",
            "也请你们多多关照她了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #149
        0x26,
        (
            "#613F#1P嗯、嗯……\x01",
            "这是当然的……\x02\x03",

            "不过，您不打算\x01",
            "把莉拉带回去吗？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x20, 0x26, 400)

    ChrTalk(    #150
        0x20,
        (
            "#2P是，其实一开始\x01",
            "是这个打算的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #151
        0x20,
        (
            "#2P但看到这孩子现在的样子，\x01",
            "我便打消了这个念头。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #152
        0x20,
        "#2P让她就这样继续生活下去……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #153
        0x20,
        (
            "#2P对这孩子来说，\x01",
            "这才是最幸福的事。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #154
        0x27,
        "#625F#1P婶婶……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x20, 0x27, 400)

    ChrTalk(    #155
        0x20,
        "#2P呵呵，别这副表情嘛。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #156
        0x20,
        (
            "#2P当然，偶尔\x01",
            "也要来看看我哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #157
        0x20,
        (
            "#2P因为我不能\x01",
            "经常来看你……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #158
        0x26,
        "#610F#1P哎呀，为什么呢？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x20, 0x26, 400)

    ChrTalk(    #159
        0x20,
        (
            "#2P还没和您提过，\x01",
            "其实我们的故乡在很远的地方。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #160
        0x20,
        (
            "#2P列曼自治州，这个地方\x01",
            "大家知道吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #161
        0x101,
        (
            "#1004F#2P咦？\x01",
            "列曼自治州！？\x02\x03",

            "这不就是协会\x01",
            "那个训练场的所在地嘛。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3676")

    ChrTalk(    #162
        0x106,
        "#051F还真有这么有趣的巧合啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_3743")

    label("loc_3676")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_36AA")

    ChrTalk(    #163
        0x103,
        "#020F还真有这么有趣的巧合呢。\x02",
    )

    CloseMessageWindow()
    Jump("loc_3743")

    label("loc_36AA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_36DE")

    ChrTalk(    #164
        0x108,
        "#070F还真有这么有趣的巧合啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_3743")

    label("loc_36DE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3712")

    ChrTalk(    #165
        0x104,
        "#030F还真有这么有趣的巧合啊～\x02",
    )

    CloseMessageWindow()
    Jump("loc_3743")

    label("loc_3712")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3743")

    ChrTalk(    #166
        0x105,
        "#040F还真有这么有趣的巧合呢。\x02",
    )

    CloseMessageWindow()

    label("loc_3743")


    ChrTalk(    #167
        0x101,
        (
            "#1015F#2P这样啊，莉拉\x01",
            "原来是外国人啊……\x02\x03",

            "（这么一说确实\x01",
            "感觉很独特……）\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x20, 0x27, 400)

    ChrTalk(    #168
        0x20,
        (
            "#2P虽说有飞船通航，\x01",
            "不过往返还是挺麻烦的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #169
        0x20,
        (
            "#2P虽然希望你\x01",
            "有机会时常来看我……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #170
        0x20,
        (
            "#2P在那之前，\x01",
            "就写信联络吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #171
        0x27,
        (
            "#621F#1P好的，那么……\x02\x03",

            "有假期的话，\x01",
            "我一定前去看您。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #172
        0x20,
        (
            "#2P嗯，我会好好等着\x01",
            "那天的到来的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #173
        0x20,
        "#2P好了，蕾妮……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #174
        0x20,
        (
            "#2P最后让我再好好\x01",
            "看一看你的脸吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_94(0x1, 0x20, 0x0, 0xC8, 0x3E8, 0x0)
    Sleep(1000)

    ChrTalk(    #175
        0x20,
        (
            "#2P真的，和姐姐\x01",
            "长得一模一样……\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x27, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #176
        0x27,
        "#622F#1P和妈妈……！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #177
        0x20,
        "#2P嗯嗯……简直是一个模子里刻出来的。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #178
        0x20,
        (
            "#2P你和你那\x01",
            "红颜薄命的妈妈……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #179
        0x27,
        "#623F#1P…………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #180
        0x20,
        (
            "#2P她一定一直\x01",
            "守护着你。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #181
        0x20,
        (
            "#2P你能够遇到这么好的人家，\x01",
            "一定也是多亏她的保佑。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #182
        0x20,
        (
            "#2P为了你的母亲，你也一定要……\x01",
            "幸福地活下去哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #183
        0x27,
        (
            "#626F#1P是，婶婶……\x02\x03",

            "……我答应您。\x02",
        )
    )

    CloseMessageWindow()
    OP_3F(0x381, 1)
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(1500)
    OP_3F(0x381, 1)
    OP_3E(0x41B, 1)
    OP_22(0x17, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #184
        "\x07\x02任务【遥远的记忆】\x07\x00完成了！\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_28(0x79, 0x4, 0x10)
    OP_28(0x79, 0x1, 0x40)
    ClearMapFlags(0x2000000)
    OP_A2(0x10F2)
    NewScene("ED6_DT21/T1101   ._SN", 111, 0, 0)
    IdleLoop()
    Return()

    # Function_6_3035 end

    def Function_7_3AC7(): pass

    label("Function_7_3AC7")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CD(0x13)"), scpexpr(EXPR_END)), "loc_3AD7")
    OP_A2(0xF)
    Jump("loc_3AE2")

    label("loc_3AD7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CD(0x14)"), scpexpr(EXPR_END)), "loc_3AE2")
    OP_A3(0xF)

    label("loc_3AE2")

    ClearChrFlags(0x13, 0x10)
    ClearChrFlags(0x14, 0x10)
    OP_4A(0x13, 255)
    OP_4A(0x14, 255)
    Fade(1000)
    SetChrPos(0x106, -45770, 0, -2880, 270)
    SetChrPos(0x101, -45760, 0, -1750, 270)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3B4D")
    SetChrPos(0x105, -44380, 0, -1770, 270)
    SetChrPos(0xF9, -44510, 0, -2770, 270)
    Jump("loc_3BA1")

    label("loc_3B4D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3B7F")
    SetChrPos(0x105, -44380, 0, -1770, 270)
    SetChrPos(0xF8, -44510, 0, -2770, 270)
    Jump("loc_3BA1")

    label("loc_3B7F")

    SetChrPos(0xF8, -44380, 0, -1770, 270)
    SetChrPos(0xF9, -44510, 0, -2770, 270)

    label("loc_3BA1")

    SetChrFlags(0xC, 0x80)
    OP_6D(-46730, 0, -2460, 0)
    OP_67(0, 6760, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_END)), "loc_3C97")

    ChrTalk(    #185
        0x13,
        (
            "请你想办法\x01",
            "再拖延点时间吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #186
        0x13,
        (
            "我们已经\x01",
            "安排人去找了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #187
        0x101,
        "#1011F请问～打扰一下行吗？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x13, 0x101, 400)
    TurnDirection(0x14, 0x101, 400)

    ChrTalk(    #188
        0x13,
        "……什么事？\x02",
    )

    CloseMessageWindow()
    OP_62(0x13, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(    #189
        0x13,
        "哎呀，你是……\x02",
    )

    CloseMessageWindow()
    Jump("loc_3D79")

    label("loc_3C97")


    ChrTalk(    #190
        0x14,
        (
            "没找到小姐\x01",
            "说什么都没用。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #191
        0x14,
        "必须尽快想办法……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #192
        0x101,
        "#1011F请问～打扰一下行吗？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x14, 0x101, 400)

    ChrTalk(    #193
        0x14,
        (
            "是？\x01",
            "有什么事情呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #194
        0x101,
        (
            "#1000F嗯，打扰你们说话了。\x02\x03",

            "我们是\x01",
            "游击士协会的人。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x13, 0x101, 400)
    OP_62(0x13, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(    #195
        0x13,
        "哎呀，你是……\x02",
    )

    CloseMessageWindow()

    label("loc_3D79")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x34A, 4)), scpexpr(EXPR_END)), "loc_3E7D")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3E15")
    TurnDirection(0x101, 0x13, 400)

    ChrTalk(    #196
        0x101,
        "#1001F你好，好久不见了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #197
        0x105,
        "#040F你好，蕾娜。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x13, 0x105, 400)

    ChrTalk(    #198
        0x13,
        "啊，连科洛丝都来了……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #199
        0x101,
        (
            "#1011F那，为什么\x01",
            "蕾娜会在这里？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3E7A")

    label("loc_3E15")

    TurnDirection(0x101, 0x13, 400)

    ChrTalk(    #200
        0x101,
        (
            "#1001F嘿嘿，好久不见了。\x01",
            "王立学院见过以后就没见过面了。\x02\x03",

            "#1011F那，为什么\x01",
            "蕾娜会在这里？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3E7A")

    Jump("loc_3FC5")

    label("loc_3E7D")

    TurnDirection(0x101, 0x13, 400)

    ChrTalk(    #201
        0x101,
        (
            "#1004F咦咦！？\x02\x03",

            "你不是蕾娜……吗。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3F3D")

    ChrTalk(    #202
        0x105,
        (
            "#040F嗯，调查学院时\x01",
            "我们见过面。\x02\x03",

            "好久不见，蕾娜\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x13, 0x105, 400)

    ChrTalk(    #203
        0x13,
        "啊，连科洛丝都来了……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #204
        0x101,
        (
            "#1011F那个，为什么\x01",
            "会在这种地方？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3FC5")

    label("loc_3F3D")

    TurnDirection(0x106, 0x101, 400)

    ChrTalk(    #205
        0x106,
        "#052F……熟人吗？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x106, 400)

    ChrTalk(    #206
        0x101,
        (
            "#1000F嗯、嗯……\x01",
            "是王立学院的学生。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3F91():
        TurnDirection(0x106, 0x13, 400)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_3F91)
    TurnDirection(0x101, 0x13, 400)

    ChrTalk(    #207
        0x101,
        (
            "#1011F但是，怎么会\x01",
            "在这种地方？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3FC5")

    TurnDirection(0x13, 0x101, 400)

    ChrTalk(    #208
        0x13,
        (
            "嗯，其实\x01",
            "是有些原因……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #209
        0x13,
        (
            "各位是看了公告板\x01",
            "才来这里的吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #210
        0x101,
        "#1000F是这样，怎么？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #211
        0x13,
        (
            "我有件事\x01",
            "想尽快委托各位处理。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #212
        0x13,
        "……你们能接受吗？\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "【是】\x01",      # 0
            "【否】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_40D7")

    ChrTalk(    #213
        0x101,
        "#1006F嗯，交给我们吧。\x02",
    )

    CloseMessageWindow()
    Call(1, 9)
    Jump("loc_41B3")

    label("loc_40D7")


    ChrTalk(    #214
        0x101,
        (
            "#1007F抱歉。\x01",
            "现在有点困难。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #215
        0x13,
        (
            "这样啊……\x01",
            "那可真伤脑筋。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #216
        0x13,
        (
            "其他的事\x01",
            "能马上办好吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #217
        0x101,
        (
            "#1015F不太清楚呢……\x02\x03",

            "#1000F不过有空了\x01",
            "就马上回来吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #218
        0x13,
        "嗯嗯，那就拜托了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #219
        0x13,
        "那么，稍后再见……\x02",
    )

    CloseMessageWindow()
    OP_28(0x7A, 0x1, 0x8000)
    OP_8C(0x13, 180, 0)
    OP_8C(0x14, 0, 0)

    label("loc_41B3")

    OP_4B(0x13, 255)
    OP_4B(0x14, 255)
    ClearChrFlags(0xC, 0x80)
    OP_A2(0x1A55)
    EventEnd(0x0)
    Return()

    # Function_7_3AC7 end

    def Function_8_41C6(): pass

    label("Function_8_41C6")

    EventBegin(0x0)
    OP_4A(0x13, 255)
    OP_4A(0x14, 255)
    ClearChrFlags(0x13, 0x10)
    ClearChrFlags(0x14, 0x10)
    Fade(1000)
    SetChrPos(0x106, -45770, 0, -2880, 270)
    SetChrPos(0x101, -45760, 0, -1750, 270)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4233")
    SetChrPos(0x105, -44380, 0, -1770, 270)
    SetChrPos(0xF9, -44510, 0, -2770, 270)
    Jump("loc_4287")

    label("loc_4233")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4265")
    SetChrPos(0x105, -44380, 0, -1770, 270)
    SetChrPos(0xF8, -44510, 0, -2770, 270)
    Jump("loc_4287")

    label("loc_4265")

    SetChrPos(0xF8, -44380, 0, -1770, 270)
    SetChrPos(0xF9, -44510, 0, -2770, 270)

    label("loc_4287")

    SetChrFlags(0xC, 0x80)
    OP_6D(-46730, 0, -2460, 0)
    OP_67(0, 6760, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    TurnDirection(0x13, 0x101, 0)
    TurnDirection(0x14, 0x101, 0)
    OP_0D()

    ChrTalk(    #220
        0x14,
        "啊，各位……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #221
        0x13,
        (
            "莫非是可以\x01",
            "接受委托了？\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "【是】\x01",      # 0
            "【否】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_437B")

    ChrTalk(    #222
        0x101,
        "#1006F嗯，交给我们吧。\x02",
    )

    CloseMessageWindow()
    Call(1, 9)
    Jump("loc_43E1")

    label("loc_437B")


    ChrTalk(    #223
        0x101,
        (
            "#1015F唔～抱歉。\x01",
            "现在还有点困难。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #224
        0x13,
        (
            "这样啊……\x02\x03",

            "那么，麻烦\x01",
            "你们稍后一定要来哦。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x13, 180, 0)
    OP_8C(0x14, 0, 0)

    label("loc_43E1")

    OP_4B(0x13, 255)
    OP_4B(0x14, 255)
    ClearChrFlags(0xC, 0x80)
    EventEnd(0x0)
    Return()

    # Function_8_41C6 end

    def Function_9_43F1(): pass

    label("Function_9_43F1")

    EventBegin(0x0)

    ChrTalk(    #225
        0x14,
        (
            "有人接受了吗。\x01",
            "唔，非常感谢……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x13, 0x14, 400)

    ChrTalk(    #226
        0x13,
        (
            "我来向各位游击士\x01",
            "说明一下情况。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #227
        0x13,
        (
            "至于和对方的应对，\x01",
            "就交给你了。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x14, 0x13, 400)

    ChrTalk(    #228
        0x14,
        "好的，那么……\x02",
    )

    CloseMessageWindow()
    OP_8C(0x14, 90, 400)

    ChrTalk(    #229
        0x14,
        (
            "小姐的事，\x01",
            "就麻烦你们了。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_44B0():

        label("loc_44B0")

        TurnDirection(0x13, 0x14, 400)
        OP_48()
        Jump("loc_44B0")

    QueueWorkItem2(0x13, 1, lambda_44B0)

    def lambda_44C1():

        label("loc_44C1")

        TurnDirection(0x101, 0x14, 400)
        OP_48()
        Jump("loc_44C1")

    QueueWorkItem2(0x101, 1, lambda_44C1)

    def lambda_44D2():

        label("loc_44D2")

        TurnDirection(0x106, 0x14, 400)
        OP_48()
        Jump("loc_44D2")

    QueueWorkItem2(0x106, 1, lambda_44D2)

    def lambda_44E3():

        label("loc_44E3")

        TurnDirection(0xF8, 0x14, 400)
        OP_48()
        Jump("loc_44E3")

    QueueWorkItem2(0xF8, 1, lambda_44E3)

    def lambda_44F4():

        label("loc_44F4")

        TurnDirection(0xF9, 0x14, 400)
        OP_48()
        Jump("loc_44F4")

    QueueWorkItem2(0xF9, 1, lambda_44F4)
    OP_43(0x14, 0x1, 0x1, 0xB)
    OP_43(0x13, 0x2, 0x1, 0xC)
    OP_6D(-43450, 0, -1960, 3000)
    OP_44(0x101, 0x1)
    OP_44(0x106, 0x1)
    OP_44(0xF8, 0x1)
    OP_44(0xF9, 0x1)
    Sleep(1000)
    OP_6D(-46730, 0, -2460, 3000)

    def lambda_454A():
        TurnDirection(0x101, 0x13, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_454A)
    Sleep(100)

    def lambda_455D():
        TurnDirection(0x106, 0x13, 400)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_455D)
    Sleep(100)

    def lambda_4570():
        TurnDirection(0xF8, 0x13, 400)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_4570)
    TurnDirection(0xF9, 0x13, 400)
    SetChrPos(0x14, -33780, 1500, 2840, 0)

    ChrTalk(    #230
        0x101,
        "#1016F请，请问～……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x13, 0x101, 400)

    ChrTalk(    #231
        0x13,
        "是？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #232
        0x101,
        "#1015F那个人……是谁？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #233
        0x13,
        "是本家的管家。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #234
        0x13,
        (
            "和我一样，是负责\x01",
            "照顾小姐的人。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #235
        0x101,
        "#1004F照，照顾小姐～？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #236
        0x13,
        "嗯嗯，是的……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #237
        0x13,
        (
            "那个暂且不提，首先\x01",
            "还是说明一下状况吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #238
        0x101,
        "#1002F啊，说得是。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #239
        0x13,
        (
            "艾丝蒂尔，\x01",
            "你认识芙拉瑟吗？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x7A, 0x1, 0x4000)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_47BF")

    ChrTalk(    #240
        0x101,
        (
            "#1011F芙拉瑟？\x02\x03",

            "#1006F啊，嗯……\x01",
            "见过的话应该会想起来吧。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_472E")

    ChrTalk(    #241
        0x105,
        (
            "#040F在调查幽灵传闻的时候\x01",
            "应该见过吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4799")

    label("loc_472E")


    ChrTalk(    #242
        0x106,
        "#050F#3P那也是王立学院的学生吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #243
        0x13,
        "嗯，是的。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #244
        0x13,
        (
            "穿着和我一样的制服，\x01",
            "看到的话马上就会认出来吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4799")


    ChrTalk(    #245
        0x101,
        (
            "#1000F芙拉瑟她\x01",
            "出什么事了吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4970")

    label("loc_47BF")


    ChrTalk(    #246
        0x101,
        (
            "#1011F芙拉瑟？\x02\x03",

            "#1006F啊，嗯……\x01",
            "我在古罗尼山顶见过她哦。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x13, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #247
        0x13,
        "！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #248
        0x13,
        (
            "你见过\x01",
            "芙拉瑟吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #249
        0x101,
        (
            "#1015F好像说早做社会实践什么的\x01",
            "在关所附近徘徊……\x02\x03",

            "#1011F……有什么问题吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #250
        0x13,
        "是，是个很大的问题……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #251
        0x13,
        (
            "因为，我的委托\x01",
            "就是寻找芙拉瑟。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #252
        0x101,
        "#1004F咦咦！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #253
        0x106,
        (
            "#051F#3P哈哈，这下可走运了。\x02\x03",

            "居然在寻找之前就已经找到了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #254
        0x101,
        (
            "#1002F不过，为什么芙拉瑟\x01",
            "会跑到山顶的关口去？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4970")


    ChrTalk(    #255
        0x13,
        "她逃跑了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #256
        0x101,
        "#1011F啊？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #257
        0x13,
        "我是说，她是逃跑的。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #258
        0x13,
        "从这家安特洛丝餐厅逃跑了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #259
        0x101,
        (
            "#1004F你说……逃跑了。\x02\x03",

            "有什么必要\x01",
            "非得从餐厅逃掉不可？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4A78")

    ChrTalk(    #260
        0x104,
        (
            "#031F#4P呼，一定是那样啦。\x02\x03",

            "就是说，吃霸王餐啦。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x104, 400)

    ChrTalk(    #261
        0x101,
        "#1019F……你以为谁都跟你一样啊。\x02",
    )

    CloseMessageWindow()

    label("loc_4A78")


    ChrTalk(    #262
        0x13,
        (
            "为什么要逃……\x01",
            "其实也正是我们想知道的。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x13, 400)

    ChrTalk(    #263
        0x13,
        (
            "因为今天对小姐来说\x01",
            "本是一个良辰佳日啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #264
        0x106,
        "#555F#3P？什么意思？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #265
        0x13,
        "……请看那边。\x02",
    )

    CloseMessageWindow()
    OP_4A(0x16, 255)
    OP_6D(-32900, 1500, 3980, 3000)
    Sleep(2000)
    OP_8C(0x101, 45, 0)
    OP_8C(0x106, 45, 0)
    OP_8C(0xF8, 45, 0)
    OP_8C(0xF9, 45, 0)
    OP_8C(0x13, 90, 0)
    Fade(1000)
    OP_6D(-46730, 0, -2460, 0)
    OP_0D()
    OP_4B(0x16, 255)

    ChrTalk(    #266
        0x101,
        "#1011F那，那是……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #267
        0x13,
        "他是某帝国贵族的子弟。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #268
        0x13,
        (
            "为了和小姐相亲，\x01",
            "特地远道而来的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #269
        0x101,
        "#1000F嗯……这样啊…………\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    TurnDirection(0x101, 0x13, 400)

    ChrTalk(    #270
        0x101,
        "#1020F#3S……啊，相亲！？\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()

    def lambda_4C30():
        TurnDirection(0x106, 0x13, 400)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_4C30)
    Sleep(100)

    def lambda_4C43():
        TurnDirection(0xF8, 0x13, 400)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_4C43)
    TurnDirection(0xF9, 0x13, 400)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4C7C")

    ChrTalk(    #271
        0x105,
        "#044F芙拉瑟……吗？\x02",
    )

    CloseMessageWindow()
    Jump("loc_4D0F")

    label("loc_4C7C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4CAE")

    ChrTalk(    #272
        0x103,
        "#023F那个叫芙拉瑟的女孩子？\x02",
    )

    CloseMessageWindow()
    Jump("loc_4D0F")

    label("loc_4CAE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4CE4")

    ChrTalk(    #273
        0x107,
        "#064F那个叫芙拉瑟的姐姐……吗？\x02",
    )

    CloseMessageWindow()
    Jump("loc_4D0F")

    label("loc_4CE4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4D0F")

    ChrTalk(    #274
        0x104,
        "#033F那个芙拉瑟……吗？\x02",
    )

    CloseMessageWindow()

    label("loc_4D0F")


    ChrTalk(    #275
        0x13,
        (
            "虽说还是学生，\x01",
            "但小姐也已年满１６……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #276
        0x13,
        (
            "作为帝国上层贵族千金，\x01",
            "连一门亲事也没有是种耻辱。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #277
        0x101,
        (
            "#1022F慢，慢着。\x02\x03",

            "#1002F比起家族的耻辱\x01",
            "应该还有更重要的东西吧。\x02\x03",

            "你们考虑过她本人的心情吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #278
        0x13,
        (
            "这门亲事的对象\x01",
            "论门第论人品都是无可挑剔的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #279
        0x13,
        (
            "小姐只要见到他，\x01",
            "一定会有好感的。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #280
        0x101,
        (
            "#1007F我说，不是这个问题……\x02\x03",

            "……嗯……总算\x01",
            "能明白一点她逃跑的理由了。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4F25")

    ChrTalk(    #281
        0x105,
        (
            "#045F啊，是呢……\x02\x03",

            "就是为了逃避\x01",
            "有违本意的亲事吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #282
        0x106,
        (
            "#552F#3P啊啊，就这么回事吧。\x02\x03",

            "不过，也要稍微\x01",
            "考虑一下别人的难处啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5183")

    label("loc_4F25")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4FC5")

    ChrTalk(    #283
        0x103,
        (
            "#027F是为了逃避\x01",
            "有违本意的亲事吧？\x02\x03",

            "#021F呼呼，不挺好的嘛。\x01",
            "真是青春的感觉啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #284
        0x106,
        (
            "#551F#3P你说什么风凉话呢。\x02\x03",

            "老为这种事\x01",
            "逃跑谁受得了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5183")

    label("loc_4FC5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_50E5")

    ChrTalk(    #285
        0x104,
        (
            "#031F是为了逃避\x01",
            "她不愿意的亲事吗？\x02\x03",

            "呼，真是不谙世事啊。\x01",
            "令我回想起我的少年时代了。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x104, 400)

    ChrTalk(    #286
        0x101,
        (
            "#1019F反正你一定是被比你大的姐姐\x01",
            "逼婚什么的吧。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x101, 400)

    ChrTalk(    #287
        0x104,
        "#033F啊，你怎么知道？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #288
        0x106,
        (
            "#551F#3P不管怎么说，可真麻烦啊。\x02\x03",

            "老为这种事\x01",
            "出逃谁受得了啊。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_50D3():
        TurnDirection(0x104, 0x13, 400)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_50D3)
    TurnDirection(0x101, 0x13, 400)
    Jump("loc_5183")

    label("loc_50E5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5183")

    ChrTalk(    #289
        0x108,
        (
            "#070F是为了逃避\x01",
            "她不愿意的亲事吗。\x02\x03",

            "呼，心情可以理解，\x01",
            "但还是太不懂事了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #290
        0x106,
        (
            "#551F#3P啊啊，有欠考虑啊。\x02\x03",

            "多少也得考虑一下\x01",
            "别人的难处嘛。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5183")


    ChrTalk(    #291
        0x13,
        "……各人有各人的想法。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #292
        0x13,
        (
            "因此，我不会对\x01",
            "诸位的意见提出异议。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #293
        0x13,
        (
            "当前最重要的事，\x01",
            "不是讨论什么自由恋爱\x01",
            "而是找到小姐。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x7A, 0x1, 0x4000)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_54DF")

    ChrTalk(    #294
        0x106,
        (
            "#050F#3P嗯，同感。\x02\x03",

            "那么，小姐会逃去哪\x01",
            "有没有什么线索？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #295
        0x13,
        (
            "芙拉瑟是一想不通\x01",
            "就会钻牛角尖的性格……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #296
        0x13,
        (
            "恐怕会跑去\x01",
            "相当远的地方。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #297
        0x101,
        (
            "#1015F相当远……\x02\x03",

            "#1002F应该不会\x01",
            "跑出城了吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #298
        0x13,
        (
            "不，城市里\x01",
            "到处都没找到。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #299
        0x13,
        (
            "这么说……\x01",
            "肯定是出城了吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #300
        0x101,
        "#1020F这、这可不得了啊！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #301
        0x13,
        (
            "因此，才会这么急得想\x01",
            "拜托诸位帮忙。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #302
        0x13,
        (
            "事态的紧急性\x01",
            "各位能理解了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #303
        0x106,
        (
            "#057F#3P呼，这你早说啊。\x02\x03",

            "给我们一些细微的线索也行。\x01",
            "哪些地方她可能去的呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #304
        0x13,
        (
            "小姐之前说过\x01",
            "要『返回学院』。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #305
        0x13,
        (
            "除此以外，\x01",
            "我也不知道什么了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #306
        0x101,
        (
            "#1002F要回学院的话，\x01",
            "只有走去卢安的路才能到啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #307
        0x106,
        (
            "#050F#3P啊啊，就先沿着去卢安\x01",
            "的路找找看吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #308
        0x101,
        (
            "#1002F嗯，就这么办吧。\x02\x03",

            "那么，蕾娜。\x01",
            "我们这就去了。\x02\x03",

            "还有什么要说的吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_555C")

    label("loc_54DF")


    ChrTalk(    #309
        0x106,
        (
            "#050F#3P嗯，同感。\x02\x03",

            "好，\x01",
            "就快去快回吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #310
        0x101,
        (
            "#1015F不过……\x01",
            "她会乖乖跟我们回来吗。\x02\x03",

            "没什么理由的话，\x01",
            "我想没那么简单哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_555C")


    ChrTalk(    #311
        0x13,
        "是的……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #312
        0x13,
        (
            "那么，就麻烦\x01",
            "给小姐传个话。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #313
        0x101,
        "#1011F传话？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #314
        0x13,
        (
            "是的，请这样\x01",
            "对芙拉瑟说吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #315
        0x13,
        "『胆小鬼』……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #316
        0x101,
        (
            "#1019F…………………………\x02\x03",

            "那个，这么说\x01",
            "没问题吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #317
        0x13,
        (
            "没有问题。\x01",
            "都在我的计算之内。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x7A, 0x1, 0x4000)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_56AD")

    ChrTalk(    #318
        0x106,
        (
            "#057F#3P别管那么多了。\x02\x03",

            "快点出发吧。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x106, 400)

    ChrTalk(    #319
        0x101,
        "#1002F嗯、嗯，明白了。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x13, 400)

    ChrTalk(    #320
        0x101,
        "#1002F那，我们就走了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_5701")

    label("loc_56AD")


    ChrTalk(    #321
        0x106,
        (
            "#053F#3P既然委托人这么说\x01",
            "我们就没必要管太多了。\x02\x03",

            "#050F要传的话……我们记下了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5701")


    ChrTalk(    #322
        0x13,
        "那么，就拜托你们了。\x02",
    )

    CloseMessageWindow()
    SetChrFlags(0x14, 0x10)
    SetChrFlags(0x13, 0x10)
    OP_28(0x7A, 0x4, 0x4)
    OP_28(0x7A, 0x4, 0x8)
    OP_28(0x7A, 0x1, 0x1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x7A, 0x1, 0x4000)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_574A")
    OP_28(0x7A, 0x1, 0x2)
    Jump("loc_5750")

    label("loc_574A")

    OP_28(0x7A, 0x1, 0x4)

    label("loc_5750")

    OP_A2(0x13)
    Return()

    # Function_9_43F1 end

    def Function_10_5754(): pass

    label("Function_10_5754")

    FadeToDark(0, 0, -1)
    EventBegin(0x0)
    SetChrFlags(0x8, 0x8)
    SetChrPos(0x13, -44110, 0, 0, 180)
    SetChrPos(0x14, -43150, 0, 610, 180)
    SetChrPos(0x12, -44180, 0, -1550, 0)
    SetChrPos(0x101, -43640, 0, -3030, 0)
    SetChrPos(0x106, -44730, 0, -3030, 0)
    SetChrPos(0xF8, -43160, 0, -4320, 0)
    SetChrPos(0xF9, -45180, 0, -4320, 0)
    SetChrChipByIndex(0x12, 33)
    SetChrFlags(0x12, 0x1)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x12, 0x10)
    ClearChrFlags(0x12, 0x40)
    ClearChrFlags(0x12, 0x4)
    ClearChrFlags(0x14, 0x10)
    ClearChrFlags(0x16, 0x10)
    OP_4A(0x13, 255)
    OP_4A(0x14, 255)
    SetChrFlags(0xC, 0x80)
    OP_6D(-43590, 11050, -920, 0)
    OP_67(0, 6760, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    FadeToBright(2000, 0)
    OP_6D(-44180, 0, -1060, 5000)
    OP_0D()
    Sleep(500)

    ChrTalk(    #323
        0x14,
        "小姐……幸好您平安无事。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #324
        0x13,
        "……等候您多时了。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x7A, 0x1, 0x20)"), scpexpr(EXPR_END)), "loc_593B")

    ChrTalk(    #325
        0x12,
        (
            "#1P我并不是自己\x01",
            "想回来的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #326
        0x12,
        (
            "#1P只是看你们还惊动了游击士，\x01",
            "不得已才陪着回来。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #327
        0x13,
        "这都没关系。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #328
        0x13,
        (
            "不管怎样最终您\x01",
            "还是回来了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_594B")

    label("loc_593B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x7A, 0x1, 0x10)"), scpexpr(EXPR_END)), "loc_594B")
    OP_2B(0x7A, 0x2)

    label("loc_594B")


    ChrTalk(    #329
        0x12,
        "#1P……………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #330
        0x12,
        (
            "#1P蕾娜，有一句话\x01",
            "我得说在前头……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #331
        0x12,
        (
            "#1P我还没有\x01",
            "原谅你哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #332
        0x13,
        (
            "是……\x01",
            "这我心知肚明。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #333
        0x13,
        (
            "不过，\x01",
            "这可以之后再说……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #334
        0x12,
        "#1P嗯，就这么办吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #335
        0x12,
        (
            "#1P反正一时半会儿\x01",
            "也说不清楚。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #336
        0x13,
        "那么，请带小姐入席……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #337
        0x14,
        "遵命。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #338
        0x14,
        (
            "请，小姐。\x01",
            "这边走。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x12, 180, 400)

    ChrTalk(    #339
        0x12,
        "#1P那么，我们就告辞了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #340
        0x12,
        (
            "#1P今日实在是\x01",
            "给你们添麻烦了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #341
        0x101,
        (
            "#1006F#4P哪里，小事一桩。\x02\x03",

            "那么，多保重哦。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5B0A")

    ChrTalk(    #342
        0x105,
        "#040F那么，以后学校见。\x02",
    )

    CloseMessageWindow()

    label("loc_5B0A")


    ChrTalk(    #343
        0x12,
        "#1P嗯，那再见了。\x02",
    )

    CloseMessageWindow()

    def lambda_5B27():

        label("loc_5B27")

        TurnDirection(0x13, 0x12, 400)
        OP_48()
        Jump("loc_5B27")

    QueueWorkItem2(0x13, 1, lambda_5B27)

    def lambda_5B38():

        label("loc_5B38")

        TurnDirection(0xFE, 0x12, 400)
        OP_48()
        Jump("loc_5B38")

    QueueWorkItem2(0x0, 1, lambda_5B38)

    def lambda_5B49():

        label("loc_5B49")

        TurnDirection(0xFE, 0x12, 400)
        OP_48()
        Jump("loc_5B49")

    QueueWorkItem2(0x1, 1, lambda_5B49)

    def lambda_5B5A():

        label("loc_5B5A")

        TurnDirection(0xFE, 0x12, 400)
        OP_48()
        Jump("loc_5B5A")

    QueueWorkItem2(0x2, 1, lambda_5B5A)

    def lambda_5B6B():

        label("loc_5B6B")

        TurnDirection(0xFE, 0x12, 400)
        OP_48()
        Jump("loc_5B6B")

    QueueWorkItem2(0x3, 1, lambda_5B6B)
    Sleep(400)
    OP_8C(0x12, 45, 400)

    def lambda_5B88():
        OP_8E(0x12, 0xFFFF5D3A, 0x0, 0x1F4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_5B88)
    OP_8C(0x14, 90, 400)
    OP_43(0x13, 0x2, 0x1, 0xD)

    def lambda_5BB1():
        OP_8E(0x14, 0xFFFF83F0, 0x5DC, 0x1F4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_5BB1)
    WaitChrThread(0x12, 0x1)
    OP_8E(0x12, 0xFFFF8009, 0x5DC, 0x1F4, 0x7D0, 0x0)
    OP_44(0x13, 0x1)
    OP_44(0x0, 0x1)
    OP_44(0x1, 0x1)
    OP_44(0x2, 0x1)
    OP_44(0x3, 0x1)
    OP_8C(0x13, 180, 400)
    OP_8E(0x13, 0xFFFF536C, 0x0, 0xFFFFFDDA, 0x3E8, 0x0)
    OP_8C(0x13, 180, 400)
    WaitChrThread(0x13, 0x2)
    Sleep(1000)

    ChrTalk(    #344
        0x13,
        "辛苦你们了。\x02",
    )

    CloseMessageWindow()

    def lambda_5C37():
        OP_8C(0x101, 0, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5C37)
    Sleep(100)

    def lambda_5C4A():
        OP_8C(0x106, 0, 400)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_5C4A)
    Sleep(100)

    def lambda_5C5D():
        OP_8C(0xF8, 0, 400)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_5C5D)
    OP_8C(0xF9, 0, 400)

    ChrTalk(    #345
        0x13,
        (
            "我代替主人，\x01",
            "衷心感谢大家的努力。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x7A, 0x1, 0x20)"), scpexpr(EXPR_END)), "loc_5D02")

    ChrTalk(    #346
        0x101,
        (
            "#1015F#4P嗯、嗯，我们\x01",
            "倒是没什么啦……\x02\x03",

            "#1002F那个，蕾娜没关系吗？\x02\x03",

            "和芙拉瑟\x01",
            "闹别扭了吧……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5E01")

    label("loc_5D02")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x7A, 0x1, 0x10)"), scpexpr(EXPR_END)), "loc_5E01")

    ChrTalk(    #347
        0x13,
        (
            "这是一点心意，\x01",
            "谨表我们的感激之情。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #348
        0x13,
        "请收下。\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #349
        "\x07\x00得到了\x1F\x58\x01\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x158, 1)

    ChrTalk(    #350
        0x101,
        (
            "#1011F#4P啊，嗯，谢谢……\x02\x03",

            "#1015F不过，虽说工作\x01",
            "算是解决……\x02\x03",

            "#1002F那个，蕾娜没关系吗？\x02\x03",

            "和芙拉瑟\x01",
            "闹别扭了吧……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5E01")


    ChrTalk(    #351
        0x13,
        (
            "不，这也\x01",
            "完全是为了小姐好。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #352
        0x13,
        (
            "我们这些人\x01",
            "生来就是要为主人着想的。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5E92")

    ChrTalk(    #353
        0x105,
        (
            "#043F可是，蕾娜……\x02\x03",

            "芙拉瑟\x01",
            "或许不是这么想的呢？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5EC8")

    label("loc_5E92")


    ChrTalk(    #354
        0x101,
        (
            "#1003F#4P可是，蕾娜……\x02\x03",

            "芙拉瑟\x01",
            "她或许没这么想？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5EC8")


    ChrTalk(    #355
        0x13,
        (
            "这……\x01",
            "是什么意思？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #356
        0x101,
        (
            "#1002F#4P就是说芙拉瑟\x01",
            "早就把你当朋友啦。\x02\x03",

            "我感觉你们的矛盾\x01",
            "就出在这里哦。\x02\x03",

            "#1015F唔，不过外人\x01",
            "也不好说什么就是了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #357
        0x13,
        "…………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #358
        0x13,
        (
            "不……\x01",
            "很有参考价值。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #359
        0x13,
        (
            "总之必须和\x01",
            "芙拉瑟好好谈谈了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #360
        0x13,
        "那么，我也失陪了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #361
        0x101,
        (
            "#1011F#4P啊，嗯。\x01",
            "工作辛苦了。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6019")

    ChrTalk(    #362
        0x105,
        "#040F那么，后会有期。\x02",
    )

    CloseMessageWindow()
    Jump("loc_6035")

    label("loc_6019")


    ChrTalk(    #363
        0x106,
        "#050F#1P啊啊，再见了。\x02",
    )

    CloseMessageWindow()

    label("loc_6035")


    ChrTalk(    #364
        0x13,
        "是，失陪了。\x02",
    )

    CloseMessageWindow()

    def lambda_604D():

        label("loc_604D")

        TurnDirection(0xFE, 0x13, 400)
        OP_48()
        Jump("loc_604D")

    QueueWorkItem2(0x0, 1, lambda_604D)

    def lambda_605E():

        label("loc_605E")

        TurnDirection(0xFE, 0x13, 400)
        OP_48()
        Jump("loc_605E")

    QueueWorkItem2(0x1, 1, lambda_605E)

    def lambda_606F():

        label("loc_606F")

        TurnDirection(0xFE, 0x13, 400)
        OP_48()
        Jump("loc_606F")

    QueueWorkItem2(0x2, 1, lambda_606F)

    def lambda_6080():

        label("loc_6080")

        TurnDirection(0xFE, 0x13, 400)
        OP_48()
        Jump("loc_6080")

    QueueWorkItem2(0x3, 1, lambda_6080)
    Sleep(400)
    OP_8C(0x13, 90, 400)
    OP_8E(0x13, 0xFFFF7748, 0x0, 0xFFFFFDDA, 0x7D0, 0x0)
    OP_44(0x0, 0x1)
    OP_44(0x1, 0x1)
    OP_44(0x2, 0x1)
    OP_44(0x3, 0x1)

    ChrTalk(    #365
        0x101,
        (
            "#1007F#4P唔……怎么感觉\x01",
            "又会发生新的争端啊～～。\x02\x03",

            "要是她们能\x01",
            "和好就好了……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6133")

    ChrTalk(    #366
        0x105,
        "#043F嗯嗯，确实……\x02",
    )

    CloseMessageWindow()

    label("loc_6133")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6184")

    ChrTalk(    #367
        0x103,
        (
            "#020F不过，我们\x01",
            "也只能帮到这里了。\x02\x03",

            "之后就看她们自己的吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6233")

    label("loc_6184")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_61E1")

    ChrTalk(    #368
        0x108,
        (
            "#070F担心可以理解，\x01",
            "不过我们也只能帮到这里了。\x02\x03",

            "之后就看她们自己的吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6233")

    label("loc_61E1")


    ChrTalk(    #369
        0x106,
        (
            "#050F啊，心情可以理解，\x01",
            "不过我们的工作就到此为止了。\x02\x03",

            "之后就看她们自己的了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6233")

    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrChipByIndex(0x12, 14)
    ClearChrFlags(0x12, 0x1)
    SetChrFlags(0x12, 0x10)
    SetChrFlags(0x12, 0x40)
    SetChrFlags(0x12, 0x4)
    SetChrPos(0x13, -33800, 1500, 1300, 0)
    SetChrPos(0x14, -31760, 1500, 1300, 0)
    SetChrPos(0x12, -32930, 1600, 2650, 0)
    OP_4B(0x13, 255)
    OP_4B(0x14, 255)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0x8, 0x8)
    OP_22(0x17, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #370
        "\x07\x02任务【失踪的小姐】\x07\x00完成了！\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_28(0x7A, 0x4, 0x10)
    SetChrPos(0x0, -43590, 0, -1450, 180)
    SetChrPos(0x1, -43590, 0, -1450, 180)
    SetChrPos(0x2, -43590, 0, -1450, 180)
    SetChrPos(0x3, -43590, 0, -1450, 180)
    OP_4A(0x0, 255)
    OP_4A(0x1, 255)
    OP_4A(0x2, 255)
    OP_4A(0x3, 255)
    OP_69(0x101, 0x0)
    OP_30(0x0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    OP_69(0x101, 0x0)
    OP_30(0x0)
    OP_8C(0x101, 180, 0)
    OP_8C(0xF7, 180, 0)
    OP_8C(0xF8, 180, 0)
    OP_8C(0xF9, 180, 0)
    OP_4A(0x0, 255)
    OP_4A(0x1, 255)
    OP_4A(0x2, 255)
    OP_4A(0x3, 255)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    Return()

    # Function_10_5754 end

    def Function_11_63A8(): pass

    label("Function_11_63A8")

    OP_8C(0xFE, 135, 400)
    OP_8E(0x14, 0xFFFF49A8, 0x0, 0xFFFFF1C8, 0x7D0, 0x0)
    OP_8E(0x14, 0xFFFF5560, 0x0, 0xFFFFF1C8, 0x7D0, 0x0)
    OP_8E(0x14, 0xFFFF5FD8, 0x0, 0xFFFFFF38, 0x7D0, 0x0)
    OP_A2(0x22)
    OP_8E(0x14, 0xFFFF6EE2, 0x5DC, 0xFFFFFF38, 0x7D0, 0x0)
    Return()

    # Function_11_63A8 end

    def Function_12_6403(): pass

    label("Function_12_6403")

    OP_A6(0x22)
    OP_44(0x13, 0x1)
    OP_8E(0x13, 0xFFFF46A6, 0x0, 0xFFFFF722, 0x3E8, 0x0)
    Sleep(150)
    OP_8C(0x13, 90, 400)
    Return()

    # Function_12_6403 end

    def Function_13_642B(): pass

    label("Function_13_642B")

    OP_6D(-41920, 0, 210, 2000)
    Sleep(1500)
    OP_6D(-44560, 0, -2000, 2000)
    Return()

    # Function_13_642B end

    SaveToFile()

Try(main)

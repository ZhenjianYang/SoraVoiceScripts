from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'T0131_1 ._SN',
        MapName             = 'Rolent',
        Location            = 'T0131.x',
        MapIndex            = 7,
        MapDefaultBGM       = "ed60010",
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
        "Function_1_3A7",          # 01, 1
        "Function_2_5A9",          # 02, 2
        "Function_3_1046",         # 03, 3
        "Function_4_17F2",         # 04, 4
        "Function_5_1BD0",         # 05, 5
        "Function_6_22C6",         # 06, 6
        "Function_7_248F",         # 07, 7
    )


    def Function_0_AA(): pass

    label("Function_0_AA")

    EventBegin(0x0)
    Fade(1000)
    SetChrPos(0x101, 38600, 0, 127160, 270)
    SetChrPos(0x103, 39970, 0, 126320, 270)
    SetChrPos(0xF8, 41010, 0, 126700, 270)
    SetChrPos(0xF9, 39700, 0, 127590, 270)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_124")
    SetChrPos(0xF9, 41010, 0, 126700, 270)
    SetChrPos(0xF8, 39700, 0, 127590, 270)

    label("loc_124")

    OP_8C(0xB, 90, 0)
    OP_6D(38020, 0, 128180, 0)
    OP_67(0, 6150, -10000, 0)
    OP_6B(2750, 0)
    OP_6C(315000, 0)
    OP_6E(280, 0)
    OP_4A(0xB, 255)
    OP_0D()

    ChrTalk(    #0
        0xB,
        "哟，艾丝蒂尔，还有大家！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xB,
        (
            "我家的\x01",
            "托露塔也醒来了！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0xB,
        (
            "这次真是快\x01",
            "担心死了，谢谢你们。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x101,
        (
            "#1000F#2P哪里，不要在意。\x02\x03",

            "那也是我们\x01",
            "的工作啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x103,
        (
            "#020F嗯，艾丝蒂尔说的对。\x02\x03",

            "……那么，还有什么\x01",
            "委托吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0xB,
        (
            "噢，原来是\x01",
            "看了那个而来的吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0xB,
        (
            "其实希望你们帮我\x01",
            "收集食材。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0xB,
        (
            "怎么样？\x01",
            "有时间做吗？\x02",
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2F6")
    Call(1, 2)
    Jump("loc_3A4")

    label("loc_2F6")


    ChrTalk(    #8
        0x101,
        (
            "#1015F#2P嗯，对不起。\x01",
            "现在不太方便。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0xB,
        "啊，不行吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0xB,
        (
            "雾都散去了，\x01",
            "你们却还是一样忙啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0xB,
        (
            "算了，等你们有空的时候\x01",
            "再来找我吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x101,
        "#1000F#2P嗯，好的！\x02",
    )

    CloseMessageWindow()
    OP_A2(0x10)
    OP_28(0x75, 0x1, 0x8000)

    label("loc_3A4")

    EventEnd(0x0)
    Return()

    # Function_0_AA end

    def Function_1_3A7(): pass

    label("Function_1_3A7")

    EventBegin(0x0)
    Fade(1000)
    SetChrPos(0x101, 38600, 0, 127160, 270)
    SetChrPos(0x103, 39970, 0, 126320, 270)
    SetChrPos(0xF8, 41010, 0, 126700, 270)
    SetChrPos(0xF9, 39700, 0, 127590, 270)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_421")
    SetChrPos(0xF9, 41010, 0, 126700, 270)
    SetChrPos(0xF8, 39700, 0, 127590, 270)

    label("loc_421")

    OP_8C(0xB, 90, 0)
    OP_6D(38020, 0, 128180, 0)
    OP_67(0, 6150, -10000, 0)
    OP_6B(2750, 0)
    OP_6C(315000, 0)
    OP_6E(280, 0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_END)), "loc_48F")

    ChrTalk(    #13
        0xB,
        (
            "怎么？还是\x01",
            "想要接受了吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4D8")

    label("loc_48F")


    ChrTalk(    #14
        0xB,
        (
            "噢，你们回来得\x01",
            "很快啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0xB,
        (
            "料理的调查和\x01",
            "食材的收集，\x01",
            "愿意接受吗？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4D8")

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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_530")
    Call(1, 2)
    Jump("loc_5A6")

    label("loc_530")


    ChrTalk(    #16
        0x101,
        "#1007F#2P抱歉，还是不太方便呢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0xB,
        (
            "什么，还是不行吗？\x01",
            "那可真遗憾。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0xB,
        (
            "算了，等你们有空的时候\x01",
            "再来找我吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x10)

    label("loc_5A6")

    EventEnd(0x0)
    Return()

    # Function_1_3A7 end

    def Function_2_5A9(): pass

    label("Function_2_5A9")


    ChrTalk(    #19
        0x101,
        (
            "#1006F#2P嗯，ＯＫ了哟。\x02\x03",

            "那……要调查\x01",
            "什么料理呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0xB,
        (
            "啊，想让你们帮忙调查的\x01",
            "是某个炖煮料理。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0xB,
        (
            "『洛连特风味炖煮』\x01",
            "好像就是它的俗称。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x14, 0x17, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(100)
    OP_62(0x103, 0x0, 2000, 0x14, 0x17, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_693")
    OP_62(0xF8, 0x0, 2300, 0x14, 0x17, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jump("loc_6D1")

    label("loc_693")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6BA")
    OP_62(0xF8, 0x0, 1700, 0x14, 0x17, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jump("loc_6D1")

    label("loc_6BA")

    OP_62(0xF8, 0x0, 2000, 0x14, 0x17, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)

    label("loc_6D1")

    Sleep(100)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6FD")
    OP_62(0xF9, 0x0, 2300, 0x14, 0x17, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jump("loc_73B")

    label("loc_6FD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_724")
    OP_62(0xF9, 0x0, 1700, 0x14, 0x17, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jump("loc_73B")

    label("loc_724")

    OP_62(0xF9, 0x0, 2000, 0x14, 0x17, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)

    label("loc_73B")

    Sleep(1000)

    ChrTalk(    #22
        0x101,
        (
            "#1019F#2P洛、洛连特风味炖煮……\x02\x03",

            "好、好像一听名字\x01",
            "就让人不想吃啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x103,
        (
            "#025F啊啊……\x01",
            "确实，一点食欲也引不起来。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xB, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(    #24
        0xB,
        (
            "啊、啊，不用太\x01",
            "在意名字啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0xB,
        (
            "总之希望你们\x01",
            "帮忙调查这个料理。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0xB,
        (
            "和城里的人打听一下，\x01",
            "一定能有线索吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0xB,
        (
            "以前这可是很\x01",
            "有名的料理呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x101,
        (
            "#1015F#2P那么，对这料理熟悉的人\x01",
            "应该都上了年纪吧。\x02\x03",

            "既然是古老的料理，\x01",
            "年轻人应该都没听过。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8FB")

    ChrTalk(    #29
        0x106,
        (
            "#051F对我们来说\x01",
            "是很有用的意见吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_96C")

    label("loc_8FB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_921")

    ChrTalk(    #30
        0x104,
        "#035F嗯，确实。\x02",
    )

    CloseMessageWindow()
    Jump("loc_96C")

    label("loc_921")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_949")

    ChrTalk(    #31
        0x108,
        "#070F嗯，确实啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_96C")

    label("loc_949")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_96C")

    ChrTalk(    #32
        0x105,
        "#040F嗯，确实。\x02",
    )

    CloseMessageWindow()

    label("loc_96C")


    ChrTalk(    #33
        0x103,
        (
            "#026F嗯，调查的目标\x01",
            "已经没疑问了。\x02\x03",

            "但有关料理本身，\x01",
            "情报还是不够啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x101,
        (
            "#1007F#2P是啊……\x02\x03",

            "#1002F有什么线索\x01",
            "可以提供吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0xB,
        "噢，那倒也没什么……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0xB,
        (
            "不过，可以去问问\x01",
            "拉欧爷爷。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0x101,
        (
            "#1004F#2P啊……？\x02\x03",

            "为什么要去问\x01",
            "拉欧爷爷呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0xB,
        (
            "本来不想说的……\x01",
            "那位老爷爷啊，\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0xB,
        (
            "好像是在梦中\x01",
            "尝到了怀念的料理。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0xB,
        (
            "一直在说要\x01",
            "要把它制作出来。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B08")

    ChrTalk(    #41
        0x107,
        (
            "#560F原、原来是这样。\x01",
            "难怪会有这样的委托……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BD9")

    label("loc_B08")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B3B")

    ChrTalk(    #42
        0x105,
        (
            "#040F原来如此……\x01",
            "是那样啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BD9")

    label("loc_B3B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B6E")

    ChrTalk(    #43
        0x108,
        (
            "#070F原来如此……\x01",
            "是那样啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BD9")

    label("loc_B6E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_BA5")

    ChrTalk(    #44
        0x104,
        (
            "#030F嗯，原来如此……\x01",
            "是那样啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BD9")

    label("loc_BA5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_BD9")

    ChrTalk(    #45
        0x106,
        (
            "#050F呼，原来如此……\x01",
            "是那样啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BD9")


    ChrTalk(    #46
        0x101,
        (
            "#1015F#2P不过，特地\x01",
            "为这个来寻求料理……\x02\x03",

            "那道料理，难道\x01",
            "就真的这么美味吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x103,
        (
            "#020F不一定是味道的缘故，\x02\x03",

            "也许是因为\x01",
            "想起了某些回忆吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0xB,
        (
            "虽然老爷爷什么都没说，\x01",
            "不过看起来一定没错的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0xB,
        (
            "总之是因为什么原因，\x01",
            "所以他无论如何都想再吃到一次。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D29")

    ChrTalk(    #50
        0x104,
        (
            "#031F呼～还真是有意思啊。\x02\x03",

            "既然如此的话，\x01",
            "我也只能慷慨相助了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DEC")

    label("loc_D29")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D6A")

    ChrTalk(    #51
        0x108,
        (
            "#070F嗯，这样的话，\x02\x03",

            "我们就帮\x01",
            "他一下好了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DEC")

    label("loc_D6A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_DA4")

    ChrTalk(    #52
        0x106,
        (
            "#051F喔，是这样啊。\x02\x03",

            "那就帮帮他吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DEC")

    label("loc_DA4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_DEC")

    ChrTalk(    #53
        0x105,
        (
            "#040F是这样吗……\x02\x03",

            "那我们要是能帮上忙的话\x01",
            "也不错啊…\x02",
        )
    )

    CloseMessageWindow()

    label("loc_DEC")

    OP_8C(0x101, 90, 400)

    ChrTalk(    #54
        0x101,
        (
            "#1006F#2P嗯，拉欧爷爷\x01",
            "也终于醒来了。\x02\x03",

            "为了庆祝，一定想\x01",
            "好好吃一顿吧。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E65")

    ChrTalk(    #55
        0x107,
        "#061F嘿嘿……是啊。\x02",
    )

    CloseMessageWindow()

    label("loc_E65")

    OP_8C(0x101, 270, 400)

    ChrTalk(    #56
        0x103,
        (
            "#020F那么，料理的事情\x01",
            "就去问拉欧爷爷吧。\x02\x03",

            "……有关工作，\x01",
            "还有什么别的注意事项吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0xB,
        (
            "啊啊～料理的事情\x01",
            "要想办法，\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0xB,
        (
            "还有，需要的食材\x01",
            "最好也一起带来吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0xB,
        (
            "也许要用到什么\x01",
            "特殊的配料也说不定。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0x101,
        (
            "#1000F#2P嗯，明白。\x02\x03",

            "那么，报告的时候\x01",
            "我们会把食材也带来的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0xB,
        "啊啊，那就拜托了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0xB,
        (
            "嗯，究竟是怎样的料理呢，\x01",
            "还真让人好奇。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0x103,
        (
            "#020F为了不辜负你的期待，\x01",
            "我们这就加油调查了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0x101,
        "#1006F#2P期待我们的报告吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0xB,
        "啊啊，拜托了。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x14)
    OP_28(0x75, 0x4, 0x4)
    OP_28(0x75, 0x4, 0x8)
    OP_28(0x75, 0x1, 0x1)
    OP_28(0x75, 0x1, 0x2)
    OP_28(0x75, 0x1, 0x4)
    Return()

    # Function_2_5A9 end

    def Function_3_1046(): pass

    label("Function_3_1046")

    EventBegin(0x0)
    OP_8C(0x11, 270, 0)
    Fade(1000)
    SetChrPos(0x101, 38190, 0, 75500, 270)
    SetChrPos(0x103, 38230, 0, 74290, 294)
    SetChrPos(0xF8, 39580, 0, 75500, 270)
    SetChrPos(0xF9, 39000, 0, 74690, 270)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10C7")
    SetChrPos(0xF9, 39580, 0, 75500, 270)
    SetChrPos(0xF8, 39000, 0, 74690, 270)

    label("loc_10C7")

    OP_6D(37010, 0, 76590, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(315000, 0)
    OP_6E(280, 0)
    OP_0D()

    ChrTalk(    #66
        0x11,
        "#1P嗯……料理还是不行吗。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0x11,
        (
            "#1P毕竟是很久前的料理，\x01",
            "太辛苦厨师了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0x101,
        "#1000F#2P拉欧爷爷，您有空吗？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x11, 0x101, 400)
    OP_62(0x11, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(    #69
        0x11,
        (
            "#1P噢噢，我还说是谁，\x01",
            "这不是卡西乌斯的丫头吗。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0x11,
        (
            "#1P怎么，找我\x01",
            "有什么事？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0x101,
        (
            "#1015F#2P嗯，想打听一下\x01",
            "料理的事情。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0x11,
        "#1P喔？料理？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0x11,
        (
            "#1P是说我梦见的那种\x01",
            "炖煮料理吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0x103,
        (
            "#020F嗯，就是那个料理的事。\x02\x03",

            "其实是受到了德瑟鲁先生的委托……\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #75
        (
            "\x07\x05他委托我们\x01",
            "调查料理的配料。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    TurnDirection(0x11, 0x103, 400)

    ChrTalk(    #76
        0x11,
        (
            "#1P啊啊～那你们\x01",
            "就来找我了解情况吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0x11,
        (
            "#1P呵呵，这小子\x01",
            "找到了强力的支援啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0x11,
        "#1P拜托你们了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0x101,
        (
            "#1008F#2P那……谢谢您了。\x02\x03",

            "#1006F不过想完成委托还\x01",
            "需要拉欧爷爷的协助啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0x103,
        (
            "#020F有关那个料理，\x01",
            "希望您能详细介绍一下。\x02\x03",

            "比如材料、味道、\x01",
            "在哪里吃过的…之类的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0x11,
        (
            "#1P原来如此，说的有道理……\x01",
            "那么我这就开始说吧。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x11, 0x101, 400)

    ChrTalk(    #82
        0x11,
        (
            "#1P首先，如你们所知，\x01",
            "这是炖煮的料理。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0x11,
        (
            "#1P不过基本的风味\x01",
            "应该是黑胡椒口味才对。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0x11,
        (
            "#1P那种香气令人食指大动，\x01",
            "吃下去的感觉很痛快。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0x101,
        (
            "#1015F#2P嗯……\x01",
            "黑胡椒的炖煮……\x02\x03",

            "#1011F啊……请您继续说。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #86
        0x11,
        (
            "#1P嗯，主材是肉……\x01",
            "还有鱼肉。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0x11,
        (
            "#1P我比较喜欢肉，\x01",
            "就先说肉吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0x11,
        (
            "#1P带着骨头的肉，\x01",
            "实在是很美味呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x11, 180, 400)

    ChrTalk(    #89
        0x11,
        (
            "#1P另外还有一些\x01",
            "特殊香草…\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x11, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_63(0x11)

    ChrTalk(    #90
        0x11,
        (
            "#1P不过很遗憾，\x01",
            "具体是什么已经忘了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0x11,
        (
            "#1P只是记得很香，\x01",
            "但不知道是什么。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0x11,
        "#1P嗯，就这些了吧……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0x101,
        (
            "#1015F#2P嗯，\x01",
            "肉骨头……\x02\x03",

            "还有香草…\x01",
            "种类未知…\x02\x03",

            "#1000F……大概就这些了吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0x103,
        "#020F还算挺具体了。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_16AF")

    ChrTalk(    #95
        0x106,
        (
            "#051F啊啊～有这些情报\x01",
            "就可以开始了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1753")

    label("loc_16AF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_16E4")

    ChrTalk(    #96
        0x108,
        (
            "#070F嗯，这下子\x01",
            "情报算是够了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1753")

    label("loc_16E4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_171B")

    ChrTalk(    #97
        0x104,
        (
            "#030F嗯，得到这些情报\x01",
            "就足够了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1753")

    label("loc_171B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1753")

    ChrTalk(    #98
        0x105,
        (
            "#040F嗯，得到这些材料以后\x01",
            "再回来吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1753")

    OP_8C(0x11, 90, 400)

    ChrTalk(    #99
        0x11,
        "#1P嗯，对你们有点帮助吧？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0x101,
        (
            "#1006F#2P当然，\x01",
            "谢谢您啦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0x11,
        "#1P那么，调查就拜托了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0x11,
        (
            "#1P想想要是能再看到那料理\x01",
            "一定会很开心的。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x11)
    OP_28(0x75, 0x1, 0x8)
    EventEnd(0x0)
    Return()

    # Function_3_1046 end

    def Function_4_17F2(): pass

    label("Function_4_17F2")

    TurnDirection(0x8, 0x101, 400)

    ChrTalk(    #103
        0x8,
        (
            "艾丝蒂尔也要找时间\x01",
            "再来店里玩吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0x8,
        (
            "我和伊莉莎一起\x01",
            "期待你们回来。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0x101,
        (
            "#1001F嗯，以后\x01",
            "要再来玩啊。\x02\x03",

            "#1011F啊，说起来的话……\x01",
            "托露塔阿姨。\x02\x03",

            "其实我们是接受德瑟鲁大叔的委托\x01",
            "来调查一些事情……\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #106
        (
            "\x07\x05诉说了在寻找拉欧爷爷\x01",
            "所说的炖煮料理食谱的事。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(    #107
        0x8,
        (
            "啊，是料理的事吧。\x01",
            "我听说了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #108
        0x103,
        (
            "#027F啊，那么……\x02\x03",

            "……托露塔阿姨也\x01",
            "应该知道的。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x103, 400)

    ChrTalk(    #109
        0x8,
        "嗯，真遗憾啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #110
        0x8,
        (
            "在我开始学烹饪的时候，\x01",
            "就已经没人做那道菜了。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x75, 0x1, 0x800)"), scpexpr(EXPR_END)), "loc_1A44")
    TurnDirection(0x103, 0x101, 400)

    ChrTalk(    #111
        0x103,
        (
            "#020F总之\x01",
            "先去报告那个食谱吧。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 400)

    ChrTalk(    #112
        0x101,
        "#1015F嗯，只有先这样了。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x101, 400)

    ChrTalk(    #113
        0x8,
        (
            "老公也很困扰，\x01",
            "怎么也要帮帮他啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1BC6")

    label("loc_1A44")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x75, 0x1, 0x400)"), scpexpr(EXPR_END)), "loc_1AD8")
    TurnDirection(0x103, 0x101, 400)

    ChrTalk(    #114
        0x103,
        (
            "#020F看来还是得\x01",
            "调查雷特拉先生家了吧？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 400)

    ChrTalk(    #115
        0x101,
        "#1015F嗯……或许是……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x101, 400)

    ChrTalk(    #116
        0x8,
        (
            "老公他也很困扰，\x01",
            "怎么也要帮帮他啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1BC6")

    label("loc_1AD8")


    ChrTalk(    #117
        0x101,
        (
            "#1025F啊，那个……\x02\x03",

            "#1015F嗯，人一上了年纪\x01",
            "果然就是这样啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #118
        0x103,
        (
            "#020F嗯，那样就好了。\x02\x03",

            "……那么，\x01",
            "继续调查吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #119
        0x101,
        (
            "#1000F啊，嗯……\x02\x03",

            "托露塔阿姨，\x01",
            "谢谢您的合作。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x101, 400)

    ChrTalk(    #120
        0x8,
        "要道谢的是我才对，\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #121
        0x8,
        (
            "老公他也很困扰，\x01",
            "调查到什么了吧？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1BC6")

    OP_A2(0x12)
    OP_28(0x75, 0x1, 0x80)
    Return()

    # Function_4_17F2 end

    def Function_5_1BD0(): pass

    label("Function_5_1BD0")

    EventBegin(0x0)
    Fade(1000)
    SetChrPos(0x101, 38600, 0, 127160, 270)
    SetChrPos(0x103, 39970, 0, 126320, 270)
    SetChrPos(0xF8, 41010, 0, 126700, 270)
    SetChrPos(0xF9, 39700, 0, 127590, 270)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1C4A")
    SetChrPos(0xF9, 41010, 0, 126700, 270)
    SetChrPos(0xF8, 39700, 0, 127590, 270)

    label("loc_1C4A")

    OP_8C(0xB, 90, 0)
    OP_6D(38020, 0, 128180, 0)
    OP_67(0, 6150, -10000, 0)
    OP_6B(2750, 0)
    OP_6C(315000, 0)
    OP_6E(280, 0)
    OP_4A(0xB, 255)
    OP_0D()

    ChrTalk(    #122
        0xB,
        (
            "哟，艾丝蒂尔。\x01",
            "调查进行得如何了？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #123
        0x101,
        (
            "#1001F#2P嗯，大概\x01",
            "知道配料了。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xB, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #124
        0xB,
        "噢，已经找到了吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #125
        0xB,
        (
            "呀，工作完成得好早啊。\x01",
            "游击士果然了不起。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #126
        0x101,
        (
            "#1015F#2P嗯，不过\x01",
            "还不能高兴太早。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #127
        0xB,
        "哦？怎么回事？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #128
        0x103,
        "#020F嗯，其实……\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #129
        (
            "\x07\x05将找到的食谱已做了改动的事情\x01",
            "做了说明。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(    #130
        0xB,
        "原来如此…是这样啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #131
        0xB,
        (
            "但是，也未必就是坏事，\x01",
            "就用那配料试试看吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #132
        0x101,
        (
            "#1007F#2P抱歉啊，德瑟鲁大叔。\x02\x03",

            "要是能找到原始版\x01",
            "的话自然最好。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #133
        0xB,
        (
            "哪里！基本部分并\x01",
            "没有变化，\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #134
        0xB,
        (
            "再加上我的技术和经验，\x01",
            "一定可以成功的！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #135
        0x103,
        "#021F呵呵，很有自信啊。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1F09")

    ChrTalk(    #136
        0x104,
        "#031F不愧是职业厨师啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1F99")

    label("loc_1F09")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1F37")

    ChrTalk(    #137
        0x105,
        "#040F不愧是专业厨师啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1F99")

    label("loc_1F37")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1F6D")

    ChrTalk(    #138
        0x108,
        "#070F嗯，专业的就是不同凡响啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1F99")

    label("loc_1F6D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1F99")

    ChrTalk(    #139
        0x107,
        (
            "#061F果然……\x01",
            "名不虚传。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F99")


    ChrTalk(    #140
        0x101,
        (
            "#1006F#2P那么，赶快\x01",
            "将调查结果告诉您吧。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #141
        "\x07\x05报告了布露姆老奶奶的食谱。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(    #142
        0xB,
        (
            "嗯嗯……\x01",
            "原来如此。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #143
        0xB,
        (
            "大致上和我想的一样。\x01",
            "材料很让人意外呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #144
        0xB,
        (
            "嗯，那么就努力\x01",
            "试着制作吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #145
        0x101,
        (
            "#1011F#2P这也就是说，\x01",
            "委托结束了？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #146
        0xB,
        "噢，还没有……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #147
        0xB,
        (
            "……之前说过吧，\x01",
            "食材的收集也想拜托你们。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #148
        0x103,
        (
            "#020F嗯，确实说过呢。\x02\x03",

            "#027F……已经准备完了吗？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 400)

    ChrTalk(    #149
        0x101,
        "#1015F#2P啊，等一下……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x388, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_EXEC_OP, "OP_40(0x389, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_40(0x396, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GE), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_40(0x397, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_40(0x399, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_40(0x39A, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GE), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_40(0x39C, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_40(0x3A1, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GE), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2199")
    OP_A2(0x15)

    label("loc_2199")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 5)), scpexpr(EXPR_END)), "loc_21D4")
    TurnDirection(0x101, 0xB, 400)

    ChrTalk(    #150
        0x101,
        (
            "#1006F#2P嗯……\x01",
            "全部收集全了呢。\x02",
        )
    )

    CloseMessageWindow()
    Call(1, 7)
    Jump("loc_22C3")

    label("loc_21D4")

    OP_62(0x101, 0x0, 2000, 0xE, 0xF, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)
    OP_63(0x101)
    TurnDirection(0x101, 0xB, 400)

    ChrTalk(    #151
        0x101,
        (
            "#1007F#2P对、对不起，\x02\x03",

            "料理需要的食材\x01",
            "还没有收集全。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #152
        0xB,
        "啊，没关系。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #153
        0xB,
        (
            "收集完以后\x01",
            "再来找我吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #154
        0x101,
        "#1003F#2P嗯……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #155
        0x103,
        (
            "#022F真是的……\x01",
            "认真确认一下啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #156
        0x101,
        "#1007F#2P……真、真丢人。\x02",
    )

    CloseMessageWindow()
    OP_28(0x75, 0x1, 0x4000)

    label("loc_22C3")

    EventEnd(0x0)
    Return()

    # Function_5_1BD0 end

    def Function_6_22C6(): pass

    label("Function_6_22C6")

    EventBegin(0x0)
    Fade(1000)
    SetChrPos(0x101, 38600, 0, 127160, 270)
    SetChrPos(0x103, 39970, 0, 126320, 270)
    SetChrPos(0xF8, 41010, 0, 126700, 270)
    SetChrPos(0xF9, 39700, 0, 127590, 270)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2340")
    SetChrPos(0xF9, 41010, 0, 126700, 270)
    SetChrPos(0xF8, 39700, 0, 127590, 270)

    label("loc_2340")

    OP_8C(0xB, 90, 0)
    OP_6D(38020, 0, 128180, 0)
    OP_67(0, 6150, -10000, 0)
    OP_6B(2750, 0)
    OP_6C(315000, 0)
    OP_6E(280, 0)
    OP_4A(0xB, 255)
    OP_0D()

    ChrTalk(    #157
        0xB,
        "噢，已经收集完毕了吗？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x388, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_EXEC_OP, "OP_40(0x389, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_40(0x396, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GE), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_40(0x397, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_40(0x399, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_40(0x39A, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GE), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_40(0x39C, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_40(0x3A1, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GE), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_240B")
    OP_A2(0x15)

    label("loc_240B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 5)), scpexpr(EXPR_END)), "loc_243B")

    ChrTalk(    #158
        0x101,
        (
            "#1006F#2P嗯！\x01",
            "全部收集到了。\x02",
        )
    )

    CloseMessageWindow()
    Call(1, 7)
    Jump("loc_248C")

    label("loc_243B")


    ChrTalk(    #159
        0x101,
        (
            "#1008F#2P啊，抱歉。\x01",
            "还没有。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #160
        0xB,
        "啊，辛苦了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #161
        0xB,
        (
            "很好，\x01",
            "终于收集全了啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_248C")

    EventEnd(0x0)
    Return()

    # Function_6_22C6 end

    def Function_7_248F(): pass

    label("Function_7_248F")

    EventBegin(0x0)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #162
        (
            "\x1F\x88\x03\x07\x00×１\x01",
            "\x1F\x89\x03\x07\x00×１\x01",
            "\x1F\x96\x03\x07\x00×２\x01",
            "\x1F\x97\x03\x07\x00×５\x01",
            "\x1F\x99\x03\x07\x00×５\x01",
            "\x1F\x9A\x03\x07\x00×２\x01",
            "\x1F\x9C\x03\x07\x00×４\x01",
            "\x1F\xA1\x03\x07\x00×２\x01",
            "\x07\x00……将以上的食材交了出去。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3F(0x388, 1)
    OP_3F(0x389, 1)
    OP_3F(0x396, 2)
    OP_3F(0x397, 5)
    OP_3F(0x399, 5)
    OP_3F(0x39A, 2)
    OP_3F(0x39C, 4)
    OP_3F(0x3A1, 2)

    ChrTalk(    #163
        0xB,
        (
            "嗯，辛苦啦。\x01",
            "这样就准备完毕了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #164
        0xB,
        (
            "能做出爷爷\x01",
            "想要的料理吗……\x01",
            "接下来就要看我的手艺了！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #165
        0xB,
        (
            "好！！拿出干劲\x01",
            "试试看吧！\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_8E(0xB, 0x8F20, 0x0, 0x1EE74, 0x7D0, 0x0)
    OP_8E(0xB, 0x8F20, 0x0, 0x1E8D4, 0x7D0, 0x0)
    OP_8C(0xB, 270, 400)
    OP_0D()
    OP_22(0x13, 0x0, 0x64)
    OP_22(0xCA, 0x0, 0x64)
    SetChrSubChip(0x13, 6)
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x11, 36530, 0, 74730, 180)
    OP_4A(0x11, 255)
    SetChrPos(0x101, 36500, 0, 73200, 0)
    SetChrPos(0x103, 37870, 0, 73310, 315)
    SetChrPos(0xF8, 37500, 0, 72090, 0)
    SetChrPos(0xF9, 36500, 0, 71860, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_26AB")
    SetChrPos(0xF9, 37500, 0, 72090, 0)
    SetChrPos(0xF8, 36500, 0, 71860, 0)

    label("loc_26AB")

    SetChrPos(0xB, 33950, 0, 75000, 90)
    OP_4A(0xB, 255)
    SetChrPos(0xA, 33590, 0, 75990, 120)
    OP_4A(0xC, 255)
    SetChrPos(0xC, 33500, 0, 76920, 120)
    OP_4A(0xA, 255)
    SetChrPos(0x12, 45380, 0, 70160, 300)
    Sleep(5000)
    OP_6D(24580, 0, 77920, 0)
    OP_67(0, 5980, -10000, 0)
    OP_6B(2950, 0)
    OP_6C(315000, 0)
    OP_6E(280, 0)

    def lambda_2743():
        OP_6D(34820, 0, 74740, 4000)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_2743)
    FadeToBright(1000, 0)
    OP_0D()
    WaitChrThread(0x11, 0x1)

    ChrTalk(    #166
        0x11,
        "#2P…………这样啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #167
        0x11,
        (
            "#2P是吗，原始的食谱\x01",
            "已经找不到了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #168
        0x101,
        (
            "#1003F#1P……嗯，很遗憾，\x02\x03",

            "虽然问过了\x01",
            "很多人…\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #169
        0x103,
        (
            "#026F#4P但还是\x01",
            "没有结果呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #170
        0x11,
        (
            "#2P哪里的话，\x01",
            "所谓的原始版也只是我的说法，\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #171
        0x11,
        (
            "#2P你们没必要\x01",
            "放在心上。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #172
        0x11,
        (
            "#2P呼，只是一想到\x01",
            "再也尝不到那种味道，\x01",
            "总还是很失望啊…\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #173
        0xB,
        "喂！爷爷！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #174
        0xB,
        (
            "灰心的话，\x01",
            "现在太早了吧？！\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x11, 0xB, 400)

    ChrTalk(    #175
        0x11,
        "#2P喔……！？\x02",
    )

    CloseMessageWindow()

    def lambda_28D6():
        TurnDirection(0xF6, 0xB, 400)
        ExitThread()

    QueueWorkItem(0xF6, 1, lambda_28D6)
    Sleep(100)

    def lambda_28E9():
        OP_8C(0xF7, 270, 400)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_28E9)

    def lambda_28F7():
        TurnDirection(0xF8, 0xB, 400)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_28F7)
    Sleep(100)

    def lambda_290A():
        TurnDirection(0xF9, 0xB, 400)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_290A)

    ChrTalk(    #176
        0xB,
        (
            "我做的料理应该\x01",
            "不会相差太多。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #177
        0xB,
        (
            "艾丝蒂尔他们辛苦找到的食谱，\x01",
            "味道不会让您失望。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #178
        0xA,
        (
            "说的对，再唠叨个没完，\x01",
            "菜就该凉了。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2999():
        OP_8C(0x101, 0, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2999)
    Sleep(100)

    def lambda_29AC():
        OP_8C(0xF7, 315, 400)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_29AC)

    def lambda_29BA():
        OP_8C(0xF8, 0, 400)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_29BA)
    Sleep(100)

    def lambda_29CD():
        OP_8C(0xF9, 0, 400)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_29CD)
    TurnDirection(0x11, 0xB, 400)

    ChrTalk(    #179
        0x101,
        (
            "#1016F哈哈，是啊，\x02\x03",

            "好不容易做出的料理，\x01",
            "还是趁热吃了吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #180
        0x103,
        (
            "#025F真是的，光顾说别的，\x01",
            "把正事都忘了。\x02\x03",

            "刚才就觉得味道很好闻，\x01",
            "早就忍耐不住了。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2AA7")

    ChrTalk(    #181
        0x107,
        (
            "#067F嘿嘿，总感觉\x01",
            "肚子饿了呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2C06")

    label("loc_2AA7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2B27")

    ChrTalk(    #182
        0x106,
        (
            "#551F啊啊～味道\x01",
            "确实很好闻呢。\x02\x03",

            "#550F可恶……\x01",
            "为什么肚子忽然饿了呢。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x106, 400)

    ChrTalk(    #183
        0x101,
        "#1019F生、生什么气嘛……\x02",
    )

    CloseMessageWindow()
    Jump("loc_2C06")

    label("loc_2B27")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2B88")

    ChrTalk(    #184
        0x108,
        (
            "#071F哈哈，忽然\x01",
            "感觉肚子饿了呢。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x108, 400)

    ChrTalk(    #185
        0x101,
        (
            "#1007F金、金先生\x01",
            "也饿了啊……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2C06")

    label("loc_2B88")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2C06")

    ChrTalk(    #186
        0x104,
        (
            "#031F嗯～确实很能\x01",
            "勾起食欲啊。\x02\x03",

            "#037F如果能有\x01",
            "原来的味道就好了…\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x104, 400)

    ChrTalk(    #187
        0x101,
        (
            "#1007F嗯，马上就要\x01",
            "试吃了啊…\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2C06")

    TurnDirection(0x11, 0x101, 400)

    ChrTalk(    #188
        0x11,
        (
            "#2P啊，真是的，\x01",
            "马上就要有结果了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #189
        0x11,
        (
            "#2P那么，我就不客气\x01",
            "开动了啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x11, 270, 400)

    def lambda_2C66():
        OP_6D(34820, 0, 74740, 1500)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_2C66)

    def lambda_2C7E():
        TurnDirection(0xF6, 0x11, 400)
        ExitThread()

    QueueWorkItem(0xF6, 1, lambda_2C7E)
    Sleep(100)

    def lambda_2C91():
        TurnDirection(0xF7, 0x11, 400)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_2C91)

    def lambda_2C9F():
        TurnDirection(0xF8, 0x11, 400)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_2C9F)
    Sleep(100)

    def lambda_2CB2():
        TurnDirection(0xF9, 0x11, 400)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_2CB2)
    Sleep(1000)

    ChrTalk(    #190
        0x11,
        "#2P呵………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #191
        0x11,
        "#2P嗯…………\x02",
    )

    CloseMessageWindow()
    Sleep(1000)

    ChrTalk(    #192
        0x101,
        "#1002F#1P（咕噜……）\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #193
        0xB,
        "#1P（……真、真紧张啊。）\x02",
    )

    CloseMessageWindow()
    OP_62(0x11, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_63(0x11)
    OP_62(0x11, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #194
        0x11,
        (
            "#2P嗯……………………\x01",
            "………………………\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #195
        0x11,
        "#2P……这、这味道？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #196
        0x101,
        "#1002F#1P怎、怎么了？\x02",
    )

    CloseMessageWindow()
    OP_8C(0x11, 180, 400)

    ChrTalk(    #197
        0x11,
        (
            "#2P这、这……\x01",
            "就是这个啊！！！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #198
        0x11,
        (
            "#3S#2P这就是我做梦都想吃\x01",
            "的炖煮料理啊！！\x02",
        )
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    OP_62(0xC, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0xB, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(100)
    OP_62(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(100)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2ECF")
    OP_62(0xF8, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_2F0D")

    label("loc_2ECF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2EF6")
    OP_62(0xF8, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_2F0D")

    label("loc_2EF6")

    OP_62(0xF8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_2F0D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2F34")
    OP_62(0xF9, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_2F72")

    label("loc_2F34")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2F5B")
    OP_62(0xF9, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_2F72")

    label("loc_2F5B")

    OP_62(0xF9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_2F72")


    ChrTalk(    #199
        0x103,
        "#023F啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #200
        0xA,
        "哎哎哎！？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2FB5")

    ChrTalk(    #201
        0x108,
        "#073F喔……\x02",
    )

    CloseMessageWindow()
    Jump("loc_301C")

    label("loc_2FB5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2FDB")

    ChrTalk(    #202
        0x106,
        "#052F真的吗……\x02",
    )

    CloseMessageWindow()
    Jump("loc_301C")

    label("loc_2FDB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2FFD")

    ChrTalk(    #203
        0x105,
        "#044F啊……\x02",
    )

    CloseMessageWindow()
    Jump("loc_301C")

    label("loc_2FFD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_301C")

    ChrTalk(    #204
        0x104,
        "#033F这……\x02",
    )

    CloseMessageWindow()

    label("loc_301C")


    ChrTalk(    #205
        0xC,
        "真、真的吗！？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x11, 0xC, 400)

    ChrTalk(    #206
        0x11,
        "#2P嗯、嗯，当然是真的。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #207
        0x11,
        (
            "#2P如此怀念的味道\x01",
            "怎么可能记错。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #208
        0x11,
        (
            "#2P我吃过的料理\x01",
            "就是这个！\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xB, 400)

    ChrTalk(    #209
        0x101,
        (
            "#1001F德瑟鲁大叔！好棒啊！！\x02\x03",

            "梦中出现的料理\x01",
            "也能做的出来!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #210
        0xB,
        (
            "嗯、嗯…\x01",
            "确实让我信心大增呢，\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #211
        0xB,
        "不过说实话，这会不会太巧了。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x11, 0xB, 400)

    ChrTalk(    #212
        0x11,
        "#2P啊，不用谦虚。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x11, 400)

    ChrTalk(    #213
        0x11,
        (
            "#2P料理做得很完美，\x01",
            "正是我想要的。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x11, 0, 400)
    OP_62(0x11, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_63(0x11)

    ChrTalk(    #214
        0x11,
        "#2P呼～吃过后让我想起了过去的事情……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #215
        0x11,
        "#2P已经久远模糊的青春……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #216
        0x11,
        (
            "#2P我曾经深爱的那个女孩子\x01",
            "非常擅长制作这道菜，\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #217
        0x11,
        (
            "#2P她嫁人的时候\x01",
            "我一个人默默地躲起来哭泣…\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #218
        0x101,
        (
            "#1016F#1P好、好悲伤\x01",
            "的青春啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #219
        0xC,
        "嘿～第一次听说呢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #220
        0xC,
        (
            "爷爷年轻的时候\x01",
            "也是性情中人啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #221
        0x103,
        "#021F呵呵，年轻人的特权啊。\x02",
    )

    CloseMessageWindow()
    OP_8C(0x11, 180, 400)

    ChrTalk(    #222
        0x11,
        (
            "#2P年轻人的特权吗……\x01",
            "正是如此呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #223
        0x11,
        (
            "#2P现在一切\x01",
            "都已经变了啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #224
        0x11,
        (
            "#2P天使一样的姑娘\x01",
            "如今也变成了满脸皱纹的老太婆。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(1000)
    ClearChrFlags(0x12, 0x80)
    OP_4A(0x12, 255)
    SetChrPos(0x12, 44480, 0, 71450, 270)

    NpcTalk(    #225
        0x12,
        "老婆婆的声音",
        "#5P……你说谁是满脸皱纹的老太婆啊！？\x02",
    )

    CloseMessageWindow()

    def lambda_33C2():

        label("loc_33C2")

        TurnDirection(0xFE, 0x12, 400)
        OP_48()
        Jump("loc_33C2")

    QueueWorkItem2(0x101, 3, lambda_33C2)

    def lambda_33D3():

        label("loc_33D3")

        TurnDirection(0xFE, 0x12, 400)
        OP_48()
        Jump("loc_33D3")

    QueueWorkItem2(0x103, 3, lambda_33D3)

    def lambda_33E4():

        label("loc_33E4")

        TurnDirection(0xFE, 0x12, 400)
        OP_48()
        Jump("loc_33E4")

    QueueWorkItem2(0xF8, 3, lambda_33E4)

    def lambda_33F5():

        label("loc_33F5")

        TurnDirection(0xFE, 0x12, 400)
        OP_48()
        Jump("loc_33F5")

    QueueWorkItem2(0xF9, 3, lambda_33F5)

    def lambda_3406():

        label("loc_3406")

        TurnDirection(0xFE, 0x12, 400)
        OP_48()
        Jump("loc_3406")

    QueueWorkItem2(0xB, 3, lambda_3406)

    def lambda_3417():

        label("loc_3417")

        TurnDirection(0xFE, 0x12, 400)
        OP_48()
        Jump("loc_3417")

    QueueWorkItem2(0xC, 3, lambda_3417)

    def lambda_3428():

        label("loc_3428")

        TurnDirection(0xFE, 0x12, 400)
        OP_48()
        Jump("loc_3428")

    QueueWorkItem2(0xA, 3, lambda_3428)
    OP_8C(0x11, 90, 400)
    OP_62(0x11, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_63(0x11)

    ChrTalk(    #226
        0x11,
        "#2P那、那声音是……\x02",
    )

    CloseMessageWindow()
    OP_6D(40740, 0, 75420, 3000)
    Sleep(1000)

    def lambda_348E():
        OP_6D(35940, 0, 74450, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_348E)
    OP_8E(0x12, 0x9DDA, 0x0, 0x12354, 0x7D0, 0x0)
    OP_8E(0x12, 0x9628, 0x0, 0x123F4, 0x7D0, 0x0)
    OP_44(0x101, 0x3)
    OP_44(0x103, 0x3)
    OP_44(0xF8, 0x3)
    OP_44(0xF9, 0x3)
    OP_44(0xB, 0x3)
    OP_44(0xC, 0x3)
    OP_44(0xA, 0x3)

    ChrTalk(    #227
        0xB,
        "布露姆老奶奶……！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #228
        0x12,
        (
            "竟然在这么多人面前\x01",
            "说别人的坏话！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #229
        0x12,
        (
            "你还是和以前一样，\x01",
            "一点都没变。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x11, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)
    OP_63(0x11)

    ChrTalk(    #230
        0x11,
        (
            "#2P啊、啊，那\x01",
            "只是随口一说…\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #231
        0xB,
        (
            "怎么了？婆婆，\x01",
            "您难得来这里啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #232
        0xA,
        "#2P嗯，好久不见啦。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #233
        0x12,
        (
            "刚才这些孩子\x01",
            "来我家问食谱，\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #234
        0x12,
        (
            "因为有点在意，\x01",
            "就过来看看。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xB, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_63(0xB)

    ChrTalk(    #235
        0xB,
        "啊？那食谱是？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #236
        0x12,
        "嗯，是我家的家传食谱。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #237
        0x12,
        (
            "在我年轻的时候，\x01",
            "是我最擅长的一道料理。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #238
        0x12,
        (
            "当时也经常做给\x01",
            "这老家伙吃呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #239
        0x101,
        "#1004F这、这么说的话……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #240
        0xA,
        (
            "#2P爷、爷爷年轻时喜欢\x01",
            "的那个女孩，就是…\x02",
        )
    )

    CloseMessageWindow()

    def lambda_370E():
        TurnDirection(0xFE, 0x11, 400)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_370E)
    Sleep(150)

    def lambda_3721():
        TurnDirection(0xFE, 0x11, 400)
        ExitThread()

    QueueWorkItem(0x103, 3, lambda_3721)

    def lambda_372F():
        TurnDirection(0xFE, 0x11, 400)
        ExitThread()

    QueueWorkItem(0xC, 3, lambda_372F)
    Sleep(150)

    def lambda_3742():
        TurnDirection(0xFE, 0x11, 400)
        ExitThread()

    QueueWorkItem(0xF8, 3, lambda_3742)

    def lambda_3750():
        TurnDirection(0xFE, 0x11, 400)
        ExitThread()

    QueueWorkItem(0xF9, 3, lambda_3750)
    Sleep(1000)
    OP_62(0x11, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #241
        0x11,
        "#2P嗯，啊啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #242
        0x11,
        (
            "#2P呼～岁月的流逝\x01",
            "真是残酷啊…\x02",
        )
    )

    CloseMessageWindow()

    def lambda_37B8():
        TurnDirection(0xFE, 0x12, 400)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_37B8)

    def lambda_37C6():
        TurnDirection(0xFE, 0x12, 400)
        ExitThread()

    QueueWorkItem(0x103, 3, lambda_37C6)

    def lambda_37D4():
        TurnDirection(0xFE, 0x12, 400)
        ExitThread()

    QueueWorkItem(0xF8, 3, lambda_37D4)

    def lambda_37E2():
        TurnDirection(0xFE, 0x12, 400)
        ExitThread()

    QueueWorkItem(0xF9, 3, lambda_37E2)
    Sleep(1000)
    TurnDirection(0x12, 0x101, 400)

    ChrTalk(    #243
        0x12,
        "啊？怎么啦？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #244
        0x101,
        "#1016F嗯，也没什么啦……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x12, 0x11, 400)

    ChrTalk(    #245
        0x12,
        "算啦，不管怎样，\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #246
        0x12,
        (
            "再次回忆到这料理\x01",
            "真是很高兴。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #247
        0x12,
        (
            "嗯，难得过来一趟，\x01",
            "好久没做料理了，就试着再做一次吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #248
        0x12,
        (
            "你们也想见识一下\x01",
            "正宗风味吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #249
        0x101,
        "#1018F啊～当然⊙\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #250
        0xB,
        "非常期待啊！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #251
        0xB,
        (
            "我也想学习一下\x01",
            "正宗的烹饪方法呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #252
        0x12,
        "那么，厨房借用一下。\x02",
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_28(0x75, 0x1, 0x1000)
    OP_28(0x75, 0x4, 0x10)
    Sleep(1000)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x20D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3998")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_AC(0x20)"), scpexpr(EXPR_END)), "loc_3962")
    Jump("loc_3998")

    label("loc_3962")

    OP_AC(0x20)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #253
        "\x06\x07\x02香辣炖煮\x07\x00的做法已经学会了。\x02",
    )

    CloseMessageWindow()

    label("loc_3998")

    OP_3F(0x236, 1)
    Sleep(400)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x17, 0x0, 0x64)

    AnonymousTalk(    #254
        "\x07\x02任务【怀念的料理】\x07\x00完成了！\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    NewScene("ED6_DT21/T0100   ._SN", 114, 0, 0)
    IdleLoop()
    Return()

    # Function_7_248F end

    SaveToFile()

Try(main)

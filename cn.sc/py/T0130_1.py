from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 洛连特

    CreateScenaFile(
        FileName            = 'T0130_1 ._SN',
        MapName             = 'Rolent',
        Location            = 'C0403.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60010",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            '',
            'ED6_DT21/T0130_1 ._SN',
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
        "Function_1_8AF",          # 01, 1
        "Function_2_9F3",          # 02, 2
        "Function_3_1826",         # 03, 3
        "Function_4_1E6E",         # 04, 4
        "Function_5_1F66",         # 05, 5
        "Function_6_2033",         # 06, 6
        "Function_7_263F",         # 07, 7
        "Function_8_33C0",         # 08, 8
        "Function_9_340F",         # 09, 9
        "Function_10_3457",        # 0A, 10
    )


    def Function_0_AA(): pass

    label("Function_0_AA")

    EventBegin(0x0)
    Fade(1000)
    Call(1, 4)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x340, 0)), scpexpr(EXPR_END)), "loc_158")

    ChrTalk(    #0
        0xFE,
        (
            "嗯～…………\x01",
            "虽然大圣堂也很有吸引力，\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        (
            "但结婚仪式还是\x01",
            "在家乡洛连特举办最好啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0xFE,
        (
            "在初次相遇的地方进行爱的宣誓… \x01",
            "真有种神圣又纯粹的感觉啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_293")

    label("loc_158")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x304, 2)), scpexpr(EXPR_END)), "loc_1AF")

    ChrTalk(    #3
        0xFE,
        "啊啊～～我可爱的艾娅莉啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0xFE,
        (
            "我要像浓雾包裹城镇那样\x01",
            "将你紧紧抱住。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_293")

    label("loc_1AF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 4)), scpexpr(EXPR_END)), "loc_1ED")

    ChrTalk(    #5
        0xFE,
        "再离我近一点，艾娅莉！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0xFE,
        "我只想看你的笑脸。\x02",
    )

    CloseMessageWindow()
    Jump("loc_293")

    label("loc_1ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x301, 4)), scpexpr(EXPR_END)), "loc_293")

    ChrTalk(    #7
        0xFE,
        "啊啊！！美丽的诞辰庆典之夜！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0xFE,
        (
            "艾娅莉……每次看到你的脸\x01",
            "就会想起那个美妙的夜晚。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0xFE,
        "在星空和花火的映衬下，\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0xFE,
        (
            "我鼓起勇气向你袒露\x01",
            "心意的那个夜晚… \x02",
        )
    )

    CloseMessageWindow()

    label("loc_293")


    ChrTalk(    #11
        0x101,
        (
            "#1007F#3P打、打扰了……\x02\x03",

            "请问现在方便吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xF, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(    #12
        0xF,
        "嗯……？\x02",
    )

    CloseMessageWindow()

    def lambda_2ED():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_2ED)
    Sleep(250)
    TurnDirection(0x10, 0x101, 400)

    ChrTalk(    #13
        0x10,
        "#2P……啊，是谁？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x101,
        (
            "#1000F#3P我们是游击士协会的人。\x02\x03",

            "您就是阿鲁姆先生吗？\x01",
            "我们是看了告示板上的委托而来的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0xF,
        "哇～终于来了吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0xF,
        (
            "太好了！\x01",
            "我等你们好久了！！\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x10, 0xF, 400)

    ChrTalk(    #17
        0x10,
        (
            "#2P太好了！阿鲁姆！\x01",
            "我好高兴啊！\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xF, 0x10, 400)

    ChrTalk(    #18
        0xF,
        "啊啊～艾娅莉。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0xF,
        (
            "你的心灵为什么\x01",
            "这样美丽？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0xF,
        (
            "明明让你痛苦\x01",
            "的人就是我…\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x10,
        "#2P不要那么说，阿鲁姆。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x10,
        (
            "#2P你心中的痛苦\x01",
            "我全都明白！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x10,
        (
            "#2P那一夜，咱们不是约定好了吗？\x01",
            "不管到什么时候，你和我……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0xF,
        (
            "……也要携手\x01",
            "走完一生…\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0xF,
        "啊啊！！艾娅莉！我爱你！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x10,
        "#2P我也是啊！阿鲁姆！！\x02",
    )

    CloseMessageWindow()
    OP_62(0x29, 0x0, 1700, 0xA, 0xB, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(1500)
    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(150)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_57E")
    OP_62(0xF8, 0x0, 2300, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jump("loc_5BC")

    label("loc_57E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5A5")
    OP_62(0xF8, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jump("loc_5BC")

    label("loc_5A5")

    OP_62(0xF8, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)

    label("loc_5BC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5E3")
    OP_62(0xF9, 0x0, 2300, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jump("loc_621")

    label("loc_5E3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_60A")
    OP_62(0xF9, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jump("loc_621")

    label("loc_60A")

    OP_62(0xF9, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)

    label("loc_621")

    Sleep(1000)

    ChrTalk(    #27
        0x101,
        (
            "#1016F#3P那、那个～……\x02\x03",

            "您有什么\x01",
            "请求呢？\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xF, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(400)

    ChrTalk(    #28
        0xF,
        "啊……！！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x10,
        "#2P对了！委托！！\x02",
    )

    CloseMessageWindow()

    def lambda_69A():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_69A)
    Sleep(150)
    TurnDirection(0x10, 0x101, 400)

    ChrTalk(    #30
        0xF,
        (
            "其、其实是一件关系到我们两个\x01",
            "将来的重要事件！！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0xF,
        (
            "希望你们马上就开始调查，\x01",
            "可以吗？\x02",
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_762")
    Call(1, 2)
    Jump("loc_896")

    label("loc_762")


    ChrTalk(    #32
        0x101,
        (
            "#1015F#3P啊～抱歉。\x02\x03",

            "马上开始的话\x01",
            "可能有些困难。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0xF,
        (
            "怎、怎么会…\x01",
            "请不要抛弃我们啊！！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x10,
        (
            "#2P求你们了……\x01",
            "这件事真的很重要！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x103,
        (
            "#020F没关系，\x01",
            "我们会回来的，放心吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x101,
        (
            "#1000F#3P嗯，等我们有空的时候\x01",
            "一定回来仔细听你们说。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0xF,
        "真、真的吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0xF,
        (
            "好、好… \x01",
            "我相信你们。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0x10,
        "#2P一定要再来啊。\x02",
    )

    CloseMessageWindow()
    OP_28(0x72, 0x1, 0x8000)

    label("loc_896")

    TurnDirection(0x10, 0xF, 0)
    TurnDirection(0xF, 0x10, 0)
    OP_4B(0xF, 255)
    OP_4B(0x10, 255)
    EventEnd(0x0)
    Return()

    # Function_0_AA end

    def Function_1_8AF(): pass

    label("Function_1_8AF")

    EventBegin(0x0)
    Fade(1000)
    Call(1, 4)
    OP_8C(0xF, 270, 0)
    OP_8C(0x10, 270, 0)
    OP_0D()

    ChrTalk(    #40
        0xF,
        "那个，各位游击士……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0xF,
        (
            "你们..可以接受\x01",
            "我的委托吗？\x02",
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_95C")
    Call(1, 2)
    Jump("loc_9DA")

    label("loc_95C")


    ChrTalk(    #42
        0x101,
        (
            "#1007F呼、呼……\x01",
            "现在确实还有点为难呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0xF,
        "怎、怎么会…\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0x101,
        (
            "#1016F抱歉抱歉。\x01",
            "下次再来听你们说明。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0x10,
        "嗯，会再来的。\x02",
    )

    CloseMessageWindow()

    label("loc_9DA")

    TurnDirection(0x10, 0xF, 0)
    TurnDirection(0xF, 0x10, 0)
    OP_4B(0xF, 255)
    OP_4B(0x10, 255)
    EventEnd(0x0)
    Return()

    # Function_1_8AF end

    def Function_2_9F3(): pass

    label("Function_2_9F3")


    ChrTalk(    #46
        0x101,
        (
            "#1006F啊，嗯。\x01",
            "没问题。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x304, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_AD1")

    ChrTalk(    #47
        0xF,
        "真、真的吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0x103,
        (
            "#020F只是，既然很急的话，\x01",
            "就麻烦您长话短说吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0xF,
        "啊啊～那个倒无所谓！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0xF,
        (
            "呀～不管怎样，\x01",
            "多谢你们了，游击士！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0xF,
        (
            "你们能来……\x01",
            "真是救了我们一命啊！！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B0A")

    label("loc_AD1")


    ChrTalk(    #52
        0xF,
        "真、真的吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0xF,
        (
            "太感谢了！！\x01",
            "谢谢了！！游击士！！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B0A")

    TurnDirection(0x10, 0xF, 400)

    ChrTalk(    #54
        0x10,
        (
            "#2P太好了！阿鲁姆！\x01",
            "我好高兴啊！\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xF, 0x10, 400)

    ChrTalk(    #55
        0xF,
        "啊啊～艾娅莉。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0xF,
        (
            "为什么你的心灵\x01",
            "这样美丽？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0x10,
        "#2P啊啊～阿鲁姆……\x02",
    )

    CloseMessageWindow()
    Sleep(1000)

    ChrTalk(    #58
        0x101,
        (
            "#1019F#4S……#2S\x02\x03",

            "……我说委托的事……～？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_BC5():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_BC5)
    Sleep(150)
    TurnDirection(0x10, 0x101, 400)

    ChrTalk(    #59
        0xF,
        "……失礼了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0xF,
        "那么，请听我说吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0x103,
        "#020F嗯，可能的话，请您尽量说简洁点。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0xF,
        (
            "想委托各位帮忙的事情并不是别的，\x01",
            "就是寻找我们的结婚戒指。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0xF,
        (
            "我拼命攒钱，好不容易\x01",
            "买到了那个高档戒指，可是… \x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0xF,
        (
            "那、那只可恨的小偷乌鸦，\x01",
            "竟然把它给偷走了！！！\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #65
        0x101,
        "#1004F#3P乌、乌鸦！？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D3F")

    ChrTalk(    #66
        0x107,
        "#064F乌鸦……是那只鸟吗？\x02",
    )

    CloseMessageWindow()
    Jump("loc_DD8")

    label("loc_D3F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D73")

    ChrTalk(    #67
        0x105,
        "#044F乌鸦吗……难道是那只鸟？\x02",
    )

    CloseMessageWindow()
    Jump("loc_DD8")

    label("loc_D73")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_DAB")

    ChrTalk(    #68
        0x104,
        "#033F所谓的乌鸦……是指那只鸟吗？\x02",
    )

    CloseMessageWindow()
    Jump("loc_DD8")

    label("loc_DAB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_DD8")

    ChrTalk(    #69
        0x106,
        "#052F乌鸦……是那只鸟吗？\x02",
    )

    CloseMessageWindow()

    label("loc_DD8")


    ChrTalk(    #70
        0xF,
        "对！总之就是那个哇哇叫的混帐了！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0xF,
        (
            "那个可恶的家伙竟然\x01",
            "把我们的结婚戒指给叼跑了！！\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x72, 0x1, 0x4000)"), scpexpr(EXPR_EXEC_OP, "OP_40(0x234, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1223")

    ChrTalk(    #72
        0x103,
        (
            "#026F确实，乌鸦的习性就是\x01",
            "喜欢收集闪光的东西呢。\x02\x03",

            "#027F话虽如此……\x01",
            "戒指被乌鸦偷走，还真是……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 400)

    ChrTalk(    #73
        0x101,
        (
            "#1011F啊，难道说……\x02\x03",

            "雪拉姐也\x01",
            "想起那个戒指了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0x103,
        (
            "#020F嗯，保险起见，\x01",
            "最好是给他看看吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0xF,
        "？？？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0xF,
        "有什么线索吗？\x02",
    )

    CloseMessageWindow()
    OP_8C(0x101, 90, 400)

    ChrTalk(    #77
        0x101,
        (
            "#1002F阿鲁姆先生，请您\x01",
            "看一下这只戒指可以吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #78 op#A
        0xF,
        "#22A嗯，当然……\x02",
    )
    Sleep(2300)

    Call(1, 5)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #79
        0x101,
        "#1004F咦咦！？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_FF7")

    ChrTalk(    #80
        0x107,
        (
            "#064F那个那个……\x01",
            "确实就是这只戒指吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10A2")

    label("loc_FF7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1023")

    ChrTalk(    #81
        0x105,
        "#044F没、没搞错吗！？\x02",
    )

    CloseMessageWindow()
    Jump("loc_10A2")

    label("loc_1023")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_104F")

    ChrTalk(    #82
        0x104,
        "#033F那个，没弄错吗？\x02",
    )

    CloseMessageWindow()
    Jump("loc_10A2")

    label("loc_104F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_107F")

    ChrTalk(    #83
        0x106,
        "#055F喂喂，不会是真的吧？\x02",
    )

    CloseMessageWindow()
    Jump("loc_10A2")

    label("loc_107F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_10A2")

    ChrTalk(    #84
        0x108,
        "#073F没弄错吗？\x02",
    )

    CloseMessageWindow()

    label("loc_10A2")


    ChrTalk(    #85
        0xF,
        "嗯、嗯……绝对没错！！！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #86
        0xF,
        "这就是我们的戒指！！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0x10,
        (
            "#2P啊啊！！女神啊……\x01",
            "衷心感谢您的恩德！！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0x103,
        (
            "#021F呵呵，没想到\x01",
            "会这么巧啊。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_115C")

    ChrTalk(    #89
        0x108,
        "#073F真是惊人的巧合呢。\x02",
    )

    CloseMessageWindow()
    Jump("loc_11F0")

    label("loc_115C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_118C")

    ChrTalk(    #90
        0x106,
        "#052F真是好惊人的巧合呢。\x02",
    )

    CloseMessageWindow()
    Jump("loc_11F0")

    label("loc_118C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_11C3")

    ChrTalk(    #91
        0x104,
        (
            "#031F哈哈哈。\x01",
            "真是惊人的巧合啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_11F0")

    label("loc_11C3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_11F0")

    ChrTalk(    #92
        0x105,
        "#044F好、好惊人的巧合啊。\x02",
    )

    CloseMessageWindow()

    label("loc_11F0")

    Call(1, 6)
    OP_28(0x72, 0x1, 0x8)
    OP_28(0x72, 0x1, 0x10)
    OP_28(0x72, 0x4, 0x10)
    TurnDirection(0x10, 0xF, 0)
    TurnDirection(0xF, 0x10, 0)
    OP_63(0x29)
    OP_4B(0xF, 255)
    OP_4B(0x10, 255)
    EventEnd(0x0)
    Jump("loc_1825")

    label("loc_1223")


    ChrTalk(    #93
        0x103,
        (
            "#027F确实，乌鸦具有\x01",
            "喜欢收集闪亮东西的习性。\x02\x03",

            "所以会对戒指这种东西\x01",
            "感兴趣的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0x101,
        (
            "#1015F#3P那么，戒指现在\x01",
            "应该在它们的巢中吧。\x02\x03",

            "#1002F是让我们来找那戒指的吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0xF,
        (
            "嗯，那就是我们\x01",
            "想委托你们办的事情。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #96
        0xF,
        (
            "虽然我明白，\x01",
            "这件事很困难。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0xF,
        (
            "但即使如此，\x01",
            "也拜托你们尽力帮我们吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0x101,
        (
            "#1007F#3P嗯，我们肯定\x01",
            "会尽力而为，不过…\x02\x03",

            "以现有的情报来说，\x01",
            "实在是不容易找到。\x02\x03",

            "#1002F……能不能再提供给我们一些线索呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0xF,
        (
            "啊啊，是要寻找\x01",
            "乌鸦的巢穴了吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0xF,
        "大概在洛连特北部吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0xF,
        (
            "那家伙飞向玛鲁加山道\x01",
            "那边去了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0xF,
        (
            "再加上现在起了大雾，\x01",
            "能追上的可能性不大了吧…\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x72, 0x1, 0x4000)"), scpexpr(EXPR_EXEC_OP, "OP_40(0x234, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1557")

    ChrTalk(    #103
        0x101,
        (
            "#1015F#3P原来如此。\x02\x03",

            "巢穴大概在北边吗……\x02\x03",

            "…啊？北边？\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x14, 0x17, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)
    OP_63(0x101)

    ChrTalk(    #104
        0x101,
        (
            "#1019F#3P（难、难道说……）\x02\x03",

            "（在塔顶上\x01",
            "  发现的那个戒指…）\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0xF,
        "嗯？怎么啦？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #106
        0x101,
        (
            "#1016F#3P呼、呼呼。没什么。\x01",
            "（一定只是心理作用吧～）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1586")

    label("loc_1557")


    ChrTalk(    #107
        0x101,
        (
            "#1015F#3P原来如此。\x02\x03",

            "巢穴大概在北边吗……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1586")


    ChrTalk(    #108
        0x103,
        (
            "#026F……我们会做个参考的。\x02\x03",

            "不管怎样，巢穴肯定\x01",
            "是在高处就对了。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_161D")

    ChrTalk(    #109
        0x108,
        (
            "#075F啊，那肯定没错的。\x02\x03",

            "真是的……\x01",
            "这真是个麻烦的工作啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_16E6")

    label("loc_161D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_166C")

    ChrTalk(    #110
        0x106,
        (
            "#551F嗯，那肯定没错。\x02\x03",

            "真是的……\x01",
            "还真是个麻烦的工作啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_16E6")

    label("loc_166C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_16BB")

    ChrTalk(    #111
        0x104,
        (
            "#034F嗯，那是肯定的啦。\x02\x03",

            "呼～还真是件\x01",
            "超级麻烦的工作啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_16E6")

    label("loc_16BB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_16E6")

    ChrTalk(    #112
        0x105,
        "#047F嗯，确实比较麻烦。\x02",
    )

    CloseMessageWindow()

    label("loc_16E6")


    ChrTalk(    #113
        0xF,
        (
            "除了协会之外，\x01",
            "我们再也找不到人可以拜托了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #114
        0xF,
        (
            "所以无论如何\x01",
            "你们也要帮帮忙啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0x10,
        (
            "#2P你们是我们唯一的希望了。\x01",
            "无论如何也请帮忙找找吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #116
        0x101,
        (
            "#1006F#3P嗯……\x01",
            "我们会努力找找看的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #117
        0x103,
        (
            "#020F那么，有什么发现的话，\x01",
            "我们会再来报告给您。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #118
        0xF,
        "期待大家！我们会一直等的！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #119
        0x10,
        "#2P加油哦！\x02",
    )

    CloseMessageWindow()
    OP_28(0x72, 0x4, 0x4)
    OP_28(0x72, 0x4, 0x8)
    OP_28(0x72, 0x1, 0x1)
    OP_28(0x72, 0x1, 0x2)
    OP_A2(0xB)
    ClearChrFlags(0xF, 0x10)

    label("loc_1825")

    Return()

    # Function_2_9F3 end

    def Function_3_1826(): pass

    label("Function_3_1826")

    EventBegin(0x0)
    Fade(1000)
    Call(1, 4)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x340, 0)), scpexpr(EXPR_END)), "loc_18D4")

    ChrTalk(    #120
        0xFE,
        (
            "嗯～…………\x01",
            "虽然大圣堂也很有吸引力，\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #121
        0xFE,
        (
            "但结婚仪式还是\x01",
            "在家乡洛连特举办最好啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #122
        0xFE,
        (
            "在初次相遇的地方进行爱的宣誓… \x01",
            "真有种神圣又纯粹的感觉啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A0F")

    label("loc_18D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x304, 2)), scpexpr(EXPR_END)), "loc_192B")

    ChrTalk(    #123
        0xFE,
        "啊啊～～我可爱的艾娅莉啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #124
        0xFE,
        (
            "我要像浓雾包裹城镇那样\x01",
            "将你紧紧抱住。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A0F")

    label("loc_192B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 4)), scpexpr(EXPR_END)), "loc_1969")

    ChrTalk(    #125
        0xFE,
        "再离我近一点，艾娅莉！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #126
        0xFE,
        "我只想看你的笑脸。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1A0F")

    label("loc_1969")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x301, 4)), scpexpr(EXPR_END)), "loc_1A0F")

    ChrTalk(    #127
        0xFE,
        "啊啊！！美丽的诞辰庆典之夜！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #128
        0xFE,
        (
            "艾娅莉……每次看到你的脸\x01",
            "就会想起那个美妙的夜晚。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #129
        0xFE,
        "在星空和花火的映衬下，\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #130
        0xFE,
        (
            "我鼓起勇气向你袒露\x01",
            "心意的那个夜晚… \x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A0F")


    ChrTalk(    #131
        0x101,
        "#1007F（还、还没停啊……）\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #132
        0xF,
        "嗯……？\x02",
    )

    CloseMessageWindow()

    def lambda_1A43():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_1A43)
    Sleep(250)
    TurnDirection(0x10, 0x101, 400)

    ChrTalk(    #133
        0x10,
        "#2P……啊，游击士啊。\x02",
    )

    CloseMessageWindow()
    OP_62(0xF, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_63(0xF)

    ChrTalk(    #134
        0xF,
        (
            "难、难道\x01",
            "你们找到戒指了！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #135
        0x103,
        (
            "#020F嗯，找到了一只符合您\x01",
            "说明的戒指。\x02\x03",

            "但不知道是不是您\x01",
            "丢失的那个。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #136
        0x101,
        (
            "#1000F所以\x01",
            "希望您能确认一下。\x02\x03",

            "阿鲁姆先生，\x01",
            "看一下这只戒指可以吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #137 op#A
        0xF,
        "#22A嗯，当然……\x02",
    )
    Sleep(2000)

    Call(1, 5)

    ChrTalk(    #138
        0x101,
        "#1004F真、真的！？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1BAD")

    ChrTalk(    #139
        0x107,
        (
            "#064F那个那个……\x01",
            "确实就是这只戒指吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C58")

    label("loc_1BAD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1BD9")

    ChrTalk(    #140
        0x105,
        "#044F没、没搞错吗！？\x02",
    )

    CloseMessageWindow()
    Jump("loc_1C58")

    label("loc_1BD9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1C05")

    ChrTalk(    #141
        0x104,
        "#033F那个，没弄错吗？\x02",
    )

    CloseMessageWindow()
    Jump("loc_1C58")

    label("loc_1C05")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1C35")

    ChrTalk(    #142
        0x106,
        "#055F喂喂，不会是真的吧？\x02",
    )

    CloseMessageWindow()
    Jump("loc_1C58")

    label("loc_1C35")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1C58")

    ChrTalk(    #143
        0x108,
        "#073F没弄错吗？\x02",
    )

    CloseMessageWindow()

    label("loc_1C58")


    ChrTalk(    #144
        0xF,
        "嗯、嗯……绝对没错！！！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #145
        0xF,
        "这就是我们的戒指！！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #146
        0x10,
        (
            "#2P啊啊！！女神啊……\x01",
            "衷心感谢您的恩德！！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #147
        0x103,
        (
            "#021F呵呵，太好了。\x01",
            "终于物归原主了啊。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1D33")

    ChrTalk(    #148
        0x108,
        (
            "#070F呼，真是没想到啊，\x02\x03",

            "竟然会在那种\x01",
            "地方找到。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E43")

    label("loc_1D33")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1D99")

    ChrTalk(    #149
        0x105,
        (
            "#040F太好了……\x01",
            "这样的话事情也就解决了。\x02\x03",

            "真是做梦也想不到会在\x01",
            "那种地方找到啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E43")

    label("loc_1D99")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1DF5")

    ChrTalk(    #150
        0x106,
        (
            "#051F啊啊，总算是解决了，\x01",
            "松了口气。\x02\x03",

            "真是没想到会在\x01",
            "那种地方找到啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E43")

    label("loc_1DF5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1E43")

    ChrTalk(    #151
        0x104,
        (
            "#030F呼～真是不容易啊。\x02\x03",

            "真没想到竟然会在\x01",
            "那种地方找到啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E43")

    Call(1, 6)
    OP_28(0x72, 0x1, 0x10)
    OP_28(0x72, 0x4, 0x10)
    TurnDirection(0x10, 0xF, 0)
    TurnDirection(0xF, 0x10, 0)
    OP_63(0x29)
    OP_4B(0xF, 255)
    OP_4B(0x10, 255)
    EventEnd(0x0)
    Return()

    # Function_3_1826 end

    def Function_4_1E6E(): pass

    label("Function_4_1E6E")

    OP_4A(0xF, 255)
    OP_4A(0x10, 255)
    SetChrPos(0x101, 62800, 0, 47270, 90)
    SetChrPos(0x103, 61790, 0, 46800, 90)
    SetChrPos(0xF8, 61270, 0, 47980, 90)
    SetChrPos(0xF9, 60320, 0, 47290, 90)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1EE9")
    SetChrPos(0xF9, 61270, 0, 47980, 90)
    SetChrPos(0xF8, 60320, 0, 47290, 90)

    label("loc_1EE9")

    OP_6D(61800, 0, 48260, 0)
    OP_67(0, 6130, -10000, 0)
    OP_6B(2870, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    OP_51(0x29, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0x10, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x29, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0x10, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x29, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0x10, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_4_1E6E end

    def Function_5_1F66(): pass

    label("Function_5_1F66")

    OP_94(0x1, 0xF, 0x0, 0xC8, 0x3E8, 0x0)
    OP_56(0x0)
    OP_59()
    OP_62(0xF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(100)

    def lambda_1F9A():
        OP_95(0xFE, 0x0, 0x0, 0x0, 0x190, 0xFA0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_1F9A)
    Sleep(900)
    OP_63(0xF)
    WaitChrThread(0xF, 0x1)

    ChrTalk(    #152
        0xF,
        "#3S……啊啊啊啊啊啊啊！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #153
        0xF,
        "那那那、那个戒指！！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #154
        0xF,
        "#3S那不就是我、我们的结婚戒指吗！！\x02",
    )

    OP_7C(0x0, 0x1F4, 0xBB8, 0x64)
    CloseMessageWindow()
    Return()

    # Function_5_1F66 end

    def Function_6_2033(): pass

    label("Function_6_2033")


    ChrTalk(    #155
        0x101,
        (
            "#1015F呼，真是无话可说了…\x02\x03",

            "城镇市民的戒指\x01",
            "最后竟然在塔顶找到…\x02\x03",

            "#1000F……呵呵～不过还是\x01",
            "先把戒指还给他吧。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #156
        "\x1F\x34\x02\x07\x00交出了。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3F(0x234, 1)
    OP_94(0x1, 0xF, 0xB4, 0xC8, 0x3E8, 0x0)

    ChrTalk(    #157
        0xF,
        "啊，谢谢……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #158
        0xF,
        "真是感激不尽！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #159
        0x10,
        (
            "#2P呵呵，相信游击士\x01",
            "果然没有错㈱\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #160
        0x101,
        "#1017F哪里哪里，没什么。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #161
        0x103,
        (
            "#020F马上就要\x01",
            "结婚了吗？\x02\x03",

            "#525F祝你们幸福哦㈱\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(    #162
        0x10,
        (
            "#2P喔…………\x01",
            "啊，谢谢！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #163
        0x10,
        (
            "#2P感、感觉真好啊！\x01",
            "被人祝福的感觉…\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xF, 0x10, 400)

    ChrTalk(    #164
        0xF,
        "不过我们会尽快习惯的！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #165
        0xF,
        (
            "我们的未来一定会\x01",
            "得到无数的祝福的！\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x10, 0xF, 400)

    ChrTalk(    #166
        0x10,
        "#2P啊啊～阿鲁姆……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #167
        0xF,
        "艾娅莉……\x02",
    )

    CloseMessageWindow()
    OP_62(0x29, 0x0, 1800, 0xA, 0xB, 0xFA, 0x0)
    Sleep(1000)
    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(100)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_22E1")
    OP_62(0xF8, 0x0, 2300, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jump("loc_231F")

    label("loc_22E1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2308")
    OP_62(0xF8, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jump("loc_231F")

    label("loc_2308")

    OP_62(0xF8, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)

    label("loc_231F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2346")
    OP_62(0xF9, 0x0, 2300, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jump("loc_2384")

    label("loc_2346")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_236D")
    OP_62(0xF9, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jump("loc_2384")

    label("loc_236D")

    OP_62(0xF9, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)

    label("loc_2384")

    Sleep(1000)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_23CF")

    ChrTalk(    #168
        0x107,
        (
            "#067F（啊哈～……\x01",
            "　完全沉浸在二人世界中了啊。)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2480")

    label("loc_23CF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_240D")

    ChrTalk(    #169
        0x105,
        "#540F（完、完全沉浸在二人世界中了啊。）\x02",
    )

    CloseMessageWindow()
    Jump("loc_2480")

    label("loc_240D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_244B")

    ChrTalk(    #170
        0x104,
        "#030F（呼～彻底沉浸在二人世界里了啊。）\x02",
    )

    CloseMessageWindow()
    Jump("loc_2480")

    label("loc_244B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2480")

    ChrTalk(    #171
        0x108,
        "#070F（这就是所谓的二人世界吗。）\x02",
    )

    CloseMessageWindow()

    label("loc_2480")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_24BA")

    ChrTalk(    #172
        0x106,
        "#552F（好像完全无视我们的存在呢。）\x02",
    )

    CloseMessageWindow()
    Jump("loc_255D")

    label("loc_24BA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_24F4")

    ChrTalk(    #173
        0x108,
        "#071F（哈哈，恋爱果然是盲目的呢。）\x02",
    )

    CloseMessageWindow()
    Jump("loc_255D")

    label("loc_24F4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_252E")

    ChrTalk(    #174
        0x104,
        "#031F（呵呵，恋爱果然是盲目的啊。）\x02",
    )

    CloseMessageWindow()
    Jump("loc_255D")

    label("loc_252E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_255D")

    ChrTalk(    #175
        0x105,
        "#048F（不过……真不错呢。）\x02",
    )

    CloseMessageWindow()

    label("loc_255D")


    ChrTalk(    #176
        0x103,
        (
            "#020F（咱们好像太打扰他们了……\x01",
            "　还是赶快离开吧。)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #177
        0x101,
        (
            "#1013F（说、说的是啊。）\x02\x03",

            "#1016F那、那么，\x01",
            "我们这就走了哦～\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x17, 0x0, 0x64)

    AnonymousTalk(    #178
        "\x07\x02任务【消失在天空的定婚戒指】\x07\x00完成了！\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrFlags(0xF, 0x10)
    SetChrFlags(0x10, 0x10)
    OP_A2(0xC)
    Return()

    # Function_6_2033 end

    def Function_7_263F(): pass

    label("Function_7_263F")

    EventBegin(0x0)
    OP_D2(0x700A8, 0x700AC, 0x8)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x8, -17310, 0, 42890, 270)
    SetChrPos(0x11, -15330, 0, 42890, 270)
    SetChrPos(0x101, -16070, 0, 44880, 180)
    SetChrPos(0x103, -15100, 0, 45270, 180)
    SetChrPos(0xF8, -16480, 0, 46150, 180)
    SetChrPos(0xF9, -15220, 0, 46480, 180)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_26E5")
    SetChrPos(0xF9, -16480, 0, 46150, 180)
    SetChrPos(0xF8, -15220, 0, 46480, 180)

    label("loc_26E5")

    OP_6D(-17110, 0, 44470, 0)
    OP_67(0, 6150, -10000, 0)
    OP_6B(2750, 0)
    OP_6C(315000, 0)
    OP_6E(280, 0)
    OP_4A(0x8, 255)
    SetChrFlags(0x9, 0x80)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(2000)
    OP_8F(0x8, 0xFFFFBE42, 0x0, 0xA78A, 0x3E8, 0x0)

    ChrTalk(    #179
        0x8,
        "──嗯。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x11, 400)

    ChrTalk(    #180
        0x8,
        (
            "让您久等了。\x01",
            "药已经做完了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #181
        0x8,
        (
            "请拿去吧。\x01",
            "这就是『千杯不醉的秘药』。\x02",
        )
    )

    CloseMessageWindow()
    OP_8E(0x11, 0xFFFFC2A2, 0x0, 0xA78A, 0x3E8, 0x0)

    ChrTalk(    #182
        0x11,
        (
            "咕、咕噜……（吞口水）\x01",
            "这就是我一直苦苦寻找的秘药……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #183
        0x11,
        (
            "服下之后不管怎么喝酒\x01",
            "也绝不会喝醉的秘药吗……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #184
        0x8,
        "对，没错，不过……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #185
        0x8,
        (
            "要想让药生效的话，必须要严格遵照\x01",
            "规定的用法和用量……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #186 op#A
        0x11,
        (
            "#38A#3S呀呵───！！！#2000W #20W \x01",
            "终于到手啦───！！！\x02",
        )
    )
    Sleep(2300)

    SetChrFlags(0x11, 0x20)

    def lambda_28C2():
        OP_95(0xFE, 0x0, 0x0, 0x0, 0x7D0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_28C2)
    OP_8C(0x11, 0, 1600)
    OP_8C(0x11, 90, 1600)
    OP_8C(0x11, 180, 1600)
    OP_8C(0x11, 270, 1600)
    OP_8C(0x11, 0, 1600)
    OP_8C(0x11, 90, 1600)
    OP_8C(0x11, 180, 1600)
    OP_8C(0x11, 270, 1600)
    WaitChrThread(0x11, 0x0)
    ClearChrFlags(0x11, 0x20)
    Sleep(500)

    ChrTalk(    #187
        0x11,
        (
            "#3S这、这样的话我终于可以挺起\x01",
            "胸膛向爱娜小姐告白了──！\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF6)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2986")
    OP_62(0xF6, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_29C4")

    label("loc_2986")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF6)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_29AD")
    OP_62(0xF6, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_29C4")

    label("loc_29AD")

    OP_62(0xF6, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_29C4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_29EB")
    OP_62(0xF9, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_2A29")

    label("loc_29EB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2A12")
    OP_62(0xF9, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_2A29")

    label("loc_2A12")

    OP_62(0xF9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_2A29")

    Sleep(120)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF7)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2A55")
    OP_62(0xF7, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_2A93")

    label("loc_2A55")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF7)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2A7C")
    OP_62(0xF7, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_2A93")

    label("loc_2A7C")

    OP_62(0xF7, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_2A93")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2ABA")
    OP_62(0xF8, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_2AF8")

    label("loc_2ABA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2AE1")
    OP_62(0xF8, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_2AF8")

    label("loc_2AE1")

    OP_62(0xF8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_2AF8")

    Sleep(800)

    ChrTalk(    #188
        0x101,
        "#1004F#1P#3S──哎哎哎哎哎哎？！？！？！\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2B50")

    ChrTalk(    #189
        0x107,
        "#064F什、什么！？\x02",
    )

    CloseMessageWindow()

    label("loc_2B50")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2B73")

    ChrTalk(    #190
        0x105,
        "#044F这……！？\x02",
    )

    CloseMessageWindow()

    label("loc_2B73")


    ChrTalk(    #191
        0x103,
        "#023F他、他刚才……说的是爱娜？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2BCF")

    ChrTalk(    #192
        0x106,
        "#052F……啊啊～我听到的确实是那样。\x02",
    )

    CloseMessageWindow()

    label("loc_2BCF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2C04")

    ChrTalk(    #193
        0x108,
        "#073F嗯，他说的确实是『爱娜』啊。\x02",
    )

    CloseMessageWindow()

    label("loc_2C04")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2C38")

    ChrTalk(    #194
        0x104,
        (
            "#032F嗯嗯……\x01",
            "这真是出乎意料啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2C38")

    TurnDirection(0x11, 0x101, 400)

    ChrTalk(    #195
        0x11,
        (
            "啊，就是游击士协会的\x01",
            "那位美丽的女子！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #196
        0x11,
        (
            "虽然听说过她是酒豪，\x01",
            "但这次我有备而去就不怕了！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #197
        0x11,
        (
            "只要服下这副药，\x01",
            "我就可以堂堂正正地约她出来了！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #198
        0x101,
        (
            "#1020F#1P原来你是为了邀约爱娜姐\x01",
            "才想要这个药的吗……？\x02\x03",

            "#1007F虽然胆量和精神值得佩服，\x01",
            "不过，实在太可怜了啊……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2DCA")

    ChrTalk(    #199
        0x104,
        (
            "#032F不过，仔细想一想的话，\x01",
            "这也是个千载难逢的好机会呀。\x02\x03",

            "如果错失了这个机会，\x01",
            "想把爱娜灌醉就是不可能的了……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2DCA")


    ChrTalk(    #200
        0x103,
        (
            "#021F呵呵～还真是个有趣的计划啊。\x02\x03",

            "爱娜酩酊大醉的样子，\x01",
            "我也很想看一次呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #201
        0x11,
        (
            "噢噢！这样说的话，\x01",
            "难道你们愿意帮我吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #202
        0x11,
        (
            "其实我也很想让大家帮我把她\x01",
            "从协会里约出来呢。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2F27")

    ChrTalk(    #203
        0x104,
        (
            "#035F呵呵，那么\x01",
            "我就来助你一臂之力吧。\x02\x03",

            "#030F……约见地点就定在\x01",
            "那间酒馆如何？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #204
        0x103,
        (
            "#020F嗯，在那里就好了。\x02\x03",

            "只要提出拼酒的话，\x01",
            "爱娜一定会出来应战的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2F7A")

    label("loc_2F27")


    ChrTalk(    #205
        0x103,
        (
            "#020F好！那你们就先去\x01",
            "酒馆等着吧。\x02\x03",

            "只要提出拼酒的话，\x01",
            "爱娜一定会出来应战的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2F7A")

    TurnDirection(0x101, 0x103, 400)

    ChrTalk(    #206
        0x101,
        "#1020F#1P等、等一下啊雪拉姐。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x101, 400)

    ChrTalk(    #207
        0x103,
        (
            "#525F哈哈～没事啦。\x01",
            "顺水推舟也未尝不可，\x02\x03",

            "既然是委托人的愿望，\x01",
            "我们自然应该全力帮忙嘛㈱\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #208
        0x101,
        (
            "#1015F#1P话是这么说……\x02\x03",

            "#1007F（但其实就是\x01",
            "　你自己也想喝酒吧……）\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #209
        0x11,
        (
            "喔喔！不愧是游击士啊！\x01",
            "连服务都这么到位。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #210
        0x11,
        (
            "那我就去酒馆里等了，\x01",
            "把爱娜小姐约出来的事就拜托啦！\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_30F1")

    ChrTalk(    #211
        0x104,
        "#031F喔喔～～那我们就快走吧，老兄！\x02",
    )

    CloseMessageWindow()

    label("loc_30F1")


    def lambda_30F7():

        label("loc_30F7")

        TurnDirection(0xFE, 0x11, 400)
        OP_48()
        Jump("loc_30F7")

    QueueWorkItem2(0xF8, 3, lambda_30F7)

    def lambda_3108():

        label("loc_3108")

        TurnDirection(0xFE, 0x11, 400)
        OP_48()
        Jump("loc_3108")

    QueueWorkItem2(0xF9, 3, lambda_3108)

    def lambda_3119():

        label("loc_3119")

        TurnDirection(0xFE, 0x11, 400)
        OP_48()
        Jump("loc_3119")

    QueueWorkItem2(0x8, 3, lambda_3119)

    def lambda_312A():

        label("loc_312A")

        TurnDirection(0xFE, 0x11, 400)
        OP_48()
        Jump("loc_312A")

    QueueWorkItem2(0x101, 3, lambda_312A)

    def lambda_313B():
        OP_8E(0xFE, 0xFFFFC2C0, 0x0, 0xB1B2, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_313B)
    OP_43(0x11, 0x0, 0x1, 0x8)
    WaitChrThread(0x103, 0x0)
    OP_44(0x101, 0x3)

    def lambda_3166():
        OP_6D(-14180, 0, 46960, 2000)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_3166)

    def lambda_317E():

        label("loc_317E")

        TurnDirection(0xFE, 0x11, 400)
        OP_48()
        Jump("loc_317E")

    QueueWorkItem2(0x103, 3, lambda_317E)
    WaitChrThread(0x11, 0x0)
    OP_44(0x103, 0x3)
    OP_44(0xF8, 0x3)
    OP_44(0xF9, 0x3)
    OP_44(0x8, 0x3)
    SetChrFlags(0x11, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_31DC")
    OP_62(0x104, 0x0, 2000, 0x8, 0x9, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    OP_43(0x104, 0x0, 0x1, 0x9)
    WaitChrThread(0x104, 0x0)
    SetChrFlags(0x104, 0x80)
    Jump("loc_31E1")

    label("loc_31DC")

    Sleep(1000)

    label("loc_31E1")

    OP_6D(-17110, 0, 44470, 2000)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_321C")

    ChrTalk(    #212
        0x107,
        "#561F走、走了呢……\x02",
    )

    CloseMessageWindow()
    Jump("loc_329D")

    label("loc_321C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_324A")

    ChrTalk(    #213
        0x105,
        "#045F他、他们走了啊……\x02",
    )

    CloseMessageWindow()
    Jump("loc_329D")

    label("loc_324A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3278")

    ChrTalk(    #214
        0x108,
        "#075F呼，这就走了吗……\x02",
    )

    CloseMessageWindow()
    Jump("loc_329D")

    label("loc_3278")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_329D")

    ChrTalk(    #215
        0x106,
        "#552F这就走了啊。\x02",
    )

    CloseMessageWindow()

    label("loc_329D")


    ChrTalk(    #216
        0x8,
        "哎呀呀，还真是急性子。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #217
        0x8,
        (
            "我还没把药的使用说明\x01",
            "讲完啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #218
        0x101,
        (
            "#1015F#1P嗯、嗯……\x01",
            "不过也没关系啦，\x02\x03",

            "如果是爱娜姐的话，\x01",
            "应该不会这么简单\x01",
            "就被约出来。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x103, 180, 400)

    ChrTalk(    #219
        0x103,
        (
            "#021F呵呵～你太小看姐姐了。\x02\x03",

            "算啦，要是有兴趣的话，\x01",
            "就去酒馆里等着吧。\x02\x03",

            "我随后就会把爱娜\x01",
            "给拉来。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x10F1)
    NewScene("ED6_DT21/T0131   ._SN", 101, 0, 0)
    IdleLoop()
    Return()

    # Function_7_263F end

    def Function_8_33C0(): pass

    label("Function_8_33C0")

    OP_8E(0xFE, 0xFFFFC996, 0x0, 0xB748, 0xBB8, 0x0)
    OP_8E(0xFE, 0xFFFFCE00, 0x0, 0xB748, 0xBB8, 0x0)

    def lambda_33EE():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_33EE)
    OP_8E(0xFE, 0xFFFFD364, 0x0, 0xB748, 0xBB8, 0x0)
    Return()

    # Function_8_33C0 end

    def Function_9_340F(): pass

    label("Function_9_340F")

    SetChrFlags(0xFE, 0x40)
    OP_8E(0xFE, 0xFFFFCE00, 0x0, 0xB748, 0x1388, 0x0)

    def lambda_342E():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_342E)
    OP_8E(0xFE, 0xFFFFD364, 0x0, 0xB748, 0x1388, 0x0)
    ClearChrFlags(0xFE, 0x40)
    OP_63(0x104)
    Return()

    # Function_9_340F end

    def Function_10_3457(): pass

    label("Function_10_3457")

    EventBegin(0x0)
    Fade(1000)
    SetChrPos(0x101, 52230, 5000, 51080, 0)
    SetChrPos(0x103, 51500, 5000, 50530, 0)
    SetChrPos(0xF8, 52220, 5000, 49650, 0)
    SetChrPos(0xF9, 52230, 5000, 48630, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_34D1")
    SetChrPos(0xF9, 52220, 5000, 49650, 0)
    SetChrPos(0xF8, 52230, 5000, 48630, 0)

    label("loc_34D1")

    OP_6D(51850, 5000, 50700, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    OP_0D()

    ChrTalk(    #220
        0x101,
        (
            "#1002F这把椅子……\x02\x03",

            "正好放在礼拜堂\x01",
            "的这个位置。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_358F")

    ChrTalk(    #221
        0x105,
        (
            "#042F『坐在女神旁边的人』……\x02\x03",

            "也许…\x01",
            "就是指这个吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3676")

    label("loc_358F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_35DC")

    ChrTalk(    #222
        0x104,
        (
            "#032F『坐在女神旁边的人』……\x02\x03",

            "说不定…\x01",
            "就是指这个吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3676")

    label("loc_35DC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_362E")

    ChrTalk(    #223
        0x106,
        (
            "#053F『坐在女神旁边的人』吗……\x02\x03",

            "#050F有可能\x01",
            "说的就是它吧？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3676")

    label("loc_362E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3676")

    ChrTalk(    #224
        0x108,
        (
            "#072F『坐在女神旁边的人』……\x02\x03",

            "也许…\x01",
            "指的就是它吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3676")


    ChrTalk(    #225
        0x101,
        "#1002F嗯……调查看看吧。\x02",
    )

    CloseMessageWindow()
    OP_94(0x1, 0x101, 0x0, 0xC8, 0x3E8, 0x0)
    Fade(250)
    SetChrChipByIndex(0x101, 10)
    SetChrSubChip(0x101, 0)
    OP_0D()
    Sleep(500)
    Sleep(1000)
    OP_62(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #226
        0x101,
        (
            "#1002F果然……\x02\x03",

            "有张卡片。\x02",
        )
    )

    CloseMessageWindow()
    Fade(250)
    SetChrChipByIndex(0x101, 65535)
    OP_0D()
    Sleep(500)
    OP_8C(0x101, 180, 400)
    Fade(1000)
    SetChrChipByIndex(0x101, 32)
    OP_0D()
    Sleep(1000)
    FadeToDark(300, 0, 100)
    OP_AD(0x240093, 0xBE, 0x64, 0x1F4)
    Sleep(1000)
    SetMessageWindowPos(-1, 300, -1, 3)
    SetChrName("")

    AnonymousTalk(    #227
        (
            "\x07\x05第二个试炼是魔方阵，\x01",
            "　　　　 ■■\x01",
            "　　　  ■■■\x01\x02",

            "    ■是森林中的东西。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_AE(0x1F4)
    Sleep(1000)
    Fade(1000)
    SetChrChipByIndex(0x101, 65535)
    OP_0D()
    Sleep(400)

    ChrTalk(    #228
        0x101,
        (
            "#1001F很好！猜对了！\x02\x03",

            "#1007F嗯……虽然解开了谜题\x01",
            "值得高兴，可是……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #229
        0x103,
        (
            "#025F……这次的暗示好像\x01",
            "和之前的完全不同啊。\x02\x03",

            "到底是什么意思呢。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3884")

    ChrTalk(    #230
        0x107,
        (
            "#063F嗯……难道是表示\x01",
            "某个场所吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3926")

    label("loc_3884")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_38BB")

    ChrTalk(    #231
        0x105,
        (
            "#042F这个也是代表\x01",
            "某个地方吧……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3926")

    label("loc_38BB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_38F4")

    ChrTalk(    #232
        0x104,
        (
            "#032F这应该也是代表\x01",
            "某一个场所吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3926")

    label("loc_38F4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3926")

    ChrTalk(    #233
        0x106,
        (
            "#050F这应该也是指\x01",
            "某个地方吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3926")


    ChrTalk(    #234
        0x101,
        (
            "#1015F根据以往的经验，\x01",
            "应该没错吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #235
        0x103,
        (
            "#020F嗯～应该就是这样。\x02\x03",

            "在城里好好调查一下吧，找找\x01",
            "有什么东西和暗示上的图形相似。\x02",
        )
    )

    CloseMessageWindow()
    OP_28(0x77, 0x1, 0x8)
    OP_28(0x77, 0x1, 0x10)
    OP_64(0x1, 0x1)
    EventEnd(0x0)
    Return()

    # Function_10_3457 end

    SaveToFile()

Try(main)

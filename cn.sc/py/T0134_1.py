from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 洛连特

    CreateScenaFile(
        FileName            = 'T0134_1 ._SN',
        MapName             = 'Rolent',
        Location            = 'C0403.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60010",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            '',
            'ED6_DT21/T0134_1 ._SN',
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
        "Function_1_758",          # 01, 1
        "Function_2_89E",          # 02, 2
        "Function_3_16D6",         # 03, 3
        "Function_4_1BC5",         # 04, 4
        "Function_5_1CBD",         # 05, 5
        "Function_6_1D8A",         # 06, 6
    )


    def Function_0_AA(): pass

    label("Function_0_AA")

    EventBegin(0x0)
    Fade(1000)
    Call(1, 4)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x302, 2)), scpexpr(EXPR_END)), "loc_13C")

    ChrTalk(    #0
        0xD,
        (
            "因为这雾的原因\x01",
            "今天也看不见星星……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xD,
        (
            "不过只要有你在，\x01",
            "我就一点儿也不寂寞。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0xD,
        (
            "因为我所寻找的星星\x01",
            "就是你啊，艾娅莉。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_13C")


    ChrTalk(    #3
        0x101,
        (
            "#1007F#3P打、打扰了……\x02\x03",

            "请问现在方便吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xD, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(    #4
        0xD,
        "嗯……？\x02",
    )

    CloseMessageWindow()

    def lambda_196():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_196)
    Sleep(250)
    TurnDirection(0xE, 0x101, 400)

    ChrTalk(    #5
        0xE,
        "#2P……啊，是谁？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x101,
        (
            "#1000F#3P我们是游击士协会的人。\x02\x03",

            "您就是阿鲁姆先生吗？\x01",
            "我们是看了告示板上的委托而来的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0xD,
        "哇～终于来了吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0xD,
        (
            "太好了！\x01",
            "我等你们好久了！！\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xE, 0xD, 400)

    ChrTalk(    #9
        0xE,
        (
            "#2P太好了！阿鲁姆！\x01",
            "我好高兴啊！\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xD, 0xE, 400)

    ChrTalk(    #10
        0xD,
        "啊啊～艾娅莉。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0xD,
        (
            "你的心灵为什么\x01",
            "这样美丽？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0xD,
        (
            "明明让你痛苦\x01",
            "的人就是我…\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0xE,
        "#2P不要那么说，阿鲁姆。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0xE,
        (
            "#2P你心中的痛苦\x01",
            "我全都明白！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0xE,
        (
            "#2P那一夜，咱们不是约定好了吗？\x01",
            "不管到什么时候，你和我……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0xD,
        (
            "……也要携手\x01",
            "走完一生…\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0xD,
        "啊啊！！艾娅莉！我爱你！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0xE,
        "#2P我也是啊！阿鲁姆！！\x02",
    )

    CloseMessageWindow()
    OP_62(0xF, 0x0, 1700, 0xA, 0xB, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(1500)
    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(150)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_427")
    OP_62(0xF8, 0x0, 2300, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jump("loc_465")

    label("loc_427")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_44E")
    OP_62(0xF8, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jump("loc_465")

    label("loc_44E")

    OP_62(0xF8, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)

    label("loc_465")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_48C")
    OP_62(0xF9, 0x0, 2300, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jump("loc_4CA")

    label("loc_48C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4B3")
    OP_62(0xF9, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jump("loc_4CA")

    label("loc_4B3")

    OP_62(0xF9, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)

    label("loc_4CA")

    Sleep(1000)

    ChrTalk(    #19
        0x101,
        (
            "#1016F#3P那、那个～……\x02\x03",

            "您有什么\x01",
            "要求呢？\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xD, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(400)

    ChrTalk(    #20
        0xD,
        "啊……！！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0xE,
        "#2P对了！委托！！\x02",
    )

    CloseMessageWindow()

    def lambda_543():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_543)
    Sleep(150)
    TurnDirection(0xE, 0x101, 400)

    ChrTalk(    #22
        0xD,
        (
            "其、其实是一件关系到我们两个\x01",
            "将来的重要事件！！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0xD,
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_60B")
    Call(1, 2)
    Jump("loc_73F")

    label("loc_60B")


    ChrTalk(    #24
        0x101,
        (
            "#1015F#3P啊～抱歉。\x02\x03",

            "马上开始的话\x01",
            "可能有些困难。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0xD,
        (
            "怎、怎么会…\x01",
            "请不要抛弃我们啊！！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0xE,
        (
            "#2P求你们了……\x01",
            "这件事真的很重要！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x103,
        (
            "#020F没关系，\x01",
            "我们会回来的，放心吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x101,
        (
            "#1000F#3P嗯，等我们有空的时候\x01",
            "一定回来仔细听你们说。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0xD,
        "真、真的吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0xD,
        (
            "好、好… \x01",
            "我相信你们。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0xE,
        "#2P一定要再来啊。\x02",
    )

    CloseMessageWindow()
    OP_28(0x72, 0x1, 0x8000)

    label("loc_73F")

    TurnDirection(0xE, 0xD, 0)
    TurnDirection(0xD, 0xE, 0)
    OP_4B(0xD, 255)
    OP_4B(0xE, 255)
    EventEnd(0x0)
    Return()

    # Function_0_AA end

    def Function_1_758(): pass

    label("Function_1_758")

    EventBegin(0x0)
    Fade(1000)
    Call(1, 4)
    OP_8C(0xD, 270, 0)
    OP_8C(0xE, 270, 0)
    OP_0D()

    ChrTalk(    #32
        0xD,
        "那个，各位游击士……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0xD,
        (
            "你们……可以接受\x01",
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_807")
    Call(1, 2)
    Jump("loc_885")

    label("loc_807")


    ChrTalk(    #34
        0x101,
        (
            "#1007F呼、呼……\x01",
            "现在确实还有点为难呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0xD,
        "怎、怎么会…\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x101,
        (
            "#1016F抱歉抱歉。\x01",
            "下次再来听你们说明。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0xE,
        "嗯，会再来的。\x02",
    )

    CloseMessageWindow()

    label("loc_885")

    TurnDirection(0xE, 0xD, 0)
    TurnDirection(0xD, 0xE, 0)
    OP_4B(0xD, 255)
    OP_4B(0xE, 255)
    EventEnd(0x0)
    Return()

    # Function_1_758 end

    def Function_2_89E(): pass

    label("Function_2_89E")


    ChrTalk(    #38
        0x101,
        (
            "#1006F啊，嗯。\x01",
            "没问题。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x304, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_978")

    ChrTalk(    #39
        0xD,
        "真、真的吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0x103,
        (
            "#020F只是，既然很急的话，\x01",
            "就麻烦您长话短说吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0xD,
        "啊啊～那个倒无所谓！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0xD,
        (
            "呀～不管怎样，\x01",
            "多谢你们了，游击士！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0xD,
        (
            "你们能来\x01",
            "真是救了我们一命啊！！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9B1")

    label("loc_978")


    ChrTalk(    #44
        0xD,
        "真、真的吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0xD,
        (
            "太感谢了！！\x01",
            "谢谢了！！游击士！！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9B1")

    TurnDirection(0xE, 0xD, 400)

    ChrTalk(    #46
        0xE,
        (
            "#2P太好了！阿鲁姆！\x01",
            "我好高兴啊！\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xD, 0xE, 400)

    ChrTalk(    #47
        0xD,
        "啊啊～艾娅莉。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0xD,
        (
            "为什么你的心灵\x01",
            "这样美丽？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0xE,
        "#2P啊啊～阿鲁姆……\x02",
    )

    CloseMessageWindow()
    Sleep(1000)

    ChrTalk(    #50
        0x101,
        (
            "#1019F#4S……#2S\x02\x03",

            "……我说委托的事…～？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_A6A():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_A6A)
    Sleep(150)
    TurnDirection(0xE, 0x101, 400)

    ChrTalk(    #51
        0xD,
        "……失礼了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0xD,
        "那么，请听我说吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0x103,
        "#020F嗯，可能的话，请您尽量说简洁点。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0xD,
        (
            "想委托各位帮忙的事情并不是别的，\x01",
            "就是寻找我们的结婚戒指。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0xD,
        (
            "我拼命攒钱，好不容易\x01",
            "买到了那个高档戒指，可是… \x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0xD,
        (
            "那、那只可恨的小偷乌鸦，\x01",
            "竟然把它给偷走了！！！\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #57
        0x101,
        "#1004F#3P乌、乌鸦！？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_BE4")

    ChrTalk(    #58
        0x107,
        "#064F乌鸦……是那只鸟吗？\x02",
    )

    CloseMessageWindow()
    Jump("loc_C7D")

    label("loc_BE4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C18")

    ChrTalk(    #59
        0x105,
        "#044F乌鸦吗……难道是那只鸟？\x02",
    )

    CloseMessageWindow()
    Jump("loc_C7D")

    label("loc_C18")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C50")

    ChrTalk(    #60
        0x104,
        "#033F所谓的乌鸦……是指那只鸟吗？\x02",
    )

    CloseMessageWindow()
    Jump("loc_C7D")

    label("loc_C50")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C7D")

    ChrTalk(    #61
        0x106,
        "#052F乌鸦……是那只鸟吗？\x02",
    )

    CloseMessageWindow()

    label("loc_C7D")


    ChrTalk(    #62
        0xD,
        "对！总之就是那个哇哇叫的混帐了！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0xD,
        (
            "那个可恶的家伙竟然\x01",
            "把我们的结婚戒指给叼跑了！！\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x72, 0x1, 0x4000)"), scpexpr(EXPR_EXEC_OP, "OP_40(0x234, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_10CE")

    ChrTalk(    #64
        0x103,
        (
            "#026F确实，乌鸦的习性就是\x01",
            "喜欢收集闪光的东西呢。\x02\x03",

            "#027F话虽如此……\x01",
            "但戒指被乌鸦偷走，还真是……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 400)

    ChrTalk(    #65
        0x101,
        (
            "#1011F啊，难道说……\x02\x03",

            "雪拉姐也\x01",
            "想起那个戒指了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0x103,
        (
            "#020F嗯，保险起见，\x01",
            "最好还是给他看看吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0xD,
        "？？？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0xD,
        "有什么线索吗？\x02",
    )

    CloseMessageWindow()
    OP_8C(0x101, 90, 400)

    ChrTalk(    #69
        0x101,
        (
            "#1002F阿鲁姆先生，请您\x01",
            "看一下这只戒指可以吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #70 op#A
        0xD,
        "#22A嗯，当然……\x02",
    )
    Sleep(2300)

    Call(1, 5)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #71
        0x101,
        "#1004F咦咦！？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_EA0")

    ChrTalk(    #72
        0x107,
        (
            "#064F那个那个……\x01",
            "确实就是这只戒指吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F4D")

    label("loc_EA0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_ECC")

    ChrTalk(    #73
        0x105,
        "#044F没、没搞错吗！？\x02",
    )

    CloseMessageWindow()
    Jump("loc_F4D")

    label("loc_ECC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_EF8")

    ChrTalk(    #74
        0x104,
        "#033F那个，没弄错吗？\x02",
    )

    CloseMessageWindow()
    Jump("loc_F4D")

    label("loc_EF8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_F2A")

    ChrTalk(    #75
        0x106,
        "#055F喂喂、，不会是真的吧？\x02",
    )

    CloseMessageWindow()
    Jump("loc_F4D")

    label("loc_F2A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_F4D")

    ChrTalk(    #76
        0x108,
        "#073F没弄错吗？\x02",
    )

    CloseMessageWindow()

    label("loc_F4D")


    ChrTalk(    #77
        0xD,
        "嗯、嗯……绝对没错！！！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0xD,
        "这就是我们的戒指！！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0xE,
        (
            "#2P啊啊！！女神啊……\x01",
            "衷心感谢您的恩德！！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0x103,
        (
            "#021F呵呵，没想到\x01",
            "会这么巧啊。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1007")

    ChrTalk(    #81
        0x108,
        "#073F真是惊人的巧合呢。\x02",
    )

    CloseMessageWindow()
    Jump("loc_109B")

    label("loc_1007")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1037")

    ChrTalk(    #82
        0x106,
        "#052F真是好惊人的巧合呢。\x02",
    )

    CloseMessageWindow()
    Jump("loc_109B")

    label("loc_1037")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_106E")

    ChrTalk(    #83
        0x104,
        (
            "#031F哈哈哈。\x01",
            "真是惊人的巧合啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_109B")

    label("loc_106E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_109B")

    ChrTalk(    #84
        0x105,
        "#044F好、好惊人的巧合啊。\x02",
    )

    CloseMessageWindow()

    label("loc_109B")

    Call(1, 6)
    OP_28(0x72, 0x1, 0x8)
    OP_28(0x72, 0x1, 0x10)
    OP_28(0x72, 0x4, 0x10)
    TurnDirection(0xE, 0xD, 0)
    TurnDirection(0xD, 0xE, 0)
    OP_63(0xF)
    OP_4B(0xD, 255)
    OP_4B(0xE, 255)
    EventEnd(0x0)
    Jump("loc_16D5")

    label("loc_10CE")


    ChrTalk(    #85
        0x103,
        (
            "#027F确实，乌鸦具有\x01",
            "喜欢收集闪亮东西的习性。\x02\x03",

            "所以会对戒指这种东西\x01",
            "感兴趣的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #86
        0x101,
        (
            "#1015F#3P那么，戒指现在\x01",
            "应该在它们的巢中吧。\x02\x03",

            "#1002F是让我们来找那戒指的吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0xD,
        (
            "嗯，那就是我们\x01",
            "想委托你们办的事情。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0xD,
        (
            "虽然我明白\x01",
            "这件事太过困难。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0xD,
        (
            "但即使如此，\x01",
            "也拜托你们尽力帮我们吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #90
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

    ChrTalk(    #91
        0xD,
        (
            "啊啊，是要寻找\x01",
            "乌鸦的巢穴了吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0xD,
        "大概在洛连特北部吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0xD,
        (
            "那家伙飞向玛鲁加山道\x01",
            "那边去了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0xD,
        (
            "再加上现在起了大雾，\x01",
            "能追上的可能性不大了吧…\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x72, 0x1, 0x4000)"), scpexpr(EXPR_EXEC_OP, "OP_40(0x234, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1402")

    ChrTalk(    #95
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

    ChrTalk(    #96
        0x101,
        (
            "#1019F#3P（难、难道说……）\x02\x03",

            "（在塔顶上\x01",
            "  发现的那个戒指…）\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0xD,
        "嗯？怎么啦？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0x101,
        (
            "#1016F#3P呼、呼呼。没什么。\x01",
            "（一定只是心理作用吧～）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1431")

    label("loc_1402")


    ChrTalk(    #99
        0x101,
        (
            "#1015F#3P原来如此。\x02\x03",

            "巢穴大概在北边吗……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1431")


    ChrTalk(    #100
        0x103,
        (
            "#026F……我们会做个参考的。\x02\x03",

            "不管怎样，巢穴肯定\x01",
            "是在高处就对了。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_14C8")

    ChrTalk(    #101
        0x108,
        (
            "#075F啊，那肯定没错的。\x02\x03",

            "真是的……\x01",
            "还真是个麻烦的工作啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1591")

    label("loc_14C8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1517")

    ChrTalk(    #102
        0x106,
        (
            "#551F嗯，那肯定没错。\x02\x03",

            "真是的……\x01",
            "还真是个麻烦的工作啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1591")

    label("loc_1517")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1566")

    ChrTalk(    #103
        0x104,
        (
            "#034F嗯，那是肯定的啦。\x02\x03",

            "呼～还真是件\x01",
            "超级麻烦的工作啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1591")

    label("loc_1566")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1591")

    ChrTalk(    #104
        0x105,
        "#047F嗯，确实比较麻烦。\x02",
    )

    CloseMessageWindow()

    label("loc_1591")


    ChrTalk(    #105
        0xD,
        (
            "除了协会之外，\x01",
            "我们再也找不到人可以拜托了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #106
        0xD,
        (
            "所以无论如何\x01",
            "你们也要帮帮忙啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0xE,
        (
            "#2P你们是我们唯一的希望了。\x01",
            "无论如何也请帮我们找找吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #108
        0x101,
        (
            "#1006F#3P嗯……\x01",
            "我们会努力找找看的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #109
        0x103,
        (
            "#020F那么，有什么发现的话\x01",
            "我们会再来报告给您。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #110
        0xD,
        "期待大家！我们会一直等的！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0xE,
        "#2P加油哦！\x02",
    )

    CloseMessageWindow()
    OP_28(0x72, 0x4, 0x4)
    OP_28(0x72, 0x4, 0x8)
    OP_28(0x72, 0x1, 0x1)
    OP_28(0x72, 0x1, 0x2)
    OP_A2(0x7)
    ClearChrFlags(0xE, 0x10)
    ClearChrFlags(0xD, 0x10)

    label("loc_16D5")

    Return()

    # Function_2_89E end

    def Function_3_16D6(): pass

    label("Function_3_16D6")

    EventBegin(0x0)
    Fade(1000)
    Call(1, 4)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x302, 2)), scpexpr(EXPR_END)), "loc_1768")

    ChrTalk(    #112
        0xD,
        (
            "因为这雾的原因\x01",
            "今天也看不见星星……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0xD,
        (
            "不过只要有你在，\x01",
            "我就一点儿也不寂寞。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #114
        0xD,
        (
            "因为我所寻找的星星\x01",
            "就是你啊，艾娅莉。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1768")


    ChrTalk(    #115
        0x101,
        "#1007F（还、还没停啊……）\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #116
        0xD,
        "嗯……？\x02",
    )

    CloseMessageWindow()

    def lambda_179C():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_179C)
    Sleep(250)
    TurnDirection(0xE, 0x101, 400)

    ChrTalk(    #117
        0xE,
        "#2P……啊，游击士。\x02",
    )

    CloseMessageWindow()
    OP_62(0xD, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_63(0xD)

    ChrTalk(    #118
        0xD,
        (
            "难、难道\x01",
            "你们找到戒指了！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #119
        0x103,
        (
            "#020F嗯，找到了一只符合您\x01",
            "说明的戒指。\x02\x03",

            "但不知道是不是您\x01",
            "丢失的那个。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #120
        0x101,
        (
            "#1000F所以\x01",
            "希望您能确认一下。\x02\x03",

            "阿鲁姆先生，\x01",
            "看一下这只戒指可以吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #121 op#A
        0xD,
        "#6A嗯，当然……\x02",
    )
    Sleep(2000)

    Call(1, 5)

    ChrTalk(    #122
        0x101,
        "#1004F真、真的！？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1904")

    ChrTalk(    #123
        0x107,
        (
            "#064F那个那个……\x01",
            "确实就是这只戒指吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_19AF")

    label("loc_1904")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1930")

    ChrTalk(    #124
        0x105,
        "#044F没、没搞错吗！？\x02",
    )

    CloseMessageWindow()
    Jump("loc_19AF")

    label("loc_1930")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_195C")

    ChrTalk(    #125
        0x104,
        "#033F那个，没弄错吗？\x02",
    )

    CloseMessageWindow()
    Jump("loc_19AF")

    label("loc_195C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_198C")

    ChrTalk(    #126
        0x106,
        "#055F喂喂，不会是真的吧？\x02",
    )

    CloseMessageWindow()
    Jump("loc_19AF")

    label("loc_198C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_19AF")

    ChrTalk(    #127
        0x108,
        "#073F没弄错吗？\x02",
    )

    CloseMessageWindow()

    label("loc_19AF")


    ChrTalk(    #128
        0xD,
        "嗯、嗯……绝对没错！！！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #129
        0xD,
        "这就是我们的戒指！！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #130
        0xE,
        (
            "#2P啊啊！！女神啊……\x01",
            "衷心感谢您的恩德！！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #131
        0x103,
        (
            "#021F呵呵，太好了。\x01",
            "终于物归原主了啊。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1A8A")

    ChrTalk(    #132
        0x108,
        (
            "#070F呼，真是没想到啊，\x02\x03",

            "竟然会在那种\x01",
            "地方找到。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1B9A")

    label("loc_1A8A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1AF0")

    ChrTalk(    #133
        0x105,
        (
            "#040F太好了……\x01",
            "这样的话事情也就解决了。\x02\x03",

            "真是做梦也想不到会在\x01",
            "那种地方找到啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1B9A")

    label("loc_1AF0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1B4C")

    ChrTalk(    #134
        0x106,
        (
            "#051F啊啊，总算是解决了，\x01",
            "松了口气。\x02\x03",

            "真是没想到会在\x01",
            "那种地方找到啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1B9A")

    label("loc_1B4C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1B9A")

    ChrTalk(    #135
        0x104,
        (
            "#030F呼～真是不容易啊。\x02\x03",

            "真没想到竟然会在\x01",
            "那种地方找到啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B9A")

    Call(1, 6)
    OP_28(0x72, 0x1, 0x10)
    OP_28(0x72, 0x4, 0x10)
    TurnDirection(0xE, 0xD, 0)
    TurnDirection(0xD, 0xE, 0)
    OP_63(0xF)
    OP_4B(0xD, 255)
    OP_4B(0xE, 255)
    EventEnd(0x0)
    Return()

    # Function_3_16D6 end

    def Function_4_1BC5(): pass

    label("Function_4_1BC5")

    OP_4A(0xD, 255)
    OP_4A(0xE, 255)
    SetChrPos(0x101, 62800, 0, 47270, 90)
    SetChrPos(0x103, 61790, 0, 46800, 90)
    SetChrPos(0xF8, 61270, 0, 47980, 90)
    SetChrPos(0xF9, 60320, 0, 47290, 90)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1C40")
    SetChrPos(0xF9, 61270, 0, 47980, 90)
    SetChrPos(0xF8, 60320, 0, 47290, 90)

    label("loc_1C40")

    OP_6D(61800, 0, 48260, 0)
    OP_67(0, 6130, -10000, 0)
    OP_6B(2870, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    OP_51(0xF, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xF, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xF, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_4_1BC5 end

    def Function_5_1CBD(): pass

    label("Function_5_1CBD")

    OP_94(0x1, 0xD, 0x0, 0xC8, 0x3E8, 0x0)
    OP_56(0x0)
    OP_59()
    OP_62(0xD, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(100)

    def lambda_1CF1():
        OP_95(0xFE, 0x0, 0x0, 0x0, 0x190, 0xFA0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_1CF1)
    Sleep(900)
    OP_63(0xD)
    WaitChrThread(0xD, 0x1)

    ChrTalk(    #136
        0xD,
        "#3S……啊啊啊啊啊啊啊！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #137
        0xD,
        "那那那、那个戒指！！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #138
        0xD,
        "#3S那不就是我、我们的结婚戒指吗！！\x02",
    )

    OP_7C(0x0, 0x1F4, 0xBB8, 0x64)
    CloseMessageWindow()
    Return()

    # Function_5_1CBD end

    def Function_6_1D8A(): pass

    label("Function_6_1D8A")


    ChrTalk(    #139
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

    AnonymousTalk(    #140
        "\x1F\x34\x02\x07\x00交出了。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3F(0x234, 1)
    OP_94(0x1, 0xD, 0xB4, 0xC8, 0x3E8, 0x0)

    ChrTalk(    #141
        0xD,
        "啊，谢谢……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #142
        0xD,
        "真是感激不尽！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #143
        0xE,
        (
            "#2P呵呵，相信游击士\x01",
            "果然没有错㈱\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #144
        0x101,
        "#1017F哪里哪里，没什么。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #145
        0x103,
        (
            "#020F马上就要\x01",
            "结婚了吗？\x02\x03",

            "#525F祝你们幸福哦㈱\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(    #146
        0xE,
        (
            "#2P喔…………\x01",
            "啊，谢谢！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #147
        0xE,
        (
            "#2P感、感觉真好啊！\x01",
            "被人祝福的感觉…\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xD, 0xE, 400)

    ChrTalk(    #148
        0xD,
        "这样的话，要尽快了！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #149
        0xD,
        (
            "我们的未来一定会\x01",
            "得到无数的祝福的！\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xE, 0xD, 400)

    ChrTalk(    #150
        0xE,
        "#2P啊啊～阿鲁姆……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #151
        0xD,
        "艾娅莉……\x02",
    )

    CloseMessageWindow()
    OP_62(0xF, 0x0, 1800, 0xA, 0xB, 0xFA, 0x0)
    Sleep(1000)
    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(100)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2036")
    OP_62(0xF8, 0x0, 2300, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jump("loc_2074")

    label("loc_2036")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_205D")
    OP_62(0xF8, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jump("loc_2074")

    label("loc_205D")

    OP_62(0xF8, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)

    label("loc_2074")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_209B")
    OP_62(0xF9, 0x0, 2300, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jump("loc_20D9")

    label("loc_209B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_20C2")
    OP_62(0xF9, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jump("loc_20D9")

    label("loc_20C2")

    OP_62(0xF9, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)

    label("loc_20D9")

    Sleep(1000)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2125")

    ChrTalk(    #152
        0x107,
        (
            "#067F（啊哈～……\x01",
            "  完全沉浸在二人世界中了啊。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_21D6")

    label("loc_2125")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2163")

    ChrTalk(    #153
        0x105,
        "#540F（完、完全沉浸在二人世界中了啊。）\x02",
    )

    CloseMessageWindow()
    Jump("loc_21D6")

    label("loc_2163")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_21A1")

    ChrTalk(    #154
        0x104,
        "#030F（呼～彻底沉浸在二人世界里了啊。）\x02",
    )

    CloseMessageWindow()
    Jump("loc_21D6")

    label("loc_21A1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_21D6")

    ChrTalk(    #155
        0x108,
        "#070F（这就是所谓的二人世界吗。）\x02",
    )

    CloseMessageWindow()

    label("loc_21D6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2210")

    ChrTalk(    #156
        0x106,
        "#552F（好像完全无视我们的存在呢。）\x02",
    )

    CloseMessageWindow()
    Jump("loc_22B3")

    label("loc_2210")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_224A")

    ChrTalk(    #157
        0x108,
        "#071F（哈哈，恋爱果然是盲目的呢。）\x02",
    )

    CloseMessageWindow()
    Jump("loc_22B3")

    label("loc_224A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2284")

    ChrTalk(    #158
        0x104,
        "#031F（呵呵，恋爱果然是盲目的啊。）\x02",
    )

    CloseMessageWindow()
    Jump("loc_22B3")

    label("loc_2284")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_22B3")

    ChrTalk(    #159
        0x105,
        "#048F（不过……真不错呢。）\x02",
    )

    CloseMessageWindow()

    label("loc_22B3")


    ChrTalk(    #160
        0x103,
        (
            "#020F（咱们好像太打扰他们了……\x01",
            "    还是赶快离开吧。)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #161
        0x101,
        (
            "#1013F（说、说的是啊。）\x02\x03",

            "#1016F那、那么……\x01",
            "我们这就走了～\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x17, 0x0, 0x64)

    AnonymousTalk(    #162
        "\x07\x02任务【消失在天空的定婚戒指】\x07\x00完成了！\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrFlags(0xD, 0x10)
    SetChrFlags(0xE, 0x10)
    OP_A2(0x6)
    Return()

    # Function_6_1D8A end

    SaveToFile()

Try(main)

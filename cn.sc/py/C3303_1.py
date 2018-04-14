from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 洛连特

    CreateScenaFile(
        FileName            = 'C3303_1 ._SN',
        MapName             = 'Rolent',
        Location            = 'C0403.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60010",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            '',
            'ED6_DT21/C3303_1 ._SN',
            '',
            '',
            '',
            '',
            'ED6_DT21/SUB000  ._SN',
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


    ScpFunction(
        "Function_0_AA",           # 00, 0
        "Function_1_1835",         # 01, 1
        "Function_2_185B",         # 02, 2
        "Function_3_1886",         # 03, 3
        "Function_4_18B6",         # 04, 4
        "Function_5_18EB",         # 05, 5
        "Function_6_1910",         # 06, 6
        "Function_7_193A",         # 07, 7
        "Function_8_1964",         # 08, 8
        "Function_9_1989",         # 09, 9
        "Function_10_1A5F",        # 0A, 10
        "Function_11_1B3A",        # 0B, 11
        "Function_12_1C15",        # 0C, 12
        "Function_13_1CF0",        # 0D, 13
        "Function_14_1DCB",        # 0E, 14
        "Function_15_1EA6",        # 0F, 15
        "Function_16_294F",        # 10, 16
    )


    def Function_0_AA(): pass

    label("Function_0_AA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x71, 0x0, 0x8)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_29(0x71, 0x0, 0x10)"), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_29(0x71, 0x0, 0x40)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_C4")
    Return()

    label("loc_C4")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x1E, 0x0, 0x4)"), scpexpr(EXPR_END)), "loc_D3")
    OP_A2(0x0)

    label("loc_D3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_14E")
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "【◇上部遇到过吉米的情况下】\x01",      # 0
            "【◇不变更】\x01",                      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_148"),
        (SWITCH_DEFAULT, "loc_14E"),
    )


    label("loc_148")

    OP_A2(0x0)
    Jump("loc_14E")

    label("loc_14E")

    ClearChrFlags(0x8, 0x80)
    OP_72(0x0, 0x4)
    SetChrPos(0x8, 9460, 40, 112460, 90)
    SetChrPos(0x10, 9460, -40, 124460, 0)

    def lambda_180():
        TurnDirection(0x0, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_180)

    def lambda_18E():
        TurnDirection(0x1, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_18E)

    def lambda_19C():
        TurnDirection(0x2, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_19C)

    def lambda_1AA():
        TurnDirection(0x3, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_1AA)
    WaitChrThread(0x3, 0x1)
    OP_62(0x0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_204")

    ChrTalk(    #0
        0x101,
        (
            "#1004F啊！？\x02\x03",

            "那、那是……！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_23C")

    label("loc_204")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_227")

    ChrTalk(    #1
        0x106,
        "#052F那家伙是……！\x02",
    )

    CloseMessageWindow()
    Jump("loc_23C")

    label("loc_227")


    ChrTalk(    #2
        0x103,
        "#023F那是……！\x02",
    )

    CloseMessageWindow()

    label("loc_23C")

    OP_6D(11140, 0, 112460, 3000)

    NpcTalk(    #3
        0x8,
        "青年",
        "哈、哈、哈……\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #4
        0x8,
        "青年",
        (
            "总、总算把宝箱\x01",
            "捞上来了～～\x02",
        )
    )

    CloseMessageWindow()
    OP_8E(0x8, 0x24F4, 0xA, 0x1B1A2, 0x7D0, 0x0)
    OP_8E(0x8, 0x2B84, 0xFFFFFFCE, 0x1B1A2, 0x7D0, 0x0)
    OP_8C(0x8, 0, 400)
    Sleep(1000)

    NpcTalk(    #5
        0x8,
        "青年",
        (
            "没错。\x01",
            "终于找到了……\x02",
        )
    )

    CloseMessageWindow()
    OP_9E(0x8, 0xF, 0x0, 0x12C, 0xBB8)
    Sleep(1000)

    NpcTalk(    #6
        0x8,
        "青年",
        "#5P#4S哇～终于找到了～！\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    Sleep(1000)
    OP_62(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)

    ChrTalk(    #7
        0x10,
        "#4S#4P……终于找到了～！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x10,
        "#3S#4P……找到了～！　#2S……到了～！　#1S……了～！\x02",
    )

    CloseMessageWindow()
    Sleep(1000)
    OP_8C(0x8, 270, 400)
    OP_62(0x8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x8)
    Sleep(400)
    OP_62(0x8, 0x0, 2000, 0x22, 0x24, 0xFA, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(400)
    OP_8C(0x8, 0, 400)
    Sleep(2000)

    NpcTalk(    #9
        0x8,
        "青年",
        "#5P#4S吉米了不起！　我爱你～！\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    Sleep(1000)

    ChrTalk(    #10
        0x10,
        "#4S#4P……了不起！　我爱你～！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x10,
        "#3S#4P……我爱你～！　#2S……爱你～！　#1S……你～！\x02",
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(2000)
    OP_63(0x8)

    NpcTalk(    #12
        0x8,
        "青年",
        (
            "……看、看来不是\x01",
            "玩这个的时候。\x02",
        )
    )

    CloseMessageWindow()
    AddParty(0x47, 0xFA, 0xFF)
    SetChrFlags(0x148, 0x8)
    OP_43(0x101, 0x0, 0x1, 0x1)
    OP_43(0xF7, 0x0, 0x1, 0x2)
    OP_43(0xF8, 0x0, 0x1, 0x3)
    OP_43(0xF9, 0x0, 0x1, 0x4)

    NpcTalk(    #13
        0x8,
        "青年",
        (
            "在魔兽到来之前\x01",
            "得先确认里面的东西……\x02",
        )
    )

    CloseMessageWindow()

    def lambda_52A():
        OP_6D(11140, 0, 110010, 2000)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_52A)
    WaitChrThread(0xF9, 0x0)
    WaitChrThread(0xF8, 0x0)
    WaitChrThread(0xF7, 0x0)
    WaitChrThread(0x8, 0x0)
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_95(0x8, 0x0, 0x0, 0x0, 0x258, 0x1388)
    Sleep(500)
    OP_63(0x8)
    TurnDirection(0x8, 0x101, 400)

    NpcTalk(    #14
        0x8,
        "青年",
        "哇、哇！！\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #15
        0x8,
        "青年",
        "怎、怎么是你们！\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_6AE")

    ChrTalk(    #16
        0x101,
        (
            "#1007F#3P你、你在这儿玩什么呢。\x02\x03",

            "还是和以前一样完全不知道何谓紧张啊。\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #17
        0x8,
        "青年",
        "咦？你、你是！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x101,
        (
            "#1006F#3P好久不见，吉米先生。\x02\x03",

            "我们曾经在卢安\x01",
            "接受过你的工作哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x8,
        "哇～真怀念啊～！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x8,
        (
            "对了，那你们今天\x01",
            "来这儿干什么？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7B7")

    label("loc_6AE")


    ChrTalk(    #21
        0x101,
        (
            "#1007F#3P你、你在这里玩什么啊。\x02\x03",

            "真是完全没紧张感的人啊。\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #22
        0x8,
        "青年",
        "说、说我没紧张感……\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #23
        0x8,
        "青年",
        (
            "哼，好歹我也去过了\x01",
            "那些需要调查的地方。\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #24
        0x8,
        "青年",
        "那么，你们到底是什么人？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x101,
        (
            "#1006F#3P我们是游击士哦。\x02\x03",

            "你是吉米先生吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x8,
        (
            "嗯，我就是吉米。\x01",
            "有什么问题吗？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_803")

    ChrTalk(    #27
        0x106,
        (
            "#050F#4P你投宿的地方\x01",
            "发出了搜寻请求。\x02\x03",

            "所以我们就来\x01",
            "找你了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_845")

    label("loc_803")


    ChrTalk(    #28
        0x103,
        (
            "#020F#4P你投宿的地方\x01",
            "发出了搜寻请求。\x02\x03",

            "所以我们就来\x01",
            "找你了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_845")


    ChrTalk(    #29
        0x8,
        (
            "这样啊，原来你们\x01",
            "是从蔡斯来接我的啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x8,
        (
            "不过很遗憾，\x01",
            "现在我还不能回去。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x8,
        (
            "其实我刚刚完成了一个\x01",
            "绝世的大发现。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8F0")

    ChrTalk(    #32
        0x107,
        "#064F就是那个……宝箱吗？\x02",
    )

    CloseMessageWindow()
    Jump("loc_945")

    label("loc_8F0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_91C")

    ChrTalk(    #33
        0x104,
        "#033F就是那个宝箱吗？\x02",
    )

    CloseMessageWindow()
    Jump("loc_945")

    label("loc_91C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_945")

    ChrTalk(    #34
        0x105,
        "#044F就是那个宝箱吗？\x02",
    )

    CloseMessageWindow()

    label("loc_945")


    ChrTalk(    #35
        0x8,
        (
            "嗯，好不容易\x01",
            "捞上来的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x101,
        (
            "#1004F#3P捞上来的……\x01",
            "莫非是从湖里？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0x8,
        (
            "真是藏在了一个\x01",
            "了不得的地方啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x8,
        (
            "嗯，不愧是\x01",
            "大海盗希尔玛的宝藏啊。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_A77")
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #39
        0x101,
        (
            "#1004F#3P啊！？\x02\x03",

            "那是吉米先生\x01",
            "找到的海盗宝藏吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0x8,
        "哼哼，没错。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0x8,
        (
            "是我根据好几张古地图\x01",
            "费尽千辛万苦才找到的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B99")

    label("loc_A77")

    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #42
        0x101,
        (
            "#1004F#3P啊！？　是、是真的吗！？\x02\x03",

            "#1016F……等等，虽然刚才装着惊讶了一下，\x01",
            "不过那个大海盗某某某到底是什么人？\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #43
        0x8,
        (
            "你竟然不知道大海盗\x01",
            "希尔玛吗！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0x8,
        (
            "真令人不敢相信。\x01",
            "这也算是一个卢安市民？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0x101,
        (
            "#1016F#3P那个……这里是\x01",
            "蔡斯。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B99")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_BFB")

    ChrTalk(    #46
        0x106,
        (
            "#551F#4P好了，先不管那么多，\x01",
            "总之动作快一点吧。\x02\x03",

            "再磨磨蹭蹭的话\x01",
            "就会被魔兽发现了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C53")

    label("loc_BFB")


    ChrTalk(    #47
        0x103,
        (
            "#025F#4P好了，这些都无所谓，\x01",
            "总之动作快一点吧。\x02\x03",

            "再磨磨蹭蹭的话\x01",
            "就会被魔兽发现了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C53")


    ChrTalk(    #48
        0x8,
        "对，差点给忘了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0x8,
        (
            "好、好吧。\x01",
            "那么，要打开箱子喽！\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x8, 0, 400)
    OP_94(0x1, 0x8, 0x0, 0xC8, 0x3E8, 0x0)
    Sleep(1000)
    OP_70(0x0, 0x3C)
    OP_22(0x2B, 0x0, 0x64)
    Sleep(1000)
    OP_62(0x8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)

    ChrTalk(    #50
        0x101,
        "#1002F#3P你、你在磨蹭什么啊？\x02",
    )

    CloseMessageWindow()
    OP_63(0x8)
    OP_94(0x1, 0x8, 0x0, 0xC8, 0x3E8, 0x0)

    ChrTalk(    #51
        0x8,
        "等、等等。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0x8,
        "这、这到底是……\x02",
    )

    CloseMessageWindow()
    OP_20(0x3E8)
    Sleep(1000)
    OP_22(0xAC, 0x0, 0x64)
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_95(0x8, 0x0, 0x0, 0xFFFFFE70, 0x258, 0x1388)

    ChrTalk(    #53
        0x8,
        (
            "哇、哇哇！？\x01",
            "吓我一跳～～\x02",
        )
    )

    CloseMessageWindow()
    OP_43(0x101, 0x0, 0x1, 0x5)
    OP_43(0xF7, 0x0, 0x1, 0x6)
    OP_43(0xF8, 0x0, 0x1, 0x7)
    OP_43(0xF9, 0x0, 0x1, 0x8)
    Sleep(2000)
    OP_44(0x101, 0x0)
    OP_44(0xF7, 0x0)
    OP_44(0xF8, 0x0)
    OP_44(0xF9, 0x0)

    ChrTalk(    #54
        0x101,
        (
            "#1004F#3P这、这是什么声音！？\x02\x03",

            "#1020F难道是……陷阱！？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_E2F")

    ChrTalk(    #55
        0x106,
        (
            "#057F#4P不知道……\x01",
            "不过我有种不好的预感。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E5E")

    label("loc_E2F")


    ChrTalk(    #56
        0x103,
        (
            "#022F#4P不知道……\x01",
            "不过我有种不好的预感。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E5E")

    OP_22(0x24B, 0x0, 0x32)
    Sleep(200)
    OP_22(0x24B, 0x0, 0x32)
    Sleep(500)
    OP_22(0x24B, 0x0, 0x46)
    Sleep(200)
    OP_22(0x24B, 0x0, 0x46)
    Sleep(200)
    OP_22(0x24B, 0x0, 0x46)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_EE4")
    OP_8C(0x108, 180, 400)
    Fade(500)
    SetChrChipByIndex(0x108, 20)
    OP_0D()

    ChrTalk(    #57
        0x108,
        (
            "#070F呼，看来是猜中了。\x02\x03",

            "#072F……这么快就来了！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F85")

    label("loc_EE4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_F38")
    OP_8C(0x104, 180, 400)
    Fade(500)
    SetChrChipByIndex(0x104, 14)
    OP_0D()

    ChrTalk(    #58
        0x104,
        (
            "#035F呼，看来是猜中了。\x02\x03",

            "……这么快就来了！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F85")

    label("loc_F38")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_F85")
    OP_8C(0x105, 180, 400)
    Fade(500)
    SetChrChipByIndex(0x105, 16)
    OP_0D()

    ChrTalk(    #59
        0x105,
        (
            "#042F看来猜中了呢。\x02\x03",

            "……这么快就来了！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F85")

    OP_43(0x8, 0x1, 0x1, 0x10)

    def lambda_F92():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_F92)

    def lambda_FA0():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_FA0)

    def lambda_FAE():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_FAE)

    def lambda_FBC():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_FBC)

    def lambda_FCA():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_FCA)
    WaitChrThread(0x8, 0x1)
    OP_1D(0x29)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    OP_43(0xA, 0x1, 0x1, 0x9)
    OP_43(0xB, 0x1, 0x1, 0xA)
    OP_43(0xC, 0x1, 0x1, 0xB)
    OP_43(0xD, 0x1, 0x1, 0xC)
    OP_43(0xE, 0x1, 0x1, 0xD)
    OP_43(0xF, 0x1, 0x1, 0xE)

    def lambda_1027():
        OP_6D(11140, 0, 95380, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1027)
    WaitChrThread(0x101, 0x1)
    Sleep(2500)
    SetChrPos(0x8, 10000, 20, 111560, 135)
    SetChrPos(0x101, 10430, -70, 109710, 225)
    SetChrPos(0xF7, 11930, -70, 109190, 180)
    SetChrPos(0xF8, 13420, -30, 109960, 135)
    SetChrPos(0xF9, 13630, -30, 111710, 135)
    SetChrChipByIndex(0x101, 8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_10AC")
    SetChrChipByIndex(0x106, 12)
    Jump("loc_10B1")

    label("loc_10AC")

    SetChrChipByIndex(0x103, 10)

    label("loc_10B1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_10C4")
    SetChrChipByIndex(0x107, 18)

    label("loc_10C4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_10D7")
    SetChrChipByIndex(0x104, 14)

    label("loc_10D7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_10EA")
    SetChrChipByIndex(0x105, 16)

    label("loc_10EA")


    def lambda_10F0():
        OP_6D(11140, 0, 111010, 4000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_10F0)
    WaitChrThread(0x101, 0x1)
    OP_8F(0x8, 0x24A4, 0x28, 0x1B620, 0x3E8, 0x0)

    ChrTalk(    #60
        0x8,
        (
            "哇、哇哇～～！\x01",
            "从这里冒出来了吗～！\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x9, 7000, -3500, 119800, 135)
    SetChrChipByIndex(0x9, 24)
    SetChrSubChip(0x9, 0)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    TurnDirection(0x101, 0x9, 800)

    ChrTalk(    #61
        0x101,
        "#1005F吉米先生，你背后！！\x02",
    )

    CloseMessageWindow()

    def lambda_11A8():
        OP_6D(8400, 0, 116840, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_11A8)

    def lambda_11C0():
        OP_6B(2480, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_11C0)

    def lambda_11D0():
        OP_6C(0, 2000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_11D0)
    Sleep(400)

    def lambda_11E5():

        label("loc_11E5")

        TurnDirection(0xFE, 0x9, 400)
        OP_48()
        Jump("loc_11E5")

    QueueWorkItem2(0xF7, 2, lambda_11E5)

    def lambda_11F6():

        label("loc_11F6")

        TurnDirection(0xFE, 0x9, 400)
        OP_48()
        Jump("loc_11F6")

    QueueWorkItem2(0xF8, 2, lambda_11F6)

    def lambda_1207():

        label("loc_1207")

        TurnDirection(0xFE, 0x9, 400)
        OP_48()
        Jump("loc_1207")

    QueueWorkItem2(0xF9, 2, lambda_1207)
    WaitChrThread(0x101, 0x1)
    OP_22(0xE3, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #62
        0x8,
        "咦……！？\x02",
    )

    CloseMessageWindow()
    LoadEffect(0x0, "map\\\\mp012_00.eff")
    LoadEffect(0x1, "monster\\\\msc0591.eff")
    LoadEffect(0x2, "monster\\\\msc0590.eff")
    ClearMapFlags(0x10)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_1287():
        OP_67(0, 5840, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1287)

    def lambda_129F():
        OP_6D(8300, 0, 115820, 2000)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_129F)

    def lambda_12B7():
        OP_6B(2640, 2000)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_12B7)
    SetChrFlags(0x9, 0x4)
    SetChrFlags(0x9, 0x800)
    ClearChrFlags(0x9, 0x80)
    OP_9F(0x9, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_12E1():
        OP_96(0xFE, 0x21A2, 0x28A, 0x1BABC, 0x1F40, 0xFA0)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_12E1)

    def lambda_12FF():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x64)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_12FF)
    OP_22(0xE4, 0x0, 0x64)
    PlayEffect(0x0, 0x0, 0xFF, 7000, -1500, 119800, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(800)

    def lambda_1350():
        OP_99(0xFE, 0x1, 0x4, 0x7D0)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_1350)
    WaitChrThread(0x9, 0x0)
    OP_22(0xE5, 0x0, 0x64)
    OP_7C(0x0, 0x258, 0xBB8, 0xC8)

    def lambda_137B():
        OP_96(0xFE, 0x2620, 0x1E, 0x1B4CC, 0x3E8, 0xFA0)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_137B)

    def lambda_1399():
        OP_9E(0xFE, 0x14, 0x0, 0x0, 0xBB8)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1399)

    def lambda_13B3():
        OP_95(0xFE, 0x0, 0x0, 0x0, 0x3E8, 0x3E8)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_13B3)

    def lambda_13D1():
        OP_99(0xFE, 0x4, 0x7, 0x3E8)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_13D1)
    WaitChrThread(0x9, 0x2)
    SetChrChipByIndex(0x9, 24)
    SetChrSubChip(0x9, 0)
    WaitChrThread(0x9, 0x0)
    ClearChrFlags(0x9, 0x800)
    OP_22(0xE5, 0x0, 0x64)
    OP_7C(0x0, 0x12C, 0xBB8, 0x64)

    def lambda_1410():
        OP_95(0xFE, 0x0, 0x0, 0x0, 0x1F4, 0x1388)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_1410)

    def lambda_142E():
        TurnDirection(0xFE, 0x9, 400)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_142E)
    WaitChrThread(0x8, 0x0)
    OP_44(0x8, 0x1)
    OP_44(0xF7, 0x2)
    OP_44(0xF8, 0x2)
    OP_44(0xF9, 0x2)
    OP_8C(0x101, 315, 0)
    OP_8C(0xF7, 315, 0)
    OP_8C(0xF8, 315, 0)
    OP_8C(0xF9, 315, 0)
    WaitChrThread(0x101, 0x1)
    WaitChrThread(0xF7, 0x1)
    WaitChrThread(0xF8, 0x1)
    WaitChrThread(0xF9, 0x1)

    def lambda_1481():
        OP_6D(10100, 0, 112800, 2000)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_1481)

    def lambda_1499():
        OP_6C(356000, 2000)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_1499)

    def lambda_14A9():
        OP_6B(3340, 2000)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_14A9)
    SetChrChipByIndex(0x9, 1)
    SetChrSubChip(0x9, 0)

    def lambda_14C3():

        label("loc_14C3")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_14C3")

    QueueWorkItem2(0x9, 3, lambda_14C3)
    OP_62(0x8, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_8F(0x8, 0x2AA8, 0xFFFFFFCE, 0x1B198, 0xBB8, 0x0)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    ChrTalk(    #63
        0x8,
        (
            "#2P哇、哇哇！\x01",
            "这边也有啊～！！\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0xF7, 0x1)
    WaitChrThread(0xF8, 0x1)
    WaitChrThread(0xF9, 0x1)
    Sleep(1000)
    SetChrFlags(0x9, 0x800)
    OP_44(0x9, 0x3)
    SetChrChipByIndex(0x9, 24)
    SetChrSubChip(0x9, 0)
    OP_99(0x9, 0x0, 0x5, 0x5DC)
    Sleep(200)
    WaitChrThread(0xF7, 0x1)
    WaitChrThread(0xF8, 0x1)
    OP_99(0x9, 0x5, 0x7, 0x5DC)
    ClearChrFlags(0x9, 0x800)
    SetChrFlags(0x9, 0x8000)
    SetChrSubChip(0x9, 0)

    def lambda_1580():

        label("loc_1580")

        OP_99(0xFE, 0x0, 0x1, 0x5DC)
        OP_48()
        Jump("loc_1580")

    QueueWorkItem2(0x9, 3, lambda_1580)

    def lambda_1593():

        label("loc_1593")

        OP_7C(0x32, 0x0, 0xBB8, 0x64)
        OP_48()
        Jump("loc_1593")

    QueueWorkItem2(0x9, 2, lambda_1593)
    PlayEffect(0x2, 0x1, 0x9, 0, 1500, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(2000)

    ChrTalk(    #64
        0x101,
        "#1019F这、这是什么……！？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1629")

    ChrTalk(    #65
        0x107,
        "#065F哎、哎呀……！\x02",
    )

    CloseMessageWindow()

    label("loc_1629")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_165D")

    ChrTalk(    #66
        0x108,
        (
            "#070F呼……\x01",
            "看样子是新的主人呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_165D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_1687")

    ChrTalk(    #67
        0x106,
        "#054F#3P小心！　敌人来了！\x02",
    )

    CloseMessageWindow()
    Jump("loc_16A7")

    label("loc_1687")


    ChrTalk(    #68
        0x103,
        "#024F#3P小心！　敌人来了！\x02",
    )

    CloseMessageWindow()

    label("loc_16A7")

    OP_63(0x8)
    OP_82(0x1, 0x2)
    OP_44(0x9, 0x2)
    OP_44(0x9, 0x3)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x9, 24)
    SetChrSubChip(0x9, 0)

    def lambda_16CE():
        OP_96(0xFE, 0x2E04, 0x0, 0x1AFB8, 0x3E8, 0x3E8)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_16CE)

    def lambda_16EC():
        OP_99(0xFE, 0x0, 0x4, 0x7D0)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_16EC)
    OP_22(0xA3, 0x0, 0x64)
    Sleep(200)
    OP_44(0xA, 0xFF)
    OP_44(0xB, 0xFF)
    OP_44(0xC, 0xFF)
    OP_44(0xD, 0xFF)
    OP_44(0xE, 0xFF)
    OP_44(0xF, 0xFF)
    SetChrPos(0x10, 11780, 0, 110520, 0)
    TurnDirection(0xA, 0x10, 0)
    TurnDirection(0xB, 0x10, 0)
    TurnDirection(0xC, 0x10, 0)
    TurnDirection(0xD, 0x10, 0)
    TurnDirection(0xE, 0x10, 0)
    TurnDirection(0xF, 0x10, 0)

    def lambda_1759():
        OP_94(0x1, 0xFE, 0x0, 0xBB8, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_1759)

    def lambda_176F():
        OP_94(0x1, 0xFE, 0x0, 0xBB8, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_176F)

    def lambda_1785():
        OP_94(0x1, 0xFE, 0x0, 0xBB8, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_1785)

    def lambda_179B():
        OP_94(0x1, 0xFE, 0x0, 0xBB8, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 2, lambda_179B)

    def lambda_17B1():
        OP_94(0x1, 0xFE, 0x0, 0xBB8, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_17B1)

    def lambda_17C7():
        OP_94(0x1, 0xFE, 0x0, 0xBB8, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 2, lambda_17C7)
    Sleep(200)
    OP_44(0x9, 0xFF)
    OP_44(0xA, 0xFF)
    OP_44(0xB, 0xFF)
    OP_44(0xC, 0xFF)
    OP_44(0xD, 0xFF)
    OP_44(0xE, 0xFF)
    OP_44(0xF, 0xFF)
    Battle(0x1EA, 0x0, 0x1, 0x0, 0xFF)
    OP_44(0x9, 0xFF)
    OP_44(0xA, 0xFF)
    OP_44(0xB, 0xFF)
    OP_44(0xC, 0xFF)
    OP_44(0xD, 0xFF)
    OP_44(0xE, 0xFF)
    OP_44(0xF, 0xFF)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (1, "loc_182D"),
        (SWITCH_DEFAULT, "loc_1830"),
    )


    label("loc_182D")

    OP_B4(0x0)
    Return()

    label("loc_1830")

    Call(1, 15)
    Return()

    # Function_0_AA end

    def Function_1_1835(): pass

    label("Function_1_1835")

    SetChrPos(0x101, 11700, -30, 102960, 0)
    OP_8E(0x101, 0x2DB4, 0xFFFFFFB0, 0x1AA4A, 0x7D0, 0x0)
    Return()

    # Function_1_1835 end

    def Function_2_185B(): pass

    label("Function_2_185B")

    Sleep(400)
    SetChrPos(0xF7, 11100, -10, 102320, 0)
    OP_8E(0xF7, 0x2B5C, 0xFFFFFFD8, 0x1A59A, 0x7D0, 0x0)
    Return()

    # Function_2_185B end

    def Function_3_1886(): pass

    label("Function_3_1886")

    Sleep(400)
    Sleep(200)
    SetChrPos(0xF8, 12540, -50, 103220, 0)
    OP_8E(0xF8, 0x30FC, 0xFFFFFFCE, 0x1A77A, 0x7D0, 0x0)
    Return()

    # Function_3_1886 end

    def Function_4_18B6(): pass

    label("Function_4_18B6")

    Sleep(400)
    Sleep(200)
    Sleep(600)
    SetChrPos(0xF9, 11970, -40, 102840, 0)
    OP_8E(0xF9, 0x2EC2, 0xFFFFFFD8, 0x1A216, 0x7D0, 0x0)
    Return()

    # Function_4_18B6 end

    def Function_5_18EB(): pass

    label("Function_5_18EB")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_190F")
    OP_8C(0x101, 315, 400)
    Sleep(200)
    OP_8C(0x101, 45, 400)
    Sleep(500)
    Jump("Function_5_18EB")

    label("loc_190F")

    Return()

    # Function_5_18EB end

    def Function_6_1910(): pass

    label("Function_6_1910")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1939")
    Sleep(100)
    OP_8C(0xF7, 270, 400)
    Sleep(200)
    OP_8C(0xF7, 89, 400)
    Sleep(300)
    Jump("Function_6_1910")

    label("loc_1939")

    Return()

    # Function_6_1910 end

    def Function_7_193A(): pass

    label("Function_7_193A")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1963")
    Sleep(100)
    OP_8C(0xF8, 89, 400)
    Sleep(200)
    OP_8C(0xF8, 270, 400)
    Sleep(400)
    Jump("Function_7_193A")

    label("loc_1963")

    Return()

    # Function_7_193A end

    def Function_8_1964(): pass

    label("Function_8_1964")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1988")
    OP_8C(0xF9, 45, 400)
    Sleep(200)
    OP_8C(0xF9, 315, 400)
    Sleep(500)
    Jump("Function_8_1964")

    label("loc_1988")

    Return()

    # Function_8_1964 end

    def Function_9_1989(): pass

    label("Function_9_1989")

    SetChrPos(0xA, 12070, 0, 82290, 0)
    OP_62(0xA, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    OP_8E(0xA, 0x2F26, 0x28, 0x16DB4, 0x1388, 0x0)
    OP_8E(0xA, 0x22CE, 0x28, 0x17ACA, 0x1388, 0x0)
    OP_62(0xA, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    OP_8E(0xA, 0x22CE, 0x14, 0x189E8, 0x1388, 0x0)
    OP_8E(0xA, 0x2E54, 0xFFFFFFF6, 0x197B2, 0x1388, 0x0)
    OP_62(0xA, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    OP_8E(0xA, 0x2E54, 0xFFFFFFF6, 0x19C30, 0x1388, 0x0)
    OP_8E(0xA, 0x3CE6, 0xFFFFFFF6, 0x1B0D0, 0x1388, 0x0)
    TurnDirection(0xA, 0x101, 400)
    OP_63(0xA)
    OP_22(0x24B, 0x0, 0x50)
    OP_43(0xA, 0x0, 0x6, 0x2)
    Return()

    # Function_9_1989 end

    def Function_10_1A5F(): pass

    label("Function_10_1A5F")

    Sleep(500)
    OP_62(0xB, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    SetChrPos(0xB, 12070, 0, 82290, 0)
    OP_8E(0xB, 0x2F26, 0x28, 0x16DB4, 0x1388, 0x0)
    OP_8E(0xB, 0x22CE, 0x28, 0x17ACA, 0x1388, 0x0)
    OP_62(0xB, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    OP_8E(0xB, 0x22CE, 0x14, 0x189E8, 0x1388, 0x0)
    OP_8E(0xB, 0x2E54, 0xFFFFFFF6, 0x197B2, 0x1388, 0x0)
    OP_62(0xB, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    OP_8E(0xB, 0x2E54, 0xFFFFFFF6, 0x19C30, 0x1388, 0x0)
    OP_8E(0xB, 0x20E4, 0xFFFFFFF6, 0x1A86A, 0x1388, 0x0)
    TurnDirection(0xB, 0x101, 400)
    OP_63(0xB)
    OP_22(0x24B, 0x0, 0x50)
    OP_43(0xB, 0x0, 0x6, 0x2)
    Return()

    # Function_10_1A5F end

    def Function_11_1B3A(): pass

    label("Function_11_1B3A")

    Sleep(1000)
    OP_62(0xC, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    SetChrPos(0xC, 12070, 0, 82290, 0)
    OP_8E(0xC, 0x2F26, 0x28, 0x16DB4, 0x1388, 0x0)
    OP_8E(0xC, 0x22CE, 0x28, 0x17ACA, 0x1388, 0x0)
    OP_62(0xC, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    OP_8E(0xC, 0x22CE, 0x14, 0x189E8, 0x1388, 0x0)
    OP_8E(0xC, 0x2E54, 0xFFFFFFF6, 0x197B2, 0x1388, 0x0)
    OP_62(0xC, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    OP_8E(0xC, 0x2E54, 0xFFFFFFF6, 0x19C30, 0x1388, 0x0)
    OP_8E(0xC, 0x3ADE, 0xFFFFFFCE, 0x1A93C, 0x1388, 0x0)
    TurnDirection(0xC, 0x101, 400)
    OP_63(0xC)
    OP_22(0x24B, 0x0, 0x50)
    OP_43(0xC, 0x0, 0x6, 0x2)
    Return()

    # Function_11_1B3A end

    def Function_12_1C15(): pass

    label("Function_12_1C15")

    Sleep(1500)
    OP_62(0xD, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    SetChrPos(0xD, 12070, 0, 82290, 0)
    OP_8E(0xD, 0x2F26, 0x28, 0x16DB4, 0x1388, 0x0)
    OP_8E(0xD, 0x22CE, 0x28, 0x17ACA, 0x1388, 0x0)
    OP_62(0xD, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    OP_8E(0xD, 0x22CE, 0x14, 0x189E8, 0x1388, 0x0)
    OP_8E(0xD, 0x2E54, 0xFFFFFFF6, 0x197B2, 0x1388, 0x0)
    OP_62(0xD, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    OP_8E(0xD, 0x2E54, 0xFFFFFFF6, 0x19C30, 0x1388, 0x0)
    OP_8E(0xD, 0x27A6, 0xFFFFFFEC, 0x1A2C0, 0x1388, 0x0)
    TurnDirection(0xD, 0x101, 400)
    OP_63(0xD)
    OP_22(0x24B, 0x0, 0x50)
    OP_43(0xD, 0x0, 0x6, 0x2)
    Return()

    # Function_12_1C15 end

    def Function_13_1CF0(): pass

    label("Function_13_1CF0")

    Sleep(2000)
    OP_62(0xE, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    SetChrPos(0xE, 12070, 0, 82290, 0)
    OP_8E(0xE, 0x2F26, 0x28, 0x16DB4, 0x1388, 0x0)
    OP_8E(0xE, 0x22CE, 0x28, 0x17ACA, 0x1388, 0x0)
    OP_62(0xE, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    OP_8E(0xE, 0x22CE, 0x14, 0x189E8, 0x1388, 0x0)
    OP_8E(0xE, 0x2E54, 0xFFFFFFF6, 0x197B2, 0x1388, 0x0)
    OP_62(0xE, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    OP_8E(0xE, 0x2E54, 0xFFFFFFF6, 0x19C30, 0x1388, 0x0)
    OP_8E(0xE, 0x3584, 0xFFFFFFEC, 0x1A3D8, 0x1388, 0x0)
    TurnDirection(0xE, 0x101, 400)
    OP_63(0xE)
    OP_22(0x24B, 0x0, 0x50)
    OP_43(0xE, 0x0, 0x6, 0x2)
    Return()

    # Function_13_1CF0 end

    def Function_14_1DCB(): pass

    label("Function_14_1DCB")

    Sleep(2500)
    OP_62(0xF, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    SetChrPos(0xF, 12070, 0, 82290, 0)
    OP_8E(0xF, 0x2F26, 0x28, 0x16DB4, 0x1388, 0x0)
    OP_8E(0xF, 0x22CE, 0x28, 0x17ACA, 0x1388, 0x0)
    OP_62(0xF, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    OP_8E(0xF, 0x22CE, 0x14, 0x189E8, 0x1388, 0x0)
    OP_8E(0xF, 0x2E54, 0xFFFFFFF6, 0x197B2, 0x1388, 0x0)
    OP_62(0xF, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    OP_8E(0xF, 0x2E54, 0xFFFFFFF6, 0x19C30, 0x1388, 0x0)
    OP_8E(0xF, 0x2E36, 0xFFFFFFEC, 0x1A108, 0x1388, 0x0)
    TurnDirection(0xF, 0x101, 400)
    OP_63(0xF)
    OP_22(0x24B, 0x0, 0x50)
    OP_43(0xF, 0x0, 0x6, 0x2)
    Return()

    # Function_14_1DCB end

    def Function_15_1EA6(): pass

    label("Function_15_1EA6")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    RemoveParty(0x47, 0xFF)
    SetMapFlags(0x10)
    OP_72(0x0, 0x4)
    OP_6F(0x0, 60)
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, 9960, 20, 109000, 0)
    SetChrPos(0x101, 10430, -70, 106710, 0)
    SetChrPos(0xF7, 11930, -70, 106190, 0)
    SetChrPos(0xF8, 13420, -30, 106960, 135)
    SetChrPos(0xF9, 13630, -30, 108710, 135)
    TurnDirection(0xF8, 0x8, 0)
    TurnDirection(0xF9, 0x8, 0)
    SetChrChipByIndex(0x101, 65535)
    SetChrChipByIndex(0xF7, 65535)
    SetChrChipByIndex(0xF8, 65535)
    SetChrChipByIndex(0xF9, 65535)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0xF, 0x80)
    OP_6D(12660, -40, 109960, 0)
    OP_67(0, 5920, -10000, 0)
    OP_6B(3030, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(    #69
        0x101,
        (
            "#1007F#4P又、又一次被\x01",
            "吓了一跳呢～\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2002")

    ChrTalk(    #70
        0x107,
        (
            "#067F好、好华丽的\x01",
            "企鹅啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2002")


    ChrTalk(    #71
        0x8,
        (
            "呼～呼～\x01",
            "我还以为会死在这里呢。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2091")

    ChrTalk(    #72
        0x108,
        (
            "#070F#2P哎呀呀，这次\x01",
            "总算是把它们击退了。\x02\x03",

            "在第二波袭击到来之前\x01",
            "赶快撤退吧。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x108, 400)
    Jump("loc_2150")

    label("loc_2091")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_20F6")

    ChrTalk(    #73
        0x104,
        (
            "#030F#2P呼，总算是把它们击退了。\x02\x03",

            "在第二波袭击到来之前\x01",
            "赶紧撤退比较好。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x104, 400)
    Jump("loc_2150")

    label("loc_20F6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2150")

    ChrTalk(    #74
        0x105,
        (
            "#040F#2P总算是击退了……\x02\x03",

            "在第二波袭击到来之前\x01",
            "赶紧撤离比较好。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x105, 400)

    label("loc_2150")


    ChrTalk(    #75
        0x8,
        "明、明白了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0x8,
        (
            "那、那我马上\x01",
            "回收宝箱里的东西吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_8B(0x8, 0x2B5C, 0x1B792, 0x190)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_21E7")

    ChrTalk(    #77
        0x106,
        (
            "#052F……不，等等。\x02\x03",

            "#050F那个就交给我们吧。\x01",
            "说不定还有什么机关。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2227")

    label("loc_21E7")


    ChrTalk(    #78
        0x103,
        (
            "#022F不，等一下。\x02\x03",

            "那个就交给我们吧。\x01",
            "说不定还有什么机关。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2227")

    OP_62(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(400)
    TurnDirection(0x8, 0xF7, 400)

    ChrTalk(    #79
        0x8,
        "确、确实如此。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0x101,
        "#1006F#4P那么我来看看。\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    OP_66(0x0)

    def lambda_2284():
        OP_6D(11140, -50, 111010, 3000)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_2284)
    OP_8E(0x101, 0x2CEC, 0xFFFFFFE2, 0x1A504, 0x7D0, 0x0)

    def lambda_22B0():

        label("loc_22B0")

        TurnDirection(0x8, 0x101, 400)
        OP_48()
        Jump("loc_22B0")

    QueueWorkItem2(0x8, 1, lambda_22B0)

    def lambda_22C1():

        label("loc_22C1")

        TurnDirection(0xF7, 0x101, 400)
        OP_48()
        Jump("loc_22C1")

    QueueWorkItem2(0xF7, 1, lambda_22C1)

    def lambda_22D2():

        label("loc_22D2")

        TurnDirection(0xF8, 0x101, 400)
        OP_48()
        Jump("loc_22D2")

    QueueWorkItem2(0xF8, 1, lambda_22D2)

    def lambda_22E3():

        label("loc_22E3")

        TurnDirection(0xF9, 0x101, 400)
        OP_48()
        Jump("loc_22E3")

    QueueWorkItem2(0xF9, 1, lambda_22E3)
    OP_8E(0x101, 0x2B66, 0xFFFFFFD8, 0x1B42C, 0x7D0, 0x0)
    OP_8C(0x101, 0, 400)
    OP_44(0x8, 0x1)
    OP_44(0xF7, 0x1)
    OP_44(0xF8, 0x1)
    OP_44(0xF9, 0x1)
    WaitChrThread(0x8, 0x0)
    OP_66(0x1)
    Sleep(1000)
    OP_62(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_63(0x101)

    ChrTalk(    #81
        0x101,
        (
            "#1015F嗯……\x01",
            "没什么特别可疑的地方了。\x02\x03",

            "这样应该没问题了……\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #82
        "\x07\x00得到了\x07\x02#16I银露宝珠\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)

    ChrTalk(    #83
        0x101,
        (
            "#1018F好，回收完成。\x02\x03",

            "#1004F……咦？这！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0x8,
        "怎、怎么了？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0x101,
        (
            "#1002F嗯、嗯。\x01",
            "箱子里有张纸条哦。\x02\x03",

            "……好像是一封信。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 180, 400)
    Fade(500)
    SetChrChipByIndex(0x101, 23)
    OP_0D()
    Sleep(400)

    ChrTalk(    #86
        0x101,
        "#1011F嗯……我看看……\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #87
        (
            "\x07\x05为了纪念我７０岁生日\x01",
            "以及海盗生涯的结束，\x01",
            "把我的『银露宝珠』藏在这里。\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #88
        (
            "\x07\x05这『宝珠』可以告知所有者\x01",
            "各种危机的来临。\x01",
            "我能活到今天\x01",
            "全仰赖于这件宝物的力量。\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #89
        (
            "\x07\x05但是，我也上年纪了。\x01",
            "现在对那些追寻它的\x01",
            "『骑士』们感到很头痛。\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #90
        (
            "\x07\x05所以让它沉入湖底。\x01",
            "发现它的人可以随意处置。\x01",
            "不过，就像我刚才所写的那样，\x01",
            "它是一件会让你感到很辛苦的宝物……\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #91
        "\x07\x05……海盗希尔玛记于此。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    Fade(500)
    SetChrChipByIndex(0x101, 65535)
    OP_0D()

    ChrTalk(    #92
        0x101,
        "#1002F…………没了。\x02",
    )

    CloseMessageWindow()
    OP_8E(0x8, 0x2B66, 0xFFFFFFCE, 0x1B01C, 0x1770, 0x0)
    TurnDirection(0x8, 0x101, 400)
    OP_62(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_94(0x1, 0x8, 0x0, 0xC8, 0x1B58, 0x0)
    OP_94(0x1, 0x101, 0xB4, 0xC8, 0x1B58, 0x0)
    OP_94(0x1, 0x8, 0xB4, 0xC8, 0x1B58, 0x0)
    OP_94(0x1, 0x101, 0x0, 0xC8, 0x1B58, 0x0)
    OP_94(0x1, 0x8, 0x0, 0xC8, 0x1B58, 0x0)
    OP_94(0x1, 0x101, 0xB4, 0xC8, 0x1B58, 0x0)
    OP_94(0x1, 0x8, 0xB4, 0xC8, 0x1B58, 0x0)
    OP_94(0x1, 0x101, 0x0, 0xC8, 0x1B58, 0x0)
    OP_94(0x1, 0x8, 0x0, 0xC8, 0x1B58, 0x0)
    OP_94(0x1, 0x101, 0xB4, 0xC8, 0x1B58, 0x0)
    OP_94(0x1, 0x8, 0xB4, 0xC8, 0x1B58, 0x0)
    OP_94(0x1, 0x101, 0x0, 0xC8, 0x1B58, 0x0)
    OP_94(0x1, 0x8, 0x0, 0xC8, 0x1B58, 0x0)
    OP_94(0x1, 0x101, 0xB4, 0xC8, 0x1B58, 0x0)

    ChrTalk(    #93
        0x8,
        (
            "#3P哇～～！\x01",
            "让、让我看看！\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x8, 400)

    ChrTalk(    #94
        0x101,
        (
            "#1016F知、知道了，\x01",
            "不用那么着急啊。\x02\x03",

            "而且，现在必须先\x01",
            "返回蔡斯。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_27DA")

    ChrTalk(    #95
        0x106,
        (
            "#053F如果你还想和那个\x01",
            "古怪的怪物战斗的话……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_280C")

    label("loc_27DA")


    ChrTalk(    #96
        0x103,
        (
            "#027F如果你还想和那个\x01",
            "古怪的怪物战斗的话……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_280C")


    def lambda_2812():
        OP_8C(0x8, 180, 400)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_2812)
    Sleep(250)
    OP_8C(0x101, 180, 400)

    ChrTalk(    #97
        0x8,
        (
            "#3P不、不不，\x01",
            "就饶了我吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0x8,
        (
            "#3P既然如此就\x01",
            "赶快回去吧。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_28A2")

    ChrTalk(    #99
        0x108,
        (
            "#070F嗯，这么做比较好。\x02\x03",

            "那就快走吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2921")

    label("loc_28A2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_28E0")

    ChrTalk(    #100
        0x104,
        (
            "#030F这个决定十分明智。\x02\x03",

            "呼，那么走吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2921")

    label("loc_28E0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2921")

    ChrTalk(    #101
        0x105,
        (
            "#040F嗯，这个决定十分明智。\x02\x03",

            "那么，我们走吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2921")


    ChrTalk(    #102
        0x101,
        "#1006F嗯，走吧。\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x10F3)
    NewScene("ED6_DT21/T3120   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_15_1EA6 end

    def Function_16_294F(): pass

    label("Function_16_294F")

    OP_24(0xAC, 0x5A)
    Sleep(100)
    OP_24(0xAC, 0x50)
    Sleep(100)
    OP_24(0xAC, 0x46)
    Sleep(100)
    OP_24(0xAC, 0x3C)
    Sleep(100)
    OP_24(0xAC, 0x32)
    Sleep(100)
    OP_24(0xAC, 0x28)
    Sleep(100)
    OP_24(0xAC, 0x1E)
    Sleep(100)
    OP_24(0xAC, 0x14)
    Sleep(100)
    OP_24(0xAC, 0xA)
    Sleep(100)
    OP_23(0xAC)
    Return()

    # Function_16_294F end

    SaveToFile()

Try(main)

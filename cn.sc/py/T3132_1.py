from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 洛连特

    CreateScenaFile(
        FileName            = 'T3132_1 ._SN',
        MapName             = 'Rolent',
        Location            = 'C0403.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60010",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            '',
            'ED6_DT21/T3132_1 ._SN',
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
        "Function_1_332",          # 01, 1
        "Function_2_530",          # 02, 2
    )


    def Function_0_AA(): pass

    label("Function_0_AA")

    EventBegin(0x0)
    Fade(1000)
    SetChrPos(0x8, -1700, 0, 2400, 192)
    SetChrPos(0x101, -2340, 0, 450, 0)
    SetChrPos(0xF7, -1190, 0, 350, 0)
    SetChrPos(0xF8, -2290, 0, -670, 0)
    SetChrPos(0xF9, -1120, 0, -670, 0)
    OP_6D(-2000, 0, 50, 0)
    OP_67(0, 6150, -10000, 0)
    OP_6B(2750, 0)
    OP_6C(315000, 0)
    OP_6E(280, 0)
    OP_0D()

    ChrTalk(    #0
        0x8,
        (
            "欢迎光临。\x01",
            "欢迎光临蔡恩拉德酒店。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x8,
        "你们是有预约的客人吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x101,
        (
            "#1011F不，不是的。\x02\x03",

            "我们是从\x01",
            "协会赶来的……\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(400)

    ChrTalk(    #3
        0x8,
        "啊，各位是游击士？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x8,
        (
            "失礼了。\x01",
            "我一直在等你们。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x8,
        (
            "那个，能不能马上\x01",
            "就着手寻找呢？\x02",
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_29B")

    ChrTalk(    #6
        0x101,
        "#1006F嗯，没问题。\x02",
    )

    CloseMessageWindow()
    Call(1, 2)
    Jump("loc_331")

    label("loc_29B")


    ChrTalk(    #7
        0x101,
        (
            "#1007F啊，对不起。\x02\x03",

            "十分抱歉，\x01",
            "现在马上开始还有些困难。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x8,
        (
            "哦，这样啊。\x01",
            "这可不好办了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x8,
        (
            "那么请你们料理完\x01",
            "手头的事之后马上过来。\x02",
        )
    )

    CloseMessageWindow()
    OP_28(0x71, 0x1, 0x8000)
    EventEnd(0x0)
    Return()

    label("loc_331")

    Return()

    # Function_0_AA end

    def Function_1_332(): pass

    label("Function_1_332")

    EventBegin(0x0)
    Fade(1000)
    SetChrPos(0x8, -1700, 0, 2400, 192)
    SetChrPos(0x101, -2340, 0, 450, 0)
    SetChrPos(0xF7, -1190, 0, 350, 0)
    SetChrPos(0xF8, -2290, 0, -670, 0)
    SetChrPos(0xF9, -1120, 0, -670, 0)
    OP_6D(-2000, 0, 50, 0)
    OP_67(0, 6150, -10000, 0)
    OP_6B(2750, 0)
    OP_6C(315000, 0)
    OP_6E(280, 0)
    OP_0D()

    ChrTalk(    #10
        0x8,
        (
            "诸位游击士，\x01",
            "我一直在等你们。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x8,
        (
            "我有必须马上拜托\x01",
            "你们的急事。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x8,
        (
            "你们没什么\x01",
            "其他的事了吧？\x02",
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4B0")

    ChrTalk(    #13
        0x101,
        (
            "#1006F让你久等了。\x01",
            "已经没问题了。\x02",
        )
    )

    CloseMessageWindow()
    Call(1, 2)
    Jump("loc_52F")

    label("loc_4B0")


    ChrTalk(    #14
        0x101,
        (
            "#1007F抱、抱歉……\x01",
            "其实现在还不行啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x8,
        "呼，你们真忙……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x8,
        (
            "没办法，\x01",
            "那就请你们尽早过来吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x101,
        "#1006F嗯，好吧。\x02",
    )

    CloseMessageWindow()
    EventEnd(0x0)
    Return()

    label("loc_52F")

    Return()

    # Function_1_332 end

    def Function_2_530(): pass

    label("Function_2_530")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x1E, 0x0, 0x4)"), scpexpr(EXPR_END)), "loc_53D")
    OP_A2(0x4)

    label("loc_53D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5B8")
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
        (0, "loc_5B2"),
        (SWITCH_DEFAULT, "loc_5B8"),
    )


    label("loc_5B2")

    OP_A2(0x4)
    Jump("loc_5B8")

    label("loc_5B8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5F9")

    ChrTalk(    #18
        0x108,
        (
            "#070F根据告示板的公告，\x01",
            "好像客人不回来了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_674")

    label("loc_5F9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_636")

    ChrTalk(    #19
        0x104,
        (
            "#030F我看了告示板，\x01",
            "好像客人不回来了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_674")

    label("loc_636")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_674")

    ChrTalk(    #20
        0x105,
        (
            "#040F看了告示板的公告，\x01",
            "好像客人不回来了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_674")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_697")

    ChrTalk(    #21
        0x106,
        "#050F就是说失踪了？\x02",
    )

    CloseMessageWindow()
    Jump("loc_6B0")

    label("loc_697")


    ChrTalk(    #22
        0x103,
        "#022F就是说失踪了？\x02",
    )

    CloseMessageWindow()

    label("loc_6B0")


    ChrTalk(    #23
        0x8,
        (
            "是、是的……\x01",
            "是这样的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x8,
        (
            "三天前出去了\x01",
            "就没回来。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x101,
        (
            "#1002F三天都没回来\x01",
            "确实令人担心呢。\x02\x03",

            "而且最近大道上也有\x01",
            "很多讨厌的魔兽……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x8,
        (
            "不，要是大道\x01",
            "的话还好……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x8,
        (
            "可是那位客人……\x01",
            "好像是去了钟乳洞。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #28
        0x101,
        (
            "#1004F钟、钟乳洞！？\x02\x03",

            "莫非是\x01",
            "卡鲁迪亚隧道中途的那个？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x8,
        (
            "是，是……\x01",
            "就是那个卡鲁迪亚钟乳洞。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x8,
        (
            "我们也拼命地\x01",
            "阻止过他……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_86E")

    ChrTalk(    #31
        0x108,
        (
            "#072F这可不好办了。\x02\x03",

            "那里不是普通人\x01",
            "能够进出的地方啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_90B")

    label("loc_86E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8C1")

    ChrTalk(    #32
        0x106,
        (
            "#057F喂喂，开什么玩笑啊。\x02\x03",

            "那里不是普通人\x01",
            "能够进出的地方啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_90B")

    label("loc_8C1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_90B")

    ChrTalk(    #33
        0x103,
        (
            "#022F这可不好办了……\x02\x03",

            "钟乳洞可是这一带\x01",
            "有名的难关呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_90B")


    ChrTalk(    #34
        0x101,
        (
            "#1003F竟然不带护卫\x01",
            "就去那种地方……\x02\x03",

            "#1002F那个客人到底是何方神圣？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x8,
        "是个很普通的青年哦。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x8,
        (
            "名字叫吉米，\x01",
            "据他说是来自卢安。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_B6B")
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #37
        0x101,
        (
            "#1004F卢、卢安的吉米先生？\x02\x03",

            "#1019F那、那莫非是……\x02",
        )
    )

    CloseMessageWindow()

    def lambda_9F4():
        TurnDirection(0xF7, 0x101, 400)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_9F4)
    Sleep(50)

    def lambda_A07():
        TurnDirection(0xF8, 0x101, 400)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_A07)
    Sleep(100)
    TurnDirection(0xF9, 0x101, 400)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_A38")

    ChrTalk(    #38
        0x106,
        "#052F你认识？\x02",
    )

    CloseMessageWindow()
    Jump("loc_A4B")

    label("loc_A38")


    ChrTalk(    #39
        0x103,
        "#023F你认识？\x02",
    )

    CloseMessageWindow()

    label("loc_A4B")

    TurnDirection(0x101, 0xF7, 400)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_AE7")

    ChrTalk(    #40
        0x101,
        (
            "#1002F嗯，我曾接过叫这个\x01",
            "名字的人的委托。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0x105,
        (
            "#043F记得他那时候在\x01",
            "寻找海盗的宝藏吧。\x02\x03",

            "他这次会不会也是\x01",
            "去钟乳洞寻找什么宝藏？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B68")

    label("loc_AE7")


    ChrTalk(    #42
        0x101,
        (
            "#1002F嗯，我曾接过叫这个\x01",
            "名字的人的委托。\x02\x03",

            "#1015F记得他那时候在\x01",
            "寻找海盗的宝藏吧。\x02\x03",

            "他这次会不会也是\x01",
            "去钟乳洞寻找什么宝藏？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B68")

    Jump("loc_BA4")

    label("loc_B6B")


    ChrTalk(    #43
        0x101,
        (
            "#1015F卢安的吉米先生。\x02\x03",

            "听上去倒像是\x01",
            "一个普通人……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BA4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_BF0")

    ChrTalk(    #44
        0x104,
        (
            "#032F总之我们要尽快\x01",
            "赶往钟乳洞。\x02\x03",

            "搞不好会\x01",
            "来不及的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C89")

    label("loc_BF0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C40")

    ChrTalk(    #45
        0x107,
        (
            "#062F总、总之得尽快\x01",
            "去钟乳洞。\x02\x03",

            "而且最近魔兽也\x01",
            "特别多……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C89")

    label("loc_C40")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C89")

    ChrTalk(    #46
        0x108,
        (
            "#072F总之我们要尽快\x01",
            "赶往钟乳洞。\x02\x03",

            "搞不好会\x01",
            "来不及的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C89")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_D10")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_CD9")

    ChrTalk(    #47
        0x106,
        "#053F嗯，越快越好。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x106, 0x8, 400)

    ChrTalk(    #48
        0x106,
        "#050F……没其他情报了吗？\x02",
    )

    CloseMessageWindow()
    Jump("loc_D0D")

    label("loc_CD9")


    ChrTalk(    #49
        0x106,
        (
            "#053F嗯，越快越好。\x02\x03",

            "#050F……没其他情报了吗？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D0D")

    Jump("loc_D88")

    label("loc_D10")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_D59")

    ChrTalk(    #50
        0x103,
        "#022F嗯，越快越好。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x8, 400)

    ChrTalk(    #51
        0x103,
        "#022F……没其他情报了吗？\x02",
    )

    CloseMessageWindow()
    Jump("loc_D88")

    label("loc_D59")


    ChrTalk(    #52
        0x103,
        (
            "#022F嗯，越快越好。\x02\x03",

            "……没其他情报了吗？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D88")


    def lambda_D8E():
        OP_8C(0x101, 0, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_D8E)
    Sleep(50)

    def lambda_DA1():
        OP_8C(0xF8, 0, 400)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_DA1)
    Sleep(100)
    OP_8C(0xF9, 0, 400)
    WaitChrThread(0xF8, 0x1)

    ChrTalk(    #53
        0x8,
        (
            "该说的我都\x01",
            "已经说了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0x8,
        (
            "那么，客人就\x01",
            "就麻烦你们了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0x101,
        "#1002F嗯，我们会尽全力的。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_E37")

    ChrTalk(    #56
        0x106,
        "#050F那我们走了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_E4E")

    label("loc_E37")


    ChrTalk(    #57
        0x103,
        "#022F那我们走了。\x02",
    )

    CloseMessageWindow()

    label("loc_E4E")

    OP_28(0x71, 0x4, 0x4)
    OP_28(0x71, 0x4, 0x8)
    OP_28(0x71, 0x1, 0x1)
    OP_28(0x71, 0x1, 0x2)
    EventEnd(0x0)
    Return()

    # Function_2_530 end

    SaveToFile()

Try(main)

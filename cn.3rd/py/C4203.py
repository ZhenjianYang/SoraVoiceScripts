from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'C4203   ._SN',
        MapName             = 'Grancel',
        Location            = 'C4203.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60031",
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
        '诺琪',                                 # 9
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


    AddCharChip(
        'ED6_DT07/CH01230 ._CH',             # 00
        'ED6_DT09/CH11120 ._CH',             # 01
        'ED6_DT09/CH11121 ._CH',             # 02
        'ED6_DT09/CH11110 ._CH',             # 03
        'ED6_DT09/CH11111 ._CH',             # 04
        'ED6_DT09/CH11130 ._CH',             # 05
        'ED6_DT09/CH11131 ._CH',             # 06
        'ED6_DT09/CH10040 ._CH',             # 07
        'ED6_DT09/CH10041 ._CH',             # 08
        'ED6_DT09/CH11140 ._CH',             # 09
        'ED6_DT09/CH11141 ._CH',             # 0A
    )

    AddCharChipPat(
        'ED6_DT07/CH01230P._CP',             # 00
        'ED6_DT09/CH11120P._CP',             # 01
        'ED6_DT09/CH11121P._CP',             # 02
        'ED6_DT09/CH11110P._CP',             # 03
        'ED6_DT09/CH11111P._CP',             # 04
        'ED6_DT09/CH11130P._CP',             # 05
        'ED6_DT09/CH11131P._CP',             # 06
        'ED6_DT09/CH10040P._CP',             # 07
        'ED6_DT09/CH10041P._CP',             # 08
        'ED6_DT09/CH11140P._CP',             # 09
        'ED6_DT09/CH11141P._CP',             # 0A
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclMonster(
        X                   = -47360,
        Z                   = 0,
        Y                   = 42620,
        Unknown_0C          = 180,
        Unknown_0E          = 1,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x3B1,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -121330,
        Z                   = 0,
        Y                   = 50600,
        Unknown_0C          = 180,
        Unknown_0E          = 5,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x3B3,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -88180,
        Z                   = 0,
        Y                   = 51510,
        Unknown_0C          = 180,
        Unknown_0E          = 9,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x3B5,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclActor(
        TriggerX            = -91330,
        TriggerZ            = 0,
        TriggerY            = 60050,
        TriggerRange        = 1000,
        ActorX              = -91210,
        ActorZ              = 1500,
        ActorY              = 60790,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 2,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_19A",          # 00, 0
        "Function_1_1AE",          # 01, 1
        "Function_2_1E3",          # 02, 2
        "Function_3_309",          # 03, 3
        "Function_4_332",          # 04, 4
        "Function_5_925",          # 05, 5
        "Function_6_D48",          # 06, 6
        "Function_7_1566",         # 07, 7
        "Function_8_15C3",         # 08, 8
    )


    def Function_0_19A(): pass

    label("Function_0_19A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 4)), scpexpr(EXPR_END)), "loc_1AD")
    OP_A3(0x2504)
    SetMapFlags(0x10000000)
    Event(0, 3)

    label("loc_1AD")

    Return()

    # Function_0_19A end

    def Function_1_1AE(): pass

    label("Function_1_1AE")

    OP_64(0x1, 0x1)
    OP_72(0x1000, 0x0)
    ExitThread()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5FE, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1CA")
    OP_6F(0x1, 0)
    Jump("loc_1D1")

    label("loc_1CA")

    OP_6F(0x1, 60)

    label("loc_1D1")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1E2")
    OP_22(0x1CD, 0x1, 0x64)

    label("loc_1E2")

    Return()

    # Function_1_1AE end

    def Function_2_1E3(): pass

    label("Function_2_1E3")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5FE, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C8")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x1, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x203, 1)"), scpexpr(EXPR_END)), "loc_257")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #0
        "\x07\x00得到了\x1F\x03\x02\x07\x00。\x02",
    )

    Jump("loc_23C")

    label("loc_23C")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2FF7)
    Jump("loc_2C5")

    label("loc_257")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #1
        (
            "宝箱里装有\x1F\x03\x02\x07\x00。\x01",
            "不过现有的数量太多，\x1F\x03\x02\x07\x00不能再拿更多了。\x02",
        )
    )

    Jump("loc_2A6")

    label("loc_2A6")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x1, 60)
    OP_70(0x1, 0x0)

    label("loc_2C5")

    Jump("loc_2FB")

    label("loc_2C8")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #2
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_2FB")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_2_1E3 end

    def Function_3_309(): pass

    label("Function_3_309")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_D6(0x0)
    OP_E3(0x0, 0xC, 1, 0x0)
    ClearParty()
    AddParty(0x0, 0xEE, 0xFF)
    OP_28(0x1D, 0x4, 0x8)
    Call(0, 4)
    Call(0, 5)
    Return()

    # Function_3_309 end

    def Function_4_332(): pass

    label("Function_4_332")

    OP_20(0x0)
    OP_23(0x1CD)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    ClearChrFlags(0x101, 0x80)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x101, -60570, 0, 90980, 90)
    SetChrPos(0x10, -59240, 0, 90940, 270)
    OP_6D(-59750, 200, 90940, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_77(0xEE, 0xB0, 0x70, 0x0, 0x0)
    OP_82(0xA4, 0x0)
    OP_82(0xA6, 0x0)
    OP_75(0xFF, 0x0, 0x5)
    OP_75(0xFF, 0x1, 0x5)
    OP_C4(0x0, 0x800)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(1000)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #3 op#A op#5
        "\x07\x00#15A～第２章　王都逸事～\x05\x02",
    )

    CloseMessageWindow()
    Sleep(2000)
    OP_56(0x0)
    Sleep(500)
    OP_1E()
    FadeToBright(3000, 0)
    OP_0D()
    Sleep(1000)
    FadeToDark(1000, 0, 80)
    Sleep(2000)

    AnonymousTalk(    #4
        (
            "\x07\x00王都格兰赛尔地下水路，北部区域――\x02\x01",

            "艾丝蒂尔为了剿灭通缉魔兽，\x01",
            "进入了这条水道。\x02\x01",

            "　\x01",
            "艾丝蒂尔正在探索目标――\x02\x01",

            "这时在她面前突然出现了一位淑女。\x02",
        )
    )

    Jump("loc_4DB")

    label("loc_4DB")

    CloseMessageWindow()

    AnonymousTalk(    #5
        (
            "\x07\x00『你、你在这种地方干什么？』\x02\x01",

            "　\x01",
            "『干什么，当然是钓鱼了。』\x02\x01",

            "丂\x01",
            "这是『钓公师团』的成员之一，\x01",
            "名为诺琪的淑女。\x02",
        )
    )

    Jump("loc_557")

    label("loc_557")

    CloseMessageWindow()

    AnonymousTalk(    #6
        (
            "\x07\x00『那、那也不必在这种地方……\x01",
            "  被魔兽袭击了可怎么办啊。』\x02\x01",

            "丂\x01",
            "艾丝蒂尔说着便想带她走――\x02\x01",

            "然而，诺琪却充耳不闻――\x02\x01",

            "丂\x01",
            "两人渐渐起了争执――\x02\x01",

            "这时，艾丝蒂尔怀中的『银色钓钩』掉落了出来。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(1000)
    OP_22(0x1CD, 0x1, 0x64)
    FadeToBright(1000, 0)
    OP_C4(0x1, 0x800)
    Sleep(500)
    OP_77(0xFF, 0xFF, 0xFF, 0x0, 0x9C4)
    OP_75(0xFF, 0x0, 0x1)
    OP_75(0xFF, 0x1, 0x1)
    Sleep(4000)
    OP_62(0x10, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #7
        0x10,
        (
            "啊，这是三种钓具之一\x01",
            "『银色钓钩』对吧！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x10,
        "你是从哪里得到的……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x101,
        (
            "#1015F三、三种钓具是……\x01",
            "是说这钓钩吗？\x02\x03",

            "这是和罗伊德先生\x01",
            "比赛钓鱼赢来的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x10,
        "！！！\x02",
    )

    Jump("loc_748")

    label("loc_748")

    CloseMessageWindow()

    ChrTalk(    #11
        0x10,
        "你是说爆钓比赛吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x10,
        (
            "我本来打算向\x01",
            "罗伊德先生挑战的，\x01",
            "没想到在这之前他居然败给别人……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x101,
        "#1011F咦……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x10,
        (
            "……好，我向你\x01",
            "挑战爆钓十回合决胜赛！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x101,
        "#1019F十、十回合决胜赛～！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x10,
        (
            "多说无用！\x01",
            "马上来堂堂正正的比试一场吧！！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x101,
        "#1004F等、等一下……\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_23(0x1CD)
    Sleep(300)
    FadeToDark(2000, 16777215, -1)
    OP_0D()
    OP_C4(0x0, 0x10)
    FadeToBright(3000, 16777215)
    OP_0D()
    FadeToDark(0, 0, -1)
    OP_0D()
    OP_C4(0x1, 0x10)
    PlayEffect(0xA4, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0xA6, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_20(0xBB8)
    OP_21()
    Return()

    # Function_4_332 end

    def Function_5_925(): pass

    label("Function_5_925")

    OP_1D(0xC0)
    OP_AD(0x240138, 0x0, 0x0, 0x1F4)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_93E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D47")
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        -1,
        330,
        0,
        (
            "【　开始　】\x01",      # 0
            "【　说明　】\x01",      # 1
            "【　结束　】\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0xFF)
    SetMessageWindowPos(72, 320, 56, 3)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_9B1"),
        (1, "loc_9DB"),
        (2, "loc_D05"),
        (SWITCH_DEFAULT, "loc_D44"),
    )


    label("loc_9B1")

    OP_AE(0x1F4)
    Sleep(1000)
    Call(0, 6)
    OP_1D(0xC0)
    OP_AD(0x240138, 0x0, 0x0, 0x1F4)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_D44")

    label("loc_9DB")

    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #18
        (
            "\x07\x05#0W―――――――――《   规则说明   》―――――――――\x01",
            "　\x01",
            "  艾丝蒂尔和诺琪将进行一对一的钓鱼对决。\x01",
            "  游戏是１０次对战的回合制，由玩家和\x01",
            "  对战对手交替行动来进行。\x01",
            "　\x01",
            "  轮到自己的回合时，首先选择要使用的钓竿和鱼饵。\x01",
            "　（※能够使用的鱼饵因钓竿而异。）\x01",
            "　\x01",
            "  选择鱼饵后，即开始钓鱼游戏。\x01",
            "　鱼上钩时，将显示[ ！]标志，\x01",
            "  请迅速按下决定按钮，把鱼钓上来。\x01",
            "　\x01",
            "―――――――――――――――――――――――――――#20W\x02",
        )
    )

    Jump("loc_B96")

    label("loc_B96")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #19
        (
            "\x07\x05#0W―――――――――《   规则说明   》―――――――――\x01",
            "　\x01",
            "  能钓到的鱼根据鱼饵的种类而变化，\x01",
            "  而且钓到的鱼也可能用作鱼饵。\x01",
            "　\x01",
            "  钓到的鱼各自有设定分数，\x01",
            "  最后获得分数多的一方获胜。\x01",
            "　\x01",
            "  此外，大鱼可能会逃走，\x01",
            "  请不要放弃多试几次。\x01",
            "　\x01",
            "　\x01",
            "　\x01",
            "―――――――――――――――――――――――――――#20W\x02",
        )
    )

    Jump("loc_CF6")

    label("loc_CF6")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    Jump("loc_D44")

    label("loc_D05")

    OP_AE(0x1F4)
    OP_5F(0x0)
    OP_56(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(1000)
    OP_D6(0x1)
    OP_E3(0x1, 0x0)
    OP_A2(0x2505)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4E1, 7)), scpexpr(EXPR_END)), "loc_D38")
    NewScene("ED6_DT21/U4169   ._SN", 105, 0, 0)
    IdleLoop()
    Jump("loc_D41")

    label("loc_D38")

    NewScene("ED6_DT21/U4121   ._SN", 110, 0, 0)
    IdleLoop()

    label("loc_D41")

    Jump("loc_D44")

    label("loc_D44")

    Jump("loc_93E")

    label("loc_D47")

    Return()

    # Function_5_925 end

    def Function_6_D48(): pass

    label("Function_6_D48")

    SetMessageWindowPos(72, 320, 56, 3)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_6D(-65390, 0, 88950, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    ClearChrFlags(0x101, 0x80)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x101, -65820, 0, 90500, 180)
    SetChrPos(0x10, -58350, 0, 90510, 180)
    OP_48()
    OP_3E(0x24F, 1)
    OP_3E(0x250, 1)
    OP_3E(0x24E, 1)
    OP_3E(0x253, 1)
    OP_3E(0x3D4, 3)
    OP_3E(0x3D5, 3)
    OP_3E(0x3D6, 3)
    OP_3E(0x3D7, 3)
    OP_22(0x1CD, 0x1, 0x64)
    FadeToBright(1000, 0)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_C0(0x1B, 0x1, 0xFFFFF470, 0xFFFFF830, 0x7EF4, 0xB4, 0xFFFFF45C, 0xFFFFF448, 0x72C4)"), scpexpr(EXPR_END)), "loc_E2F")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_E39")

    label("loc_E2F")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_E39")

    EventBegin(0x0)
    ClearChrFlags(0x101, 0x80)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x101, -60570, 0, 90980, 90)
    SetChrPos(0x10, -59240, 0, 90940, 270)
    OP_6D(-59750, 200, 90940, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    Sleep(3000)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (1, "loc_EBA"),
        (0, "loc_103B"),
        (SWITCH_DEFAULT, "loc_103E"),
    )


    label("loc_EBA")

    FadeToBright(1000, 0)
    OP_1E()
    Sleep(1000)

    ChrTalk(    #20
        0x101,
        "#1003F输、输掉了……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x10,
        (
            "哦呵呵呵呵！\x01",
            "这个银色钓钩是我的了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x10,
        (
            "我超越团长的日子\x01",
            "看来也不远了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x101,
        "#1009F呜～真是不甘心啊。\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_20(0x7D0)
    OP_0D()
    OP_23(0x1CD)
    Sleep(1000)
    SetMessageWindowPos(-1, 80, -1, -1)
    SetChrName("")

    AnonymousTalk(    #24
        "\x18\x07\x05再度挑战小游戏吗？\x02",
    )

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        -1,
        200,
        0,
        (
            "【 再挑战 】\x01",      # 0
            "【回到门前】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(1000)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (1, "loc_1002"),
        (0, "loc_102C"),
        (SWITCH_DEFAULT, "loc_103B"),
    )


    label("loc_1002")

    OP_D6(0x1)
    OP_E3(0x1, 0x0)
    OP_A2(0x2505)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4E1, 7)), scpexpr(EXPR_END)), "loc_101D")
    NewScene("ED6_DT21/U4169   ._SN", 105, 0, 0)
    IdleLoop()
    Jump("loc_1026")

    label("loc_101D")

    NewScene("ED6_DT21/U4121   ._SN", 110, 0, 0)
    IdleLoop()

    label("loc_1026")

    Jump("loc_103B")

    label("loc_102C")

    OP_D6(0x1)
    OP_D6(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    label("loc_103B")

    Jump("loc_103E")

    label("loc_103E")

    FadeToBright(1000, 0)
    OP_1E()
    Sleep(1000)

    ChrTalk(    #25
        0x10,
        (
            "怎、怎么会这样。\x01",
            "我居然会输……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x101,
        (
            "#1000F呼，这下你满意了？\x02\x03",

            "好了，总之快回城里去吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x10,
        (
            "比起胜负，\x01",
            "你更关心我的安危……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x10,
        "呵呵，真是败给你了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x10,
        (
            "来，\x01",
            "请收下这个吧。\x02",
        )
    )

    Jump("loc_112D")

    label("loc_112D")

    CloseMessageWindow()
    OP_8E(0x10, 0xFFFF15FA, 0x0, 0x1630A, 0x7D0, 0x0)
    Sleep(500)
    FadeToDark(300, 0, 100)
    OP_0D()
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #30
        "\x07\x05从诺琪处得到了金色钓竿。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_8F(0x10, 0xFFFF1898, 0x0, 0x1633C, 0x7D0, 0x0)
    Sleep(500)

    ChrTalk(    #31
        0x101,
        (
            "#1004F哇，闪闪发亮！\x02\x03",

            "#1008F……这个给我没问题吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x10,
        (
            "当然了。\x01",
            "这也是比赛的规定嘛。\x02",
        )
    )

    Jump("loc_1229")

    label("loc_1229")

    CloseMessageWindow()

    ChrTalk(    #33
        0x10,
        (
            "……不过，\x01",
            "你可不能大意哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x10,
        (
            "还有我们的首领\x01",
            "『团长』在呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x101,
        "#1011F团、团长……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x10,
        (
            "对，身为钓公师团的创始者，\x01",
            "拥有最强的本领的\x01",
            "费瑟尔团长。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0x10,
        (
            "即使你不在意输赢，\x01",
            "这两种钓具也会唤来团长……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x10,
        (
            "就算你不答应，\x01",
            "和团长决一胜负的时刻也必然会来临。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0x101,
        (
            "#1015F嗯、嗯～……\x01",
            "是这样吗？\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_23(0x1CD)
    OP_20(0xBB8)
    Sleep(3000)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #40
        (
            "\x07\x05――名叫费瑟尔的人\x01",
            "究竟有怎样的本事呢。\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #41
        (
            "\x07\x05艾丝蒂尔一方面虽然觉得麻烦，\x01",
            "另一方面又无法否定\x01",
            "想要挑战试试的心情。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_D6(0x1)
    OP_E3(0x1, 0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x1D, 0x0, 0x20)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_14A5")
    Sleep(3000)
    OP_28(0x1D, 0x4, 0x10)
    OP_28(0x1D, 0x4, 0x20)
    OP_28(0x1E, 0x4, 0x2)
    OP_3E(0x1AB, 1)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #42
        "\x07\x00得到了\x1F\xAB\x01\x07\x00。\x02",
    )

    Jump("loc_146E")

    label("loc_146E")

    CloseMessageWindow()
    AddMira(5000)
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #43
        "\x07\x00得到了\x07\x02５０００米拉\x07\x00。\x02",
    )

    Jump("loc_1499")

    label("loc_1499")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)

    label("loc_14A5")

    Sleep(2000)
    SetMessageWindowPos(-1, 100, -1, -1)
    SetChrName("")

    AnonymousTalk(    #44
        "\x18\x07\x05继续进入第三章吗？\x02",
    )

    Sleep(1000)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        -1,
        200,
        0,
        (
            "【进入第三章】\x01",      # 0
            "【 回到门前 】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(1000)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (1, "loc_1534"),
        (0, "loc_1556"),
        (SWITCH_DEFAULT, "loc_1565"),
    )


    label("loc_1534")

    OP_A2(0x2505)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4E1, 7)), scpexpr(EXPR_END)), "loc_154A")
    NewScene("ED6_DT21/U4169   ._SN", 105, 0, 0)
    IdleLoop()
    Jump("loc_1553")

    label("loc_154A")

    NewScene("ED6_DT21/U4121   ._SN", 110, 0, 0)
    IdleLoop()

    label("loc_1553")

    Jump("loc_1565")

    label("loc_1556")

    OP_A2(0x2504)
    NewScene("ED6_DT21/R2201   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_1565")

    label("loc_1565")

    Return()

    # Function_6_D48 end

    def Function_7_1566(): pass

    label("Function_7_1566")

    EventBegin(0x1)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #45
        "\x07\x05门紧紧地关着。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_90(0x0, 0x0, 0x0, 0x5DC, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Return()

    # Function_7_1566 end

    def Function_8_15C3(): pass

    label("Function_8_15C3")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #46
        "\x07\x05机关门被封得很紧。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    # Function_8_15C3 end

    SaveToFile()

Try(main)

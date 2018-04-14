from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 卢安

    CreateScenaFile(
        FileName            = 'T2513   ._SN',
        MapName             = 'Ruan',
        Location            = 'T2513.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60014",
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


    AddCharChip(
        'ED6_DT27/CH03003 ._CH',             # 00
        'ED6_DT07/CH00043 ._CH',             # 01
    )

    AddCharChipPat(
        'ED6_DT27/CH03003P._CP',             # 00
        'ED6_DT07/CH00043P._CP',             # 01
    )

    ScpFunction(
        "Function_0_BA",           # 00, 0
        "Function_1_FC",           # 01, 1
        "Function_2_155",          # 02, 2
        "Function_3_155D",         # 03, 3
        "Function_4_1579",         # 04, 4
        "Function_5_1595",         # 05, 5
        "Function_6_15B1",         # 06, 6
        "Function_7_15CD",         # 07, 7
        "Function_8_15E9",         # 08, 8
    )


    def Function_0_BA(): pass

    label("Function_0_BA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_D0")
    OP_A3(0x10F0)
    SetMapFlags(0x10000000)
    Event(0, 8)
    Jump("loc_FB")

    label("loc_D0")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (108, "loc_E8"),
        (109, "loc_E8"),
        (112, "loc_E8"),
        (113, "loc_E8"),
        (SWITCH_DEFAULT, "loc_FB"),
    )


    label("loc_E8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x244, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_F8")
    Event(0, 2)

    label("loc_F8")

    Jump("loc_FB")

    label("loc_FB")

    Return()

    # Function_0_BA end

    def Function_1_FC(): pass

    label("Function_1_FC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x244, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_114")
    OP_B1("t2513_y")
    Jump("loc_11D")

    label("loc_114")

    OP_B1("t2513_n")

    label("loc_11D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_END)), "loc_127")
    Jump("loc_154")

    label("loc_127")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x403, 7)), scpexpr(EXPR_END)), "loc_13F")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x59), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapFlags(0x2000000)
    Jump("loc_154")

    label("loc_13F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x402, 3)), scpexpr(EXPR_END)), "loc_154")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x6E), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapFlags(0x2000000)

    label("loc_154")

    Return()

    # Function_1_FC end

    def Function_2_155(): pass

    label("Function_2_155")

    EventBegin(0x0)
    ClearMapFlags(0x1)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (108, "loc_174"),
        (109, "loc_199"),
        (112, "loc_1BE"),
        (113, "loc_1E3"),
        (SWITCH_DEFAULT, "loc_208"),
    )


    label("loc_174")

    SetChrPos(0x101, 56060, 1000, 17010, 126)
    SetChrPos(0x105, 55790, 1000, 15650, 126)
    Jump("loc_208")

    label("loc_199")

    SetChrPos(0x101, 63650, 1000, 17010, 206)
    SetChrPos(0x105, 63920, 1000, 15650, 206)
    Jump("loc_208")

    label("loc_1BE")

    SetChrPos(0x101, 56840, 1000, 12230, 52)
    SetChrPos(0x105, 55920, 1000, 12290, 52)
    Jump("loc_208")

    label("loc_1E3")

    SetChrPos(0x101, 63220, 1000, 12000, 325)
    SetChrPos(0x105, 64230, 1000, 11610, 325)
    Jump("loc_208")

    label("loc_208")

    Sleep(500)

    ChrTalk(    #0
        0x101,
        "#1026F#5P啊……\x02",
    )

    CloseMessageWindow()
    Sleep(100)

    def lambda_22D():
        OP_6D(58730, 2850, 2760, 4000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_22D)

    def lambda_245():
        OP_6C(18000, 4000)
        ExitThread()

    QueueWorkItem(0x105, 3, lambda_245)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (108, "loc_267"),
        (109, "loc_27D"),
        (112, "loc_293"),
        (113, "loc_2A9"),
        (SWITCH_DEFAULT, "loc_2BF"),
    )


    label("loc_267")

    OP_43(0x101, 0x1, 0x0, 0x3)
    Sleep(800)
    OP_43(0x105, 0x1, 0x0, 0x4)
    Jump("loc_2BF")

    label("loc_27D")

    OP_43(0x101, 0x1, 0x0, 0x3)
    Sleep(800)
    OP_43(0x105, 0x1, 0x0, 0x5)
    Jump("loc_2BF")

    label("loc_293")

    OP_43(0x101, 0x1, 0x0, 0x3)
    Sleep(800)
    OP_43(0x105, 0x1, 0x0, 0x6)
    Jump("loc_2BF")

    label("loc_2A9")

    OP_43(0x101, 0x1, 0x0, 0x3)
    Sleep(800)
    OP_43(0x105, 0x1, 0x0, 0x7)
    Jump("loc_2BF")

    label("loc_2BF")

    WaitChrThread(0x105, 0x1)
    WaitChrThread(0x105, 0x3)

    ChrTalk(    #1
        0x101,
        "#1025F#5P……………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x105,
        (
            "#542F#7P……好奇妙的感觉啊。\x02\x03",

            "虽然只是几个月前的事，\x01",
            "但却觉得非常怀念呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x101,
        "#1025F#5P嗯……\x02",
    )

    CloseMessageWindow()
    OP_AD(0x2400C0, 0x0, 0x0, 0x1F4)
    Sleep(1000)
    Sleep(2000)
    OP_AE(0x1F4)
    Sleep(1000)

    def lambda_37B():

        label("loc_37B")

        TurnDirection(0xFE, 0x101, 0)
        OP_48()
        Jump("loc_37B")

    QueueWorkItem2(0x105, 1, lambda_37B)

    def lambda_38C():
        OP_8E(0xFE, 0xEAEC, 0x3E8, 0x2CEC, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_38C)

    def lambda_3A7():
        OP_6D(60140, 700, 12000, 3500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3A7)

    def lambda_3BF():
        OP_6C(0, 3500)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_3BF)
    WaitChrThread(0x101, 0x1)
    OP_44(0x105, 0x1)
    WaitChrThread(0x101, 0x2)
    SetChrFlags(0x101, 0x4)
    OP_96(0x101, 0xEAEC, 0x2BC, 0x2ADA, 0xC8, 0xFA0)
    SetChrChipByIndex(0x101, 0)
    Sleep(500)

    ChrTalk(    #4
        0x101,
        (
            "#1025F#5P自那之后，\x01",
            "真的是发生了太多的事情……\x02\x03",

            "只是温柔美丽的约修亚\x01",
            "公主已经不在了……\x02\x03",

            "现在，只有我们两个人\x01",
            "坐在这个舞台上……\x02\x03",

            "#1016F感觉真是不可思议啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x105,
        (
            "#047F是啊……\x02\x03",

            "#040F嗯…艾丝蒂尔。\x01",
            "能让我坦白一件事吗？\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x101, 0x10)
    TurnDirection(0x101, 0x105, 0)
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x4), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_4FE")
    SetChrSubChip(0x101, 2)
    Jump("loc_519")

    label("loc_4FE")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_514")
    SetChrSubChip(0x101, 2)
    Jump("loc_519")

    label("loc_514")

    SetChrSubChip(0x101, 1)

    label("loc_519")

    OP_8C(0x101, 180, 0)
    SetChrFlags(0x101, 0x10)

    ChrTalk(    #6
        0x101,
        "#1004F#5P咦……？\x02",
    )

    CloseMessageWindow()
    OP_20(0x7D0)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (108, "loc_559"),
        (109, "loc_596"),
        (112, "loc_5D3"),
        (113, "loc_610"),
        (SWITCH_DEFAULT, "loc_64D"),
    )


    label("loc_559")

    OP_8E(0x105, 0xE786, 0x0, 0x2CEC, 0x7D0, 0x0)
    SetChrFlags(0x105, 0x4)
    OP_96(0x105, 0xE786, 0x2BC, 0x2ADA, 0xC8, 0xFA0)
    SetChrChipByIndex(0x105, 1)
    Sleep(500)
    Jump("loc_64D")

    label("loc_596")

    OP_8E(0x105, 0xEE8E, 0x0, 0x2CEC, 0x7D0, 0x0)
    SetChrFlags(0x105, 0x4)
    OP_96(0x105, 0xEE8E, 0x2BC, 0x2ADA, 0xC8, 0xFA0)
    SetChrChipByIndex(0x105, 1)
    Sleep(500)
    Jump("loc_64D")

    label("loc_5D3")

    OP_8E(0x105, 0xE786, 0x0, 0x2CEC, 0x7D0, 0x0)
    SetChrFlags(0x105, 0x4)
    OP_96(0x105, 0xE786, 0x2BC, 0x2ADA, 0xC8, 0xFA0)
    SetChrChipByIndex(0x105, 1)
    Sleep(500)
    Jump("loc_64D")

    label("loc_610")

    OP_8E(0x105, 0xEE8E, 0x0, 0x2CEC, 0x7D0, 0x0)
    SetChrFlags(0x105, 0x4)
    OP_96(0x105, 0xEE8E, 0x2BC, 0x2ADA, 0x1F4, 0xFA0)
    SetChrChipByIndex(0x105, 1)
    Sleep(500)
    Jump("loc_64D")

    label("loc_64D")

    OP_21()
    OP_1D(0x76)
    Sleep(500)

    ChrTalk(    #7
        0x105,
        (
            "#540F我……\x01",
            "我很喜欢约修亚。\x02\x03",

            "在第一次见面时，就感觉到他的身上\x01",
            "有一种奇妙的魅力，\x01",
            "把我深深地吸引住了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x101,
        (
            "#1004F#5P………………………………\x02\x03",

            "#1025F……是吗。\x02\x03",

            "#1016F啊哈哈…果然是这样吗。\x01",
            "虽然我以前就有这种感觉……\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x105, 0x10)
    TurnDirection(0x105, 0x101, 0)
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x105, 0x4), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_755")
    SetChrSubChip(0x105, 2)
    Jump("loc_770")

    label("loc_755")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x105, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_76B")
    SetChrSubChip(0x105, 2)
    Jump("loc_770")

    label("loc_76B")

    SetChrSubChip(0x105, 1)

    label("loc_770")

    OP_8C(0x105, 180, 0)
    SetChrFlags(0x105, 0x10)

    ChrTalk(    #9
        0x105,
        (
            "#542F在舞台剧最后一幕的吻戏时，\x01",
            "我的心跳得好快。\x02\x03",

            "虽然觉得有些\x01",
            "对不起艾丝蒂尔，\x01",
            "但我根本没办法不投入到剧情中……\x02\x03",

            "#045F当时完全没有感觉是在演戏，\x01",
            "就好像自己的吻真的被他夺去一样。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x101,
        (
            "#1013F#5P是、是这样啊……\x02\x03",

            "科洛丝你…\x01",
            "还真是大胆啊……好意外。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x105,
        (
            "#542F呵呵，其实平时的我\x01",
            "就是这样的啦，尤莉亚小姐也\x01",
            "对我很头疼呢。\x02\x03",

            "#047F不过那个时候……\x01",
            "当戴尔蒙市长用枪口\x01",
            "对准你的时候……\x02\x03",

            "约修亚他……\x01",
            "约修亚他的眼神真的好可怕……\x02\x03",

            "在那时我才感受到，\x01",
            "你在他的心中是多么重要。\x02\x03",

            "#542F也终于明白…\x01",
            "你们之间根本就没有我介入的余地。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x101,
        (
            "#1015F#5P嗯、嗯嗯……\x02\x03",

            "也许我说这种话有些不太合适，不过… \x01",
            "你现在就放弃的话未免有点早吧。\x02\x03",

            "#1007F说实话，科洛丝要和我竞争的话…\x01",
            "胜负还很难预料呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x105,
        (
            "#048F真是的～艾丝蒂尔\x01",
            "你实在太不了解自己了。\x02\x03",

            "竟然完全都不清楚\x01",
            "自己有多大的魅力。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x101,
        (
            "#1019F#5P呜……\x01",
            "换句话说就是我太笨了吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x105,
        (
            "#045F呵呵，才没有那种事呢。\x02\x03",

            "#542F我最喜欢艾丝蒂尔你\x01",
            "这种可爱和率直……\x02\x03",

            "我想约修亚也一定\x01",
            "和我一样吧。\x02\x03",

            "所以从某种意义上说，\x01",
            "我和约修亚可以算是知音了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x101,
        (
            "#1004F#5P啊……说起来的话\x01",
            "我也有这种感觉呢。\x02\x03",

            "#1015F你们都是那种头脑聪明、\x01",
            "举止端正、外表清秀的类型……\x02\x03",

            "所以当时我还说你们很般配，\x01",
            "挑唆约修亚和你……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x105,
        (
            "#049F我在认识特蕾莎院长之前\x01",
            "每天都过着孤独的生活。\x02\x03",

            "约修亚在遇到\x01",
            "艾丝蒂尔之前\x01",
            "大概也是如此吧。\x02\x03",

            "#047F但我和他之间有一点不同，\x01",
            "……那就是他比我坚强。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x101,
        "#1004F#5P坚强？\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x105, 0)
    Sleep(500)

    ChrTalk(    #19
        0x105,
        (
            "#043F祖母大人指名让我担当\x01",
            "下一任的女王。\x02\x03",

            "以现在的状况来考虑，\x01",
            "也许这种决定很正确……\x02\x03",

            "#047F但我一旦当上了女王……\x01",
            "就再也无法做回『科洛丝』的身份了。\x02\x03",

            "只能以肩负重大权利和责任的\x01",
            "科洛蒂娅·冯·奥赛雷丝的\x01",
            "身份过完一生。\x02\x03",

            "那样的话，就再也不能和朋友轻松交谈，\x01",
            "不能和院长撒娇，也不能和那些可爱的\x01",
            "孩子们拥抱玩耍……\x02\x03",

            "#049F每当想起这些的时候我就好害怕……\x02\x03",

            "害怕自己再次回到那种孤独的生活，\x01",
            "但同时我也对自己的懦弱感到羞愧……\x02\x03",

            "至今也还没能给祖母\x01",
            "一个明确的答复……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x101,
        "#1026F#5P科洛丝……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x105,
        (
            "#542F从这一点上看，约修亚\x01",
            "实在比我坚强太多了。\x02\x03",

            "虽然他深深地爱着你，十分不愿意\x01",
            "从你身边离开……\x02\x03",

            "但为了避免你被牵连\x01",
            "到自己的事情中，他还是\x01",
            "毅然选择了离开……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x101,
        (
            "#1003F#5P……嗯，约修亚确实很坚强。\x02\x03",

            "#1010F但是……\x01",
            "我认为他的坚强用错了地方。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x105, 0x1), scpexpr(EXPR_PUSH_LONG, 0xEAEC), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_F8B")
    SetChrSubChip(0x105, 1)
    Jump("loc_F90")

    label("loc_F8B")

    SetChrSubChip(0x105, 2)

    label("loc_F90")

    Sleep(500)

    ChrTalk(    #23
        0x105,
        "#044F咦……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x101,
        (
            "#1025F#5P科洛丝毕竟是要担任治理整个国家的\x01",
            "女王，有这种烦恼也是理所当然的。\x02\x03",

            "感到不安是再正常不过的，\x01",
            "如果没有这种感觉那才奇怪呢。\x02\x03",

            "即便是如此这般的烦恼，都无法\x01",
            "阻止你去追寻正确的答案，这样的科洛丝\x01",
            "一定能成为一个称职的好女王。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x105,
        "#542F艾丝蒂尔……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x101,
        (
            "#1002F#5P但是约修亚……\x02\x03",

            "约修亚他…根本就没有烦恼过！\x02\x03",

            "他根本就没有留恋和犹豫，\x01",
            "那么坚决地就从我们身边离去……\x02\x03",

            "#1003F这一点……\x01",
            "才是我最不能原谅他的地方！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x105,
        (
            "#043F艾丝蒂尔……\x02\x03",

            "#047F……嗯，说的对。\x01",
            "确实不能原谅他。\x02\x03",

            "#042F他完全都没有考虑过\x01",
            "女孩子的心情啊！\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    OP_62(0x105, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_63(0x101)
    OP_63(0x105)

    ChrTalk(    #28
        0x101,
        "#1016F#5P#1K扑哧……\x02",
    )


    ChrTalk(    #29
        0x105,
        "#045F#1K哈哈哈……\x02",
    )

    Sleep(1000)
    OP_56(0x1)
    OP_59()
    Sleep(500)

    ChrTalk(    #30
        0x101,
        (
            "#1017F#5P能和科洛丝成为朋友\x01",
            "真是太好了。\x02\x03",

            "能让我这么痛快地倾诉\x01",
            "心里话的对象实在太少了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x105,
        (
            "#041F呵呵，我也是啊。\x02\x03",

            "#542F刚才说了好多\x01",
            "难为情的话，不过……\x02\x03",

            "嗯…请不要误解啊？\x02\x03",

            "我现在对约修亚已经\x01",
            "不再有那种想法了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x101,
        (
            "#1016F#5P啊啊～没关系的没关系的。\x02\x03",

            "#1017F喜欢就是喜欢，\x01",
            "没必要刻意去抑制。\x01",
            "我已经完全明白了。\x02\x03",

            "有什么感觉就要坦率地表达出来，\x01",
            "这才是青春呢，对吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x105,
        (
            "#045F艾丝蒂尔～你真是的……\x02\x03",

            "#540F嗯…如果说我对他一点感觉都没有了，\x01",
            "那肯定是假话，不过……\x02\x03",

            "我现在更大的愿望是帮助\x01",
            "你们两个重新……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x101,
        (
            "#1012F#5P嗯嗯！我明白的。\x02\x03",

            "#1006F……好了。\x01",
            "这次聊得真是太尽兴了。\x02\x03",

            "咱们还是继续去调查学生们吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x105,
        (
            "#045F啊～说的对。\x02\x03",

            "在太阳落山之前\x01",
            "我们还是抓紧时间调查吧。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_20(0x7D0)
    OP_0D()
    OP_6D(60140, 1000, 12380, 0)
    OP_67(0, 2930, -10000, 0)
    OP_6B(1420, 0)
    OP_6C(0, 0)
    OP_6E(673, 0)
    SetChrSubChip(0x101, 0)
    SetChrSubChip(0x105, 0)
    SetChrChipByIndex(0x101, 65535)
    SetChrChipByIndex(0x105, 65535)
    SetChrPos(0x101, 60140, 1000, 12380, 180)
    SetChrPos(0x105, 60140, 1000, 12380, 180)
    Sleep(500)
    OP_21()
    OP_1D(0xE)
    FadeToBright(1000, 0)
    OP_A2(0x1220)
    EventEnd(0x0)
    Return()

    # Function_2_155 end

    def Function_3_155D(): pass

    label("Function_3_155D")

    OP_8E(0xFE, 0xEAEC, 0x0, 0x391C, 0x7D0, 0x0)
    OP_8C(0xFE, 180, 400)
    Return()

    # Function_3_155D end

    def Function_4_1579(): pass

    label("Function_4_1579")

    OP_8E(0xFE, 0xE786, 0x0, 0x3C8C, 0x7D0, 0x0)
    OP_8C(0xFE, 180, 400)
    Return()

    # Function_4_1579 end

    def Function_5_1595(): pass

    label("Function_5_1595")

    OP_8E(0xFE, 0xEE8E, 0x0, 0x3C8C, 0x7D0, 0x0)
    OP_8C(0xFE, 180, 400)
    Return()

    # Function_5_1595 end

    def Function_6_15B1(): pass

    label("Function_6_15B1")

    OP_8E(0xFE, 0xE786, 0x0, 0x3624, 0x7D0, 0x0)
    OP_8C(0xFE, 180, 400)
    Return()

    # Function_6_15B1 end

    def Function_7_15CD(): pass

    label("Function_7_15CD")

    OP_8E(0xFE, 0xEE8E, 0x0, 0x3624, 0x7D0, 0x0)
    OP_8C(0xFE, 180, 400)
    Return()

    # Function_7_15CD end

    def Function_8_15E9(): pass

    label("Function_8_15E9")

    EventBegin(0x0)
    SetChrFlags(0x102, 0x80)
    OP_6D(1070, -250, -3000, 0)
    OP_67(0, 5920, -10000, 0)
    OP_6B(3300, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)

    def lambda_1633():
        OP_6D(1580, -250, 13840, 5000)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1633)
    FadeToBright(1000, 0)
    WaitChrThread(0x102, 0x1)
    Sleep(1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x10FE)
    OP_A2(0x10FB)
    NewScene("ED6_DT21/T2500   ._SN", 125, 0, 0)
    IdleLoop()
    Return()

    # Function_8_15E9 end

    SaveToFile()

Try(main)

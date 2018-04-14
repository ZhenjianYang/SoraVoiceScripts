from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 卢安

    CreateScenaFile(
        FileName            = 'T2611   ._SN',
        MapName             = 'Ruan',
        Location            = 'T2611.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60032",
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
        '烛台',                                 # 9
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
        'ED6_DT06/CH20021 ._CH',             # 00
        'ED6_DT07/CH00024 ._CH',             # 01
        'ED6_DT07/CH00054 ._CH',             # 02
        'ED6_DT26/CH20311 ._CH',             # 03
    )

    AddCharChipPat(
        'ED6_DT06/CH20021P._CP',             # 00
        'ED6_DT07/CH00024P._CP',             # 01
        'ED6_DT07/CH00054P._CP',             # 02
        'ED6_DT26/CH20311P._CP',             # 03
    )

    DeclNpc(
        X                   = 8920,
        Z                   = 6000,
        Y                   = 27470,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1245184,
        ChipIndex           = 0x0,
        NpcIndex            = 0x1E2,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclActor(
        TriggerX            = 9080,
        TriggerZ            = 4000,
        TriggerY            = 28080,
        TriggerRange        = 1300,
        ActorX              = 8920,
        ActorZ              = 6000,
        ActorY              = 27470,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -39000,
        TriggerZ            = 0,
        TriggerY            = 30250,
        TriggerRange        = 1300,
        ActorX              = -39000,
        ActorZ              = 1000,
        ActorY              = 30250,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 44990,
        TriggerZ            = 0,
        TriggerY            = 3460,
        TriggerRange        = 800,
        ActorX              = 44990,
        ActorZ              = 1000,
        ActorY              = 3460,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 5,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 43000,
        TriggerZ            = 0,
        TriggerY            = 25500,
        TriggerRange        = 1500,
        ActorX              = 42980,
        ActorZ              = 1000,
        ActorY              = 25500,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 6,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -80200,
        TriggerZ            = 250,
        TriggerY            = 31450,
        TriggerRange        = 1000,
        ActorX              = -80240,
        ActorZ              = 250,
        ActorY              = 32100,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 2,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_19E",          # 00, 0
        "Function_1_19F",          # 01, 1
        "Function_2_20A",          # 02, 2
        "Function_3_321",          # 03, 3
        "Function_4_710",          # 04, 4
        "Function_5_B5B",          # 05, 5
        "Function_6_D5E",          # 06, 6
        "Function_7_14DF",         # 07, 7
    )


    def Function_0_19E(): pass

    label("Function_0_19E")

    Return()

    # Function_0_19E end

    def Function_1_19F(): pass

    label("Function_1_19F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x245, 1)), scpexpr(EXPR_END)), "loc_1AF")
    OP_10(0x5, 0x0)
    OP_10(0x17, 0x1)
    Jump("loc_1B5")

    label("loc_1AF")

    OP_10(0x5, 0x1)
    OP_10(0x17, 0x0)

    label("loc_1B5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x268, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C7")
    OP_6F(0xB, 0)
    Jump("loc_1CE")

    label("loc_1C7")

    OP_6F(0xB, 60)

    label("loc_1CE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x244, 5)), scpexpr(EXPR_END)), "loc_1D9")
    OP_64(0x0, 0x1)

    label("loc_1D9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x244, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x244, 6)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1E9")
    OP_64(0x1, 0x1)

    label("loc_1E9")

    OP_72(0x1, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x245, 0)), scpexpr(EXPR_END)), "loc_1FE")
    OP_64(0x2, 0x1)
    OP_71(0x1, 0x10)

    label("loc_1FE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x245, 1)), scpexpr(EXPR_END)), "loc_209")
    OP_64(0x3, 0x1)

    label("loc_209")

    Return()

    # Function_1_19F end

    def Function_2_20A(): pass

    label("Function_2_20A")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x268, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2E2")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0xB, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1F5, 1)"), scpexpr(EXPR_END)), "loc_279")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #0
        "\x07\x00得到了\x1F\xF5\x01\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1341)
    Jump("loc_2DF")

    label("loc_279")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #1
        (
            "宝箱里装有\x1F\xF5\x01\x07\x00。   \x01",
            "所持物品已经满了，\x1F\xF5\x01\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0xB, 60)
    OP_70(0xB, 0x0)

    label("loc_2DF")

    Jump("loc_313")

    label("loc_2E2")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #2
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_313")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_2_20A end

    def Function_3_321(): pass

    label("Function_3_321")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_33B")
    Call(0, 7)
    FadeToBright(0, 0)

    label("loc_33B")

    EventBegin(0x0)
    Fade(1000)
    SetChrPos(0x101, 9240, 4000, 27500, 8)
    SetChrPos(0x105, 10120, 4000, 27470, 313)
    SetChrPos(0xF7, 7810, 4000, 27040, 39)
    SetChrPos(0x104, 9270, 4000, 26150, 7)
    SetChrPos(0x127, 8070, 4000, 26100, 36)
    OP_6D(9230, 4000, 27500, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_0D()

    ChrTalk(    #3
        0x105,
        (
            "#042F#4P『虚无之炎』……\x01",
            "是说这个烛台吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x101,
        (
            "#1006F#6P确实只有这一根蜡烛\x01",
            "没有点燃。\x02\x03",

            "好，调查看看吧。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #5
        "\x07\x05烛台中有卡片。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    Sleep(300)
    Fade(250)
    SetChrChipByIndex(0x101, 3)
    SetChrSubChip(0x101, 0)
    OP_0D()
    Sleep(500)
    FadeToDark(300, 0, 100)
    OP_AD(0x240094, 0xBE, 0x64, 0x1F4)
    Sleep(1000)
    SetMessageWindowPos(-1, 300, -1, 3)
    SetChrName("")

    AnonymousTalk(    #6
        (
            "\x07\x05　第二个诅咒在教室\x01",
            "　寻找『向南的学生』\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_AE(0x1F4)
    Sleep(1000)
    LoadEffect(0x0, "map\\\\mpfire6.eff")
    PlayEffect(0x0, 0xFF, 0x101, 0, 600, 400, 0, 0, 0, 800, 800, 800, 0xFF, 0, 0, 0, 0)
    OP_22(0x86, 0x0, 0x64)
    SetChrChipByIndex(0x101, 65535)
    SetChrSubChip(0x101, 0)
    Sleep(1000)
    OP_62(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_8F(0x101, 0x240E, 0xFA0, 0x69FA, 0x7D0, 0x0)
    Sleep(500)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)

    AnonymousTalk(    #7
        "\x07\x05卡片突然着火烧没了。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    ChrTalk(    #8
        0x101,
        (
            "#1020F#6P哇哇……\x02\x03",

            "#1007F但、但是\x01",
            "答对了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x104,
        (
            "#030F嗯，这次是教室了吧。\x02\x03",

            "#035F明明没人才对，\x01",
            "却说『向南的学生』吗……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x101, 400)
    Sleep(400)

    ChrTalk(    #10
        0x105,
        (
            "#042F记得教室在\x01",
            "左翼的１层和２层各有两间，\x01",
            "应该有共计４间。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_6D1")

    ChrTalk(    #11
        0x106,
        (
            "#051F#6P好……一边看罗盘\x01",
            "一边调查看看吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6FC")

    label("loc_6D1")


    ChrTalk(    #12
        0x103,
        (
            "#020F#6P一边看罗盘\x01",
            "一边调查比较好吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6FC")

    OP_64(0x0, 0x1)
    OP_65(0x1, 0x1)
    OP_A2(0x1225)
    OP_28(0x84, 0x1, 0x4)
    EventEnd(0x0)
    Return()

    # Function_3_321 end

    def Function_4_710(): pass

    label("Function_4_710")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_72A")
    Call(0, 7)
    FadeToBright(0, 0)

    label("loc_72A")

    EventBegin(0x0)
    Fade(1000)
    SetChrPos(0x101, -37320, 0, 30250, 270)
    SetChrPos(0xF7, -37650, 0, 31430, 225)
    SetChrPos(0x105, -37880, 0, 29190, 315)
    SetChrPos(0x104, -39220, 0, 28840, 360)
    SetChrPos(0x127, -38860, 0, 31650, 180)
    OP_6D(-38470, 0, 30820, 0)
    OP_67(0, 6150, -10000, 0)
    OP_6B(2750, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #13
        0x127,
        (
            "#153F其他的座位都四处散乱着，\x01",
            "只有这里的桌椅是放得好好的呢～\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_84B")

    ChrTalk(    #14
        0x106,
        (
            "#050F朝向的方向也是正南……\x01",
            "大概，就是说这里吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_87F")

    label("loc_84B")


    ChrTalk(    #15
        0x103,
        (
            "#022F朝向的方向也是正南……\x01",
            "大概，就是这里吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_87F")


    ChrTalk(    #16
        0x101,
        "#1002F那么，调查看看吧。\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #17
        "\x07\x05调查抽屉里发现了卡片。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    Sleep(300)
    Fade(250)
    SetChrChipByIndex(0x101, 3)
    SetChrSubChip(0x101, 0)
    OP_0D()
    Sleep(500)
    FadeToDark(300, 0, 100)
    OP_AD(0x240095, 0xBE, 0x64, 0x1F4)
    Sleep(1000)
    SetMessageWindowPos(-1, 300, -1, 3)
    SetChrName("")

    AnonymousTalk(    #18
        (
            "\x07\x05　第三个诅咒在庭院\x01",
            "  寻找『落下的头』\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_AE(0x1F4)
    Sleep(1000)
    LoadEffect(0x0, "map\\\\mpfire6.eff")
    PlayEffect(0x0, 0xFF, 0x101, 0, 600, 400, 0, 0, 0, 800, 800, 800, 0xFF, 0, 0, 0, 0)
    OP_22(0x86, 0x0, 0x64)
    SetChrChipByIndex(0x101, 65535)
    SetChrSubChip(0x101, 0)
    Sleep(1000)
    OP_62(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)

    AnonymousTalk(    #19
        "\x07\x05卡片突然着火烧没了。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    ChrTalk(    #20
        0x101,
        (
            "#1004F哇哟……\x02\x03",

            "#1006F好像找对了，\x01",
            "不过接下来是哪里呢?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x104,
        (
            "#035F『庭园』和『落下的头』啊。\x02\x03",

            "#030F挺夸张的，\x01",
            "这也是什么比喻吧。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_64(0x1, 0x1)
    OP_A2(0x1226)
    OP_28(0x84, 0x1, 0x8)
    SetChrPos(0x101, -37320, 0, 30250, 270)
    SetChrPos(0xF7, -37320, 0, 30250, 270)
    SetChrPos(0x105, -37320, 0, 30250, 270)
    SetChrPos(0x104, -37320, 0, 30250, 270)
    SetChrPos(0x127, -37320, 0, 30250, 270)
    OP_6D(-37320, 0, 30250, 0)
    OP_67(0, 6150, -10000, 0)
    OP_6B(2750, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    Sleep(500)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    Return()

    # Function_4_710 end

    def Function_5_B5B(): pass

    label("Function_5_B5B")

    EventBegin(0x0)
    Fade(1000)
    OP_6D(44710, 0, 3440, 0)
    OP_67(0, 6150, -10000, 0)
    OP_6B(2750, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    SetChrPos(0x101, 44390, 0, 2910, 0)
    SetChrPos(0xF7, 43210, 0, 2890, 45)
    SetChrPos(0x105, 45590, 0, 2820, 315)
    SetChrPos(0x104, 45160, 0, 1650, 0)
    SetChrPos(0x127, 43950, 0, 1770, 0)
    OP_0D()
    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #22
        "\x07\x05门上着锁。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x244, 7)), scpexpr(EXPR_END)), "loc_CF0")
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "【使用后门的钥匙】\x01",      # 0
            "【使用旧钥匙】\x01",          # 1
            "【不使用】\x01",              # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_C9A"),
        (1, "loc_CBA"),
        (2, "loc_CE1"),
        (SWITCH_DEFAULT, "loc_CED"),
    )


    label("loc_C9A")


    AnonymousTalk(    #23
        "\x07\x05钥匙不相合。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    Jump("loc_CED")

    label("loc_CBA")

    FadeToBright(300, 0)
    Sleep(500)
    OP_22(0x73, 0x0, 0x64)
    Sleep(1000)
    OP_64(0x2, 0x1)
    OP_71(0x1, 0x10)
    OP_A2(0x1228)
    Jump("loc_CED")

    label("loc_CE1")

    FadeToBright(300, 0)
    Jump("loc_CED")

    label("loc_CED")

    Jump("loc_D5B")

    label("loc_CF0")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "【使用后门的钥匙】\x01",      # 0
            "【不使用】\x01",              # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_D3E"),
        (SWITCH_DEFAULT, "loc_D52"),
    )


    label("loc_D3E")


    AnonymousTalk(    #24
        "\x07\x05钥匙不相合。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_D52")

    FadeToBright(300, 0)

    label("loc_D5B")

    EventEnd(0x0)
    Return()

    # Function_5_B5B end

    def Function_6_D5E(): pass

    label("Function_6_D5E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D78")
    Call(0, 7)
    FadeToBright(0, 0)

    label("loc_D78")

    EventBegin(0x0)
    Fade(1000)
    SetChrPos(0x101, 43100, 0, 22930, 0)
    SetChrPos(0xF7, 41900, 0, 23180, 0)
    SetChrPos(0x105, 44610, 0, 23420, 315)
    SetChrPos(0x104, 43520, 0, 21510, 8)
    SetChrPos(0x127, 41550, 0, 21200, 17)
    OP_6D(43080, 0, 25000, 0)
    OP_67(0, 7280, -10000, 0)
    OP_6B(1180, 0)
    OP_6C(35000, 0)
    OP_6E(688, 0)
    OP_0D()
    Sleep(1000)

    ChrTalk(    #25
        0x101,
        "#1004F好像是……龙的雕像呢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x105,
        (
            "#040F#2P这个雕像记得以前\x01",
            "就放在这里了。\x02\x03",

            "好像是以前在利贝尔栖息的\x01",
            "古代龙的塑像……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_F70")

    ChrTalk(    #27
        0x106,
        (
            "#053F哼，真有品。\x02\x03",

            "#050F总之，调查看看\x01",
            "有没有什么机关吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_8E(0x106, 0xA85C, 0x0, 0x5DC0, 0x7D0, 0x0)
    OP_8C(0x106, 0, 400)
    Sleep(1000)
    OP_8C(0x106, 45, 400)
    Sleep(1000)
    OP_8C(0x106, 315, 400)
    Sleep(1000)
    OP_8C(0x106, 0, 400)
    Sleep(1000)
    Fade(500)
    SetChrFlags(0x106, 0x2)
    SetChrChipByIndex(0x106, 2)
    SetChrSubChip(0x106, 1)
    OP_0D()
    Sleep(1000)
    OP_62(0x106, 0xFFFFFED4, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #28
        0x106,
        "#051F#5P……是这个了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_103D")

    label("loc_F70")


    ChrTalk(    #29
        0x103,
        (
            "#026F唔，有感觉。\x02\x03",

            "#020F总之，调查看看\x01",
            "有没有什么机关吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_8E(0x103, 0xA85C, 0x0, 0x5DC0, 0x7D0, 0x0)
    OP_8C(0x103, 0, 400)
    Sleep(1000)
    OP_8C(0x103, 45, 400)
    Sleep(1000)
    OP_8C(0x103, 315, 400)
    Sleep(1000)
    OP_8C(0x103, 0, 400)
    Sleep(1000)
    Fade(500)
    SetChrFlags(0x103, 0x2)
    SetChrChipByIndex(0x103, 1)
    SetChrSubChip(0x103, 1)
    OP_0D()
    Sleep(1000)
    OP_62(0x103, 0xFFFFFED4, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #30
        0x103,
        "#027F#5P中啦㈱\x02",
    )

    CloseMessageWindow()

    label("loc_103D")

    OP_22(0x82, 0x0, 0x64)
    Sleep(1000)
    FadeToDark(300, 0, -1)
    OP_0D()
    OP_22(0x70, 0x0, 0x64)
    Sleep(4000)
    FadeToBright(300, 0)
    ClearChrFlags(0x106, 0x2)
    ClearChrFlags(0x103, 0x2)
    SetChrChipByIndex(0x103, 65535)
    SetChrChipByIndex(0x106, 65535)
    SetChrSubChip(0x103, 0)
    SetChrSubChip(0x106, 0)
    SetChrPos(0x101, 43100, 0, 47930, 0)
    SetChrPos(0xF7, 41900, 0, 48180, 0)
    SetChrPos(0x105, 44610, 0, 48420, 315)
    SetChrPos(0x104, 43380, 0, 46320, 0)
    SetChrPos(0x127, 41690, 0, 46310, 0)
    OP_6D(43080, 0, 48770, 0)
    OP_67(0, 7280, -10000, 0)
    OP_6B(1180, 0)
    OP_6C(35000, 0)
    OP_6E(688, 0)
    OP_0D()
    Sleep(1000)

    ChrTalk(    #31
        0x105,
        (
            "#044F竟、竟然有这种东西\x01",
            "在雕像底下……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x104,
        (
            "#030F呼……品味不错。\x02\x03",

            "总觉得\x01",
            "相当张扬啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x127,
        (
            "#151F是啊～\x01",
            "服务精神满满呢～\x02\x03",

            "要是在旅游名胜\x01",
            "说不定还能聚集客人～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x101,
        (
            "#1015F不过……\x01",
            "我刚刚就在想。\x02\x03",

            "卡片什么的\x01",
            "要说是幽灵作祟不是很奇怪？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_129B")
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "【◇烛台失窃任务没有完成】\x01",      # 0
            "【◇烛台失窃任务完成了】\x01",        # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1282"),
        (1, "loc_128A"),
        (SWITCH_DEFAULT, "loc_1292"),
    )


    label("loc_1282")

    OP_28(0x57, 0x3, 0x10)
    Jump("loc_1292")

    label("loc_128A")

    OP_28(0x57, 0x4, 0x10)
    Jump("loc_1292")

    label("loc_1292")

    FadeToBright(300, 0)

    label("loc_129B")

    TurnDirection(0x105, 0x101, 400)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x57, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_1358")

    ChrTalk(    #35
        0x105,
        (
            "#047F确实，没有实体的灵\x01",
            "不大可能做这种事。\x02\x03",

            "#049F而且刚才的谜题\x01",
            "总觉得有印象似的……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x105, 400)

    ChrTalk(    #36
        0x101,
        (
            "#1004F#6P啊，科洛丝也是？\x02\x03",

            "#1007F我也觉得这势头\x01",
            "好像在哪有印象……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_138F")

    label("loc_1358")

    TurnDirection(0x105, 0x101, 400)

    ChrTalk(    #37
        0x105,
        (
            "#043F确实，没有实体的灵\x01",
            "不大可能做这种事。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_138F")

    TurnDirection(0xF7, 0x101, 400)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_13E4")

    ChrTalk(    #38
        0x106,
        (
            "#057F无论如何\x01",
            "都不是能用常理来对付的对手。\x02\x03",

            "小心谨慎地下去吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1428")

    label("loc_13E4")


    ChrTalk(    #39
        0x103,
        (
            "#022F无论如何\x01",
            "都不是能用常理来对付的对手。\x02\x03",

            "小心谨慎地下去吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1428")

    OP_A2(0x1229)
    OP_28(0x84, 0x1, 0x20)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6D(44540, 0, 50140, 0)
    OP_67(0, 6150, -10000, 0)
    OP_6B(2750, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    SetChrPos(0x101, 44540, 0, 50140, 0)
    SetChrPos(0xF7, 44540, 0, 50140, 0)
    SetChrPos(0x105, 44540, 0, 50140, 0)
    SetChrPos(0x104, 44540, 0, 50140, 0)
    SetChrPos(0x127, 44540, 0, 50140, 0)
    Sleep(500)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    Return()

    # Function_6_D5E end

    def Function_7_14DF(): pass

    label("Function_7_14DF")

    FadeToDark(0, 0, -1)
    OP_A3(0x1200)
    OP_A3(0x1201)
    RemoveParty(0x2, 0xFF)
    RemoveParty(0x5, 0xFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "【◇选择雪拉扎德为队友】\x01",      # 0
            "【◇选择阿加特为队友】\x01",        # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1559"),
        (1, "loc_155F"),
        (SWITCH_DEFAULT, "loc_1565"),
    )


    label("loc_1559")

    OP_A2(0x1200)
    Jump("loc_1565")

    label("loc_155F")

    OP_A2(0x1201)
    Jump("loc_1565")

    label("loc_1565")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_1573")
    AddParty(0x2, 0xF7, 0xFF)
    Jump("loc_1577")

    label("loc_1573")

    AddParty(0x5, 0xF7, 0xFF)

    label("loc_1577")

    Return()

    # Function_7_14DF end

    SaveToFile()

Try(main)

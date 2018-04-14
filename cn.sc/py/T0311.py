from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 洛连特

    CreateScenaFile(
        FileName            = 'T0311   ._SN',
        MapName             = 'Rolent',
        Location            = 'T0311.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60084",
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
        '提妲',                                 # 9
        '科洛丝',                               # 10
        '雪拉扎德',                             # 11
        'tarotto',                              # 12
        'tarotto',                              # 13
        'tarotto',                              # 14
        'tarotto',                              # 15
        'tarotto',                              # 16
        'tarotto',                              # 17
        '酒杯',                                 # 18
        '照片',                                 # 19
        '莱娜',                                 # 20
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
        'ED6_DT06/CH20008 ._CH',             # 00
        'ED6_DT26/CH20230 ._CH',             # 01
        'ED6_DT26/CH20226 ._CH',             # 02
        'ED6_DT07/CH00023 ._CH',             # 03
        'ED6_DT06/CH20133 ._CH',             # 04
        'ED6_DT26/CH20328 ._CH',             # 05
        'ED6_DT06/CH20021 ._CH',             # 06
        'ED6_DT26/CH20338 ._CH',             # 07
        'ED6_DT26/CH20333 ._CH',             # 08
        'ED6_DT26/CH20315 ._CH',             # 09
        'ED6_DT26/CH20278 ._CH',             # 0A
    )

    AddCharChipPat(
        'ED6_DT06/CH20008P._CP',             # 00
        'ED6_DT26/CH20230P._CP',             # 01
        'ED6_DT26/CH20226P._CP',             # 02
        'ED6_DT07/CH00023P._CP',             # 03
        'ED6_DT06/CH20133P._CP',             # 04
        'ED6_DT26/CH20328P._CP',             # 05
        'ED6_DT06/CH20021P._CP',             # 06
        'ED6_DT26/CH20338P._CP',             # 07
        'ED6_DT26/CH20333P._CP',             # 08
        'ED6_DT26/CH20315P._CP',             # 09
        'ED6_DT26/CH20278P._CP',             # 0A
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 589834,
        ChipIndex           = 0xA,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 589834,
        ChipIndex           = 0xA,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 589834,
        ChipIndex           = 0xA,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 589834,
        ChipIndex           = 0xA,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 589834,
        ChipIndex           = 0xA,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 589834,
        ChipIndex           = 0xA,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 327686,
        ChipIndex           = 0x6,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 786438,
        ChipIndex           = 0x6,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclEvent(
        X                   = 250,
        Y                   = 0,
        Z                   = -4510,
        Range               = 1700,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x2BC,
        Unknown_18          = 0x0,
        Unknown_1C          = 7,
    )


    DeclActor(
        TriggerX            = 146350,
        TriggerZ            = 0,
        TriggerY            = 144640,
        TriggerRange        = 800,
        ActorX              = 147980,
        ActorZ              = 1200,
        ActorY              = 145500,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 72740,
        TriggerZ            = 0,
        TriggerY            = 71390,
        TriggerRange        = 800,
        ActorX              = 73030,
        ActorZ              = 1200,
        ActorY              = 72380,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 8470,
        TriggerZ            = 0,
        TriggerY            = 67050,
        TriggerRange        = 1200,
        ActorX              = 8470,
        ActorZ              = 500,
        ActorY              = 67050,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 5,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 9830,
        TriggerZ            = 0,
        TriggerY            = 70700,
        TriggerRange        = 800,
        ActorX              = 9830,
        ActorZ              = 800,
        ActorY              = 70700,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 6,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_332",          # 00, 0
        "Function_1_35B",          # 01, 1
        "Function_2_49F",          # 02, 2
        "Function_3_95B",          # 03, 3
        "Function_4_BF7",          # 04, 4
        "Function_5_E78",          # 05, 5
        "Function_6_F42",          # 06, 6
        "Function_7_F8A",          # 07, 7
        "Function_8_253A",         # 08, 8
    )


    def Function_0_332(): pass

    label("Function_0_332")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_343")
    OP_A3(0x10F0)
    Event(0, 2)
    Jump("loc_35A")

    label("loc_343")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 1)), scpexpr(EXPR_END)), "loc_35A")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x75), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x10F1)
    Event(0, 8)

    label("loc_35A")

    Return()

    # Function_0_332 end

    def Function_1_35B(): pass

    label("Function_1_35B")

    OP_78(0x8C, 0x8C, 0xB4)
    OP_82(0x80, 0x0)
    OP_82(0x81, 0x0)
    OP_79(0x0, 0x2)
    OP_79(0x2, 0x2)
    OP_79(0x3, 0x2)
    OP_79(0x4, 0x2)
    OP_79(0x5, 0x2)
    OP_79(0x6, 0x2)
    OP_79(0x7, 0x2)
    OP_79(0x8, 0x2)
    OP_79(0x9, 0x2)
    OP_79(0xA, 0x2)
    OP_79(0xB, 0x2)
    OP_79(0xC, 0x2)
    OP_79(0xD, 0x2)
    OP_79(0xE, 0x2)
    OP_79(0xF, 0x2)
    OP_79(0x10, 0x2)
    OP_79(0x11, 0x2)
    OP_79(0x12, 0x2)
    OP_79(0x13, 0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x302, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x305, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_49E")
    SetChrFlags(0x8, 0x2)
    SetChrFlags(0x8, 0x4)
    SetChrFlags(0x8, 0x40)
    SetChrPos(0x8, 148300, 400, 144950, 180)
    SetChrChipByIndex(0x8, 1)
    SetChrSubChip(0x8, 0)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x2)
    SetChrFlags(0x9, 0x4)
    SetChrFlags(0x9, 0x40)
    SetChrPos(0x9, 72990, 450, 72950, 270)
    SetChrChipByIndex(0x9, 2)
    SetChrSubChip(0x9, 0)
    ClearChrFlags(0x9, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 1)), scpexpr(EXPR_END)), "loc_433")
    OP_6F(0x6, 10)
    OP_70(0x6, 0xA)
    Jump("loc_441")

    label("loc_433")

    OP_6F(0x6, 15)
    OP_70(0x6, 0xF)

    label("loc_441")

    OP_72(0x2, 0x10)
    OP_71(0x7, 0x0)
    OP_71(0x7, 0x4)
    OP_72(0x0, 0x4)
    OP_72(0x0, 0x20)
    OP_72(0x7, 0x20)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 2)), scpexpr(EXPR_END)), "loc_477")
    OP_6F(0x0, 12)
    OP_70(0x0, 0xC)
    Jump("loc_49E")

    label("loc_477")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_490")
    OP_6F(0x0, 12)
    OP_70(0x0, 0xC)
    Jump("loc_49E")

    label("loc_490")

    OP_6F(0x0, 50)
    OP_70(0x0, 0x32)

    label("loc_49E")

    Return()

    # Function_1_35B end

    def Function_2_49F(): pass

    label("Function_2_49F")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_6D(144440, 0, 145300, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    OP_BB(0x0, 0x1, 0x43)
    OP_BD()
    SetChrFlags(0x101, 0x2)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x101, 0x40)
    SetChrFlags(0x8, 0x2)
    SetChrFlags(0x8, 0x4)
    SetChrFlags(0x8, 0x40)
    SetChrChipByIndex(0x101, 0)
    SetChrSubChip(0x101, 0)
    SetChrChipByIndex(0x8, 1)
    SetChrSubChip(0x8, 0)
    SetChrPos(0x8, 148300, 400, 144950, 180)
    SetChrPos(0x101, 147700, 450, 145270, 180)
    ClearChrFlags(0x8, 0x80)
    OP_71(0x7, 0x0)
    OP_71(0x7, 0x4)
    OP_72(0x0, 0x4)
    OP_72(0x0, 0x20)
    OP_72(0x7, 0x20)
    OP_6F(0x0, 11)
    OP_70(0x0, 0xB)
    Sleep(500)
    FadeToBright(1000, 0)
    OP_6D(148090, 0, 145410, 2500)
    OP_0D()
    OP_22(0x7, 0x0, 0x46)
    Sleep(1000)
    OP_62(0x101, 0xFFFFFDDA, 1200, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_6F(0x0, 11)
    OP_70(0x0, 0x14)
    OP_99(0x101, 0x0, 0x7, 0x320)
    Sleep(200)

    ChrTalk(    #0
        0x101,
        "#1340F#5P………啊……………\x02",
    )

    SetChrSubChip(0x101, 17)
    CloseMessageWindow()
    SetChrSubChip(0x101, 20)
    Sleep(500)
    SetChrSubChip(0x101, 23)
    Sleep(500)
    SetChrSubChip(0x101, 20)
    Sleep(500)
    SetChrSubChip(0x101, 23)
    OP_99(0x101, 0x12, 0x13, 0x320)
    SetChrSubChip(0x101, 17)

    ChrTalk(    #1
        0x101,
        (
            "#1335F刚才是……门的声音吧……\x02\x03",

            "#451F………………………………\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(1000)
    ClearChrFlags(0x101, 0x2)
    ClearChrFlags(0x101, 0x4)
    SetChrChipByIndex(0x101, 65535)
    SetChrSubChip(0x101, 0)
    SetChrPos(0x101, 146350, 0, 144660, 270)
    OP_6D(146930, 0, 144820, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #2
        0x8,
        "#40W……嗯…………\x02",
    )

    CloseMessageWindow()
    OP_6F(0x0, 20)
    OP_70(0x0, 0x32)
    OP_99(0x8, 0x0, 0x9, 0x258)
    OP_8C(0x101, 90, 400)
    SetChrSubChip(0x8, 10)
    Sleep(300)

    ChrTalk(    #3
        0x8,
        (
            "#1252F#40W……啊……\x02\x03",

            "姐姐……\x01",
            "……怎么了……？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x101,
        (
            "#1336F#6P抱歉，吵醒你了啊。\x02\x03",

            "#1333F我担心门是不是关好了，\x01",
            "去确认一下。\x02\x03",

            "马上回来，你睡吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x8,
        (
            "#1250F#40W……嗯……知道了……\x02\x03",

            "#1251F姐姐……\x01",
            "……早点回来哦……\x02",
        )
    )

    CloseMessageWindow()
    OP_99(0x8, 0xB, 0x13, 0x320)
    Sleep(1000)

    ChrTalk(    #6
        0x101,
        (
            "#1336F#6P嘿嘿……真可爱。\x02\x03",

            "#1331F嗯～突然心血来潮\x01",
            "想戳戳她脸蛋了。\x02\x03",

            "#455F……喔，不行不行。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    SetChrFlags(0x101, 0x4)
    OP_8F(0x101, 0x23CF8, 0x0, 0x235AA, 0x1F4, 0x0)
    Sleep(500)
    OP_6F(0x0, 50)
    OP_70(0x0, 0xC)
    OP_73(0x0)
    Sleep(1000)
    OP_8F(0x101, 0x23BAE, 0x0, 0x23514, 0x1F4, 0x0)
    ClearChrFlags(0x101, 0x4)
    Sleep(500)
    OP_8C(0x101, 180, 400)
    Sleep(500)
    ClearChrFlags(0x101, 0x40)

    ChrTalk(    #7
        0x101,
        (
            "#1335F#5P（虽然可能是雪拉姐\x01",
            "  或者科洛丝……)\x02\x03",

            "（不过还是去确认一下门关没关好吧……）\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1817)
    OP_28(0x90, 0x1, 0x400)
    OP_31(0x0, 0xFE, 0x0)
    OP_31(0x1, 0xFE, 0x0)
    OP_31(0x2, 0xFE, 0x0)
    OP_31(0x6, 0xFE, 0x0)
    OP_31(0x4, 0xFE, 0x0)
    OP_31(0x5, 0xFE, 0x0)
    OP_31(0x7, 0xFE, 0x0)
    OP_31(0x3, 0xFE, 0x0)
    EventEnd(0x0)
    Return()

    # Function_2_49F end

    def Function_3_95B(): pass

    label("Function_3_95B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BAA")
    EventBegin(0x0)
    Fade(1000)
    OP_6D(72560, 0, 72180, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    SetChrPos(0x101, 72610, 0, 71390, 360)
    OP_0D()
    Sleep(500)

    ChrTalk(    #8
        0x9,
        "#1240F#40W呼……呼……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x101,
        (
            "#457F睡得好香……\x02\x03",

            "#1336F呵呵，科洛丝啊，\x01",
            "把她带到约修亚的房间的时候\x01",
            "还手忙脚乱了呢……\x02\x03",

            "真可爱。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x9,
        "#1241F#40W……嗯………\x02",
    )

    CloseMessageWindow()
    OP_99(0x9, 0x0, 0x5, 0x5DC)
    Sleep(300)
    OP_62(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(    #11
        0x9,
        (
            "#1241F#40W……老师……大家……\x02\x03",

            "#40W……我………\x01",
            "………怎么办…………\x02\x03",

            "#40W……………………………\x02\x03",

            "#1240F#40W呼……呼……\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #12
        0x101,
        "#1339F科洛丝……\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    SetChrFlags(0x101, 0x4)
    OP_8F(0x101, 0x11BC0, 0x0, 0x1179C, 0x1F4, 0x0)
    Sleep(500)
    OP_B0(0x6, 0xF)
    OP_6F(0x6, 15)
    OP_70(0x6, 0xA)
    OP_99(0x9, 0x5, 0x7, 0x3E8)
    OP_73(0x6)
    Sleep(1000)
    OP_8F(0x101, 0x11BA2, 0x0, 0x116DE, 0x1F4, 0x0)
    ClearChrFlags(0x101, 0x4)
    Sleep(500)

    ChrTalk(    #13
        0x101,
        "#1337F……我们俩都要加油哦。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1819)
    EventEnd(0x0)
    Jump("loc_BF6")

    label("loc_BAA")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #14
        "\x07\x05科洛丝以平静的表情熟睡着。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    TalkEnd(0xFF)

    label("loc_BF6")

    Return()

    # Function_3_95B end

    def Function_4_BF7(): pass

    label("Function_4_BF7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C4C")
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #15
        "\x07\x05提妲以平静的表情熟睡着。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Jump("loc_E77")

    label("loc_C4C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E2D")
    EventBegin(0x0)
    Fade(1000)
    OP_6D(147270, 0, 145070, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    SetChrPos(0x101, 146350, 0, 144680, 90)
    OP_0D()
    Sleep(500)

    ChrTalk(    #16
        0x8,
        (
            "#1253F#40W……呜……\x02\x03",

            "#40W爸爸……妈妈……\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(    #17
        0x8,
        (
            "#1253F#40W我……\x01",
            "会好好听话……\x02\x03",

            "#40W姐姐她们\x01",
            "也在一起……\x02\x03",

            "#40W……所以……放心吧……\x02\x03",

            "#40W……………………………\x02\x03",

            "#1251F#40W嘿嘿……呜喵呜喵……\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #18
        0x101,
        "#1339F#6P提妲……\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    SetChrFlags(0x101, 0x4)
    OP_8F(0x101, 0x23CF8, 0x0, 0x235AA, 0x1F4, 0x0)
    Sleep(500)
    OP_6F(0x0, 50)
    OP_70(0x0, 0xC)
    OP_73(0x0)
    Sleep(1000)
    OP_8F(0x101, 0x23BAE, 0x0, 0x23528, 0x1F4, 0x0)
    ClearChrFlags(0x101, 0x4)
    Sleep(500)

    ChrTalk(    #19
        0x101,
        (
            "#1342F#6P没关系……\x01",
            "有我们在。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x181A)
    EventEnd(0x0)
    Jump("loc_E77")

    label("loc_E2D")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #20
        "\x07\x05提妲以平静的表情熟睡着。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    TalkEnd(0xFF)

    label("loc_E77")

    Return()

    # Function_4_BF7 end

    def Function_5_E78(): pass

    label("Function_5_E78")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F01")
    OP_8C(0x101, 180, 0)

    ChrTalk(    #21
        0x101,
        "#453F啊……\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #22
        "\x07\x05床还是温热的。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(    #23
        0x101,
        (
            "#1335F雪拉姐……\x01",
            "去哪儿了呢？\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x181B)
    TalkEnd(0xFF)
    Jump("loc_F41")

    label("loc_F01")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #24
        "\x07\x05床还是温热的。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    TalkEnd(0xFF)

    label("loc_F41")

    Return()

    # Function_5_E78 end

    def Function_6_F42(): pass

    label("Function_6_F42")

    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #25
        "\x07\x05门上着锁。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    # Function_6_F42 end

    def Function_7_F8A(): pass

    label("Function_7_F8A")

    EventBegin(0x0)
    SetChrFlags(0xA, 0x4)
    SetChrPos(0xA, -8070, 200, 2290, 180)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0x11, -7800, 700, 1240, 0)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0xC, -8140, 730, 1400, 0)
    SetChrPos(0xD, -8640, 730, 1400, 0)
    SetChrPos(0xF, -8140, 730, 940, 0)
    SetChrPos(0x10, -8640, 730, 940, 0)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    TurnDirection(0x101, 0x103, 0)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_6D(-8070, 0, 2290, 3000)

    ChrTalk(    #26
        0xA,
        "#026F……………………………\x02",
    )

    CloseMessageWindow()
    SetChrPos(0x101, 820, 0, -2480, 300)

    ChrTalk(    #27
        0x101,
        "#3P雪拉姐……\x02",
    )

    CloseMessageWindow()
    OP_62(0xA, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_10AB():
        OP_8E(0xFE, 0xFFFFEC50, 0x0, 0xFFFFFEE8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_10AB)

    def lambda_10C6():
        OP_6D(-6710, 0, 880, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_10C6)
    SetChrSubChip(0xA, 1)
    WaitChrThread(0x101, 0x1)

    ChrTalk(    #28
        0xA,
        (
            "#023F呀……\x01",
            "艾丝蒂尔，怎么了？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x101,
        (
            "#454F嗯，听到点声音\x01",
            "就醒来了。\x02\x03",

            "是雪拉姐啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0xA,
        (
            "#020F是啊……\x02\x03",

            "#021F呵呵，感觉到气息就醒来～\x01",
            "挺像正游击士的样子了嘛？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x101,
        (
            "#1331F嘿嘿……\x01",
            "可能有点紧张了。\x02\x03",

            "#1336F似乎发生了很多事\x01",
            "脑子有点混乱。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0xA,
        "#524F是吗……\x02",
    )

    CloseMessageWindow()

    def lambda_11E8():
        OP_8E(0xFE, 0xFFFFE2D2, 0x0, 0xFFFFFE52, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_11E8)

    def lambda_1203():
        OP_6D(-7650, 0, 970, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1203)
    Sleep(500)
    SetChrSubChip(0xA, 0)
    WaitChrThread(0x101, 0x1)
    SetChrFlags(0x101, 0x4)

    def lambda_122F():
        OP_96(0xFE, 0xFFFFDFEE, 0xC8, 0xFFFFFDBC, 0x1F4, 0xFA0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_122F)
    OP_8C(0x101, 0, 1000)
    WaitChrThread(0x101, 0x1)
    SetChrChipByIndex(0x101, 5)
    Sleep(1000)

    ChrTalk(    #33
        0x101,
        "#1333F#6P雪拉姐，在看什么啊？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0xA,
        "#027F#5P这个啊……\x02",
    )

    CloseMessageWindow()

    def lambda_129E():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0xC8)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_129E)
    SetChrFlags(0xA, 0x2)
    SetChrChipByIndex(0xA, 4)
    OP_99(0xA, 0x8, 0xA, 0x190)
    Sleep(500)

    ChrTalk(    #35
        0xA,
        (
            "#026F#5P逆位的皇帝。\x02\x03",

            "慈悲，共鸣，信任，障碍，不成熟。\x01",
            "──还有对敌人的困惑。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x101,
        (
            "#1335F#6P感、感觉上，\x01",
            "真是张故弄玄虚的卡牌啊。\x02\x03",

            "#455F对敌人的困惑，\x01",
            "稍微有点不理解……\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xC, 10)
    SetChrSubChip(0xC, 12)

    def lambda_1381():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0xC8)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_1381)
    ClearChrFlags(0xA, 0x2)
    SetChrSubChip(0xA, 0)
    SetChrChipByIndex(0xA, 3)
    Sleep(500)

    ChrTalk(    #37
        0xA,
        (
            "#026F#5P呵呵……\x02\x03",

            "#524F今天不是\x01",
            "给艾丝蒂尔占卜的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x101,
        "#453F#6P啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0xA,
        (
            "#020F#5P呵呵，你似乎\x01",
            "也有心事呢。\x02\x03",

            "那个记者的事？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0x101,
        (
            "#1340F#6P啊……\x02\x03",

            "#452F………………………………\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0xA,
        (
            "#524F#5P并不是在逼你。\x02\x03",

            "只是，心情整理好之后\x01",
            "说出来也好哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0x101,
        (
            "#452F#6P…………………………\x02\x03",

            "#1340F雪拉姐……\x01",
            "能听我倾诉吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0xA,
        (
            "#027F#5P你就是我妹妹。\x02\x03",

            "姐姐这身份\x01",
            "就是这时候用的哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0x101,
        (
            "#1339F#6P雪拉姐……\x02\x03",

            "#452F……这个，能看看吗？\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #45
        "\x07\x05把朵洛希的照片递给雪拉扎德。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(    #46
        0xA,
        "#023F#5P照片……？\x02",
    )

    CloseMessageWindow()
    Fade(500)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0xA, 0x2)
    SetChrChipByIndex(0xA, 4)
    SetChrSubChip(0xA, 9)
    Sleep(1000)

    ChrTalk(    #47
        0xA,
        (
            "#023F#5P…………………………\x01",
            "…………………………\x02\x03",

            "#026F……原来如此啊。\x02\x03",

            "#524F这个，就是\x01",
            "你消沉的原因啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0x101,
        "#455F#6P……嗯………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0xA,
        (
            "#027F#5P应该是为隐秘活动\x01",
            "而准备的藏身之地……\x02\x03",

            "没错，要是他还身为游击士\x01",
            "就不能用这方法了。\x02\x03",

            "那……目标是什么呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0x101,
        "#1335F#6P雪拉姐……你不惊讶吗？\x02",
    )

    CloseMessageWindow()
    Fade(500)
    ClearChrFlags(0xA, 0x2)
    SetChrSubChip(0xA, 0)
    SetChrChipByIndex(0xA, 3)
    OP_0D()
    Sleep(500)

    ChrTalk(    #51
        0xA,
        (
            "#026F#5P说实话，我还以为\x01",
            "他在做更严重的事呢。\x02\x03",

            "#524F但是，空贼艇的抢夺事件\x01",
            "只是把士兵打晕了而已。\x02\x03",

            "的确很像是约修亚\x01",
            "会做得事情。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0x101,
        "#1339F#6P是，是啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0xA,
        (
            "#025F#5P不过，被拍到照片\x01",
            "就有点大意了。\x02\x03",

            "不像他呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0x101,
        (
            "#1336F#6P这个嘛……\x01",
            "因为这是朵洛希拍的照片嘛。\x02\x03",

            "一扯上照相机，\x01",
            "她可是有天才的运气和实力嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0xA,
        "#027F#5P原来如此，那个戴眼镜的女孩啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0x101,
        (
            "#452F#6P……对了，雪拉姐。\x02\x03",

            "这个照片……\x01",
            "是不是应该交给协会？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0xA,
        (
            "#026F#5P身为一个游击士，\x01",
            "被赋予的义务只有一个。\x02\x03",

            "#020F就是拯救被恶人伤害的\x01",
            "民间人士而已。\x02\x03",

            "你觉得约修亚和空贼混在一起\x01",
            "是想伤害民间人士吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0x101,
        (
            "#1330F#6P那、那种事\x01",
            "约修亚不可能会做的！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0xA,
        (
            "#027F#5P那就没有特地\x01",
            "报告的义务了。\x02\x03",

            "我也不打算\x01",
            "特地去报告这事。\x02\x03",

            "说到底，你只要\x01",
            "相信约修亚就行了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0x101,
        "#452F#6P……………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0xA,
        "#524F#5P还是说……你不相信他？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0x101,
        (
            "#452F#6P相信……虽然相信……\x02\x03",

            "#455F但是……很不安……\x02\x03",

            "他在我不知道的地方，\x01",
            "带着那冰冷的眼神……做些胡来的事……\x02\x03",

            "看起来就像\x01",
            "对自己的事漠不关心一样……\x02\x03",

            "#1341F干脆和爸爸商量\x01",
            "想办法找到他好了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0xA,
        "#023F#5P……艾丝蒂尔……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0x101,
        (
            "#1340F#6P但是，那我\x01",
            "是为什么到这里来的？\x02\x03",

            "不就是为了亲手\x01",
            "把约修亚带回来吗？\x02\x03",

            "#455F……想到这里\x01",
            "脑子就混乱了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0xA,
        (
            "#026F#5P是吗……\x02\x03",

            "#524F不过啊，艾丝蒂尔。\x02\x03",

            "你就算不这么焦急，\x01",
            "一样也会找到答案的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0x101,
        "#1340F#6P……啊………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0xA,
        (
            "#020F#5P现在的你，应该能够\x01",
            "把握好自己的心情。\x02\x03",

            "你只是迷失了\x01",
            "自己想做的事而已。\x02\x03",

            "不要着急，在自己心中\x01",
            "一定能找到答案的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0x101,
        "#1339F#6P雪拉姐……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0xA,
        (
            "#027F#5P和下船之后相比\x01",
            "似乎镇定多了。\x02\x03",

            "至少，现在应该做的事\x01",
            "你不是看得很清楚吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0x101,
        (
            "#1336F#6P嗯、嗯……\x02\x03",

            "#454F知道鲁克和伊莉莎的妈妈\x01",
            "倒下的时候……\x02\x03",

            "知道沮丧也没用，\x01",
            "反而有了干劲。\x02\x03",

            "然后，焦躁的心情\x01",
            "也减弱了……\x02\x03",

            "#1335F我……还是太单纯了吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0xA,
        (
            "#027F#5P呵呵，没这回事。\x02\x03",

            "只是，你似乎不习惯\x01",
            "停下来的生活。\x02\x03",

            "你是那种不断向前进\x01",
            "就会找到答案的类型。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0x101,
        (
            "#455F#6P呜呜……好像被捉弄了一样\x01",
            "真是高兴不起来。\x02\x03",

            "#1337F不过，谢谢雪拉姐。\x02\x03",

            "总觉得……\x01",
            "好像能够找到答案了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0xA,
        (
            "#027F#5P呵呵……\x01",
            "没什么大不了的。\x02\x03",

            "#021F话说回来……\x01",
            "约修亚也挺有一手的嘛。\x02\x03",

            "搞不好和那个空贼小姑娘\x01",
            "正打得火热呢㈱\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0x101,
        (
            "#455F#6P怎、怎么说到那去了……\x02\x03",

            "#459F还、还不确定\x01",
            "是那种关系啦！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0xA,
        (
            "#027F#5P哎呀，是吗？\x02\x03",

            "我记得她是个有点逞强、\x01",
            "蛮男孩子气的女生吧。\x02\x03",

            "而且，也觉得\x01",
            "品性不错……\x02\x03",

            "#021F说不定是个不错的发展㈱\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0x101,
        "#459F#6P真是的，雪拉姐……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0xA,
        (
            "#027F#5P同生死共患难之间\x01",
            "萌生了爱情……\x02\x03",

            "#023F啊，不过艾丝蒂尔。\x01",
            "你不用担心哦？\x02\x03",

            "#021F就算约修亚被抢走了，\x01",
            "你只要夺回来就行了！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0x101,
        (
            "#1338F#6P……下次打死我\x01",
            "也不找雪拉姐商量了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0xA,
        (
            "#021F#5P呵呵，开玩笑啦。\x02\x03",

            "#526F好了，关于约修亚的烦恼，\x01",
            "往这方面想就比较好了呢。\x02\x03",

            "这才比较像个年轻女孩子哦？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0x101,
        (
            "#455F#6P可是这方面\x01",
            "其实也很复杂……\x02\x03",

            "#1334F……就算不是这样～\x01",
            "还有科洛丝呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0xA,
        "#023F#5P啊？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0x101,
        (
            "#1336F#6P没、没什么的。\x02\x03",

            "#1331F似乎不知不觉的就镇定下来了。\x01",
            "我这就去睡了……\x02\x03",

            "雪拉姐还不睡吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0xA,
        (
            "#524F#5P不，我也去睡了。\x02\x03",

            "难得阿加特他们\x01",
            "这么费心。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0x101,
        (
            "#453F#6P这么说来……\x02\x03",

            "#1340F……………………………\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0xA,
        "#020F#5P什么？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #86
        0x101,
        (
            "#1335F#6P……倒是雪拉姐\x01",
            "是不是有什么烦恼？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0xA,
        (
            "#026F#5P算是吧……\x01",
            "是有烦恼。\x02\x03",

            "#020F不过，两三天内\x01",
            "应该就会告诉大家了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0x101,
        (
            "#455F#6P是吗。\x02\x03",

            "#454F嗯，那我\x01",
            "就不作多余的担心了。\x02\x03",

            "不过……\x01",
            "千万别逞强哦？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0xA,
        (
            "#021F#5P呵呵，不必担心了。\x02\x03",

            "#027F还要照顾\x01",
            "身边的妹妹才行呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0x101,
        (
            "#455F#6P真是的……\x02\x03",

            "#1337F算啦。\x01",
            "晚安，雪拉姐。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0xA,
        "#021F#5P晚安，艾丝蒂尔。\x02",
    )

    CloseMessageWindow()

    def lambda_239B():
        OP_96(0xFE, 0xFFFFE2BE, 0x0, 0xFFFFFD94, 0x1F4, 0xFA0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_239B)
    SetChrSubChip(0x101, 0)
    SetChrChipByIndex(0x101, 65535)
    OP_8C(0x101, 90, 1000)
    WaitChrThread(0x101, 0x1)
    Sleep(500)
    SetChrSubChip(0xA, 1)

    def lambda_23D9():
        OP_8E(0x101, 0xBAE, 0x0, 0xFFFFF5E2, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_23D9)

    def lambda_23F4():
        OP_6D(-5170, 0, -30, 4000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_23F4)
    WaitChrThread(0x101, 0x1)

    def lambda_2411():
        OP_6D(-7600, 0, 2870, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2411)

    def lambda_2429():
        OP_6E(245, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_2429)
    Sleep(1000)
    SetChrSubChip(0xA, 0)
    WaitChrThread(0x101, 0x3)

    def lambda_2448():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0xC8)
        ExitThread()

    QueueWorkItem(0xD, 2, lambda_2448)
    SetChrFlags(0xA, 0x2)
    SetChrChipByIndex(0xA, 4)
    OP_99(0xA, 0x8, 0xA, 0x190)
    Sleep(500)

    ChrTalk(    #92
        0xA,
        (
            "#522F#5P逆位的皇帝。\x02\x03",

            "慈悲，共鸣，信任，障碍，不成熟。\x01",
            "──还有对敌人的困惑。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xA, 11)
    Sleep(1000)

    ChrTalk(    #93
        0xA,
        (
            "#026F#5P只是迷失了\x01",
            "该做的事，是吗……\x02\x03",

            "#524F呵呵……会是谁呢。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_20(0x1770)
    OP_0D()
    Sleep(3000)
    OP_22(0x118, 0x0, 0x28)
    Sleep(3000)
    OP_21()
    OP_A2(0x10F1)
    NewScene("ED6_DT21/T0300   ._SN", 101, 0, 0)
    IdleLoop()
    Return()

    # Function_7_F8A end

    def Function_8_253A(): pass

    label("Function_8_253A")

    EventBegin(0x0)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x101, 0x2)
    SetChrPos(0x101, 147700, 350, 145310, 320)
    SetChrChipByIndex(0x101, 7)
    SetChrSubChip(0x101, 0)
    SetChrFlags(0x13, 0x40)
    SetChrFlags(0x13, 0x4)
    SetChrFlags(0x13, 0x2)
    SetChrPos(0x13, 147960, 100, 145220, 320)
    SetChrChipByIndex(0x13, 8)
    SetChrSubChip(0x13, 8)
    ClearChrFlags(0x13, 0x80)
    OP_6D(145670, 400, 145530, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    OP_71(0x7, 0x0)
    OP_71(0x7, 0x4)
    OP_72(0x0, 0x4)
    OP_72(0x0, 0x20)
    OP_72(0x7, 0x20)
    OP_6F(0x0, 15)
    OP_70(0x0, 0xF)
    FadeToBright(1000, 0)
    OP_6D(148490, 400, 145420, 4000)
    OP_62(0x101, 0xFFFFFED4, 1300, 0x1C, 0x21, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x101)
    Sleep(1000)
    OP_51(0x13, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_51(0x13, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_51(0x13, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    Sleep(1000)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #94
        (
            "\x07\x05而夜晚，在母亲温暖的\x01",
            "怀抱中入睡……\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    FadeToDark(2000, 0, -1)
    OP_0D()
    ClearChrFlags(0x101, 0x4)
    SetChrChipByIndex(0x101, 65535)
    Sleep(500)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #95
        (
            "\x07\x05没有悲伤，\x01",
            "充满温柔的每一天……\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #96
        (
            "\x07\x05那确实──\x01",
            "是令人满足的时光。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    SetMapFlags(0x2000000)
    OP_A2(0x10F4)
    NewScene("ED6_DT21/T0300   ._SN", 101, 0, 0)
    IdleLoop()
    Return()

    # Function_8_253A end

    SaveToFile()

Try(main)

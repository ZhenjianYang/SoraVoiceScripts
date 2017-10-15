from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'T5112   ._SN',
        MapName             = 'Other',
        Location            = 'T5112.x',
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
            'ED6_DT21/SUB000  ._SN',
            ''
        ],
    )

    BuildStringList(
        '@FileName',                            # 8
        'Robert',                               # 9
        'Broken Lance',                         # 10
        'Novel',                                # 11
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
        'ED6_DT07/CH01450 ._CH',             # 00
        'ED6_DT26/CH20267 ._CH',             # 01
        'ED6_DT06/CH20021 ._CH',             # 02
    )

    AddCharChipPat(
        'ED6_DT07/CH01450P._CP',             # 00
        'ED6_DT26/CH20267P._CP',             # 01
        'ED6_DT06/CH20021P._CP',             # 02
    )

    DeclNpc(
        X                   = 26690,
        Z                   = 0,
        Y                   = 5140,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = 18860,
        Z                   = -300,
        Y                   = 5310,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 140520,
        Z                   = 650,
        Y                   = -33440,
        Direction           = 85,
        Unknown2            = 0,
        Unknown3            = 1703938,
        ChipIndex           = 0x2,
        NpcIndex            = 0x166,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclActor(
        TriggerX            = 25470,
        TriggerZ            = -300,
        TriggerY            = 4940,
        TriggerRange        = 800,
        ActorX              = 26690,
        ActorZ              = 1500,
        ActorY              = 5140,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 18860,
        TriggerZ            = -300,
        TriggerY            = 5310,
        TriggerRange        = 800,
        ActorX              = 18860,
        ActorZ              = -300,
        ActorY              = 5310,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 6,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 21170,
        TriggerZ            = 0,
        TriggerY            = 17380,
        TriggerRange        = 800,
        ActorX              = 20960,
        ActorZ              = 1000,
        ActorY              = 18200,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 7,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 26900,
        TriggerZ            = 0,
        TriggerY            = 7220,
        TriggerRange        = 800,
        ActorX              = 28160,
        ActorZ              = 1000,
        ActorY              = 7060,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 8,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 19970,
        TriggerZ            = -300,
        TriggerY            = 5580,
        TriggerRange        = 800,
        ActorX              = 19970,
        ActorZ              = -300,
        ActorY              = 5580,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 9,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 26550,
        TriggerZ            = 110,
        TriggerY            = 15520,
        TriggerRange        = 800,
        ActorX              = 27430,
        ActorZ              = 1110,
        ActorY              = 16059,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 10,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 14070,
        TriggerZ            = 0,
        TriggerY            = 17590,
        TriggerRange        = 800,
        ActorX              = 14070,
        ActorZ              = 1000,
        ActorY              = 17590,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 11,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 85780,
        TriggerZ            = 0,
        TriggerY            = 41480,
        TriggerRange        = 700,
        ActorX              = 85180,
        ActorZ              = 500,
        ActorY              = 41480,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 20,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 113640,
        TriggerZ            = 0,
        TriggerY            = 41480,
        TriggerRange        = 700,
        ActorX              = 113040,
        ActorZ              = 500,
        ActorY              = 41480,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 20,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 140520,
        TriggerZ            = 0,
        TriggerY            = -33440,
        TriggerRange        = 800,
        ActorX              = 140520,
        ActorZ              = 1000,
        ActorY              = -33440,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 12,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_28A",          # 00, 0
        "Function_1_2B0",          # 01, 1
        "Function_2_328",          # 02, 2
        "Function_3_3CF",          # 03, 3
        "Function_4_3D4",          # 04, 4
        "Function_5_76D",          # 05, 5
        "Function_6_965",          # 06, 6
        "Function_7_97F",          # 07, 7
        "Function_8_999",          # 08, 8
        "Function_9_9B3",          # 09, 9
        "Function_10_9CD",         # 0A, 10
        "Function_11_9E7",         # 0B, 11
        "Function_12_A01",         # 0C, 12
        "Function_13_A57",         # 0D, 13
        "Function_14_ACB",         # 0E, 14
        "Function_15_BEE",         # 0F, 15
        "Function_16_D56",         # 10, 16
        "Function_17_E53",         # 11, 17
        "Function_18_F79",         # 12, 18
        "Function_19_10A2",        # 13, 19
        "Function_20_24F5",        # 14, 20
    )


    def Function_0_28A(): pass

    label("Function_0_28A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x203, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x204, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_29F")
    SetChrFlags(0x8, 0x80)
    OP_64(0x0, 0x1)

    label("loc_29F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x203, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x203, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2AF")
    Event(0, 5)

    label("loc_2AF")

    Return()

    # Function_0_28A end

    def Function_1_2B0(): pass

    label("Function_1_2B0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x203, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x204, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2D2")
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x2)
    SetChrSubChip(0x9, 0)
    OP_64(0x0, 0x1)
    Jump("loc_302")

    label("loc_2D2")

    OP_64(0x1, 0x1)
    OP_64(0x2, 0x1)
    OP_64(0x3, 0x1)
    OP_64(0x4, 0x1)
    OP_64(0x5, 0x1)
    OP_64(0x6, 0x1)
    OP_65(0x0, 0x1)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x2)
    SetChrSubChip(0x9, 0)

    label("loc_302")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x216, 5)), scpexpr(EXPR_END)), "loc_312")
    SetChrFlags(0xA, 0x80)
    OP_64(0x9, 0x1)

    label("loc_312")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x203, 3)), scpexpr(EXPR_END)), "loc_327")
    SetMapFlags(0x2000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x51), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_327")

    Return()

    # Function_1_2B0 end

    def Function_2_328(): pass

    label("Function_2_328")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_END)),
        (0, "loc_359"),
        (1, "loc_365"),
        (2, "loc_371"),
        (3, "loc_37D"),
        (4, "loc_389"),
        (5, "loc_395"),
        (6, "loc_3A1"),
        (SWITCH_DEFAULT, "loc_3AD"),
    )


    label("loc_359")

    OP_99(0xFE, 0x0, 0x7, 0x5AA)
    Jump("loc_3B9")

    label("loc_365")

    OP_99(0xFE, 0x0, 0x7, 0x60E)
    Jump("loc_3B9")

    label("loc_371")

    OP_99(0xFE, 0x0, 0x7, 0x640)
    Jump("loc_3B9")

    label("loc_37D")

    OP_99(0xFE, 0x0, 0x7, 0x578)
    Jump("loc_3B9")

    label("loc_389")

    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_3B9")

    label("loc_395")

    OP_99(0xFE, 0x0, 0x7, 0x546)
    Jump("loc_3B9")

    label("loc_3A1")

    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_3B9")

    label("loc_3AD")

    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_3B9")

    label("loc_3B9")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3CE")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_3B9")

    label("loc_3CE")

    Return()

    # Function_2_328 end

    def Function_3_3CF(): pass

    label("Function_3_3CF")

    Call(0, 4)
    Return()

    # Function_3_3CF end

    def Function_4_3D4(): pass

    label("Function_4_3D4")

    TalkBegin(0x8)
    OP_A2(0x1007)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x2D6, 0x0)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x208, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_590")

    ChrTalk(    #0
        0x8,
        (
            "Hey, Estelle...is that a 'Heaven's Eye'\x01",
            "quartz you have there?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x8,
        (
            "Well, I'll be damned.\x01",
            "That's some pretty high-grade quartz.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x8,
        (
            "You'll need to upgrade an orbment slot\x01",
            "in order to set one of those.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x8,
        (
            "It requires a fair bit of sepith, but it'll also\x01",
            "increase your orbment's EP charge capacity,\x01",
            "so you should give it a try.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x8,
        (
            "If you select 'Slots' from 'Upgrade/Exchange,'\x01",
            "you can upgrade your slots.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)
    OP_A2(0x1041)
    TalkEnd(0x8)
    Return()

    label("loc_590")

    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "Talk\x01",                  # 0
            "Upgrade/Exchange\x01",      # 1
            "Shop\x01",                  # 2
            "Leave\x01",                 # 3
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5FE")
    OP_0D()
    OP_A9(0xFA)
    OP_56(0x0)
    TalkEnd(0x8)
    Return()

    label("loc_5FE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_617")
    OP_0D()
    OP_A9(0xFB)
    OP_56(0x0)
    TalkEnd(0x8)
    Return()

    label("loc_617")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_628")
    TalkEnd(0x8)
    Return()

    label("loc_628")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_713")

    ChrTalk(    #5
        0x8,
        (
            "You can't set a high-grade quartz without\x01",
            "an upgraded slot. You'd damage the\x01",
            "orbment if you tried!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x8,
        (
            "You'll need sepith to upgrade your slots,\x01",
            "but a nice bonus is that the upgrade\x01",
            "increases your max EP capacity, too.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_769")

    label("loc_713")


    ChrTalk(    #7
        0x8,
        "Be careful, you two.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x8,
        (
            "If you need your orbments tuned,\x01",
            "come see me any time.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_769")

    TalkEnd(0x8)
    Return()

    # Function_4_3D4 end

    def Function_5_76D(): pass

    label("Function_5_76D")

    EventBegin(0x0)
    OP_6D(20200, 0, 18730, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 18800, -800, 500, 0)
    SetChrPos(0x10A, 19720, -800, 500, 0)
    OP_9F(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x10A, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_7EA():
        OP_6D(18420, -300, 3580, 4000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_7EA)
    Sleep(2000)

    def lambda_807():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_807)

    def lambda_819():
        OP_8E(0x101, 0x4970, 0xFFFFFDDA, 0x85C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_819)
    Sleep(200)

    def lambda_839():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x10A, 2, lambda_839)
    OP_8E(0x10A, 0x4D08, 0xFFFFFDDA, 0x6AE, 0x7D0, 0x0)
    Sleep(500)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #9
        0x101,
        (
            "#1026F#3POh...\x02\x03",

            "That spear looks a lot like...\x01",
            "um, Kurt's...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x10A,
        "#813F...\x02",
    )

    CloseMessageWindow()
    OP_8C(0x10A, 270, 500)
    Sleep(500)

    ChrTalk(    #11
        0x10A,
        (
            "#810FUh, well, let's have a look around. Yeah.\x02\x03",

            "There might be, uh, clues. Or something...\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 90, 500)

    ChrTalk(    #12
        0x101,
        "#1002F#3PRight...\x02",
    )

    CloseMessageWindow()
    OP_A2(0x101C)
    OP_28(0x80, 0x1, 0x2)
    EventEnd(0x0)
    SetMapFlags(0x2000000)
    Return()

    # Function_5_76D end

    def Function_6_965(): pass

    label("Function_6_965")

    EventBegin(0x0)
    Call(0, 13)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x204, 2)), scpexpr(EXPR_END)), "loc_977")
    EventEnd(0x0)
    Jump("loc_979")

    label("loc_977")

    EventEnd(0x1)

    label("loc_979")

    SetMapFlags(0x2000000)
    Return()

    # Function_6_965 end

    def Function_7_97F(): pass

    label("Function_7_97F")

    EventBegin(0x0)
    Call(0, 14)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x204, 2)), scpexpr(EXPR_END)), "loc_991")
    EventEnd(0x0)
    Jump("loc_993")

    label("loc_991")

    EventEnd(0x1)

    label("loc_993")

    SetMapFlags(0x2000000)
    Return()

    # Function_7_97F end

    def Function_8_999(): pass

    label("Function_8_999")

    EventBegin(0x0)
    Call(0, 15)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x204, 2)), scpexpr(EXPR_END)), "loc_9AB")
    EventEnd(0x0)
    Jump("loc_9AD")

    label("loc_9AB")

    EventEnd(0x1)

    label("loc_9AD")

    SetMapFlags(0x2000000)
    Return()

    # Function_8_999 end

    def Function_9_9B3(): pass

    label("Function_9_9B3")

    EventBegin(0x0)
    Call(0, 16)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x204, 2)), scpexpr(EXPR_END)), "loc_9C5")
    EventEnd(0x0)
    Jump("loc_9C7")

    label("loc_9C5")

    EventEnd(0x1)

    label("loc_9C7")

    SetMapFlags(0x2000000)
    Return()

    # Function_9_9B3 end

    def Function_10_9CD(): pass

    label("Function_10_9CD")

    EventBegin(0x0)
    Call(0, 17)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x204, 2)), scpexpr(EXPR_END)), "loc_9DF")
    EventEnd(0x0)
    Jump("loc_9E1")

    label("loc_9DF")

    EventEnd(0x1)

    label("loc_9E1")

    SetMapFlags(0x2000000)
    Return()

    # Function_10_9CD end

    def Function_11_9E7(): pass

    label("Function_11_9E7")

    EventBegin(0x0)
    Call(0, 18)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x204, 2)), scpexpr(EXPR_END)), "loc_9F9")
    EventEnd(0x0)
    Jump("loc_9FB")

    label("loc_9F9")

    EventEnd(0x1)

    label("loc_9FB")

    SetMapFlags(0x2000000)
    Return()

    # Function_11_9E7 end

    def Function_12_A01(): pass

    label("Function_12_A01")

    SetChrFlags(0xA, 0x80)
    OP_64(0x9, 0x1)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #13
        "\x07\x00Found #570i.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_59()
    OP_3E(0x23A, 1)
    OP_A2(0x10B5)
    TalkEnd(0xFF)
    Return()

    # Function_12_A01 end

    def Function_13_A57(): pass

    label("Function_13_A57")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #14
        (
            "\x07\x05A broken spear is lying on the ground.\x01",
            "It appears to belong to Kurt.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    Return()

    # Function_13_A57 end

    def Function_14_ACB(): pass

    label("Function_14_ACB")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #15
        (
            "\x07\x05The window is broken, and shards\x01",
            "of glass lie on the floor.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x203, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BE9")
    OP_A2(0x101D)
    OP_28(0x80, 0x1, 0x4)

    ChrTalk(    #16
        0x101,
        (
            "#1015FThis is the window that jaeger\x01",
            "leapt through last night, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x10A,
        (
            "#812FYeah.\x02\x03",

            "He was really skilled--you could tell\x01",
            "from the way he handled himself.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BE9")

    Call(0, 19)
    Return()

    # Function_14_ACB end

    def Function_15_BEE(): pass

    label("Function_15_BEE")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #18
        "\x07\x05The orbal telephone has been smashed to pieces.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x203, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D51")
    OP_A2(0x101E)
    OP_28(0x80, 0x1, 0x8)

    ChrTalk(    #19
        0x10A,
        (
            "#1316FDang it. No surprise from pro mercenaries,\x01",
            "I guess. No way they wouldn't cut all the\x01",
            "obvious means of communication.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x101,
        (
            "#1002FYeah, they don't want us calling\x01",
            "for any reinforcements.\x02\x03",

            "Damn, that's going to make this\x01",
            "even harder...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D51")

    Call(0, 19)
    Return()

    # Function_15_BEE end

    def Function_16_D56(): pass

    label("Function_16_D56")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #21
        "\x07\x05The floor is stained with blood.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x203, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E4E")
    OP_A2(0x101F)
    OP_28(0x80, 0x1, 0x10)

    ChrTalk(    #22
        0x101,
        "#1026FIs this...Kurt's?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x10A,
        (
            "#813FI, I, uh... I think so...\x02\x03",

            "But, I mean, there isn't a lot,\x01",
            "so his injuries probably aren't...\x01",
            "f-fatal... Yeah...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E4E")

    Call(0, 19)
    Return()

    # Function_16_D56 end

    def Function_17_E53(): pass

    label("Function_17_E53")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #24
        "\x07\x05The barrels of foodstuffs are empty.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x204, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F74")
    OP_A2(0x1020)
    OP_28(0x80, 0x1, 0x20)

    ChrTalk(    #25
        0x101,
        "#1004FThe enemy took our food, too?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x10A,
        (
            "#812FYeah, they're the only ones\x01",
            "who would have, I think.\x02\x03",

            "And I don't see Phyllis anywhere--no blood,\x01",
            "thank Aidios. I wonder what happened...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F74")

    Call(0, 19)
    Return()

    # Function_17_E53 end

    def Function_18_F79(): pass

    label("Function_18_F79")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #27
        (
            "\x07\x05There are bits of paper left behind,\x01",
            "indicating something was torn away\x01",
            "from the board.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x204, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_109D")
    OP_A2(0x1021)
    OP_28(0x80, 0x1, 0x40)

    ChrTalk(    #28
        0x101,
        "#1002FHey, wasn't there a map pinned up on here?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x10A,
        (
            "#812FYeah, just like the one we have.\x02\x03",

            "#818FIf they have that, then that means...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_109D")

    Call(0, 19)
    Return()

    # Function_18_F79 end

    def Function_19_10A2(): pass

    label("Function_19_10A2")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x203, 5)), scpexpr(EXPR_END)), "loc_10BD")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_10BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x203, 6)), scpexpr(EXPR_END)), "loc_10CE")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_10CE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x203, 7)), scpexpr(EXPR_END)), "loc_10DF")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_10DF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x204, 0)), scpexpr(EXPR_END)), "loc_10F0")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_10F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x204, 1)), scpexpr(EXPR_END)), "loc_1101")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_1101")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_110F")
    Return()

    label("loc_110F")

    OP_64(0x1, 0x1)
    OP_64(0x2, 0x1)
    OP_64(0x3, 0x1)
    OP_64(0x4, 0x1)
    OP_64(0x5, 0x1)
    OP_64(0x6, 0x1)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x101, 21280, 0, 9960, 170)
    SetChrPos(0x10A, 22640, 0, 9100, 262)
    OP_6D(23000, 0, 10260, 0)
    OP_67(0, 5830, -10000, 0)
    OP_6B(3230, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #30
        0x101,
        (
            "#3P#1015FOkay, so we've given the lodge a once-over...\x02\x03",

            "It looks like the second floor is completely\x01",
            "untouched. They only roughed up the first floor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x10A,
        (
            "#4P#1316FYeah... I get the feeling there\x01",
            "might be a reason for that...\x02\x03",

            "#816FAnd now that we know that, I think I have\x01",
            "an idea about what the enemy is doing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x101,
        "#3P#1004FYou do?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x10A,
        (
            "#4P#812FSome of it still doesn't quite make\x01",
            "sense, but a few of the pieces are\x01",
            "coming together, I think.\x02\x03",

            "Think about it. We've seen what's in the lodge,\x01",
            "and there was that tent in the forest.\x02\x03",

            "If we put together the clues we've\x01",
            "found in those two places...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x101,
        "#3P#1006FAhh, I think I get it!\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMessageWindowPos(-1, 50, -1, -1)
    SetChrName("")

    AnonymousTalk(    #35
        "\x18\x07\x05What did the foe do?\x02",
    )


    Menu(
        0,
        -1,
        150,
        0,
        (
            "Retreat from Le Locle\x01",         # 0
            "Seal the Canyon Entrance\x01",      # 1
            "Move to a New Base\x01",            # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_14E5"),
        (1, "loc_1612"),
        (2, "loc_1720"),
        (SWITCH_DEFAULT, "loc_17EC"),
    )


    label("loc_14E5")


    ChrTalk(    #36
        0x10A,
        (
            "#4P#813FNnnno, I don't think so.\x02\x03",

            "If they'd just retreated flat-out, they\x01",
            "wouldn't...want or need to take Kurt...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0x101,
        "#3P#1007FOh, good point...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x10A,
        (
            "#4P#812FThe tent was probably a staging\x01",
            "point for attacking the lodge.\x02\x03",

            "Which means it was abandoned...\x01",
            "because they've moved somewhere else!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_17EC")

    label("loc_1612")

    OP_2B(0x7E, 0x1)

    ChrTalk(    #39
        0x10A,
        (
            "#4P#817FThere's a pretty good chance of that, yeah.\x02\x03",

            "#810FThere's another thing we can say\x01",
            "with certainty, though, I bet.\x02\x03",

            "The tent was probably a staging\x01",
            "point for attacking the lodge.\x02\x03",

            "Which means it was abandoned...\x01",
            "because they've moved somewhere else!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_17EC")

    label("loc_1720")

    OP_2B(0x7E, 0x3)

    ChrTalk(    #40
        0x10A,
        (
            "#4P#810FExactamundo!\x01",
            "Glad we're on the same page, Estelle!\x02\x03",

            "The tent was probably a staging\x01",
            "point for attacking the lodge.\x02\x03",

            "Which means it was abandoned...\x01",
            "because they've moved somewhere else!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_17EC")


    ChrTalk(    #41
        0x101,
        (
            "#3P#1004FOh, I get it!\x02\x03",

            "#1015FBut they're obviously not using\x01",
            "the lodge as a base either. Hmm...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0x10A,
        (
            "#4P#812FWell, they probably realized that\x01",
            "it's hard to defend the lodge.\x02\x03",

            "If the guild ends up sending reinforcements,\x01",
            "they're going to need a defensible position\x01",
            "where they can keep the hostages.\x02\x03",

            "So they must've taken a position\x01",
            "somewhere in Le Locle that they\x01",
            "think they can defend easily.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0x101,
        (
            "#3P#1006FYeah, okay, that makes a lot of sense.\x02\x03",

            "So the only place like that\x01",
            "around here would be...\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x8, 20220, -550, 0, 181)

    NpcTalk(    #44
        0x8,
        "Man's Voice",
        "#1PYou two!\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x10A, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_1A4D():
        OP_6D(22240, -300, 7440, 1500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1A4D)
    TurnDirection(0x101, 0x8, 400)
    TurnDirection(0x10A, 0x8, 400)
    OP_4A(0x8, 255)
    OP_9F(0x8, 0x0, 0x0, 0x0, 0x0, 0x0)
    ClearChrFlags(0x8, 0x80)

    def lambda_1A87():
        OP_9F(0x8, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_1A87)
    OP_8E(0x8, 0x4F1A, 0xFFFFFDDA, 0x7A8, 0x7D0, 0x0)
    WaitChrThread(0x101, 0x1)
    WaitChrThread(0x8, 0x0)

    ChrTalk(    #45
        0x10A,
        "#814F#6POh!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0x101,
        (
            "#1004FRobert!\x02\x03",

            "#1018FHey, you're safe! Are you okay?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1B02():
        OP_8E(0xFE, 0x57DA, 0xFFFFFED4, 0x1B1C, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x10A, 0, lambda_1B02)
    Sleep(100)

    def lambda_1B22():
        OP_8E(0xFE, 0x52A8, 0xFFFFFED4, 0x1B80, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1B22)
    Sleep(200)

    def lambda_1B42():
        OP_8E(0xFE, 0x5334, 0xFFFFFED4, 0x14BE, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_1B42)
    WaitChrThread(0x10A, 0x0)
    OP_8C(0x10A, 224, 500)
    WaitChrThread(0x101, 0x0)
    WaitChrThread(0x8, 0x0)

    NpcTalk(    #47
        0x8,
        "Robert",
        (
            "Y-Yeah, I'm fine... Last night, Kurt\x01",
            "gave me a chance to get away...\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #48
        0x8,
        "Robert",
        "I've been hiding ever since then.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0x101,
        "#3P#1008FOh, okay...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0x10A,
        "#6P#1314FWe're still really glad you're safe.\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #51
        0x8,
        "Robert",
        (
            "Forgive me...\x01",
            "I ran away and abandoned everyone.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #52
        0x8,
        "Robert",
        "I'm a pathetic excuse for a man, I know.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0x101,
        (
            "#3P#1016FHey, don't be so hard on yourself.\x01",
            "These are jaegers, after all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0x10A,
        (
            "#6P#1310FYeah, she's right!\x02\x03",

            "If anything, we're lucky they\x01",
            "have one less hostage!\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #55
        0x8,
        "Robert",
        "I see... Thank you, girls.\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #56
        0x8,
        "Robert",
        (
            "So do you two have any idea where Kurt\x01",
            "and Phyllis are? You mentioned...hostages.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0x101,
        "#3P#1003FWell...\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #58
        (
            "\x07\x05Estelle and Anelace relayed their theory that the enemy had\x01",
            "taken the two as hostages and moved to a new base.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    NpcTalk(    #59
        0x8,
        "Robert",
        "I get it. A base that'd be easy to defend...\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #60
        0x8,
        "Robert",
        "Grimsel Fortress, then. Has to be.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0x101,
        "#3P#1004FGrimsel WHAT?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0x10A,
        "#6P#814FTh-There's a FORTRESS in the canyon?!\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #63
        0x8,
        "Robert",
        (
            "Well, we call it a 'fortress,'\x01",
            "but it isn't really one.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #64
        0x8,
        "Robert",
        (
            "It's a new training ground we built recently,\x01",
            "based on modern military facilities.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #65
        0x8,
        "Robert",
        (
            "The idea is to train bracers in counter-terror\x01",
            "operations in hijacked military bases,\x01",
            "that sort of thing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0x101,
        (
            "#3P#1015FI never realized there was a place like that\x01",
            "in the canyon... It IS on the map, though...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x10A, 500)
    Sleep(500)

    ChrTalk(    #67
        0x101,
        "#6P#1002F...Anelace.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x10A, 0x101, 500)

    ChrTalk(    #68
        0x10A,
        "#4P#816FYeah... Let's do it!\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #69
        0x8,
        "Robert",
        "H-Hey...\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #70
        0x8,
        "Robert",
        (
            "You two aren't thinking of taking the fight\x01",
            "to them all by yourselves, are you?!\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #71
        0x8,
        "Robert",
        (
            "You need to at least call\x01",
            "the guild for backup, or...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x8, 500)
    TurnDirection(0x10A, 0x8, 500)

    ChrTalk(    #72
        0x101,
        "#3P#1002FThey smashed the phone to bits, Robert.\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #73
        0x8,
        "Robert",
        "They...SMASHED MY PHONE?! THOSE--\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0x10A,
        (
            "#6P#812FUm, Robert, calm down, please!\x01",
            "Can you try and fix the phone?\x02\x03",

            "If you can get it working, contact\x01",
            "the guild as soon as you can!\x01",
            "Let them know what's happened!\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #75
        0x8,
        "Robert",
        "...Okay.\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #76
        0x8,
        "Robert",
        (
            "If you need me to tune your orbments,\x01",
            "just stop by the workshop.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #77
        0x8,
        "Robert",
        "Good luck, girls. I'll be praying for you!\x02",
    )

    CloseMessageWindow()

    def lambda_2381():
        OP_6D(24810, 0, 6590, 1500)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_2381)

    def lambda_2399():
        OP_8E(0xFE, 0x5BF4, 0x0, 0x16E4, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_2399)
    OP_8C(0x101, 89, 500)
    OP_8C(0x10A, 89, 500)
    WaitChrThread(0x8, 0x0)

    def lambda_23C7():
        OP_8E(0xFE, 0x609A, 0x0, 0x1AB8, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_23C7)
    WaitChrThread(0x8, 0x0)

    def lambda_23E7():
        OP_8E(0xFE, 0x68CE, 0x0, 0x1AEA, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_23E7)
    WaitChrThread(0x8, 0x0)

    def lambda_2407():
        OP_8E(0xFE, 0x6842, 0x0, 0x1414, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_2407)
    WaitChrThread(0x8, 0x0)
    OP_8C(0x8, 258, 500)
    OP_43(0x8, 0x0, 0x0, 0x2)
    WaitChrThread(0x8, 0x1)

    def lambda_243A():
        OP_6D(22920, -300, 7620, 1200)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_243A)
    OP_4B(0x8, 255)
    OP_65(0x0, 0x1)
    WaitChrThread(0x8, 0x1)
    OP_8C(0x10A, 262, 500)

    ChrTalk(    #78
        0x10A,
        (
            "#4P#816FOkay. Let's go, Estelle.\x02\x03",

            "Time to make a two-girl assault\x01",
            "on Grimsel Fortress!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0x101,
        "#3P#1018FLet's do it!\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1022)
    OP_28(0x80, 0x1, 0x80)
    OP_28(0x80, 0x1, 0x100)
    OP_28(0x80, 0x1, 0x200)
    OP_65(0x7, 0x1)
    OP_65(0x8, 0x1)
    Return()

    # Function_19_10A2 end

    def Function_20_24F5(): pass

    label("Function_20_24F5")

    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "Rest\x01",      # 0
            "Stop\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_257D")
    OP_20(0xBB8)
    FadeToDark(1000, 0, -1)
    Sleep(700)
    OP_22(0xD, 0x0, 0x64)
    OP_0D()
    OP_31(0x0, 0xFE, 0x0)
    OP_31(0x9, 0xFE, 0x0)
    OP_8C(0x0, 270, 0)
    OP_30(0x0)
    Sleep(3500)
    OP_1E()
    FadeToBright(1000, 0)
    OP_0D()
    OP_56(0x0)
    TalkEnd(0xFF)
    Return()

    label("loc_257D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2597")
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    label("loc_2597")

    Return()

    # Function_20_24F5 end

    SaveToFile()

Try(main)

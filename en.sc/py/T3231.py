from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 蔡斯

    CreateScenaFile(
        FileName            = 'T3231   ._SN',
        MapName             = 'Zeiss',
        Location            = 'T3231.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60015",
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
        'Recia',                                # 9
        'Alvin',                                # 10
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
        'ED6_DT07/CH01150 ._CH',             # 00
        'ED6_DT07/CH01020 ._CH',             # 01
    )

    AddCharChipPat(
        'ED6_DT07/CH01150P._CP',             # 00
        'ED6_DT07/CH01020P._CP',             # 01
    )

    DeclNpc(
        X                   = -100,
        Z                   = 0,
        Y                   = 120,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = -580,
        Z                   = 0,
        Y                   = -5020,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )


    DeclActor(
        TriggerX            = -1900,
        TriggerZ            = 0,
        TriggerY            = 5070,
        TriggerRange        = 800,
        ActorX              = -1900,
        ActorZ              = 1000,
        ActorY              = 5070,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 5,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -1890,
        TriggerZ            = 0,
        TriggerY            = -4990,
        TriggerRange        = 800,
        ActorX              = -1890,
        ActorZ              = 1000,
        ActorY              = -4990,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 6,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_142",          # 00, 0
        "Function_1_18A",          # 01, 1
        "Function_2_1D1",          # 02, 2
        "Function_3_1F5",          # 03, 3
        "Function_4_A76",          # 04, 4
        "Function_5_D7A",          # 05, 5
        "Function_6_109B",         # 06, 6
        "Function_7_13C0",         # 07, 7
    )


    def Function_0_142(): pass

    label("Function_0_142")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_16E")
    SetChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x402, 2)), scpexpr(EXPR_END)), "loc_16B")
    SetChrPos(0x9, -1110, 0, -3330, 90)

    label("loc_16B")

    Jump("loc_189")

    label("loc_16E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_END)), "loc_17D")
    ClearChrFlags(0x8, 0x80)
    Jump("loc_189")

    label("loc_17D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 0)), scpexpr(EXPR_END)), "loc_189")
    ClearChrFlags(0x8, 0x80)

    label("loc_189")

    Return()

    # Function_0_142 end

    def Function_1_18A(): pass

    label("Function_1_18A")

    OP_72(0x8, 0x10)
    OP_72(0x9, 0x10)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1D0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x402, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D0")
    OP_71(0x0, 0x4)
    OP_71(0x1, 0x4)
    OP_71(0x2, 0x4)
    OP_71(0x3, 0x4)
    OP_71(0x4, 0x4)
    OP_82(0x80, 0x0)
    OP_82(0x81, 0x0)
    OP_82(0x82, 0x0)
    OP_82(0x83, 0x0)
    OP_82(0x84, 0x0)

    label("loc_1D0")

    Return()

    # Function_1_18A end

    def Function_2_1D1(): pass

    label("Function_2_1D1")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1F4")
    OP_8D(0xFE, -1080, -1680, 1450, 3260, 2000)
    Jump("Function_2_1D1")

    label("loc_1F4")

    Return()

    # Function_2_1D1 end

    def Function_3_1F5(): pass

    label("Function_3_1F5")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x286, 0)), scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_5C0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_499")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_END)), "loc_356")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_2CC")

    ChrTalk(    #0
        0x8,
        (
            "Obviously the best way to check\x01",
            "the temperature of the baths is to\x01",
            "have a quick soak, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x8,
        (
            "It's part of my cleaning duties!\x01",
            "I-I'm not slacking off, I swear!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_353")

    label("loc_2CC")


    ChrTalk(    #2
        0x8,
        (
            "Aaaah, what a nice bath.\x01",
            "Yup, I can confirm a fact that\x01",
            "the baths are juuust fine now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x8,
        "Okay, I'd better get back to work!\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_353")

    Jump("loc_496")

    label("loc_356")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 0)), scpexpr(EXPR_END)), "loc_496")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_3F2")

    ChrTalk(    #4
        0x8,
        (
            "I really was gonna clean the baths,\x01",
            "you know.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x8,
        (
            "But there's so much steam that\x01",
            "you can barely see your hand in\x01",
            "front of your face.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_496")

    label("loc_3F2")


    ChrTalk(    #6
        0x8,
        (
            "I really was gonna clean the baths,\x01",
            "you know.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x8,
        (
            "But there's so much steam that\x01",
            "you can barely see your hand in\x01",
            "front of your face.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x8,
        "What's going on?\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_496")

    Jump("loc_5BD")

    label("loc_499")

    TurnDirection(0xFE, 0x104, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_552")

    ChrTalk(    #9
        0x8,
        (
            "Forgive me, Lord Olivier. You came\x01",
            "aaaaall this way, and yet you can't\x01",
            "even go in the springs.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x8,
        (
            "I don't know why, but the hot springs\x01",
            "are boiling! Literally.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5BD")

    label("loc_552")


    ChrTalk(    #11
        0x8,
        (
            "*siiigh*\x01",
            "Oh, Lord Olivier is so dreamy...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x8,
        (
            "I wish he would whisk me away\x01",
            "to the Imperial capital!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5BD")

    Jump("loc_A72")

    label("loc_5C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_652")

    ChrTalk(    #13
        0x8,
        (
            "I went in to clean the baths earlier,\x01",
            "but I couldn't even get started.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x8,
        (
            "There's too much steam in there!\x01",
            "I can't see a thing.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_706")

    label("loc_652")


    ChrTalk(    #15
        0x8,
        (
            "I didn't have anything better to do,\x01",
            "so I got a part-time job here cleaning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x8,
        (
            "All the customers are so old, though.\x01",
            "Would be nice if got some eye candy\x01",
            "once in a while...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_706")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_81C")

    ChrTalk(    #17
        0x8,
        "Huh...? Am I dreaming?\x02",
    )

    CloseMessageWindow()
    Sleep(1000)
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(400)

    ChrTalk(    #18
        0x8,
        (
            "Aaaaaaahhhh!\x01",
            "Lord Olivier, you're back!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x8,
        (
            "Heeheehee, I'm so happy!\x01",
            "You're back, you're back!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x101,
        "#1004F(L-Lord Olivier...?)\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x104,
        (
            "#031FIt's been a while, my princess.\x01",
            "Have you been a good girl?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_94C")

    label("loc_81C")

    TurnDirection(0x8, 0x104, 500)

    ChrTalk(    #22
        0x8,
        "Huh...? Am I dreaming?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x8,
        "Could he really be...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x104,
        (
            "#031FIt's been a while, my princess.\x01",
            "Have you been a good girl?\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(400)

    ChrTalk(    #25
        0x8,
        (
            "Aaaaaaahhhh! I knew it!\x01",
            "Lord Olivier, you're back!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x8,
        (
            "Heeheehee, I'm so happy!\x01",
            "You're back, you're back!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x101,
        "#1004F(L-Lord Olivier...?)\x02",
    )

    CloseMessageWindow()

    label("loc_94C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9FE")

    ChrTalk(    #28
        0x8,
        (
            "Forgive me, Lord Olivier. You came\x01",
            "aaaaall this way, and yet you can't\x01",
            "even go in the springs.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x8,
        (
            "I don't know why, but the hot springs\x01",
            "are boiling! Literally.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A6C")

    label("loc_9FE")


    ChrTalk(    #30
        0x8,
        "Please, Milord, sing for me again?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x8,
        (
            "My heart goes all aflutter whenever\x01",
            "you're playing your lute. ㈱\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A6C")

    OP_A2(0x1430)
    OP_A2(0x0)

    label("loc_A72")

    TalkEnd(0x8)
    Return()

    # Function_3_1F5 end

    def Function_4_A76(): pass

    label("Function_4_A76")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x402, 2)), scpexpr(EXPR_END)), "loc_BA1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B0E")

    ChrTalk(    #32
        0xFE,
        (
            "Aaaahh, nothing's finer than a\x01",
            "freshly drawn bath.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0xFE,
        (
            "It was worth sticking around until\x01",
            "they were up and running again.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)
    Jump("loc_B9E")

    label("loc_B0E")


    ChrTalk(    #34
        0xFE,
        (
            "Aaaahh, nothing's finer than a\x01",
            "freshly drawn bath.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0xFE,
        (
            "I'm gonna take another dip in a bit.\x01",
            "Who says you can't have two baths\x01",
            "in one day?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B9E")

    Jump("loc_D76")

    label("loc_BA1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_D76")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CDA")

    ChrTalk(    #36
        0xFE,
        (
            "I was told the pumps are broken,\x01",
            "so the baths are closed to the public.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0xFE,
        (
            "There's NO WAY I'm gonna let a little\x01",
            "thing like a broken pump keep me from\x01",
            "my precious baths after we came this far!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0xFE,
        (
            "So I'm staying put until they open\x01",
            "up again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0xFE,
        "Don't try to stop me! I won't budge!\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2)
    Jump("loc_D76")

    label("loc_CDA")


    ChrTalk(    #40
        0xFE,
        (
            "How could I not use the springs\x01",
            "after coming all this way?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0xFE,
        (
            "So I'm staying right here until they\x01",
            "open up again, and no one's gonna\x01",
            "stop me! Hmph!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D76")

    TalkEnd(0xFE)
    Return()

    # Function_4_A76 end

    def Function_5_D7A(): pass

    label("Function_5_D7A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x402, 2)), scpexpr(EXPR_END)), "loc_D88")
    Call(0, 7)
    Jump("loc_1097")

    label("loc_D88")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_E1A")
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #42
        (
            "\x07\x05There is a sign on the door. 'Due to pump failure,\x01",
            "the hot springs are temporarily closed.'\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    Jump("loc_1097")

    label("loc_E1A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1003")
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #43
        (
            "\x07\x05There is a sign on the door. 'Due to dangerous temperatures,\x01",
            "entry to the hot springs is temporarily restricted.'\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_F68")

    ChrTalk(    #44
        0x103,
        (
            "#020FIf we want to go in, we'll need to do\x01",
            "something about the baths boiling.\x02\x03",

            "Let's hurry to the spring's source\x01",
            "through that wooden gate out back.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1000")

    label("loc_F68")


    ChrTalk(    #45
        0x106,
        (
            "#050FIf we wanna go in, we'll need to do\x01",
            "something about the baths boiling.\x02\x03",

            "Let's hurry to the spring's source\x01",
            "through that wooden gate out back.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1000")

    Jump("loc_1097")

    label("loc_1003")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x290, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1015")
    Call(0, 7)
    Jump("loc_1097")

    label("loc_1015")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #46
        (
            "\x07\x05-Women's Bath-\x01",
            "If you would like to use this service,\x01",
            "please let the front desk know.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)

    label("loc_1097")

    TalkEnd(0xFF)
    Return()

    # Function_5_D7A end

    def Function_6_109B(): pass

    label("Function_6_109B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x402, 2)), scpexpr(EXPR_END)), "loc_10AC")
    OP_A2(0x3)
    Call(0, 7)
    Jump("loc_13BC")

    label("loc_10AC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_113E")
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #47
        (
            "\x07\x05There is a sign on the door. 'Due to pump failure,\x01",
            "the hot springs are temporarily closed.'\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    Jump("loc_13BC")

    label("loc_113E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1327")
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #48
        (
            "\x07\x05There is a sign on the door. 'Due to dangerous temperatures,\x01",
            "entry to the hot springs is temporarily restricted.'\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_128C")

    ChrTalk(    #49
        0x103,
        (
            "#020FIf we want to go in, we'll need to do\x01",
            "something about the baths boiling.\x02\x03",

            "Let's hurry to the spring's source\x01",
            "through that wooden gate out back.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1324")

    label("loc_128C")


    ChrTalk(    #50
        0x106,
        (
            "#050FIf we wanna go in, we'll need to do\x01",
            "something about the baths boiling.\x02\x03",

            "Let's hurry to the spring's source\x01",
            "through that wooden gate out back.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1324")

    Jump("loc_13BC")

    label("loc_1327")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x290, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_133C")
    OP_A2(0x3)
    Call(0, 7)
    Jump("loc_13BC")

    label("loc_133C")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #51
        (
            "\x07\x05-Men's Bath-\x01",
            "If you would like to use this service,\x01",
            "please let the front desk know.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)

    label("loc_13BC")

    TalkEnd(0xFF)
    Return()

    # Function_6_109B end

    def Function_7_13C0(): pass

    label("Function_7_13C0")

    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        10,
        1,
        (
            "[Bathe]\x01",      # 0
            "[Leave]\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_5F(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1421"),
        (1, "loc_164B"),
        (SWITCH_DEFAULT, "loc_164E"),
    )


    label("loc_1421")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_143E")
    OP_6F(0x9, 0)
    OP_70(0x9, 0x1D)
    Sleep(200)
    Jump("loc_1451")

    label("loc_143E")

    OP_6F(0x8, 0)
    OP_70(0x8, 0x1D)
    Sleep(200)

    label("loc_1451")

    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6F(0x8, 0)
    OP_6F(0x9, 0)
    Sleep(600)
    OP_22(0xA2, 0x0, 0x64)
    Sleep(1500)
    OP_22(0xB, 0x0, 0x64)
    Sleep(800)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_1515")
    SetChrPos(0x0, -1000, 0, -5090, 90)
    SetChrPos(0x1, -1000, 0, -5090, 90)
    SetChrPos(0x2, -1000, 0, -5090, 90)
    SetChrPos(0x3, -1000, 0, -5090, 90)
    SetChrPos(0x4, -1000, 0, -5090, 90)
    SetChrPos(0x5, -1000, 0, -5090, 90)
    SetChrPos(0x6, -1000, 0, -5090, 90)
    SetChrPos(0x7, -1000, 0, -5090, 90)
    Jump("loc_159D")

    label("loc_1515")

    SetChrPos(0x0, -1000, 0, 4900, 90)
    SetChrPos(0x1, -1000, 0, 4900, 90)
    SetChrPos(0x2, -1000, 0, 4900, 90)
    SetChrPos(0x3, -1000, 0, 4900, 90)
    SetChrPos(0x4, -1000, 0, 4900, 90)
    SetChrPos(0x5, -1000, 0, 4900, 90)
    SetChrPos(0x6, -1000, 0, 4900, 90)
    SetChrPos(0x7, -1000, 0, 4900, 90)

    label("loc_159D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_15B0")
    OP_31(0x0, 0xFB, 0x0)

    label("loc_15B0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_15C3")
    OP_31(0x1, 0xFB, 0x0)

    label("loc_15C3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_15D6")
    OP_31(0x2, 0xFB, 0x0)

    label("loc_15D6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_15E9")
    OP_31(0x3, 0xFB, 0x0)

    label("loc_15E9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_15FC")
    OP_31(0x5, 0xFB, 0x0)

    label("loc_15FC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_160F")
    OP_31(0x4, 0xFB, 0x0)

    label("loc_160F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1622")
    OP_31(0x6, 0xFB, 0x0)

    label("loc_1622")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1635")
    OP_31(0x7, 0xFB, 0x0)

    label("loc_1635")

    OP_69(0x0, 0x0)
    OP_30(0x0)
    FadeToBright(1000, 0)
    OP_0D()
    Jump("loc_1651")

    label("loc_164B")

    Jump("loc_1651")

    label("loc_164E")

    Jump("loc_1651")

    label("loc_1651")

    OP_A3(0x3)
    TalkEnd(0xFF)
    Return()

    # Function_7_13C0 end

    SaveToFile()

Try(main)

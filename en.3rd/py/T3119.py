from ED63RDScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 蔡斯

    CreateScenaFile(
        FileName            = 'T3119   ._SN',
        MapName             = 'Zeiss',
        Location            = 'T3119.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60013",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            'ED6_DT21/T3119   ._SN',
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
        'Professor Russell',                    # 9
        'Erika',                                # 10
        'Dan',                                  # 11
        'Supervisor Travis',                    # 12
        'Wilmont',                              # 13
        'Target Camera',                        # 14
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
        'ED6_DT07/CH02020 ._CH',             # 00
        'ED6_DT07/CH02620 ._CH',             # 01
        'ED6_DT07/CH01190 ._CH',             # 02
        'ED6_DT07/CH01540 ._CH',             # 03
        'ED6_DT07/CH01450 ._CH',             # 04
        'ED6_DT27/CH03970 ._CH',             # 05
        'ED6_DT27/CH03980 ._CH',             # 06
    )

    AddCharChipPat(
        'ED6_DT07/CH02020P._CP',             # 00
        'ED6_DT07/CH02620P._CP',             # 01
        'ED6_DT07/CH01190P._CP',             # 02
        'ED6_DT07/CH01540P._CP',             # 03
        'ED6_DT07/CH01450P._CP',             # 04
        'ED6_DT27/CH03970P._CP',             # 05
        'ED6_DT27/CH03980P._CP',             # 06
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

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
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
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -440,
        Z                   = 0,
        Y                   = 10490,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = 4650,
        Z                   = 1000,
        Y                   = 6180,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x80,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclEvent(
        X                   = -106990,
        Y                   = 0,
        Z                   = -550,
        Range               = 1000,
        Unknown_10          = 0x8CA,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 11,
    )


    DeclActor(
        TriggerX            = -540,
        TriggerZ            = 0,
        TriggerY            = 6300,
        TriggerRange        = 800,
        ActorX              = -540,
        ActorZ              = 900,
        ActorY              = 6300,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 10,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_1E6",          # 00, 0
        "Function_1_21C",          # 01, 1
        "Function_2_235",          # 02, 2
        "Function_3_2DC",          # 03, 3
        "Function_4_546",          # 04, 4
        "Function_5_7C2",          # 05, 5
        "Function_6_138C",         # 06, 6
        "Function_7_1406",         # 07, 7
        "Function_8_142E",         # 08, 8
        "Function_9_14C6",         # 09, 9
        "Function_10_14F1",        # 0A, 10
        "Function_11_34D5",        # 0B, 11
    )


    def Function_0_1E6(): pass

    label("Function_0_1E6")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x1A), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1FC")
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)

    label("loc_1FC")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x19), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_21B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 4)), scpexpr(EXPR_END)), "loc_21B")
    OP_A3(0x2504)
    SetMapFlags(0x10000000)
    Event(0, 5)

    label("loc_21B")

    Return()

    # Function_0_1E6 end

    def Function_1_21C(): pass

    label("Function_1_21C")

    OP_71(0x402, 0x0)
    ExitThread()
    OP_72(0x403, 0x0)
    ExitThread()
    OP_71(0x412, 0x0)
    ExitThread()
    OP_71(0x415, 0x0)
    ExitThread()
    Return()

    # Function_1_21C end

    def Function_2_235(): pass

    label("Function_2_235")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_END)),
        (0, "loc_266"),
        (1, "loc_272"),
        (2, "loc_27E"),
        (3, "loc_28A"),
        (4, "loc_296"),
        (5, "loc_2A2"),
        (6, "loc_2AE"),
        (SWITCH_DEFAULT, "loc_2BA"),
    )


    label("loc_266")

    OP_99(0xFE, 0x0, 0x7, 0x5AA)
    Jump("loc_2C6")

    label("loc_272")

    OP_99(0xFE, 0x0, 0x7, 0x60E)
    Jump("loc_2C6")

    label("loc_27E")

    OP_99(0xFE, 0x0, 0x7, 0x640)
    Jump("loc_2C6")

    label("loc_28A")

    OP_99(0xFE, 0x0, 0x7, 0x578)
    Jump("loc_2C6")

    label("loc_296")

    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_2C6")

    label("loc_2A2")

    OP_99(0xFE, 0x0, 0x7, 0x546)
    Jump("loc_2C6")

    label("loc_2AE")

    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_2C6")

    label("loc_2BA")

    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_2C6")

    label("loc_2C6")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2DB")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_2C6")

    label("loc_2DB")

    Return()

    # Function_2_235 end

    def Function_3_2DC(): pass

    label("Function_3_2DC")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F0, 5)), scpexpr(EXPR_END)), "loc_542")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_445")

    ChrTalk(    #0
        0xFE,
        (
            "Erika actually submitted an outline for the\x01",
            "Capel Project back in the day, you know.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        (
            "She had to back down after losing a bet to \x01",
            "Professor Russell, though, so it never saw\x01",
            "the light of day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0xFE,
        (
            "Not that much would have likely changed even\x01",
            "if it had. Whichever of them is in charge,\x01",
            "we're basically bound to suffer all the same...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_542")

    label("loc_445")


    ChrTalk(    #3
        0xFE,
        (
            "I swear, he's only just finished getting the Capel\x01",
            "back up and running, and he's off working on a\x01",
            "new invention.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0xFE,
        (
            "It really is amazing what those Russells are \x01",
            "capable of.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0xFE,
        (
            "They seem to have limitless energy when it\x01",
            "comes to technology.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_542")

    TalkEnd(0xFE)
    Return()

    # Function_3_2DC end

    def Function_4_546(): pass

    label("Function_4_546")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F0, 5)), scpexpr(EXPR_END)), "loc_7BE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_68C")

    ChrTalk(    #6
        0xFE,
        (
            "The Capel's a pretty complex thing, made up of\x01",
            "multiple different units connected together.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0xFE,
        (
            "So while the Capel itself was completely intact,\x01",
            "getting all the data back and everything up and\x01",
            "running again took over two months.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0xFE,
        (
            "That was an experience I hope I never have to\x01",
            "go through again...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7BE")

    label("loc_68C")


    ChrTalk(    #9
        0xFE,
        (
            "You remember that whole Orbal Shutdown \x01",
            "Phenomenon thing that happened?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0xFE,
        (
            "After that was over and we switched the Capel\x01",
            "back on, it ended up malfunctioning on us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0xFE,
        "...Erasing ALL of the data on the thing. All of it!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0xFE,
        (
            "It's taken us TWO WHOLE MONTHS to get it back\x01",
            "in order, too! Uuugh...\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_7BE")

    TalkEnd(0xFE)
    Return()

    # Function_4_546 end

    def Function_5_7C2(): pass

    label("Function_5_7C2")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_6D(820, 0, 12190, 0)
    OP_67(0, 5160, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(37000, 0)
    OP_6E(280, 0)
    OP_71(0x403, 0x0)
    ExitThread()
    OP_72(0x415, 0x0)
    ExitThread()
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    SetChrFlags(0x10, 0x40)
    SetChrFlags(0x11, 0x40)
    SetChrFlags(0x12, 0x40)
    SetChrPos(0x11, -430, 0, 10460, 0)
    SetChrPos(0x107, -1670, 0, 2060, 0)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #13
        0x11,
        (
            "#1452FSo this is what we're up against...\x02\x03",

            "It looks like it's not even performing at 10%\x01",
            "of its true capabilities, either.\x02\x03",

            "#1457FThese are some downright terrifying specs.\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0x6D, 0x0, 0x64)
    Sleep(500)

    ChrTalk(    #14
        0x107,
        "#061F#1PMom!\x02",
    )

    CloseMessageWindow()
    OP_59()
    Sleep(500)
    SetChrPos(0x107, 950, 0, 2620, 0)

    def lambda_951():
        OP_8E(0xFE, 0x3B6, 0x0, 0x1F18, 0x1194, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_951)
    WaitChrThread(0x107, 0x1)

    def lambda_971():
        OP_8E(0xFE, 0xFFFFFE52, 0x0, 0x22F6, 0x1194, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_971)
    WaitChrThread(0x107, 0x1)
    OP_8C(0x107, 0, 500)
    Sleep(300)
    OP_62(0x107, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #15
        0x107,
        (
            "#064F#12PWait! How in the world...?\x02\x03",

            "Isn't that data on Pater-Mater?\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x11, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x11, 0x107, 500)
    Sleep(300)

    ChrTalk(    #16
        0x11,
        "#1450F#5PHi there, Tita. You came at just the right time.\x02",
    )

    CloseMessageWindow()

    def lambda_A65():
        OP_8E(0xFE, 0xFFFFFE52, 0x0, 0x274C, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_A65)
    WaitChrThread(0x11, 0x1)

    ChrTalk(    #17
        0x11,
        "#1456F#5PYou've seen this robot in person, right?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x107,
        (
            "#560F#12PUmm... Well, yeah, but...\x02\x03",

            "...why do you ask?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x11,
        (
            "#1451F#5PWhat was it like in person?!\x02\x03",

            "Tell me everything you know!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_B41():
        OP_8E(0xFE, 0xFFFFFE52, 0x0, 0x25E4, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_B41)
    WaitChrThread(0x11, 0x1)

    def lambda_B61():
        OP_9E(0xFE, 0xF, 0x0, 0x3E8, 0x7D0)
        ExitThread()

    QueueWorkItem(0x107, 2, lambda_B61)
    Sleep(1000)

    ChrTalk(    #20
        0x107,
        "#067F#12PUmm... I... Umm...\x02",
    )

    CloseMessageWindow()
    OP_62(0x107, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x107)
    Sleep(500)

    ChrTalk(    #21
        0x107,
        (
            "#561F#12PW-Well, it was really big...but other than that,\x01",
            "I couldn't tell much just from looking at it...\x02",
        )
    )

    CloseMessageWindow()

    def lambda_C2F():
        OP_8F(0xFE, 0xFFFFFE52, 0x0, 0x274C, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_C2F)
    WaitChrThread(0x11, 0x1)

    ChrTalk(    #22
        0x11,
        (
            "#1833F#5POh, right... I suppose you wouldn't be able to.\x02\x03",

            "#1833FIt's an awful lot taller than you, after all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x107,
        (
            "#0564F#12PUmm... Mom?\x02\x03",

            "What're you looking at Pater-Mater's data for,\x01",
            "anyway?\x02\x03",

            "I thought you were here to work on some new \x01",
            "invention?\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x107, 270, 500)
    Sleep(600)
    OP_8C(0x107, 80, 500)
    Sleep(600)
    OP_8C(0x107, 0, 500)
    Sleep(300)
    OP_62(0x107, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_63(0x107)
    Sleep(300)
    OP_62(0x107, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #24
        0x107,
        "#064F#12P...Wait... You're not...\x02",
    )

    CloseMessageWindow()
    SetChrPos(0x10, -1670, 0, 2060, 0)

    NpcTalk(    #25
        0x10,
        "Voice",
        "#1PThat we are.\x02",
    )

    CloseMessageWindow()
    OP_59()
    OP_20(0xBB8)
    SetChrPos(0x10, -170, 0, 500, 0)
    SetChrPos(0x12, -910, 0, -210, 0)

    def lambda_E28():
        OP_8C(0xFE, 180, 500)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_E28)

    def lambda_E36():
        OP_8C(0xFE, 180, 500)
        ExitThread()

    QueueWorkItem(0x107, 2, lambda_E36)

    def lambda_E44():
        OP_6D(-430, 0, 8650, 2500)
        ExitThread()

    QueueWorkItem(0x15, 0, lambda_E44)

    def lambda_E5C():
        OP_6C(0, 2500)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_E5C)

    def lambda_E6C():
        OP_67(0, 5540, -10000, 2500)
        ExitThread()

    QueueWorkItem(0x15, 2, lambda_E6C)

    def lambda_E84():
        OP_8E(0xFE, 0xFFFFFF56, 0x0, 0x111C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_E84)
    Sleep(500)

    def lambda_EA4():
        OP_8E(0xFE, 0xFFFFFC72, 0x0, 0xE10, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_EA4)
    WaitChrThread(0x15, 0x0)
    WaitChrThread(0x12, 0x1)
    Sleep(300)

    ChrTalk(    #26
        0x12,
        (
            "#1460F#6PThe two of us are ready to start work at\x01",
            "any time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x11,
        (
            "#1456F#5PAll right, then. \x02\x03",

            "#1457FThen it's time to get right to work on our task--\x01",
            "making an archaism capable of competing against\x01",
            "our buddy Pater-Mater.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #28
        0x11,
        "#1455F#3SLet the Orbal Gear Project begin!#2S\x02",
    )

    OP_7C(0x0, 0x190, 0xFA0, 0x12C)
    CloseMessageWindow()
    OP_62(0x107, 0x0, 1700, 0x28, 0x2B, 0x64, 0x0)
    Sleep(500)
    TurnDirection(0x107, 0x11, 600)
    Sleep(500)
    OP_63(0x107)

    ChrTalk(    #29
        0x107,
        "#065F#6P#3SWhaaaaaat?!\x02",
    )

    OP_7C(0x0, 0x12C, 0xBB8, 0x12C)
    CloseMessageWindow()
    FadeToDark(2000, 0, -1)

    def lambda_1055():
        OP_6B(3200, 3000)
        ExitThread()

    QueueWorkItem(0x107, 3, lambda_1055)
    OP_0D()
    OP_44(0x10, 0xFF)
    OP_44(0x11, 0xFF)
    OP_44(0x12, 0xFF)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x12, 0x80)
    Sleep(3000)
    OP_6D(820, 0, 12190, 0)
    OP_67(0, 5160, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(37000, 0)
    OP_6E(280, 0)
    SetChrPos(0x107, -430, 0, 10460, 0)
    OP_1D(0x53)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(1000)

    ChrTalk(    #30
        0x107,
        (
            "#062F#40WWhy...?\x02\x03",

            "Why do I feel like this...?\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x107, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x107)
    Sleep(500)
    OP_8C(0x107, 180, 400)
    Sleep(300)

    def lambda_1143():
        OP_6D(630, 0, 11140, 2000)
        ExitThread()

    QueueWorkItem(0x107, 2, lambda_1143)

    def lambda_115B():
        OP_8E(0xFE, 0xFFFFFE52, 0x0, 0x2210, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_115B)
    WaitChrThread(0x107, 0x1)
    WaitChrThread(0x107, 0x2)
    Sleep(300)

    ChrTalk(    #31
        0x107,
        (
            "#063F#5P(Usually when I hear about something\x01",
            "new being invented, I get all excited.)\x02\x03",

            "(I get so caught up in what's happening\x01",
            "that I tune out to the world around me\x01",
            "and focus on helping Grandpa.)\x02\x03",

            "(But today...I just feel a little bit sad...)\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    OP_C5(0x0, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS583._CH")
    OP_C6(0x0, 0x3, -1, 500, 0)
    Sleep(1000)
    OP_C6(0x0, 0x3, 16777215, 1000, 0)
    Sleep(2000)

    ChrTalk(    #32
        0x107,
        "#562F#5PThis doesn't feel right...\x02",
    )

    CloseMessageWindow()
    Sleep(300)

    def lambda_1303():
        OP_6D(630, 0, 12500, 1500)
        ExitThread()

    QueueWorkItem(0x107, 2, lambda_1303)

    def lambda_131B():
        OP_67(0, 4500, -10000, 1500)
        ExitThread()

    QueueWorkItem(0x107, 3, lambda_131B)
    OP_8C(0x107, 0, 300)
    WaitChrThread(0x107, 0x2)
    Sleep(500)

    ChrTalk(    #33
        0x107,
        "#063F#12P#40WRenne...\x02",
    )

    CloseMessageWindow()

    def lambda_135F():
        OP_6B(2900, 3000)
        ExitThread()

    QueueWorkItem(0x15, 3, lambda_135F)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_20(0xFA0)
    OP_21()
    Sleep(1000)
    OP_A2(0x2504)
    NewScene("ED6_DT21/T3115   ._SN", 104, 0, 0)
    IdleLoop()
    Return()

    # Function_5_7C2 end

    def Function_6_138C(): pass

    label("Function_6_138C")

    OP_8C(0x10, 180, 500)
    OP_62(0x10, 0x0, 2000, 0x8, 0x9, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)

    def lambda_13B0():
        OP_8E(0xFE, 0xFFFFFEF2, 0x0, 0x46A, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_13B0)
    WaitChrThread(0x10, 0x1)

    def lambda_13D0():
        OP_8E(0xFE, 0xFFFFFCB8, 0x0, 0x1AE, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_13D0)
    WaitChrThread(0x10, 0x1)

    def lambda_13F0():
        OP_8E(0xFE, 0xFFFFFCB8, 0x0, 0xFFFFFA6A, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_13F0)
    Return()

    # Function_6_138C end

    def Function_7_1406(): pass

    label("Function_7_1406")

    OP_8C(0x12, 180, 500)
    Sleep(300)

    def lambda_1418():
        OP_8E(0xFE, 0xFFFFFC72, 0x0, 0xFFFFFA2E, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_1418)
    Return()

    # Function_7_1406 end

    def Function_8_142E(): pass

    label("Function_8_142E")

    OP_62(0x11, 0x0, 2000, 0x8, 0x9, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)

    def lambda_144B():
        OP_8E(0xFE, 0xFFFFF8E4, 0x0, 0x2274, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_144B)
    WaitChrThread(0x11, 0x1)

    def lambda_146B():
        OP_8E(0xFE, 0xFFFFF8E4, 0x0, 0x5DC, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_146B)
    WaitChrThread(0x11, 0x1)

    def lambda_148B():
        OP_8E(0xFE, 0xFFFFFC04, 0x0, 0x2BC, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_148B)
    WaitChrThread(0x11, 0x1)

    def lambda_14AB():
        OP_8E(0xFE, 0xFFFFFC04, 0x0, 0xFFFFFA2E, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_14AB)
    WaitChrThread(0x11, 0x1)
    Return()

    # Function_8_142E end

    def Function_9_14C6(): pass

    label("Function_9_14C6")

    OP_62(0x107, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Sleep(300)
    OP_8C(0x107, 0, 600)
    Sleep(1000)
    OP_8C(0x107, 180, 600)
    Return()

    # Function_9_14C6 end

    def Function_10_14F1(): pass

    label("Function_10_14F1")

    ClearMapFlags(0x1)
    EventBegin(0x0)
    OP_6D(-200, 0, 7100, 1000)
    FadeToDark(300, 0, 100)
    OP_22(0x9D, 0x0, 0x64)
    SetChrName("CAPEL")
    SetMessageWindowPos(250, 78, 36, 12)

    AnonymousTalk(    #34
        (
            "\x07\x02#1SThe Orbal Calculator\x01",
            "CAPEL SYSTEM Ver.7.0\x01",
            "Copyright(C) Z.C.F. 1197-1202\x01",
            "MODE:Information Retrieval\x01",
            "#200W　#20W\x01",
            "MEMORY_CHECK#100W..........#20WOK!\x01",
            "#200W　#20W\x01",
            "#1SAccessing database.\x01",
            "Select information to search.\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_160D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_34B2")
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        55,
        80,
        1,
        "[Central Factory]\x01",
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1658"),
        (SWITCH_DEFAULT, "loc_34A2"),
    )


    label("loc_1658")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3492")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        1,
        55,
        153,
        1,
        (
            "[Establishment]\x01",       # 0
            "[Universal Tech]\x01",      # 1
            "[Related Topics]\x01",      # 2
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_16C2"),
        (1, "loc_1F99"),
        (2, "loc_3091"),
        (SWITCH_DEFAULT, "loc_3482"),
    )


    label("loc_16C2")


    AnonymousTalk(    #35
        (
            "\x07\x02#1S[S1154] (S: Septian Calendar) - Death of Professor\x01",
            "C. Epstein in the sovereign state of Leman.\x01",
            "[S1155] Professor A. Russell returns to the Liberl\x01",
            "Kingdom. He proposes the spread of orbment\x01",
            "technology to a chilly reception.\x01",
            "[S1157] Professor Russell forms a partnership\x01",
            "with the Zeiss Clockmaker's Union. Together,\x01",
            "they establish the Zeiss Engineering Factory\x01",
            "(later renamed the Central Factory).\x01",
            "[S1160] After numerous visits from Edgar III,\x01",
            "funding was received which allowed Professor Russell\x01",
            "to take his place at the head of the factory.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #36
        (
            "\x07\x02#1S[S1162] Edgar III dies, and Alicia II assumes the\x01",
            "throne.\x01",
            "[S1164] Construction is completed on the\x01",
            "Langland Bridge.\x01",
            "[S1168] The first orbal-powered airship, the\x01",
            "Calatrava, is completed. (39 failed test flights\x01",
            "before success was achieved.)\x01",
            "[S1173] The Zeiss Engineering Factory is renamed \x01",
            "Zeiss Central Factory and begins sharing \x01",
            "technology with the Verne Company and Reinford \x01",
            "Company.\x01",
            "[S1175] The Liberl Orbalship Corporation is\x01",
            "established, and the transit commuter airship,\x01",
            "the Linde, is commissioned.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #37
        (
            "\x07\x02#1S[S1177] Transit commuter airship, the Cecilia,\x01",
            "is commissioned.\x01",
            "[S1178] Factory airship, the Leibnitz, is\x01",
            "completed.\x01",
            "[S1180] The Zeiss Central Factory is dismantled\x01",
            "and reconstructed at its current site. The\x01",
            "partially-underground factory in the Kaldia\x01",
            "Hills is completed.\x01",
            "[S1182] Professor Russell resigns from his\x01",
            "position as factory chief and is succeeded by\x01",
            "Murdock.\x01",
            "[S1185] Natural Science and Medical Research\x01",
            "divisions are founded.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #38
        (
            "\x07\x02#1S[S1187] The passenger ship, Eterna, sinks in\x01",
            "Calvard waters. Crown prince Judis dies.\x01",
            "[S1190] The Orbal Network, a joint venture with\x01",
            "the Epstein Foundation, is publicly announced.\x01",
            "[S1192] Outbreak of the Hundred Days War. The\x01",
            "Central Factory is taken by the Erebonian Army.\x01",
            "Prof. Russell develops patrol airships at Leiston \x01",
            "Fortress, which are used to mount a highly \x01",
            "effective counteroffensive, and soon become \x01",
            "central to the Royal Army.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #39
        (
            "\x07\x02#1S[S1193] Liberl and Erebonia sign a peace accord.\x01",
            "Orbment exports to the Erebonian Empire resume.\x01",
            "[S1197] Version 1.0 of the Capel orbal computer\x01",
            "is completed.\x01",
            "[S1199] Development commences on the high-speed\x01",
            "cruiser, the Arseille.\x01",
            "[S1202] The Arseille is completed and flight tests\x01",
            "commence.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_348F")

    label("loc_1F99")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3081")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x6C, 0x1, 0x4)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x6C, 0x1, 0x8)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x6C, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2044")

    Menu(
        2,
        55,
        259,
        1,
        (
            "[Orbments]\x01",               # 0
            "[Crystal Circuits]\x01",       # 1
            "[Septium]\x01",                # 2
            "[Airships]\x01",               # 3
            "[Orbal Weaponry]\x01",         # 4
            "[Tactical Orbments]\x01",      # 5
            "[Bracer Guild Sign]\x01",      # 6
        )
    )

    Jump("loc_20A5")

    label("loc_2044")


    Menu(
        2,
        55,
        259,
        1,
        (
            "[Orbments]\x01",               # 0
            "[Crystal Circuits]\x01",       # 1
            "[Septium]\x01",                # 2
            "[Airships]\x01",               # 3
            "[Orbal Weaponry]\x01",         # 4
            "[Tactical Orbments]\x01",      # 5
        )
    )


    label("loc_20A5")

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_20CD"),
        (1, "loc_22AA"),
        (2, "loc_23B4"),
        (3, "loc_2541"),
        (4, "loc_2740"),
        (5, "loc_29B4"),
        (6, "loc_2E49"),
        (SWITCH_DEFAULT, "loc_3071"),
    )


    label("loc_20CD")


    AnonymousTalk(    #40
        (
            "\x07\x02#1SEntry: Orbment\x01",
            "General term for devices that draw orbal energy\x01",
            "from septium, invented 50 years ago by Prof. C.\x01",
            "Epstein. The clockwork mechanism inside causes a\x01",
            "reaction between quartz, which in turn produces\x01",
            "a variety of different phenomena. Their greatest\x01",
            "advantages over combustion engines is that the\x01",
            "orbal energy within them is gradually restored\x01",
            "over time and the variety of different phenomena\x01",
            "they can produce. They are also much more\x01",
            "economically efficient.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_307E")

    label("loc_22AA")


    AnonymousTalk(    #41
        (
            "\x07\x02#1SEntry: Crystal Circuit (Quartz)\x01",
            "An electrical circuit with a crystalline structure\x01",
            "made from processed septium fragments (sepith).\x01",
            "They serve as an energy source but also cause\x01",
            "varied phenomena, which are only seen when they\x01",
            "are placed inside an orbment.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_307E")

    label("loc_23B4")


    AnonymousTalk(    #42
        (
            "\x07\x02#1SEntry: Septium\x01",
            "A grouping of seven gemstones found throughout\x01",
            "the continent. Prized as jewels for eons, it was\x01",
            "also regarded as a symbol of mystery. The invention\x01",
            "of technology to refine and process septium \x01",
            "fragments too small to use as jewels, called \x01",
            "sepith, and make them into quartz, resulted in a \x01",
            "massive increase in the importance of septium as\x01",
            "a resource across the continent.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_307E")

    label("loc_2541")


    AnonymousTalk(    #43
        (
            "\x07\x02#1SEntry: Orbal Airships/'Orbalships'\x01",
            "Commonly regarded as the crowning achievement\x01",
            "of orbment technology. Enables the power of\x01",
            "flight by combining a flight engine to control\x01",
            "gravity and an orbal engine to provide vast\x01",
            "amounts of energy. Because of the need for \x01",
            "high-efficiency orbal energy transfer and the\x01",
            "complexity of controlling the airship, many\x01",
            "modern orbalships are equipped with highly capable\x01",
            "orbal arithmetic logic units. Orbalships less than\x01",
            "20 arge in length are simply called 'airships.'\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_307E")

    label("loc_2740")


    AnonymousTalk(    #44
        (
            "\x07\x02#1SEntry: Orbal Weaponry\x01",
            "Any firearm or cannon powered with orbment tech-\x01",
            "nology. Currently the most common form of military\x01",
            "weaponry among many nations. With orbal firearms,\x01",
            "energy is focused in a helical path along the\x01",
            "barrel, down to a tiny point, which then forces a\x01",
            "large metal projectile outward at high velocity.\x01",
            "These guns can fire more rounds than traditional\x01",
            "gunpowder arms, and at adjustable levels of force.\x01",
            "Orbal Cannons, meanwhile, fire shells containing\x01",
            "energy which explode on impact. Similar to orbal\x01",
            "guns, these have less recoil than gunpowder-using\x01",
            "cannons, and their power can be similarly adjusted.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_307E")

    label("loc_29B4")


    AnonymousTalk(    #45
        (
            "\x07\x02#1SEntry: Tactical Orbments/'Battle Orbments'\x01",
            "Orbments used to manipulate orbal magics.\x01",
            "Usually no larger than a pocket watch, so its\x01",
            "internal workings are extremely minute and\x01",
            "elegantly constructed. When quartz designed\x01",
            "for tactical orbment use is installed, it improves\x01",
            "the abilities of its bearer.\x01",
            "When this quartz synchronizes with the bearer\x01",
            "(a.k.a. the 'Resonance Phenomenon'), the\x01",
            "internal mechanisms take over the otherwise\x01",
            "complex process that would be required to use\x01",
            "magic, allowing just about anyone to use it in\x01",
            "the form of orbal arts. Furthermore, the arts\x01",
            "the user is able to use can be changed depending\x01",
            "on the combination of quartz inside.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #46
        (
            "\x07\x02#1SEntry: New Model Orbments\x01",
            "A new class of tactical orbments massively\x01",
            "upgraded from the preceding models developed by\x01",
            "the Epstein Foundation. In comparison to the old\x01",
            "model's six quartz slots, the new model has seven\x01",
            "slots.\x01",
            "This new model allows for more flexible quartz\x01",
            "arrangements, new combinations of usable orbal\x01",
            "magic, and even drastic increases in power.\x01",
            "However, as the architecture is drastically\x01",
            "different from the predecessor model, there is\x01",
            "no interchangeability in quartz between models.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_307E")

    label("loc_2E49")

    OP_28(0x6C, 0x1, 0x8)

    AnonymousTalk(    #47
        (
            "\x07\x02#1SEntry: Bracer Guild Sign\x01",
            "A metal sign removed from the Zeiss branch of the\x01",
            "incompetent Bracer Guild by the genius and dashing\x01",
            "Phantom Thief Bleublanc. While its financial value\x01",
            "is insignificant, the shock to guild members is likely\x01",
            "considerable, and reading this now must fill you with\x01",
            "shame. Ah, I have probably said enough. I need to\x01",
            "provide the next key.\x01\x01",
            "---The third key is in the city. Gaze up at\x01",
            "the [Three Hatted Brothers].---\x01\x01",
            "Note: this entry will self-delete. You are\x01",
            "recommended to commit this entry to a memo\x01",
            "immediately.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_307E")

    label("loc_3071")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_307E")

    label("loc_307E")

    Jump("loc_1F99")

    label("loc_3081")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x2)
    Jump("loc_348F")

    label("loc_3091")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3472")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        2,
        55,
        255,
        1,
        (
            "[Combustion Engine]\x01",      # 0
            "[Gasoline]\x01",               # 1
            "[Haulage Vehicle]\x01",        # 2
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_30FA"),
        (1, "loc_3207"),
        (2, "loc_334A"),
        (SWITCH_DEFAULT, "loc_3462"),
    )


    label("loc_30FA")


    AnonymousTalk(    #48
        (
            "\x07\x02#1SEntry: Combustion Engine\x01",
            "A machine which generates usable energy by\x01",
            "burning fuel within. Less efficient than its\x01",
            "orbal counterpart, due to issues with gaseous\x01",
            "exhaust and noise pollution.\x01\x01",
            "[Combustion Engine] \x01",
            "Number Owned: 1\x01",
            "Owner: Maintenance Chief Gustav\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_346F")

    label("loc_3207")


    AnonymousTalk(    #49
        (
            "\x07\x02#1SEntry: Gasoline\x01",
            "A liquid derived from the purification of the\x01",
            "naturally-occurring hydrocarbon compound known as\x01",
            "petroleum. Used primarily as fuel for combustion\x01",
            "engines and as an industrial solvent.\x01\x01",
            "[Republic-Manufactured Gasoline]\x01",
            "Emergency Stores: 20 mid-sized tanks\x01",
            "Repository: Orbment Manufacturing Factory\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_346F")

    label("loc_334A")

    OP_28(0x29, 0x1, 0x8000)

    AnonymousTalk(    #50
        (
            "\x07\x02#1SEntry: Orbal Haulage Vehicle\x01",
            "Any wheeled vehicle powered by orbal energy.\x01",
            "Widely considered uncomfortable to ride and\x01",
            "very limited in speed. Primarily used for\x01",
            "transporting cargo.\x01\x01",
            "[Orbment-Powered Vehicle]\x01",
            "Owner: No Data\x01",
            "Repository: Underground Factory Entrance\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_346F")

    label("loc_3462")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_346F")

    label("loc_346F")

    Jump("loc_3091")

    label("loc_3472")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x2)
    Jump("loc_348F")

    label("loc_3482")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_348F")

    label("loc_348F")

    Jump("loc_1658")

    label("loc_3492")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x1)
    Jump("loc_34AF")

    label("loc_34A2")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_34AF")

    label("loc_34AF")

    Jump("loc_160D")

    label("loc_34B2")

    SetMessageWindowPos(72, 320, 56, 3)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    EventEnd(0x1)
    Return()

    # Function_10_14F1 end

    def Function_11_34D5(): pass

    label("Function_11_34D5")

    SetPlaceName(0x9A)
    Return()

    # Function_11_34D5 end

    SaveToFile()

Try(main)

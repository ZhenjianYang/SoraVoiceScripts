from ED6ScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 蔡斯

    CreateScenaFile(
        FileName            = 'R3403   ._SN',
        MapName             = 'Zeiss',
        Location            = 'R3403.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60030",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            'ED6_DT01/R3403   ._SN',
            'ED6_DT01/R3403_1 ._SN',
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
        'Rudi',                                 # 9
        'Antoine',                              # 10
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
        'ED6_DT07/CH01500 ._CH',             # 00
        'ED6_DT07/CH01700 ._CH',             # 01
    )

    AddCharChipPat(
        'ED6_DT07/CH01500P._CP',             # 00
        'ED6_DT07/CH01700P._CP',             # 01
    )

    DeclNpc(
        X                   = 612030,
        Z                   = -50,
        Y                   = -62600,
        Direction           = 359,
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


    DeclEvent(
        X                   = 602300,
        Y                   = -1000,
        Z                   = -48740,
        Range               = 599000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0xFFFF13E8,
        Unknown_18          = 0x0,
        Unknown_1C          = 7,
    )


    ScpFunction(
        "Function_0_11A",          # 00, 0
        "Function_1_208",          # 01, 1
        "Function_2_21B",          # 02, 2
        "Function_3_231",          # 03, 3
        "Function_4_591",          # 04, 4
        "Function_5_59C",          # 05, 5
        "Function_6_9B7",          # 06, 6
        "Function_7_B03",          # 07, 7
    )


    def Function_0_11A(): pass

    label("Function_0_11A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_129")
    Jump("loc_156")

    label("loc_129")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_141")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x52), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_156")

    label("loc_141")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_156")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x51), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_156")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (100, "loc_166"),
        (101, "loc_178"),
        (SWITCH_DEFAULT, "loc_198"),
    )


    label("loc_166")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_175")
    OP_A2(0x507)
    Event(0, 5)

    label("loc_175")

    Jump("loc_198")

    label("loc_178")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_195")
    SetMapFlags(0x10000000)
    OP_A2(0x534)
    Event(0, 6)

    label("loc_195")

    Jump("loc_198")

    label("loc_198")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_1A7")
    ClearChrFlags(0x8, 0x80)
    Jump("loc_207")

    label("loc_1A7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 0)), scpexpr(EXPR_END)), "loc_1B1")
    Jump("loc_207")

    label("loc_1B1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_1BB")
    Jump("loc_207")

    label("loc_1BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_1DB")
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, 610200, -40, -62060, 180)
    Jump("loc_207")

    label("loc_1DB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_1E5")
    Jump("loc_207")

    label("loc_1E5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_207")
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x10)
    SetChrPos(0x8, 618600, -10, -47550, 46)

    label("loc_207")

    Return()

    # Function_0_11A end

    def Function_1_208(): pass

    label("Function_1_208")

    OP_16(0x2, 0xFA0, 0x76E58, 0xFFFD40E0, 0x3003A)
    Return()

    # Function_1_208 end

    def Function_2_21B(): pass

    label("Function_2_21B")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_230")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_21B")

    label("loc_230")

    Return()

    # Function_2_21B end

    def Function_3_231(): pass

    label("Function_3_231")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_2CD")
    TalkBegin(0xFE)

    ChrTalk(    #0
        0xFE,
        (
            "Faye hasn't been herself since\x01",
            "getting back from the factory\x01",
            "ship.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        (
            "I wonder if something happened\x01",
            "between her and her old boyfriend?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_58D")

    label("loc_2CD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_51D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_38F")
    TalkBegin(0xFE)

    ChrTalk(    #2
        0xFE,
        "Okay, be careful out there.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0xFE,
        (
            "That's the only one I've got,\x01",
            "so make sure you don't lose\x01",
            "it along the way!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0xFE,
        (
            "*sigh* I've got to buckle down\x01",
            "and get working myself.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_51A")

    label("loc_38F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x29, 0x1, 0x8)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x29, 0x1, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3AA")
    Call(1, 2)
    Jump("loc_51A")

    label("loc_3AA")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_45C")

    ChrTalk(    #5
        0xFE,
        (
            "Man, Faye really chewed\x01",
            "me out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0xFE,
        (
            "I bet she thinks I'm totally\x01",
            "worthless.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0xFE,
        (
            "She just broke up with that guy,\x01",
            "too. My one chance...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0xFE,
        "...and I blew it.\x02",
    )

    CloseMessageWindow()
    Jump("loc_51A")

    label("loc_45C")

    OP_A2(0x1)

    ChrTalk(    #9
        0xFE,
        "Good job, loser.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0xFE,
        (
            "Man, Faye really chewed\x01",
            "me out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0xFE,
        (
            "I bet she thinks I'm totally\x01",
            "worthless.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0xFE,
        (
            "She just broke up with that guy,\x01",
            "too. My one chance...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0xFE,
        "...and I blew it.\x02",
    )

    CloseMessageWindow()

    label("loc_51A")

    Jump("loc_58D")

    label("loc_51D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_58D")
    TalkBegin(0xFE)

    ChrTalk(    #14
        0xFE,
        "...Okay, that makes eight cans.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0xFE,
        "Check and double check!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0xFE,
        "Let's check in on the factory.\x02",
    )

    CloseMessageWindow()

    label("loc_58D")

    TalkEnd(0xFE)
    Return()

    # Function_3_231 end

    def Function_4_591(): pass

    label("Function_4_591")

    ClearMapFlags(0x800)
    OP_1B(0x0, 0x0, 0xFFFF)
    Return()

    # Function_4_591 end

    def Function_5_59C(): pass

    label("Function_5_59C")

    ClearMapFlags(0x1)
    EventBegin(0x0)
    OP_6D(600200, 0, -54800, 0)
    OP_6C(0, 0)
    SetChrPos(0x101, 596400, 0, -54800, 90)
    SetChrPos(0x102, 595000, 0, -53500, 90)
    SetChrPos(0x107, 595000, 0, -55200, 90)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(    #17
        0x101,
        "#004FOh...!\x02",
    )

    CloseMessageWindow()

    def lambda_611():
        OP_8E(0xFE, 0x967D0, 0x0, 0xFFFF29F0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_611)
    Sleep(200)

    def lambda_631():
        OP_8E(0xFE, 0x96258, 0x0, 0xFFFF2B80, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_631)
    Sleep(500)

    def lambda_651():
        OP_8E(0xFE, 0x962BC, 0x0, 0xFFFF25A4, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_651)

    def lambda_66C():
        OP_6D(618500, 0, -53800, 3500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_66C)

    def lambda_684():
        OP_6C(45000, 3300)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_684)
    WaitChrThread(0x101, 0x1)
    Sleep(500)

    ChrTalk(    #18
        0x101,
        (
            "#501FThe tunnel ends here...\x02\x03",

            "So, does that mean...this\x01",
            "is the entrance to Zeiss?\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x107, 0x1)
    TurnDirection(0x107, 0x101, 400)

    ChrTalk(    #19
        0x107,
        (
            "#060FThat's right.\x02\x03",

            "It leads right into the basement\x01",
            "of the central factory.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_753():
        OP_6D(615770, -90, -54810, 1200)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_753)
    OP_8C(0x101, 270, 400)
    WaitChrThread(0x101, 0x2)

    ChrTalk(    #20
        0x101,
        "#006FI'm excited to see it!\x02",
    )

    CloseMessageWindow()
    OP_8C(0x102, 135, 400)

    ChrTalk(    #21
        0x102,
        (
            "#015FThe central factory is the pride\x01",
            "and joy of Zeiss, since it's an\x01",
            "industrial city.\x02\x03",

            "#010FI'd heard it was big, but\x01",
            "that's about all I really\x01",
            "know...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x107,
        (
            "#061FWell, yeah. It's really huge.\x02\x03",

            "Anyone who's not used to the\x01",
            "layout could get lost in a hurry.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x101,
        (
            "#004FBrrrr...\x01",
            "There's a creepy thought.\x02\x03",

            "#007FI'm beginning to worry whether\x01",
            "or not we'll really be able to\x01",
            "make it to the guild...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x107,
        (
            "#560FThe way out to the city is\x01",
            "up on the first floor.\x02\x03",

            "I'll show you how to get there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x101,
        "#001FThanks.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x102,
        "#010FWell, let's go in.\x02",
    )

    CloseMessageWindow()
    EventEnd(0x0)
    Return()

    # Function_5_59C end

    def Function_6_9B7(): pass

    label("Function_6_9B7")

    EventBegin(0x0)
    OP_6D(619220, 250, -53680, 0)
    SetChrPos(0x106, 618640, 0, -54820, 270)
    SetChrPos(0x101, 619650, 750, -54420, 270)
    SetChrPos(0x102, 619020, 250, -55970, 270)
    SetChrPos(0x107, 620220, 1000, -55430, 270)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(    #27
        0x101,
        "#002FDo you think they ran in here?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x106,
        (
            "#552FNo, not a chance... There are no\x01",
            "fresh footprints here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x102,
        (
            "#012FThey wouldn't have had\x01",
            "time to cover them up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x107,
        "#065FSo...first floor?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x101,
        "#005FYeah, let's hurry!\x02",
    )

    CloseMessageWindow()
    ClearMapFlags(0x10000000)
    NewScene("ED6_DT01/T3111   ._SN", 103, 0, 0)
    IdleLoop()
    Return()

    # Function_6_9B7 end

    def Function_7_B03(): pass

    label("Function_7_B03")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_BB7")
    EventBegin(0x1)
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #32
        0x102,
        (
            "#010FFirst, we need to cancel\x01",
            "at the departure gate.\x02\x03",

            "If we don't follow procedure, it'll\x01",
            "just cause trouble for the clerk.\x02",
        )
    )

    CloseMessageWindow()
    OP_90(0x0, 0x5DC, 0x0, 0x0, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Jump("loc_1AD1")

    label("loc_BB7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_CFF")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C6D")
    OP_A2(0x0)
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #33
        0x102,
        (
            "#010FIs this the way to the\x01",
            "Kaldia Tunnel?\x02\x03",

            "It's almost time to set off, so\x01",
            "we shouldn't wander too far.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(    #34
        0x101,
        "#000FYeah, you're right.\x02",
    )

    CloseMessageWindow()
    Jump("loc_CE1")

    label("loc_C6D")

    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #35
        0x102,
        (
            "#010FThis way leads to the\x01",
            "Kaldia Tunnel.\x02\x03",

            "It's almost time to set off, so\x01",
            "we shouldn't wander too far.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CE1")

    OP_90(0x0, 0x5DC, 0x0, 0x0, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Jump("loc_1AD1")

    label("loc_CFF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_F57")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E4D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DCA")
    OP_A2(0x0)
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #36
        0x102,
        (
            "#017FEstelle, where are you going?\x02\x03",

            "To reach Leiston Fortress, we\x01",
            "have to go out the eastern door.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(    #37
        0x101,
        "#004FOh... Really?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x102,
        "#018FI swear...\x02",
    )

    CloseMessageWindow()
    Jump("loc_E4A")

    label("loc_DCA")

    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #39
        0x102,
        (
            "#017FTo reach Leiston Fortress, we\x01",
            "have to go out the eastern door.\x02\x03",

            "Didn't you just write this\x01",
            "down in your notes?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E4A")

    Jump("loc_F39")

    label("loc_E4D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_ECA")
    OP_A2(0x0)

    ChrTalk(    #40
        0x102,
        (
            "#012FThis way leads to the\x01",
            "Kaldia Tunnel.\x02\x03",

            "To reach Leiston Fortress, we\x01",
            "have to go out the eastern door.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F39")

    label("loc_ECA")


    ChrTalk(    #41
        0x102,
        (
            "#012FThis way leads to the\x01",
            "Kaldia Tunnel.\x02\x03",

            "To reach Leiston Fortress, we\x01",
            "have to go out the eastern door.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F39")

    OP_90(0x0, 0x5DC, 0x0, 0x0, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Jump("loc_1AD1")

    label("loc_F57")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1189")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_105A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1008")
    OP_A2(0x0)
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(    #42
        0x101,
        (
            "#000FAh... Yeah, it's about time we\x01",
            "report in at the guild.\x02\x03",

            "We could learn something new.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #43
        0x102,
        "#010FRight. Let's go.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1057")

    label("loc_1008")


    ChrTalk(    #44
        0x101,
        (
            "#000FFor now, we should head to\x01",
            "the guild.\x02\x03",

            "We could learn something new.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1057")

    Jump("loc_116B")

    label("loc_105A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10FA")
    OP_A2(0x0)
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #45
        0x102,
        (
            "#010FWe should go to the guild and\x01",
            "see what they have to say.\x02\x03",

            "Maybe they've found some\x01",
            "useful info.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(    #46
        0x101,
        "#000FYeah, let's go.\x02",
    )

    CloseMessageWindow()
    Jump("loc_116B")

    label("loc_10FA")

    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #47
        0x102,
        (
            "#010FWe should go to the guild and\x01",
            "see what they have to say.\x02\x03",

            "Maybe they've found some\x01",
            "useful info.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_116B")

    OP_90(0x0, 0x5DC, 0x0, 0x0, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Jump("loc_1AD1")

    label("loc_1189")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1435")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1283")
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #48
        0x102,
        (
            "#012FWait a second, Estelle.\x02\x03",

            "Let's go back to the guildhouse first\x01",
            "and check over the old records.\x02\x03",

            "We still really don't know enough\x01",
            "about this 'Zemuria Moss' stuff.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(    #49
        0x101,
        "#002FThat sounds fine to me.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1417")

    label("loc_1283")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_135D")
    TurnDirection(0x102, 0x107, 400)

    ChrTalk(    #50
        0x102,
        (
            "#012FHold on a second, Tita.\x02\x03",

            "Let's go back to the guildhouse first\x01",
            "and check over the old records.\x02\x03",

            "We still really don't know enough\x01",
            "about this 'Zemuria Moss' stuff.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x107, 0x102, 400)

    ChrTalk(    #51
        0x107,
        "#060FOkay.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1417")

    label("loc_135D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1417")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_137F")
    TurnDirection(0x102, 0x1, 400)
    Jump("loc_1386")

    label("loc_137F")

    TurnDirection(0x102, 0x0, 400)

    label("loc_1386")


    ChrTalk(    #52
        0x102,
        (
            "#012FWe know what the priest said,\x01",
            "but I'd still like to look over\x01",
            "the old records.\x02\x03",

            "We should get more intel on\x01",
            "this 'Zemuria Moss' stuff.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1417")

    OP_90(0x0, 0x5DC, 0x0, 0x0, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Jump("loc_1AD1")

    label("loc_1435")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_15DE")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1498")

    ChrTalk(    #53
        0x101,
        (
            "#002F(Oh, the tunnel is this way. \x01",
            "We need to go to the church.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_15C0")

    label("loc_1498")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14ED")

    ChrTalk(    #54
        0x102,
        (
            "#012F(Oh, the tunnel is this way. \x01",
            "We need to go to the church.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_15C0")

    label("loc_14ED")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1542")

    ChrTalk(    #55
        0x107,
        (
            "#062F(Oh, the tunnel is this way. \x01",
            "We need to go to the church.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_15C0")

    label("loc_1542")


    ChrTalk(    #56
        0x108,
        (
            "#070F(Hmm... This way leads to\x01",
            "the tunnel.)\x02\x03",

            "(It'd be ideal for training,\x01",
            "but we must go to the church,\x01",
            "for the moment.)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_15C0")

    OP_90(0x0, 0x5DC, 0x0, 0x0, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Jump("loc_1AD1")

    label("loc_15DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1765")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_16D6")
    OP_A2(0x0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1662")

    ChrTalk(    #57
        0x106,
        (
            "#050FBah... Chasing them turned\x01",
            "up nothing useful.\x02\x03",

            "We'd better get back to\x01",
            "the guild.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_16D3")

    label("loc_1662")

    TurnDirection(0x106, 0x0, 400)

    ChrTalk(    #58
        0x106,
        (
            "#050FHey, where do you think\x01",
            "you're going?\x02\x03",

            "Let's get to the guildhouse, and\x01",
            "don't spare the horses.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_16D3")

    Jump("loc_1747")

    label("loc_16D6")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_16EC")
    TurnDirection(0x106, 0x1, 400)
    Jump("loc_16F3")

    label("loc_16EC")

    TurnDirection(0x106, 0x0, 400)

    label("loc_16F3")


    ChrTalk(    #59
        0x106,
        (
            "#050FChasing them turned up nothing\x01",
            "useful. We'd better get back\x01",
            "to the guild.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1747")

    OP_90(0x0, 0x5DC, 0x0, 0x0, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Jump("loc_1AD1")

    label("loc_1765")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_18E7")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1844")
    TurnDirection(0x102, 0x101, 400)
    OP_A2(0x0)

    ChrTalk(    #60
        0x102,
        (
            "#010FWe still have something to\x01",
            "deliver for the professor.\x02\x03",

            "You DID make a note of what it\x01",
            "is we're delivering, right?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(    #61
        0x101,
        (
            "#009FD-Don't be a jerk!\x02\x03",

            "Of course I wrote it down.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_18C9")

    label("loc_1844")

    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #62
        0x102,
        (
            "#010FWe still have something to\x01",
            "deliver for the professor.\x02\x03",

            "For now, we should focus on\x01",
            "getting the things he asked\x01",
            "for.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_18C9")

    OP_90(0x0, 0x5DC, 0x0, 0x0, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Jump("loc_1AD1")

    label("loc_18E7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_197C")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_190B")
    TurnDirection(0x102, 0x1, 400)
    Jump("loc_1912")

    label("loc_190B")

    TurnDirection(0x102, 0x0, 400)

    label("loc_1912")


    ChrTalk(    #63
        0x102,
        (
            "#010FThis way leads to the\x01",
            "Kaldia Tunnel.\x02\x03",

            "Let's go see the professor.\x02",
        )
    )

    CloseMessageWindow()
    OP_90(0x0, 0x5DC, 0x0, 0x0, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Jump("loc_1AD1")

    label("loc_197C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1AD1")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_19DA")

    ChrTalk(    #64
        0x101,
        (
            "#006F(This is the tunnel. We've\x01",
            "got to go to Tita's place.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1AB6")

    label("loc_19DA")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1A3F")

    ChrTalk(    #65
        0x102,
        (
            "#010F(This way goes back to the Kaldia\x01",
            "Tunnel. We've got to go to Tita's\x01",
            "place.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1AB6")

    label("loc_1A3F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1AB6")

    ChrTalk(    #66
        0x107,
        (
            "#065FOops... This way goes back\x01",
            "to the Kaldia Tunnel.\x02\x03",

            "(I need to show everyone\x01",
            "the way to my house.)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1AB6")

    OP_90(0x0, 0x5DC, 0x0, 0x0, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)

    label("loc_1AD1")

    Return()

    # Function_7_B03 end

    SaveToFile()

Try(main)

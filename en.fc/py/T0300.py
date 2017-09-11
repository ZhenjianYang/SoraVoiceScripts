from ED6ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'T0300   ._SN',
        MapName             = 'Rolent',
        Location            = 'T0300.x',
        MapIndex            = 15,
        MapDefaultBGM       = "ed60088",
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
        'Joshua',                               # 9
        'Cassius',                              # 10
        'Glass',                                # 11
        'Elize Highway',                        # 12
    )

    DeclEntryPoint(
        Unknown_00              = 2000,
        Unknown_04              = 0,
        Unknown_08              = -6000,
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
        Unknown_30              = 315,
        Unknown_32              = 0,
        Unknown_34              = 360,
        Unknown_36              = 0,
        Unknown_38              = 0,
        Unknown_3A              = 15,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )

    DeclEntryPoint(
        Unknown_00              = 9600,
        Unknown_04              = 875,
        Unknown_08              = 300,
        Unknown_0C              = 4,
        Unknown_0E              = 118,
        Unknown_10              = 0,
        Unknown_14              = 9500,
        Unknown_18              = -10000,
        Unknown_1C              = 0,
        Unknown_20              = 0,
        Unknown_24              = 0,
        Unknown_28              = 2800,
        Unknown_2C              = 262,
        Unknown_30              = 315,
        Unknown_32              = 0,
        Unknown_34              = 360,
        Unknown_36              = 0,
        Unknown_38              = 0,
        Unknown_3A              = 15,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )

    DeclEntryPoint(
        Unknown_00              = 9600,
        Unknown_04              = 875,
        Unknown_08              = 300,
        Unknown_0C              = 4,
        Unknown_0E              = 118,
        Unknown_10              = 0,
        Unknown_14              = 9500,
        Unknown_18              = -10000,
        Unknown_1C              = 0,
        Unknown_20              = 0,
        Unknown_24              = 0,
        Unknown_28              = 2800,
        Unknown_2C              = 262,
        Unknown_30              = 315,
        Unknown_32              = 0,
        Unknown_34              = 360,
        Unknown_36              = 0,
        Unknown_38              = 0,
        Unknown_3A              = 15,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )

    DeclEntryPoint(
        Unknown_00              = 9600,
        Unknown_04              = 875,
        Unknown_08              = 300,
        Unknown_0C              = 4,
        Unknown_0E              = 118,
        Unknown_10              = 0,
        Unknown_14              = 9500,
        Unknown_18              = -10000,
        Unknown_1C              = 0,
        Unknown_20              = 0,
        Unknown_24              = 0,
        Unknown_28              = 2800,
        Unknown_2C              = 262,
        Unknown_30              = 315,
        Unknown_32              = 0,
        Unknown_34              = 360,
        Unknown_36              = 0,
        Unknown_38              = 0,
        Unknown_3A              = 15,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )


    AddCharChip(
        'ED6_DT07/CH00010 ._CH',             # 00
        'ED6_DT07/CH02000 ._CH',             # 01
        'ED6_DT06/CH20030 ._CH',             # 02
        'ED6_DT06/CH20011 ._CH',             # 03
        'ED6_DT06/CH20021 ._CH',             # 04
        'ED6_DT06/CH20132 ._CH',             # 05
    )

    AddCharChipPat(
        'ED6_DT07/CH00010P._CP',             # 00
        'ED6_DT07/CH02000P._CP',             # 01
        'ED6_DT06/CH20030P._CP',             # 02
        'ED6_DT06/CH20011P._CP',             # 03
        'ED6_DT06/CH20021P._CP',             # 04
        'ED6_DT06/CH20132P._CP',             # 05
    )

    DeclNpc(
        X                   = 11500,
        Z                   = 0,
        Y                   = -3400,
        Direction           = 135,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x1C1,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 2000,
        Z                   = 450,
        Y                   = -1200,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x1C1,
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
        Unknown3            = 262148,
        ChipIndex           = 0x4,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 4110,
        Z                   = -1000,
        Y                   = -46140,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0xFF,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclActor(
        TriggerX            = 21670,
        TriggerZ            = 0,
        TriggerY            = -2000,
        TriggerRange        = 800,
        ActorX              = 21670,
        ActorZ              = 1500,
        ActorY              = -1980,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 12,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 21670,
        TriggerZ            = 0,
        TriggerY            = 0,
        TriggerRange        = 800,
        ActorX              = 21670,
        ActorZ              = 1500,
        ActorY              = 20,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 13,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 21670,
        TriggerZ            = 0,
        TriggerY            = 2000,
        TriggerRange        = 800,
        ActorX              = 21670,
        ActorZ              = 1500,
        ActorY              = 2020,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 14,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_292",          # 00, 0
        "Function_1_437",          # 01, 1
        "Function_2_491",          # 02, 2
        "Function_3_49C",          # 03, 3
        "Function_4_502",          # 04, 4
        "Function_5_5C8",          # 05, 5
        "Function_6_1106",         # 06, 6
        "Function_7_114F",         # 07, 7
        "Function_8_1168",         # 08, 8
        "Function_9_1169",         # 09, 9
        "Function_10_1BD6",        # 0A, 10
        "Function_11_1C19",        # 0B, 11
        "Function_12_1C2F",        # 0C, 12
        "Function_13_1D11",        # 0D, 13
        "Function_14_1D68",        # 0E, 14
    )


    def Function_0_292(): pass

    label("Function_0_292")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (1, "loc_2A6"),
        (2, "loc_311"),
        (3, "loc_3B2"),
        (SWITCH_DEFAULT, "loc_436"),
    )


    label("loc_2A6")

    ClearMapFlags(0x1)
    SetChrChipByIndex(0x8, 2)
    SetChrPos(0x8, -6220, 3450, 4390, 180)
    SetChrFlags(0x8, 0x4)

    def lambda_2CC():

        label("loc_2CC")

        OP_99(0xFE, 0x0, 0x7, 0x320)
        OP_48()
        Jump("loc_2CC")

    QueueWorkItem2(0x8, 1, lambda_2CC)
    ClearChrFlags(0x8, 0x80)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x46), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_6D(7170, 3450, -16520, 0)
    OP_6C(308000, 0)
    FadeToBright(2000, 0)
    Event(0, 5)
    Jump("loc_436")

    label("loc_311")

    ClearMapFlags(0x1)
    ClearChrFlags(0x101, 0x80)
    ClearChrFlags(0x102, 0x80)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x101, 0x8)
    ClearChrFlags(0x102, 0x8)
    ClearChrFlags(0x9, 0x8)
    SetChrPos(0x102, 6021, 450, 3014, 90)
    SetChrPos(0x9, 9600, 500, -2310, 90)
    SetChrChipByIndex(0x9, 10)
    SetChrFlags(0x9, 0x4)
    SetChrPos(0xA, 10000, 1100, -3300, 0)
    ClearChrFlags(0xA, 0x80)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x54), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_6D(-2924, 0, -6598, 0)
    OP_6C(48000, 0)
    OP_77(0x7, 0x45, 0x91, 0x0, 0x0)
    FadeToBright(500, 0)
    Event(0, 9)
    Jump("loc_436")

    label("loc_3B2")

    OP_A2(0x219)
    RemoveParty(0x1, 0xFF)
    RemoveParty(0x3, 0xFF)
    RemoveParty(0x2, 0xFF)
    RemoveParty(0x6, 0xFF)
    RemoveParty(0x4, 0xFF)
    RemoveParty(0x5, 0xFF)
    RemoveParty(0x7, 0xFF)
    AddParty(0x0, 0xFF)
    OP_31(0x0, 0x0, 0x3)
    OP_37(0x0, 0x0)
    OP_41(0x0, 0xF1)
    OP_41(0x0, 0x1)
    OP_35(0x0, 0x96)
    OP_36(0x0, 0xE6)
    OP_31(0x1, 0x0, 0x3)
    OP_37(0x1, 0x0)
    OP_41(0x1, 0x1F)
    OP_41(0x1, 0xF1)
    OP_35(0x1, 0xA0)
    OP_36(0x1, 0xEB)
    SetMapFlags(0x1000000)
    SetMapFlags(0x800000)
    OP_16(0x0)
    SetChrChipByIndex(0x8, 0)
    SetChrPos(0x8, -6220, 3450, 4390, 180)
    SetChrFlags(0x8, 0x4)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 4)
    Jump("loc_436")

    label("loc_436")

    Return()

    # Function_0_292 end

    def Function_1_437(): pass

    label("Function_1_437")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_44F")
    OP_B1("t0300_y")
    Jump("loc_458")

    label("loc_44F")

    OP_B1("t0300_n")

    label("loc_458")

    OP_16(0x2, 0xFA0, 0xFFFE17B8, 0xFFFDF878, 0x30003)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 3)), scpexpr(EXPR_END)), "loc_490")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_482")
    SetMapFlags(0x800)

    label("loc_482")

    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_1B(0x0, 0x0, 0x2)

    label("loc_490")

    Return()

    # Function_1_437 end

    def Function_2_491(): pass

    label("Function_2_491")

    ClearMapFlags(0x800)
    OP_1B(0x0, 0x0, 0xFFFF)
    Return()

    # Function_2_491 end

    def Function_3_49C(): pass

    label("Function_3_49C")

    EventBegin(0x0)
    OP_6D(-186290, 0, -48440, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    PlayMovie(0x0, "ed6_op.avi")
    OP_56(0x2)
    FadeToDark(2000, 0, -1)
    OP_0D()
    PlayMovie(0x1, "")
    Sleep(2000)
    Call(0, 4)
    Return()

    # Function_3_49C end

    def Function_4_502(): pass

    label("Function_4_502")

    EventBegin(0x0)
    SetChrFlags(0x0, 0x80)
    OP_22(0x1C2, 0x1, 0x64)
    OP_6D(800, -1000, -24180, 0)
    OP_67(0, 5600, -10000, 0)
    OP_6B(4000, 0)
    OP_6C(350000, 0)
    OP_6E(262, 0)
    FadeToBright(2000, 0)

    def lambda_55A():
        OP_6D(4000, 0, -1000, 8000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_55A)

    def lambda_572():
        OP_67(0, 8000, -10000, 8000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_572)

    def lambda_58A():
        OP_6C(45000, 8000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_58A)
    Sleep(8000)

    def lambda_59F():
        OP_6B(3000, 5000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_59F)
    Sleep(2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    SetMapFlags(0x100000)
    NewScene("ED6_DT01/T0310   ._SN", 1, 0, 0)
    IdleLoop()
    Return()

    # Function_4_502 end

    def Function_5_5C8(): pass

    label("Function_5_5C8")

    EventBegin(0x0)
    ClearMapFlags(0x1)
    OP_1F(0x64, 0x3E8)
    SetChrPos(0x101, -1860, 3450, 930, 270)
    SetChrFlags(0x101, 0x40)
    OP_43(0x101, 0x0, 0x0, 0x6)
    OP_43(0x8, 0x0, 0x0, 0x7)
    OP_43(0x9, 0x0, 0x0, 0x8)
    OP_6D(-5250, 3450, 3230, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(4380, 0)
    OP_6C(226000, 0)
    OP_6E(262, 0)

    def lambda_643():
        OP_6C(45000, 10000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_643)

    def lambda_653():
        OP_67(0, 5000, -10000, 10000)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_653)
    Sleep(5000)

    def lambda_670():
        OP_67(0, 6200, -10000, 10000)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_670)
    OP_6B(3000, 10000)
    Sleep(4000)
    OP_70(0x2, 0x3C)
    Sleep(500)
    OP_A2(0x0)
    OP_A5(0x0)
    OP_21()
    OP_44(0x8, 0x1)
    OP_22(0x7B, 0x0, 0x64)
    SetChrChipByIndex(0x101, 5)

    def lambda_6B7():

        label("loc_6B7")

        OP_99(0xFE, 0x0, 0x2, 0x5DC)
        OP_48()
        Jump("loc_6B7")

    QueueWorkItem2(0x101, 1, lambda_6B7)
    SetChrFlags(0x101, 0x2)
    Sleep(2000)
    OP_44(0x101, 0x1)

    ChrTalk(    #0
        0x101,
        (
            "#001FNice, Joshua!\x02\x03",

            "Bravo!\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0)
    ClearChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 65535)
    OP_1D(0x58)
    Fade(250)
    SetChrChipByIndex(0x8, 0)
    SetChrSubChip(0x8, 0)
    OP_0D()
    Sleep(400)
    TurnDirection(0x8, 0x101, 400)

    ChrTalk(    #1
        0x8,
        (
            "#010FGood morning, Estelle.\x02\x03",

            "I hope I didn't wake you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x101,
        (
            "#000FNah, I was already up when I heard\x01",
            "you start to play.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_7A1():
        OP_6D(-5850, 3450, 4410, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7A1)
    OP_8E(0x101, 0xFFFFE7B4, 0xD7A, 0xB2C, 0x7D0, 0x0)
    TurnDirection(0x101, 0x8, 400)
    Sleep(100)
    TurnDirection(0x8, 0x101, 400)

    ChrTalk(    #3
        0x101,
        (
            "#001F#4PI can't believe how awake you are,\x01",
            "though. Even the roosters still have\x01",
            "bags under their eyes!\x02\x03",

            "Not that I mind, what with that siren\x01",
            "song of yours gently lulling this\x01",
            "beautiful woman from her slumber!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x8,
        (
            "#017F#6PWhat do you mean, 'woman'? We're\x01",
            "the same age and I'm hardly a man.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x101,
        (
            "#502F#4PTsk, tsk, tsk.\x01",
            "How wrong you are, Joshua!\x02\x03",

            "We may be the same age, but I\x01",
            "am clearly THE woman of the\x01",
            "house.\x02\x03",

            "And that makes you something\x01",
            "like my loyal follower, wouldn't\x01",
            "you agree?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x8,
        (
            "#010F#6PYeah, yeah.\x01",
            "How fortunate for you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x101,
        (
            "#009F#4PYou could at least try and sound\x01",
            "a TINY bit sincere...\x02\x03",

            "#501FIt really is a nice tune, though.\x01",
            "Cheerful, yet somehow wistful...\x02\x03",

            "I like your other songs too,\x01",
            "of course, but this one's\x01",
            "my favorite.\x02\x03",

            "#505FEr...what's it called again?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x8,
        "#010F#6P'The Whereabouts of Light.'\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x101,
        (
            "#006F#4PThat's right,\x01",
            "'The Whereabouts of Light.'\x02\x03",

            "#007FI wish I could play the harmonica like you,\x01",
            "Joshua.\x02\x03",

            "Sadly, it's a lot harder than it looks...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x8,
        (
            "#010F#6PCompared to what it takes to use a staff,\x01",
            "I think the harmonica is much easier.\x02\x03",

            "#010FIt's really just a matter of concentration.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x101,
        (
            "#506F#4PYou're probably right. I guess my problem\x01",
            "is just that if I don't do something that uses\x01",
            "my whole body, I start to feel drowsy.\x02\x03",

            "#006FOkay, playing the harmonica is fine and all,\x01",
            "but how about getting some exercise, too!\x02\x03",

            "All your hobbies are sitting-around kind of\x01",
            "stuff like reading and music.\x02\x03",

            "#502FNo girl is gonna be impressed with just\x01",
            "that!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x8,
        (
            "#017F#6PWell, excuse me for being so unpopular with the\x01",
            "ladies.\x02\x03",

            "#010FAlthough, I feel like I should be the one lecturing\x01",
            "you about your hobbies.\x02\x03",

            "I mean, what kind of boy wants a girl who loves\x01",
            "fishing, collecting bugs, and has a fetish for sports\x01",
            "shoes?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x101,
        (
            "#007F#4PEr...\x01",
            "...That's enough talk about hobbies for now...\x02\x03",

            "#509FAnd for your information, I graduated from\x01",
            "bug collecting a long time ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x8,
        (
            "#019F#6PReally? I'll believe that when I stop finding\x01",
            "beetles in the hallway.\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x9, -6050, 0, -2610, 0)
    ClearChrFlags(0x9, 0x80)

    NpcTalk(    #15
        0x9,
        "Man's Voice",
        "#1PHey, Estelle! Joshua!\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_A2(0x0)
    OP_A2(0x1)
    OP_6D(-6400, 3450, -400, 1500)

    ChrTalk(    #16
        0x101,
        "#501FMorning, Dad!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x8,
        (
            "#010FGood morning, Dad.\x01",
            "Is breakfast ready?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x9,
        (
            "#080FIt's ready and waiting!\x02\x03",

            "Why don't the both of you hurry on down\x01",
            "before it gets cold?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x101,
        "#006FOkay!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x8,
        "#010FI'm on my way!\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_44(0x101, 0xFF)
    OP_44(0x8, 0xFF)
    OP_44(0x9, 0xFF)
    NewScene("ED6_DT01/T0310   ._SN", 2, 0, 0)
    IdleLoop()
    Return()

    # Function_5_5C8 end

    def Function_6_1106(): pass

    label("Function_6_1106")

    OP_A6(0x0)
    SetChrPos(0x101, -1860, 3450, 930, 270)
    SetChrFlags(0xFE, 0x40)
    OP_8E(0xFE, 0xFFFFF3D0, 0xD7A, 0x3DE, 0x7D0, 0x0)
    ClearChrFlags(0xFE, 0x40)
    OP_A3(0x0)
    OP_A6(0x0)
    TurnDirection(0xFE, 0x9, 400)
    OP_A3(0x0)
    OP_A6(0x0)
    OP_A3(0x0)
    Return()

    # Function_6_1106 end

    def Function_7_114F(): pass

    label("Function_7_114F")

    OP_A6(0x1)
    Sleep(400)
    TurnDirection(0xFE, 0x9, 400)
    OP_A3(0x1)
    OP_A6(0x1)
    OP_A3(0x1)
    Return()

    # Function_7_114F end

    def Function_8_1168(): pass

    label("Function_8_1168")

    Return()

    # Function_8_1168 end

    def Function_9_1169(): pass

    label("Function_9_1169")

    EventBegin(0x0)
    OP_77(0x7, 0x45, 0x91, 0x0, 0x0)
    OP_6B(3000, 0)
    OP_43(0x102, 0x0, 0x0, 0xA)
    OP_43(0x9, 0x0, 0x0, 0xB)
    ClearChrFlags(0x101, 0x80)
    ClearChrFlags(0x101, 0x8)
    SetChrPos(0x101, 0, 0, 0, 0)
    ClearChrFlags(0x102, 0x80)
    ClearChrFlags(0x102, 0x8)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0x9, 0x8)
    OP_A2(0x2)
    OP_6D(7500, 450, 1022, 8000)
    OP_A5(0x2)
    OP_6B(2800, 2000)
    OP_0D()
    OP_70(0x1, 0x3C)
    OP_73(0x1)
    OP_A2(0x1)
    OP_A5(0x1)

    ChrTalk(    #21
        0x102,
        "#010FDad...\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x9, 1)
    Sleep(300)

    ChrTalk(    #22
        0x9,
        "#080FAre you still awake, Joshua?\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1)
    OP_6D(10020, 450, -790, 2000)
    OP_A5(0x1)

    ChrTalk(    #23
        0x102,
        (
            "#010FYou'd better hold off on the\x01",
            "liquor or Estelle will get mad\x01",
            "again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x9,
        (
            "#080FThis is just my way of lifting my spirits\x01",
            "before I travel. How about yourself?\x01",
            "Would you like to join me for a drink?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x102,
        (
            "#018FI'll pass. Actually, what I should\x01",
            "be saying here is: don't offer\x01",
            "alcohol to minors!\x02\x03",

            "#018FI'm not like Schera, who would\x01",
            "jump at any chance to enjoy\x01",
            "a drink or ten.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x9,
        (
            "#080FHa ha...that's because she holds\x01",
            "her liquor much better than I do.\x02\x03",

            "#080F...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x102,
        (
            "#012F...\x02\x03",

            "#012FThere's something really serious\x01",
            "happening, isn't there?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x9,
        (
            "#085FThere's no conclusive evidence,\x01",
            "but there appears to be some sort\x01",
            "of movement within the Empire...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x102,
        (
            "#012FThe Erebonian Empire...?\x02\x03",

            "#012FThat sounds pretty suspicious.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x9,
        (
            "#082FThis movement doesn't appear to\x01",
            "be overt, but that's what has me\x01",
            "worried...\x02\x03",

            "I intend to do a little probing at\x01",
            "the Erebonian embassy to see\x01",
            "what turns up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x102,
        (
            "#010FUnderstood.\x01",
            "I'll make sure to look after\x01",
            "Estelle while you're gone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x9,
        (
            "#080FDon't you spoil that girl,\x01",
            "you hear me?\x02\x03",

            "#080FNow that she's become a bracer,\x01",
            "she needs to learn to look after\x01",
            "herself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x102,
        (
            "#011FEstelle will be fine.\x02\x03",

            "#011FShe's got good instincts, and despite\x01",
            "being a bit rough around the edges,\x01",
            "she has talent with the staff as well.\x02\x03",

            "#011FThere's no doubt in my mind that\x01",
            "she'll be a first-class bracer\x01",
            "someday.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x9,
        (
            "#085FYet at present, she's like a babe in\x01",
            "arms who knows nothing about the\x01",
            "realities of the world around her.\x02\x03",

            "#085FAt some point in time, she'll\x01",
            "have to choose which path to\x01",
            "follow in life.\x02\x03",

            "#082FAnd, Joshua...\x01",
            "The same thing can be said\x01",
            "for you, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x102,
        "#013F...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x9,
        (
            "#085FIt's already been 5 years since\x01",
            "you became a part of this family,\x01",
            "hasn't it?\x02\x03",

            "#085FHow time does fly...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0x102,
        (
            "#015FYes...\x02\x03",

            "#015FIt sure does seem that way.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x9,
        (
            "#082FAbout what you said back then...\x01",
            "Are you sure you won't reconsider\x01",
            "taking those words back?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0x102,
        (
            "#013F...\x02\x03",

            "#013FFor me, keeping my word is\x01",
            "what defines who I am.\x02\x03",

            "#013FIf I can't do something as simple\x01",
            "as that...I don't know how I could\x01",
            "live with myself.\x02\x03",

            "#013FI know this may sound stubborn,\x01",
            "but I can't take back what I said.\x01",
            "I'm sorry...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0x9,
        (
            "#080FThere's no need to apologize...\x02\x03",

            "#080FBut, I'd like you to remember this.\x02\x03",

            "#080FNo matter what path you choose\x01",
            "in life, you can't erase these \x01",
            "past 5 years.\x02\x03",

            "#080FEstelle and I will always be\x01",
            "your family.\x02\x03",

            "#080FNo matter what may befall you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0x102,
        (
            "#013F*nod*\x02\x03",

            "#013F...\x02\x03",

            "#019FThanks...Dad...\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_44(0x9, 0xFF)
    OP_20(0x9C4)
    ClearMapFlags(0x2000000)
    NewScene("ED6_DT01/T0700   ._SN", 1, 0, 0)
    IdleLoop()
    Return()

    # Function_9_1169 end

    def Function_10_1BD6(): pass

    label("Function_10_1BD6")

    OP_A6(0x1)
    OP_8E(0xFE, 0x212C, 0x1C2, 0xAB5, 0x7D0, 0x0)
    TurnDirection(0xFE, 0x9, 400)
    OP_A3(0x1)
    OP_A6(0x1)
    OP_8E(0xFE, 0x2710, 0x1C2, 0xFFFFFF56, 0x7D0, 0x0)
    TurnDirection(0xFE, 0x9, 400)
    OP_A3(0x1)
    Return()

    # Function_10_1BD6 end

    def Function_11_1C19(): pass

    label("Function_11_1C19")

    OP_A6(0x2)
    OP_6C(315000, 8000)
    OP_A3(0x2)
    OP_A6(0x2)
    OP_A3(0x2)
    Return()

    # Function_11_1C19 end

    def Function_12_1C2F(): pass

    label("Function_12_1C2F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1CBA")
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #42
        (
            "\x07\x05Looking a little closer,\x01",
            "there's something written on it.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("")

    AnonymousTalk(    #43
        "\x07\x05'Stupid Joshua!'\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    Jump("loc_1D0D")

    label("loc_1CBA")

    OP_A2(0x3)
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #44
        "\x07\x05There's a standing log for staff practice.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)

    label("loc_1D0D")

    TalkEnd(0xFF)
    Return()

    # Function_12_1C2F end

    def Function_13_1D11(): pass

    label("Function_13_1D11")

    OP_A2(0x4)
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #45
        "\x07\x05There's a standing log for staff practice.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_13_1D11 end

    def Function_14_1D68(): pass

    label("Function_14_1D68")

    OP_A2(0x5)
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #46
        "\x07\x05There's a standing log for staff practice.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_14_1D68 end

    SaveToFile()

Try(main)

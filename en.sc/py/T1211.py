from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 柏斯

    CreateScenaFile(
        FileName            = 'T1211   ._SN',
        MapName             = 'Bose',
        Location            = 'T1211.x',
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
        'Agate',                                # 9
        'Tita',                                 # 10
        'Agate',                                # 11
        'Pot',                                  # 12
        'Tita',                                 # 13
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
        'ED6_DT07/CH00050 ._CH',             # 00
        'ED6_DT07/CH00060 ._CH',             # 01
        'ED6_DT26/CH20365 ._CH',             # 02
        'ED6_DT26/CH20351 ._CH',             # 03
        'ED6_DT26/CH20350 ._CH',             # 04
        'ED6_DT26/CH20366 ._CH',             # 05
        'ED6_DT26/CH20206 ._CH',             # 06
        'ED6_DT26/CH20205 ._CH',             # 07
        'ED6_DT26/CH20425 ._CH',             # 08
        'ED6_DT26/CH20455 ._CH',             # 09
    )

    AddCharChipPat(
        'ED6_DT07/CH00050P._CP',             # 00
        'ED6_DT07/CH00060P._CP',             # 01
        'ED6_DT26/CH20365P._CP',             # 02
        'ED6_DT26/CH20351P._CP',             # 03
        'ED6_DT26/CH20350P._CP',             # 04
        'ED6_DT26/CH20366P._CP',             # 05
        'ED6_DT26/CH20206P._CP',             # 06
        'ED6_DT26/CH20205P._CP',             # 07
        'ED6_DT26/CH20425P._CP',             # 08
        'ED6_DT26/CH20455P._CP',             # 09
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x185,
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
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x185,
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
        Unknown3            = 8,
        ChipIndex           = 0x8,
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
        NpcIndex            = 0x185,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    ScpFunction(
        "Function_0_19A",          # 00, 0
        "Function_1_1D6",          # 01, 1
        "Function_2_1DE",          # 02, 2
        "Function_3_1DD3",         # 03, 3
        "Function_4_3778",         # 04, 4
    )


    def Function_0_19A(): pass

    label("Function_0_19A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_1B9")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x53), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x10F0)
    SetMapFlags(0x10000000)
    Event(0, 2)
    Jump("loc_1D5")

    label("loc_1B9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 1)), scpexpr(EXPR_END)), "loc_1D5")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x50), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x10F1)
    SetMapFlags(0x10000000)
    Event(0, 3)

    label("loc_1D5")

    Return()

    # Function_0_19A end

    def Function_1_1D6(): pass

    label("Function_1_1D6")

    OP_B1("T1211")
    Return()

    # Function_1_1D6 end

    def Function_2_1DE(): pass

    label("Function_2_1DE")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    OP_6D(-25200, 0, 47910, 0)
    OP_67(0, 6150, -10000, 0)
    OP_6B(2850, 0)
    OP_6C(315000, 0)
    OP_6E(280, 0)
    SetChrPos(0x8, -24200, 400, 47000, 0)
    OP_9F(0x9, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x9, -28470, 0, 41130, 270)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    OP_9F(0x9, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x9, 7)
    SetChrSubChip(0x9, 0)
    SetChrFlags(0x8, 0x2)
    SetChrChipByIndex(0x8, 2)
    SetChrSubChip(0x8, 0)
    SetChrFlags(0x8, 0x4)
    OP_6F(0x0, 10)
    SetChrPos(0xB, -29470, 700, 41170, 0)
    ClearChrFlags(0xB, 0x80)
    LoadEffect(0x0, "map\\\\onsen00.eff")
    OP_C5(0x0, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS106._CH")
    OP_C5(0x1, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS192._CH")
    OP_C5(0x2, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS193._CH")
    OP_C5(0x3, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS194._CH")
    Sleep(1000)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("Girl's Voice")

    AnonymousTalk(    #0
        (
            "\x07\x0CHey, Agate!\x02\x03",

            "Agate, c'mon...!\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(500)
    OP_C6(0x0, 0x4, 0, 0, 0)
    OP_C6(0x0, 0x3, -1, 1500, 0)
    Sleep(2000)
    SetMessageWindowPos(320, 260, -1, -1)
    SetChrName("Red-Haired Girl")

    AnonymousTalk(    #1
        (
            "\x07\x0CHeehee, are you looking forward to\x01",
            "your birthday?\x02\x03",

            "I've got a preeeesent that I'm sure'll\x01",
            "make you super-duper happy! ♪\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(50, 300, -1, -1)
    SetChrName("Red-Haired Boy")

    AnonymousTalk(    #2
        (
            "\x07\x0CHuh... Somethin' I'll like, huh?\x02\x03",

            "You gonna make something tasty for me?\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(320, 260, -1, -1)
    SetChrName("Red-Haired Girl")

    AnonymousTalk(    #3
        (
            "\x07\x0CWhat, noooo! Why would you think of food\x01",
            "when I mention a birthday present?!\x02\x03",

            "Presents should be things that last, y'know?\x01",
            "Something you treasure forever!\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(50, 300, -1, -1)
    SetChrName("Red-Haired Boy")

    AnonymousTalk(    #4
        (
            "\x07\x0CYou really think so?\x02\x03",

            "Something that'll last and\x01",
            "that I'll treasure...\x02\x03",

            "Hey, maybe a hunting knife or something?\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(320, 260, -1, -1)
    SetChrName("Red-Haired Girl")

    AnonymousTalk(    #5
        (
            "\x07\x0CYou just GOT a hunting knife from\x01",
            "the village elder, dummy!\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_C6(0x1, 0x4, 0, 0, 0)
    OP_C6(0x1, 0x3, -1, 500, 0)
    Sleep(500)
    SetMessageWindowPos(320, 260, -1, -1)
    SetChrName("Red-Haired Girl")

    AnonymousTalk(    #6
        (
            "\x07\x0CThe answer is...an ACCESSORY!\x01",
            "Handmade by yooours truly!\x02\x03",

            "It's, um, not done yet, though.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(50, 300, -1, -1)
    SetChrName("Red-Haired Boy")

    AnonymousTalk(    #7
        (
            "\x07\x0CWh-Whoa, hey!\x02\x03",

            "An 'accessory'? Like, what kind of accessory?\x01",
            "I'm not a girl, y'know!\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_C6(0x0, 0x4, 0, 0, 0)
    OP_C6(0x0, 0x3, 16777215, 0, 0)
    OP_C6(0x0, 0x3, -1, 500, 0)
    Sleep(500)
    SetMessageWindowPos(320, 260, -1, -1)
    SetChrName("Red-Haired Girl")

    AnonymousTalk(    #8
        (
            "\x07\x0CC'mon, Agate! You're so boring!\x02\x03",

            "Even boys can be stylish and cute if they have\x01",
            "some kind of accessory!\x02\x03",

            "If you have one, Agate, even a stick in the mud\x01",
            "like you will get aaaaaalllllll the ladies! ♪\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(50, 300, -1, -1)
    SetChrName("Red-Haired Boy")

    AnonymousTalk(    #9
        "\x07\x0CHey, c'mon, knock it off...\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_C6(0x2, 0x4, 0, 0, 0)
    OP_C6(0x2, 0x3, 16777215, 0, 0)
    OP_C6(0x2, 0x3, -1, 500, 0)
    Sleep(500)
    SetMessageWindowPos(320, 260, -1, -1)
    SetChrName("Red-Haired Girl")

    AnonymousTalk(    #10
        (
            "\x07\x0CDo you...um...really not want it?\x02\x03",

            "You've always taken care of me,\x01",
            "so I wanted to give something back...\x02\x03",

            "I've been working really hard to make it,\x01",
            "but if it's really not something you'd\x01",
            "like...\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(50, 300, -1, -1)
    SetChrName("Red-Haired Boy")

    AnonymousTalk(    #11
        (
            "\x07\x0CErk...\x02\x03",

            "Just...don't make it too cute\x01",
            "or flashy, okay?!\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_C6(0x0, 0x4, 0, 0, 0)
    OP_C6(0x0, 0x3, 16777215, 0, 0)
    OP_C6(0x0, 0x3, -1, 500, 0)
    Sleep(500)
    SetMessageWindowPos(320, 260, -1, -1)
    SetChrName("Red-Haired Girl")

    AnonymousTalk(    #12
        (
            "\x07\x0CHeehee! Don't worry.\x02\x03",

            "It's simple but cool.\x01",
            "It'll fit you perfectly, Agate, I promise!\x02\x03",

            "Especially since you're so tall!\x01",
            "Yeah, it'll be perfect, I bet.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(50, 300, -1, -1)
    SetChrName("Red-Haired Boy")

    AnonymousTalk(    #13
        (
            "\x07\x0CYeah, I get it, I get it.\x02\x03",

            "You've got me all curious now, so just...\x01",
            "make it good, okay?\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_C6(0x1, 0x4, 0, 0, 0)
    OP_C6(0x1, 0x3, 16777215, 0, 0)
    OP_C6(0x1, 0x3, -1, 500, 0)
    Sleep(500)
    SetMessageWindowPos(320, 260, -1, -1)
    SetChrName("Red-Haired Girl")

    AnonymousTalk(    #14
        (
            "\x07\x0CAhaha, I will!\x02\x03",

            "Hey...Agate?\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(50, 300, -1, -1)
    SetChrName("Agate")

    AnonymousTalk(    #15
        "\x07\x0CWhat is it, Mischa?\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_C6(0x3, 0x4, 0, 0, 0)
    OP_C6(0x3, 0x3, 16777215, 0, 0)
    OP_C6(0x3, 0x3, -1, 500, 0)
    Sleep(500)
    SetMessageWindowPos(320, 260, -1, -1)
    SetChrName("Mischa")

    AnonymousTalk(    #16
        (
            "\x07\x0CI just want to say...thank you. So much.\x02\x03",

            "For always being my big brother...\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C6(0x0, 0x3, 16777215, 0, 0)
    OP_C6(0x1, 0x3, 16777215, 0, 0)
    OP_C6(0x2, 0x3, 16777215, 0, 0)
    OP_C6(0x3, 0x3, 16777215, 1000, 0)
    FadeToDark(2000, 16777215, -1)
    OP_0D()
    OP_C7(0x0, 0x3, 0x3)
    OP_C6(0x0, 0x6, 0, 0, 0)
    OP_C6(0x1, 0x6, 0, 0, 0)
    OP_C6(0x2, 0x6, 0, 0, 0)
    OP_C6(0x3, 0x6, 0, 0, 0)
    Sleep(3000)
    PlayEffect(0x0, 0x0, 0xB, 300, 400, -300, 0, 0, 0, 300, 200, 300, 0xFF, 0, 0, 0, 0)
    FadeToBright(2000, 16777215)
    OP_0D()
    Sleep(500)
    OP_99(0x8, 0xA, 0xB, 0x3E8)
    Sleep(500)

    ChrTalk(    #17
        0x8,
        "#1281F#6PWh...\x02",
    )

    CloseMessageWindow()
    OP_62(0x8, 0x258, 1400, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_63(0x8)
    OP_99(0x8, 0xB, 0xA, 0x3E8)
    Sleep(100)
    SetChrSubChip(0x8, 0)
    Sleep(500)

    ChrTalk(    #18
        0x8,
        "#1282F#6P...A dream, huh?\x02",
    )

    CloseMessageWindow()
    OP_99(0x8, 0xA, 0xB, 0x3E8)
    Sleep(100)
    SetChrSubChip(0x8, 15)
    Sleep(500)

    ChrTalk(    #19
        0x8,
        "#1289F#6PThis is...\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #20
        0x9,
        "Girl's Voice",
        "#2PYeah, this should be good.\x02",
    )

    CloseMessageWindow()
    OP_9F(0x9, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
    OP_62(0x8, 0x258, 1400, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    SetChrSubChip(0x8, 11)
    Sleep(100)
    SetChrSubChip(0x8, 12)

    ChrTalk(    #21
        0x8,
        "#1281F#4PMischa...?\x02",
    )

    CloseMessageWindow()
    OP_6D(-27180, 0, 44810, 2000)
    OP_62(0x9, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    TurnDirection(0x9, 0x8, 400)

    ChrTalk(    #22
        0x9,
        (
            "#1264F#5PAgate!\x02\x03",

            "#1261FOh, thank Aidios, you're awake!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_F6C():
        OP_8E(0xFE, 0xFFFF9C78, 0x0, 0xB644, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_F6C)

    def lambda_F87():
        OP_6D(-25360, 0, 48370, 2000)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_F87)
    WaitChrThread(0x9, 0x1)
    OP_8C(0x9, 90, 400)
    WaitChrThread(0x9, 0x2)

    ChrTalk(    #23
        0x8,
        "#1281F#4PShortstuff...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x9,
        (
            "#1263F#6PH-How are your injuries?\x01",
            "Do you feel okay?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x8,
        "#1280F#4PPffff, yeah, this is no--\x02",
    )

    CloseMessageWindow()
    OP_B0(0x0, 0xA)
    OP_6F(0x0, 10)
    OP_70(0x0, 0x28)
    OP_99(0x8, 0x0, 0x4, 0x384)
    OP_9E(0x8, 0x14, 0x0, 0x12C, 0xBB8)
    Sleep(500)

    ChrTalk(    #26
        0x8,
        "#1285F#4PGhk...!\x02",
    )

    OP_99(0x8, 0x7, 0x9, 0x4B0)
    CloseMessageWindow()
    OP_62(0x9, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_62(0x9, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)

    ChrTalk(    #27
        0x9,
        (
            "#1265F#6PN-No, don't move! You need to sleep!\x02\x03",

            "Your wounds aren't healed at all yet!\x02",
        )
    )

    CloseMessageWindow()
    OP_B0(0x0, 0xF)
    OP_6F(0x0, 40)
    OP_70(0x0, 0x3C)
    OP_99(0x8, 0x9, 0x7, 0x3E8)
    OP_99(0x8, 0x4, 0x6, 0x3E8)
    Sleep(500)

    ChrTalk(    #28
        0x8,
        (
            "#1280F#4PHeh, c'mon. Stuff like this ain't a big deal.\x02\x03",

            "They'll heal fine even if you ignore 'em--\x02",
        )
    )

    CloseMessageWindow()
    SetChrFlags(0x9, 0x2)
    SetChrChipByIndex(0x9, 9)
    SetChrSubChip(0x9, 0)
    OP_99(0x9, 0x0, 0x1, 0x7D0)
    Sleep(250)

    ChrTalk(    #29
        0x9,
        "#1268F#6P#3SN-NO!\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    Sleep(100)
    Fade(250)
    SetChrSubChip(0x9, 5)
    OP_0D()
    Sleep(250)
    OP_99(0x9, 0x5, 0x3, 0x5DC)
    Sleep(500)

    ChrTalk(    #30
        0x9,
        (
            "#1262F#6PI promised Estelle!\x02\x03",

            "I promised I wouldn't let you out of bed\x01",
            "until you were better!\x02",
        )
    )

    CloseMessageWindow()
    OP_99(0x8, 0x12, 0x14, 0x4B0)
    Sleep(250)

    ChrTalk(    #31
        0x8,
        "#1281F#4PH-Hey...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x9,
        "#1262F#6PNo. Nnno. Nnnnnnnnnno.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x8,
        "#1284F#4PI get it, I get it, already!\x02",
    )

    CloseMessageWindow()
    OP_99(0x8, 0x14, 0x12, 0x3E8)
    Sleep(100)
    OP_6F(0x0, 30)
    OP_70(0x0, 0xA)
    OP_99(0x8, 0x6, 0x0, 0x3E8)
    Sleep(800)

    ChrTalk(    #34
        0x9,
        "#1271F#6PPhew!\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(250)
    ClearChrFlags(0x9, 0x2)
    SetChrChipByIndex(0x9, 7)
    SetChrSubChip(0x9, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #35
        0x8,
        (
            "#1282F#4PSheesh. Gettin' all worked up over\x01",
            "a bunch'a scratches...\x02",
        )
    )

    CloseMessageWindow()
    OP_99(0x8, 0xA, 0xB, 0x4B0)
    OP_99(0x8, 0xB, 0xC, 0x4B0)
    Sleep(300)

    ChrTalk(    #36
        0x8,
        (
            "#1281F#4PHoly crap, it's nighttime already.\x02\x03",

            "Where the heck is everyone?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0x9,
        (
            "#1260F#6PThey all went back to the city for\x01",
            "a while.\x02\x03",

            "They made some kind of promise\x01",
            "with General Morgan, I think.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x8,
        "#1284F#4PA promise with MORGAN?!\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #39
        "\x07\x05Tita conveyed Estelle's message to Agate.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(    #40
        0x8,
        (
            "#1280F#4PAh, I see.\x01",
            "So they got Morgan moving, did they?\x02\x03",

            "The guild oughtta be hearin' from the\x01",
            "army right about now, in that case.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x8, 11)
    Sleep(500)

    ChrTalk(    #41
        0x8,
        "#1283F#4PWell hell, I can't just--\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0x9,
        "#1262F#6P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0x8,
        (
            "#1288F#4P...'stay here' is what I wanna say, but on\x01",
            "the other hand, it IS pretty late tonight.\x02\x03",

            "#1280FWe'll get out to Bose tomorrow morning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0x9,
        "#1265F#6PBut-!\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x8, 12)
    Sleep(300)

    ChrTalk(    #45
        0x8,
        (
            "#1280F#4PLook, I've had a good, long rest.\x01",
            "I'm seriously feeling better.\x02\x03",

            "These really are just scratches.\x01",
            "They'll heal up even if I'm workin' hard.\x02\x03",

            "I'm fine, don't worry.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0x9,
        "#1263F#6PYou're sure you're not forcing yourself?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x8,
        (
            "#1293F#4PHey, give the veteran bracer a little bit\x01",
            "of credit, here.\x02\x03",

            "I ain't so crazy as to go overboard on stuff\x01",
            "like dragons or the society twice.\x02\x03",

            "#1289F...I can't keep puttin' you in danger,\x01",
            "either.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0x9,
        "#1264F#6POh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0x8,
        (
            "#1280F#4PPoint is, I sure don't have the guts to\x01",
            "anger my scary little nursemaid.\x02\x03",

            "Trust me a little, here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0x9,
        (
            "#1271F#6POoooh, Agate...\x02\x03",

            "#1260FI guess you do look a lot better, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0x8,
        (
            "#1280F#4PTold you, didn't I?\x02\x03",

            "I know my limits better than anyone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0x9,
        (
            "#1266F#6PHeehee... That's good...\x02\x03",

            "#1269F...Nnn...\x02",
        )
    )

    CloseMessageWindow()
    SetChrFlags(0x9, 0x2)
    SetChrChipByIndex(0x9, 4)
    SetChrSubChip(0x9, 0)
    OP_99(0x9, 0x0, 0x6, 0x3E8)
    OP_62(0x8, 0x258, 1400, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #53
        0x8,
        "#1284F#4PHey, what's wrong?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0x9,
        "#1272F#6P*sniffle*... *hic*...\x02",
    )

    CloseMessageWindow()
    OP_B0(0x0, 0xA)
    OP_6F(0x0, 10)
    OP_70(0x0, 0x3C)
    OP_99(0x8, 0x0, 0x6, 0x5DC)
    OP_99(0x8, 0x12, 0x14, 0x5DC)
    OP_62(0x8, 0x0, 1600, 0x28, 0x2B, 0x64, 0x3)

    ChrTalk(    #55
        0x8,
        (
            "#1284F#4PI said I'm okay! Really!\x02\x03",

            "I swear to the Goddess, I ain't lyin'!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0x9,
        (
            "#1272F#6P*sniffle* N-No, that's not it...\x02\x03",

            "I'm so relieved... It's just so...so...\x02\x03",

            "#1269FUuuuu-wa...\x02",
        )
    )

    CloseMessageWindow()
    OP_99(0x9, 0x7, 0xB, 0x3E8)
    Sleep(300)

    ChrTalk(    #57
        0x9,
        "#1268F#6P#4SWAAAAAAAAAAAAAAAH!\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)

    def lambda_1B05():

        label("loc_1B05")

        OP_99(0xFE, 0xB, 0xD, 0x3E8)
        OP_48()
        Jump("loc_1B05")

    QueueWorkItem2(0x9, 1, lambda_1B05)
    CloseMessageWindow()

    ChrTalk(    #58
        0x8,
        (
            "#1288F#4PErk...\x02\x03",

            "#1290FC'mon, shortstuff, calm down.\x01",
            "I get it, I get it.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(800)
    SetChrPos(0x8, -25540, 0, 46100, 270)
    ClearChrFlags(0x8, 0x2)
    SetChrChipByIndex(0x8, 6)
    SetChrSubChip(0x8, 0)
    OP_B0(0x0, 0xF)
    OP_6F(0x0, 20)
    OP_70(0x0, 0xA)
    OP_6D(-26020, 0, 47720, 1000)
    OP_0D()
    OP_8C(0x8, 0, 400)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x2)
    OP_44(0x9, 0x1)
    SetChrSubChip(0x9, 16)
    Sleep(1000)
    OP_99(0x9, 0x11, 0x16, 0x3E8)

    def lambda_1BDD():

        label("loc_1BDD")

        OP_99(0xFE, 0x16, 0x12, 0x3E8)
        OP_48()
        Jump("loc_1BDD")

    QueueWorkItem2(0x9, 1, lambda_1BDD)
    Sleep(500)

    ChrTalk(    #59
        0x8,
        (
            "#1290F#6PI'm sorry, Tita.\x01",
            "I guess I made you worry pretty bad, huh?\x02\x03",

            "After charging off alone, I get broken\x01",
            "like a twig in a fight I had no chance\x01",
            "of winning...\x02\x03",

            "And then, on top of all that, I made you\x01",
            "do that crazy thing to protect me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0x9,
        "#1269F#4PY-Y-Y-Yeah! *sniffle* Agate, you dummy!\x02",
    )

    CloseMessageWindow()
    OP_44(0x9, 0x1)
    OP_99(0x9, 0x17, 0x1F, 0x5DC)
    Sleep(300)

    ChrTalk(    #61
        0x9,
        (
            "#1272F#4PI was so worried and I saw you get hurt and,\x01",
            "and...!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0x8,
        (
            "#1290F#6PYeah, you're right...\x02\x03",

            "#1291FI really am a complete idiot.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_0D()
    ClearMapFlags(0x2000000)
    OP_A2(0x10F6)
    NewScene("ED6_DT21/E0811   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_2_1DE end

    def Function_3_1DD3(): pass

    label("Function_3_1DD3")

    EventBegin(0x0)
    OP_DB()
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    OP_6D(-26550, 0, 42500, 0)
    OP_67(0, 5150, -10000, 0)
    OP_6B(2850, 0)
    OP_6C(315000, 0)
    OP_6E(280, 0)
    SetChrPos(0x8, -25540, 0, 46100, 0)
    SetChrFlags(0x8, 0x80)
    SetChrChipByIndex(0x8, 6)
    SetChrSubChip(0x8, 0)
    SetChrPos(0xB, -29470, 700, 41170, 0)
    ClearChrFlags(0xB, 0x80)
    LoadEffect(0x0, "map\\\\onsen00.eff")
    PlayEffect(0x0, 0x0, 0xB, 300, 400, -300, 0, 0, 0, 300, 200, 300, 0xFF, 0, 0, 0, 2000)
    SetChrPos(0x9, -25480, 0, 46660, 180)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x40)
    SetChrFlags(0x9, 0x2)
    SetChrChipByIndex(0x9, 4)
    SetChrSubChip(0x9, 31)
    OP_6F(0x0, 5)

    def lambda_1ED7():
        OP_6D(-26020, 0, 47720, 4000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1ED7)

    def lambda_1EEF():
        OP_67(0, 6150, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1EEF)
    FadeToBright(1000, 0)
    OP_0D()
    WaitChrThread(0x101, 0x1)
    Sleep(500)
    OP_DC()

    ChrTalk(    #63
        0x9,
        "#1271F#4P*sniffle*...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0x8,
        "#1290F#6PFeel a bit calmer now?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0x9,
        "#1271F#4PMm-hmm.\x02",
    )

    CloseMessageWindow()
    OP_99(0x9, 0x1F, 0x23, 0x320)
    Sleep(500)

    ChrTalk(    #66
        0x9,
        "#1263F#4PI-I'm sorry. I didn't mean to cry like that.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0x8,
        (
            "#1288F#6PEesh. You sure know how to shock a guy,\x01",
            "you know that?\x02\x03",

            "That whole thing sent shivers down my spine\x01",
            "way worse than when I fought that silver-\x01",
            "haired idiot.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0x9,
        (
            "#1267F#4P*sniffle* Ahaha...\x02\x03",

            "#1264FOh, yeah...\x02",
        )
    )

    CloseMessageWindow()
    OP_99(0x9, 0x23, 0x21, 0x320)
    Sleep(300)

    ChrTalk(    #69
        0x9,
        (
            "#1260F#4PUm, Agate, are you hungry?\x02\x03",

            "I made some soup with some things\x01",
            "the village elder left!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0x8,
        (
            "#1280F#6PAhh, that's what smelled so good.\x01",
            "Right on.\x02\x03",

            "#1281F...Wait, hold on.\x02\x03",

            "Why's the kitchen...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0x9,
        "#1264F#4PHuh?\x02",
    )

    CloseMessageWindow()
    Fade(500)
    ClearChrFlags(0x9, 0x2)
    SetChrChipByIndex(0x9, 7)
    SetChrSubChip(0x9, 0)
    ClearChrFlags(0x8, 0x80)
    SetChrChipByIndex(0x8, 6)
    SetChrSubChip(0x8, 0)
    OP_0D()

    def lambda_21AC():
        OP_6D(-27810, 0, 45350, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_21AC)
    OP_8C(0x8, 270, 400)
    OP_8C(0x8, 180, 400)
    Sleep(1000)
    OP_8E(0x8, 0xFFFF9AB6, 0x0, 0xAD8E, 0x3E8, 0x0)
    Sleep(500)
    OP_8C(0x8, 90, 400)
    Sleep(500)
    OP_8C(0x8, 270, 400)
    Sleep(1000)

    ChrTalk(    #72
        0x8,
        (
            "#1284F#5PLemme look... Oh, you gotta be kidding me.\x02\x03",

            "There's a few spots that're a little different,\x01",
            "but it looks just like it did back then.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_229B():

        label("loc_229B")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_229B")

    QueueWorkItem2(0x9, 1, lambda_229B)
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_22C8():
        OP_6D(-26430, 0, 47750, 2000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_22C8)
    OP_8C(0x8, 0, 400)
    Sleep(1000)
    OP_8E(0x8, 0xFFFF993A, 0x0, 0xB75C, 0x3E8, 0x0)
    WaitChrThread(0x0, 0x1)
    Sleep(500)

    ChrTalk(    #73
        0x8,
        (
            "#1290F#6PAnd there's somethin' like this, too...\x02\x03",

            "#1291FHeh...I'm amazed it survived.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0x9,
        "#1264F#4PHuuuuh?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x9, 400)
    Sleep(500)

    ChrTalk(    #75
        0x8,
        (
            "#1290F#6POh, right, I'm probably losing you, aren't I?\x02\x03",

            "My place actually burned down ten years ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0x9,
        "#1270F#4PYou mean...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0x8,
        (
            "#1282F#6POne of those incendiary shells from the\x01",
            "Imperials hit it dead on.\x02\x03",

            "It caught fire instantly and burned down\x01",
            "straight to the foundations.\x02\x03",

            "#1289FI'd heard the village elder was his usual nutty\x01",
            "self and had it rebuilt, but...\x02\x03",

            "Didn't think they'd try to put the furniture\x01",
            "and decorations back together, even.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0x9,
        "#1265F#4P...\x02",
    )

    CloseMessageWindow()
    OP_8C(0x8, 180, 400)
    Sleep(500)

    ChrTalk(    #79
        0x8,
        (
            "#1280F#6PI never could bring myself to come in\x01",
            "here before.\x02\x03",

            "Guess I really gotta tell them thanks,\x01",
            "given how much they did.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0x9,
        (
            "#1265F#4P...\x02\x03",

            "So, um, then...\x02\x03",

            "That's when...Mischa...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0x8,
        (
            "#1282F#6P...\x02\x03",

            "#1290FHah. Secret's out, huh?\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x8, 90, 300)

    def lambda_2661():
        OP_6D(-26720, 0, 47740, 2000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_2661)
    OP_8F(0x8, 0xFFFF97E6, 0x0, 0xB6A8, 0x1F4, 0x0)
    OP_44(0x9, 0x1)
    Fade(1000)
    SetChrFlags(0x8, 0x2)
    SetChrChipByIndex(0x8, 3)
    SetChrSubChip(0x8, 0)
    SetChrPos(0x8, -26500, 0, 46620, 90)
    OP_0D()
    Sleep(500)
    OP_99(0x8, 0x0, 0x2, 0x320)
    Sleep(500)

    ChrTalk(    #82
        0x8,
        (
            "#1282F#6PShe was makin' me a present for my birthday.\x02\x03",

            "It was a handmade...accessory of some kind\x01",
            "that she thought'd look good on me.\x02\x03",

            "When we were fleein' for the mountains,\x01",
            "she ran back to the house to get it.\x02\x03",

            "And that's when the house was hit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0x9,
        "#1263F#4P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0x8,
        (
            "#1289F#6PWhen they finally pulled her out, she was...\x01",
            "burned pretty badly, let's put it that way.\x02\x03",

            "And even after everything she suffered, she still\x01",
            "had that present clutched in her hands.\x02\x03",

            "The metal parts were hopelessly melted,\x01",
            "but the stones were still okay.\x02\x03",

            "#1290FTake a look.\x02",
        )
    )

    CloseMessageWindow()
    OP_99(0x8, 0x2, 0x4, 0x320)
    Sleep(300)
    OP_99(0x8, 0x4, 0x7, 0x320)
    Sleep(500)

    ChrTalk(    #85
        0x9,
        "#1270F#4PIt's pretty...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #86
        0x8,
        (
            "#1290F#6PThey ain't even septium, ain't even valuable.\x01",
            "Just some pretty rocks.\x02\x03",

            "Probably somethin' she found down by the river.\x02\x03",

            "#1282FI've lost count of the number of times\x01",
            "I've thought, 'All for this?'\x02\x03",

            "S'funny, though, you know?\x01",
            "I can't blame her or get angry at her for it.\x02",
        )
    )

    CloseMessageWindow()
    OP_99(0x8, 0x7, 0x9, 0x320)
    Sleep(500)

    ChrTalk(    #87
        0x8,
        (
            "#1289F#6PI never intended for it to be a memento\x01",
            "of her.\x02\x03",

            "When I left the village, though, it was the\x01",
            "only thing I couldn't part with.\x01",
            "Even when I became a Raven down in Ruan.\x02\x03",

            "#1290FHaha. Pretty pathetic for a thug, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0x9,
        "#1262F#4PNo, not at all!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0x8,
        (
            "#1282F#6PNo. It's pretty damn pathetic.\x02\x03",

            "Long as I could hold on to this,\x01",
            "I could also hold on to my anger.\x02\x03",

            "#1286FMy anger at myself, my anger at the worthless,\x01",
            "spineless son of a bitch who couldn't even save\x01",
            "his own sister.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0x9,
        "#1265F#4PBut-!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0x8,
        (
            "#1289F#6PI ended up puttin' all that pent-up rage\x01",
            "into every swing of my sword.\x02\x03",

            "So long as I did that, I could at least\x01",
            "look like I was keepin' it together.\x02\x03",

            "#1291F...A half-baked man trapped by rage and\x01",
            "self-deception and unable to move on.\x02\x03",

            "Heheh. It's exactly like that bastard said.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0x9,
        "#1263F#4PAgate...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0x8,
        (
            "#1280F#6PNah. It's worse, ain't it?\x02\x03",

            "I'm just a piece of shit who runs away\x01",
            "from anything painful.\x02\x03",

            "I'm the thing I hate most.\x01",
            "A goddamned loser of a dog runnin'\x01",
            "around with my tail between my legs.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #94
        0x8,
        (
            "#1292F#6P#3SHa-ha-ha...\x01",
            "I'm pathetic! Absolutely pathetic!\x02",
        )
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()

    ChrTalk(    #95
        0x9,
        (
            "#1263F#4PAgate...I...\x02\x03",

            "#1271F...\x02",
        )
    )

    CloseMessageWindow()
    OP_20(0x7D0)

    def lambda_2EE1():
        OP_6D(-26900, 0, 47740, 2000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_2EE1)
    OP_8E(0x9, 0xFFFF9AA2, 0x0, 0xB644, 0x1F4, 0x0)
    SetChrPos(0x9, -26480, 0, 46610, 270)
    SetChrPos(0xC, -25950, 0, 46610, 270)
    SetChrFlags(0x9, 0x8000)
    SetChrFlags(0x9, 0x2)
    SetChrChipByIndex(0x9, 3)
    SetChrSubChip(0x9, 48)
    OP_99(0x9, 0x30, 0x32, 0x3E8)
    OP_1D(0x76)
    Sleep(500)

    ChrTalk(    #96
        0xC,
        (
            "#1271F#4PI, um...don't really understand how you\x01",
            "feel, Agate...\x02\x03",

            "I don't think I can really try to understand\x01",
            "what makes you feel so hurt.\x02\x03",

            "#1262FBut. I think I need to say something.\x01",
            "In Mischa's place.\x02",
        )
    )

    CloseMessageWindow()
    OP_99(0x8, 0xA, 0xB, 0x3E8)

    ChrTalk(    #97
        0x8,
        "#1281F#6PHm?\x02",
    )

    CloseMessageWindow()
    Fade(500)

    def lambda_3043():
        OP_6B(2700, 500)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_3043)
    OP_0D()

    ChrTalk(    #98
        0xC,
        (
            "#1268F#4P#3S...Don't you DARE make fun of\x01",
            "my big brother!\x02",
        )
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    Sleep(300)

    ChrTalk(    #99
        0xC,
        (
            "#1274F#4PYou don't know the first THING about what\x01",
            "makes my brother such a good guy!\x02\x03",

            "I know my brother better than anyone else!\x02\x03",

            "#1268FI won't let anyone talk badly about my\x01",
            "brother, even if it's you yourself!\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x8, 0xFFFFFF6A, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)

    ChrTalk(    #100
        0x8,
        "#1284F#6PWh--\x02",
    )

    CloseMessageWindow()

    def lambda_31AB():
        OP_6D(-27000, 0, 47520, 1500)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_31AB)
    OP_99(0x9, 0x33, 0x37, 0x4B0)

    def lambda_31CC():
        OP_99(0x9, 0x38, 0x3B, 0x4B0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_31CC)

    def lambda_31DC():
        OP_99(0x8, 0x18, 0x1B, 0x4B0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_31DC)
    WaitChrThread(0x0, 0x1)
    Sleep(500)

    ChrTalk(    #101
        0x8,
        "#1281F#6PHuh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0x9,
        (
            "#1272F#4PI know I might not measure up to Mischa,\x01",
            "but, but...\x02\x03",

            "I still know a lot of good things about you,\x01",
            "Agate!\x02\x03",

            "And, and so, it makes me so sad to hear\x01",
            "you say such bad things about yourself...\x02\x03",

            "It made me kind of angry despite not really\x01",
            "understanding what you meant...\x02\x03",

            "And, and...and...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0x8,
        (
            "#1281F#6P...\x02\x03",

            "#1291F...Hahaha. Oh, man.\x02\x03",

            "#1290FBustin' out the lectures, soundin' exactly\x01",
            "like Mischa.\x02\x03",

            "You sure are acting grown-up,\x01",
            "shortstuff.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0x9,
        (
            "#1274F#4PD-Don't treat me like a kid!\x02\x03",

            "I, I just...\x02\x03",

            "#1272FI was really sad...and really angry.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0x8,
        (
            "#1290F#6PSad and angry...\x02\x03",

            "#1291F...\x02\x03",

            "I don't know the first thing about myself,\x01",
            "huh?\x02\x03",

            "You really hit it on the head.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(1000)

    def lambda_34B7():
        OP_6D(-26720, 0, 47740, 1000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_34B7)
    ClearChrFlags(0x9, 0x2)
    SetChrChipByIndex(0x9, 7)
    SetChrSubChip(0x9, 0)
    SetChrSubChip(0x8, 0)
    SetChrFlags(0x9, 0x4)
    SetChrFlags(0x9, 0x20)
    SetChrPos(0x8, -26640, 0, 46620, 90)
    SetChrPos(0x9, -26070, 0, 46640, 270)
    SetChrFlags(0x9, 0x80)
    SetChrChipByIndex(0x8, 5)
    SetChrSubChip(0x8, 0)
    OP_0D()
    Sleep(500)
    OP_99(0x8, 0x0, 0x4, 0x320)
    OP_99(0x8, 0x4, 0x2, 0x320)
    Sleep(500)

    ChrTalk(    #106
        0x9,
        "#1273F#4POh...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0x8,
        (
            "#1290F#6PThanks, Tita.\x02\x03",

            "You really helped me see it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #108
        0x9,
        "#1266F#4PAgate...\x02",
    )

    CloseMessageWindow()
    OP_99(0x8, 0x5, 0x6, 0x320)
    Sleep(500)

    ChrTalk(    #109
        0x8,
        (
            "#1282F#6PThere ain't no point in tryin' to judge\x01",
            "yourself when all you can see is your own,\x01",
            "limited vision of yourself.\x02\x03",

            "All you can really do is plow on.\x02\x03",

            "Anger, sadness... Neither have anything to\x01",
            "do with it. You just have to go straight\x01",
            "on until you find an answer.\x02",
        )
    )

    CloseMessageWindow()
    OP_99(0x8, 0x6, 0xB, 0x384)
    Sleep(500)

    ChrTalk(    #110
        0x8,
        (
            "#1290F#6PHeh, maybe then...\x02\x03",

            "Maybe then I'll finally understand why\x01",
            "I've held on to this thing for so long.\x02",
        )
    )

    CloseMessageWindow()
    OP_DB()
    FadeToDark(3000, 0, -1)
    OP_0D()
    OP_20(0xBB8)
    OP_21()
    Sleep(500)
    OP_22(0xD, 0x0, 0x64)
    Sleep(2000)
    Sleep(2000)
    Sleep(1500)
    OP_DC()
    ClearMapFlags(0x2000000)
    OP_A2(0x10F1)
    NewScene("ED6_DT21/T1103   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_3_1DD3 end

    def Function_4_3778(): pass

    label("Function_4_3778")

    OP_8E(0xFE, 0xFFFF9AA2, 0x0, 0xB644, 0x3E8, 0x0)
    SetChrPos(0x9, -26500, 0, 46620, 270)
    SetChrFlags(0x9, 0x8000)
    SetChrFlags(0x9, 0x2)
    SetChrChipByIndex(0x9, 3)
    SetChrSubChip(0x9, 32)
    Return()

    # Function_4_3778 end

    SaveToFile()

Try(main)
